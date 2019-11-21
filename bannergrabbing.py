import socket
import sys

# IPv4 TCP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# machines range
for host in range(80,100):
    # port file
    ports = open('ports.txt','r')
    # banners (vulnerable services)
    banners = open('banners.txt','r')
    for port in ports:
        try:
            # open socket
            socket.connect(( str(sys.argv[1] + '.' + str(host)), int(port) ))
            print('Connecting to' + str(sys.argv[1]) + 'on the port' + str(port))
            # segs until timeout
            socket.settimeout(1)
            # getting the banner from the server
            banner = socket.recv(1024)
            # checking banner list
            for vuln in banners:
                # check if banner matches the vulnerable banners on the banners.txt file
                if banner.strip() in vuln.strip():
                    print('We found it' + banner)
                    print('Host: ' + str(sys.argv[1]) + '.' + str(host))
                    print('Port: ' + str(port))
        except:
            print('Error connecting to: ' + str(sys.argv[1] + '.' + str(host)) + ':' + str(port))


# run it like = bannergrabbing.py 192.168.1 (network segment)
# the banners.txt assumes that the listed services are vulnerable
