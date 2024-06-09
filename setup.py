from setuptools import setup, find_packages

setup(
    name='dumptls',
    version='0.1.0',  # This will be dynamically updated by the GitHub Action
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'dumptls=dumptls.cli:download_tls_certs',
        ],
    },
    author='Dejan Gregor',
    author_email='developer@cloudfever.uk',
    description='A tool to download TLS certificates including intermediate and root CA certs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/dumptls',  # Replace with your actual URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)