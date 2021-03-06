#!/usr/bin/env python
import socket
import gevent
import random
from gevent.monkey import patch_all
patch_all()

UDP_IP = "127.0.0.1"
UDP_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)


def jailer(ip):
    seeds = [random.randint(1, 100) for _ in xrange(10)]
    while True:
        #print("ip {} action".format(ip))
        if random.randint(1, seeds[0]) == 1:
            sock.sendto("action test {} 1 10 100 30".format(ip), (UDP_IP, UDP_PORT))
        if random.randint(1, seeds[1]) == 1:
            sock.sendto("action test2 {} 1 10 100 30".format(ip), (UDP_IP, UDP_PORT))
        if random.randint(1, seeds[2]) == 1:
            sock.sendto("action test3 {} 1 10 100 30".format(ip), (UDP_IP, UDP_PORT))
        if random.randint(1, seeds[3]) == 1:
            sock.sendto("action test4 {} 1 10 100 30".format(ip), (UDP_IP, UDP_PORT))
        if random.randint(1, seeds[4]) == 1:
            sock.sendto("action test5 {} 1 10 100 30".format(ip), (UDP_IP, UDP_PORT))
        if random.randint(1, seeds[5]) == 1:
            sock.sendto("action test6 {} 1 10 100 30".format(ip), (UDP_IP, UDP_PORT))
        gevent.sleep(random.uniform(0, 0.2))

for i in xrange(1000):
    print("spawning new ip")
    gevent.spawn(jailer, "{}.{}.{}.{}".format(random.randint(1, 255),
                                              random.randint(1, 255),
                                              random.randint(1, 255),
                                              random.randint(1, 255)))
gevent.wait()
