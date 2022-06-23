"""
Guided exercise 6.18
Author: Noam Cohen
Purpose: Write a simple plan, that create Three Way Handshake with google server.
Note: The code is written in a simple way, with remarks and explains how the plan working.
"""


from scapy.all import *
from scapy.layers.inet import TCP, IP


def main():
    syn_segment = TCP(dport=80, seq=123, flags='S')

    syn_packet = IP(dst='www.google.com')/syn_segment
    syn_packet.show()
    # send(syn_packet)

    syn_ack_packet = sr1(syn_packet)
    syn_ack_packet.show()

    ack_segment = TCP(dport=80, seq=syn_ack_packet[TCP].ack, ack=syn_ack_packet[TCP].seq + 1, flags='A')

    ack_packet = IP(dst='www.google.com')/ack_segment
    ack_packet.show()
    send(ack_packet)


if __name__ == "__main__":
    main()
