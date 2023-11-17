# Net Slash - Network Traffic Capture Script

**Net Slash** is a Bash script designed to capture network traffic using TCPDump, a command-line packet analyzer. This script prompts the user for various parameters, allowing customization of the network capture. The captured traffic is saved to pcap files for later analysis.

## Usage

### Prerequisites

Ensure that TCPDump is installed on your system before running the script.

```bash
sudo apt install tcpdump
```

### Running the Script

1. Clone or download the script to your local machine.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the following command:

```bash
./netslash.sh
```

4. Follow the prompts to provide the necessary information for the network capture.

## Parameters

- **Duration:** The duration of the network capture in seconds. The default is set to 10 seconds.

- **Network Interfaces:** Specify the network interfaces to monitor, separated by space. Leave blank to capture traffic on all interfaces.

- **Packet Type:** Specify the type of packets to capture (e.g., 'tcp', 'udp'). Leave blank to capture all packets.

## Capture Details

The script captures network traffic and saves it to pcap files. If no specific network interfaces are provided, it captures traffic on all available interfaces. The captured files are named in the format `capture_interface.pcap` and stored in the same directory as the script.

## Analyzing Captured Traffic

The script automatically analyzes the captured traffic after the specified duration. It displays the captured packets for each interface using TCPDump.

## Example

```bash
./netslash.sh
```

Follow the prompts to set the capture duration, specify network interfaces, and choose the packet type. The script will capture, analyze, and display the network traffic accordingly.
