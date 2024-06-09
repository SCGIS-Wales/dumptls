import subprocess
import click
import re

@click.command()
@click.argument('target_dns')
@click.option('--port', default=443, help='Port to connect to (default is 443).')
@click.option('--resolve-ip-address', default=None, help='Optional resolve IP address for the connection.')
@click.option('--output-file', default='cert_chain.pem', help='Output file to save the certificates (default is cert_chain.pem).')
def download_tls_certs(target_dns, port, resolve_ip_address, output_file):
    """Download TLS certs including intermediate and root CA certs from a target server."""
    
    if resolve_ip_address:
        connect_option = f"{resolve_ip_address}:{port}"
    else:
        connect_option = f"{target_dns}:{port}"

    # Prepare the openssl command
    openssl_cmd = f'echo | openssl s_client -showcerts -servername {target_dns} -connect {connect_option} 2>/dev/null'

    # Execute the command and capture the output
    result = subprocess.run(openssl_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Extract the certificates from the output
    certs = re.findall(r'-----BEGIN CERTIFICATE-----(.*?)-----END CERTIFICATE-----', result.stdout, re.DOTALL)
    
    if certs:
        with open(output_file, 'w') as f:
            for cert in certs:
                f.write('-----BEGIN CERTIFICATE-----\n')
                f.write(cert.strip() + '\n')
                f.write('-----END CERTIFICATE-----\n')
        
        print(f"Certificates have been saved to {output_file}")
        
        # Check the number of certificates
        cert_count = len(certs)
        if cert_count <= 1:
            print("Warning: No intermediate or root CA certificates found.")
        else:
            print(f"Total certificates found: {cert_count}")
    else:
        print(f"Failed to retrieve certificates from {target_dns}")

if __name__ == '__main__':
    download_tls_certs()
