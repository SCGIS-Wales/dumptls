import subprocess
import click
import re
from OpenSSL import crypto

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('target_dns', required=False)
@click.option('--port', default=443, help='Port to connect to (default is 443).')
@click.option('--resolve-ip-address', default=None, help='Optional resolve IP address for the connection.')
@click.option('--output-file', default='cert_chain.pem', help='Output file to save the certificates (default is cert_chain.pem).')
def download_tls_certs(target_dns, port, resolve_ip_address, output_file):
    """Download TLS certs including intermediate and root CA certs from a target server."""
    if not target_dns:
        click.echo(download_tls_certs.get_help(click.Context(download_tls_certs)))
        return
    
    if resolve_ip_address:
        connect_option = f"{resolve_ip_address}:{port}"
    else:
        connect_option = f"{target_dns}:{port}"

    # Prepare the openssl command
    openssl_cmd = f'echo | openssl s_client -showcerts -servername {target_dns} -connect {connect_option} 2>/dev/null'

    # Execute the command and capture the output
    result = subprocess.run(openssl_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Extract the certificates from the output
    certs = re.findall(r'(-----BEGIN CERTIFICATE-----(.*?)-----END CERTIFICATE-----)', result.stdout, re.DOTALL)
    
    if certs:
        with open(output_file, 'w') as f:
            for cert in certs:
                f.write(cert[0] + '\n\n')
        
        click.echo(f"Certificates have been saved to {output_file}")

        for cert_text in certs:
            cert_obj = crypto.load_certificate(crypto.FILETYPE_PEM, cert_text[0])
            common_name = cert_obj.get_subject().CN
            serial_number = cert_obj.get_serial_number()
            click.echo(f"Common Name: {common_name}, Serial Number: {serial_number}")
    else:
        click.echo(f"Failed to retrieve certificates from {target_dns}")

if __name__ == '__main__':
    download_tls_certs()
