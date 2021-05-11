#!/usr/bin/python3
from dpkt import pcap, ethernet, UnpackError, tcp, ip
from sys import argv  

f = open(argv[1], "rb")
pcap = pcap.Reader(f)
dictionary = {}

for ts, buf in pcap:
        try:
                eth = ethernet.Ethernet(buf)
        except UnpackError:
                continue
        if eth.type != ethernet.ETH_TYPE_IP: continue
        ip = eth.data

        if ip.p == 6:
                packet = ip.data
                if packet.flags & tcp.TH_SYN != 0:
                        if ip.src not in dictionary: dictionary[ip.src] = {'SYN' : 0, 'SYN+ACK' : 0}
                        if ip.dst not in dictionary: dictionary[ip.dst] = {'SYN' : 0, 'SYN+ACK' : 0} 
                        if packet.flags & tcp.TH_ACK != 0: dictionary[ip.dst]['SYN+ACK'] += 1
                        else: dictionary[ip.src]['SYN'] += 1

for item in dictionary.items():
        if item[1]['SYN'] > item[1]['SYN+ACK'] * 3:
                hexstring = str(item[0].hex())
                targetIp = []
                for i in range(0, len(hexstring), 2):
                        targetIp.append(str(int(hexstring[i:i + 2], 16)))
                print(targetIp[0] + '.' + targetIp[1] + '.' + targetIp[2] + '.' + targetIp[3])
           
f.close()
