#!/bin/bash

# Ask the user for the duration of the network capture
read -p "Enter the duration (in seconds) for the network capture (default is 10 seconds): " duration
duration=${duration:-10}

# Identify the Network Interface
echo "Identifying network interfaces..."
sudo tcpdump -D

# Ask the user for the specific network interfaces
read -p "Enter the network interfaces you want to monitor (separated by space), or leave blank for all interfaces: " interfaces

# Ask the user for the type of packets to capture
read -p "Enter the type of packets you want to capture (e.g., 'tcp', 'udp'), or leave blank for all packets: " packet_type

# Capture Network Traffic and Save it to a File
echo "Capturing network traffic..."
if [ -z "$interfaces" ]
then
  interfaces=$(sudo tcpdump -D | awk -F. '{print \$2}')
fi
dir=$(pwd)
for interface in $interfaces
do
  echo "Capturing traffic on $interface..."
  if [ -z "$packet_type" ]
  then
    sudo tcpdump -i $interface -w "$dir/capture_$interface.pcap" &
  else
    sudo tcpdump -i $interface $packet_type -w "$dir/capture_$interface.pcap" &
  fi
done

# Wait for the specified duration
echo "Capturing traffic for $duration seconds..."
sleep $duration

# Stop capturing network traffic
echo "Stopping traffic capture..."
sudo pkill tcpdump

# Analyze Captured Traffic
echo "Analyzing captured traffic..."
for interface in $interfaces
do
  echo "Analyzing traffic on $interface..."
  sudo tcpdump -r "$dir/capture_$interface.pcap"
done
