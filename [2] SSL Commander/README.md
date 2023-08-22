# SSL Commander

SSL Commander is a Python-based server-client communication tool that provides secure and encrypted communication over SSL-encrypted sockets. This tool allows you to send commands from a client to a server securely and receive responses while ensuring the confidentiality and integrity of the data transferred.

## Features

- Secure communication using SSL/TLS encryption.
- Command execution on the server and sending of results back to the client.
- Upload and download files securely between client and server.
- Easy-to-use command-line interface for both server and client.

## Usage

### Server

1. Open a terminal and navigate to the project directory.
2. Run the server using the command:

``` python
python ken_ryx_katana.py
```

3. Choose the option to start as a client.
4. The client will connect to the server using SSL encryption.
5. Enter commands to execute on the server. Use the following format:
- For executing a command: `command <your-command>`
- For uploading a file: `upload <file-path>`
- For downloading a file: `download <file-name>`

## Requirements

- Python 3.x
- The `cryptography` library (used for SSL encryption)

Install the required libraries using the following command:
``` bash
pip install cryptography
```
