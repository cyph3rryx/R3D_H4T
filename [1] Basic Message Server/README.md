# Basic Message Server

This project provides basic examples of TCP and UDP server implementations using Python's built-in socket library. The TCP server listens for incoming connections and receives messages, while the UDP server listens for incoming datagrams (messages) from clients.

## Table of Contents

- [TCP Server](#tcp-server)
- [UDP Server](#udp-server)
- [Usage](#usage)
  
## TCP Server

The TCP server example demonstrates how to create a basic server that listens for incoming connections and receives messages over TCP.

## UDP Server
The UDP server example demonstrates how to create a basic server that listens for incoming datagrams (messages) over UDP.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/basic-message-server.git
cd basic-message-server
```

2. To run the TCP server, execute:

```python
tcp_server.py
```

The server will start listening on 127.0.0.1:12345. You can customize the host and port in the tcp_server.py script.

To run the UDP server, execute:

```python
udp_server.py
```

The server will start listening on 127.0.0.1:12345. You can customize the host and port in the udp_server.py script.

To test the servers, you can use corresponding TCP and UDP clients to establish connections and send messages or datagrams to the servers.
