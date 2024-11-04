# ARP Spoofing Tool – Gateway Impersonation

## Introduction
This tool performs ARP spoofing by sending ARP replies to a target device, making it believe that our device is the network gateway. This can redirect network traffic from the victim to our device. **This tool is for educational and authorized testing purposes only**.

## Disclaimer
**Use this tool responsibly.** ARP spoofing can disrupt network functionality and is illegal if used without permission. This tool should only be used in environments where you have explicit authorization for network testing.

## Features
- Impersonates the network gateway by sending ARP replies to the specified target device.
- Flexible options to specify the target and gateway IP addresses.

## Prerequisites
- Python 3.x installed
- Run with administrator privileges (e.g., `sudo` on Linux).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/haftom-github/ARP-spoof.git
   cd arp-spoof

## Usage
To run the ARP spoofing tool, use the following command:
```bash
sudo python3 arp.py <VICTIM_MAC> <GATEWAY_MAC> <VICTIM_IP> <GATEWAY_IP> <INTERFACE>
```

### Example
```bash
sudo python3 arp.py AA:BB:CC:DD:EE:FF 11:22:33:44:55:66 192.168.1.5 192.168.1.1 wlan0
```

## Analyzing Traffic with Wireshark

To analyze the traffic being redirected to your device instead of the intended gateway, you can use Wireshark with specific filters.

### Setting Up Wireshark
1. **Open Wireshark** and start capturing on the interface you are using for ARP spoofing (e.g., `wlan0`).
2. **Use the following display filter** to isolate packets intended for the gateway:
   ```plaintext
   arp || ip.dst == <GATEWAY_IP>

## Enabling IP Forwarding
To ensure network traffic intended to go to the gateway is correctly forwarded to the gateway, you need to enable IP forwarding on your device. 

### On Linux
Use the following command to enable IP forwarding temporarily (for the current session only):
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

### On macOS
Use this command to enable IP forwarding temporarily:
```bash
sudo sysctl -w net.inet.ip.forwarding=1
```

### On Windows
To enable IP forwarding on Windows, use the following command in Command Prompt with administrator privileges:
```cmd
netsh interface ipv4 set interface "YOUR_INTERFACE_NAME" forwarding=enabled
```
Replace `"YOUR_INTERFACE_NAME"` with the name of the network interface you’re using (you can list interfaces with `ipconfig`).

### Stopping the Program
To stop the program, press `Ctrl + C`.

## Troubleshooting
- **Permission Denied**: Run with `sudo` or administrator privileges.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact Information
For questions or feedback, please reach out to Haftom at [haftish.tsegay@gmail.com](mailto:haftish.tsegay@gmail.com).