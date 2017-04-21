"""
Automating scans

Usage:
  initscanner.py [-i TARGET] [-qn] [-t|-u]
  initscanner.py [-h | --help]

Options:
  -h --help  Show this help message and exit.
  -q  Perform quick Nmap scan.
  -u  Perform in-depths Nmap UDP scan(Only). Mutually exclusive with -t flag.
  -t  Perform in-depths Nmap TCP scan(Only). Mutually exclusive with -u flag.
  -n  Specify output filename

Examples:
  initscanner.py -i 192.168.0.1 -q  # Perform quick Nmap scan on host 192.168.0.1
  initscanner.py -i 192.168.0.1 -t  # Perform indepth Nmap UDP scan on host 192.168.0.1
  initscanner.py -i 192.168.0.1 -u  # Perform indepth Nmap TCP scan on host 192.168.0.1
  initscanner.py -i 192.168.0.1  # Perform indepths Nmap UDP, TCP scan on host 192.168.0.1

"""


from docopt import docopt
from _thread import start_new_thread
import subprocess
target=""
quick=False
udponly=False
tcponly=False
threadc=0


# Change -p80 to -p- for prod
# Scan TCP
def nmap_tcp_basic():
    global threadc
    threadc += 1
    nmapstr = "nmap -Pn -vv -n -p- -oG " + target + "_basic_tcp.txt " + target
    print (nmapstr)
    subprocess.check_call(['nmap', '-Pn', '-vv', '-n', '-p80', '-oG', target + '_basic_tcp.txt', target])
    threadc -= 1
    if (quick):
        # need to run parsing of ^ result
        return "DONE"
    else:
        return "DONEO"


def nmap_udp_basic():
    global threadc
    thread += 1
    nmapstr = "nmap -Pn -vv -n -sU -oG " + target + "_basic_udp.txt " + target
    print (nmapstr)
    subprocess.check_call(['nmap', '-Pn', '-vv', '-n', '-sU', '-oG', target + '_basic_udp.txt', target])
    print ("DONE UDP")


def nmap_initializer():
    print ("Initializing")
    try:
        if (tcp):
            start_new_thread(nmap_tcp_basic,())
        if (udp):
            start_new_thread(nmap_udp_basic,())
#        _thread.start_new_thread(nmap_tcp_basic, ())
#        _thread.start_new_thread(nmap_udp_basic, ())
    except:
        print ("Error: Unable to create thread")

    while threadc > 0:
        print (threadc)
        pass
    print ("X")
    print (res)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    target = arguments['TARGET']
    quick = arguments['-q']
    udponly = arguments['-u']
    tcponly = arguments['-t']
    print(arguments)
    nmap_initializer()




