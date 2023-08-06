import nmap
import socket

class Network:

    def __init__(
        self,
        network
        )-> None:

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn -v -n')
        self.hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    @property
    def free(self):
        ip = []
        for host, status in self.hosts_list:
            if status == 'down': ip.append(host)
        return ip
    
    @property
    def busy(self):
        ip = []
        for host, status in self.hosts_list:
            if status == 'up': ip.append(host)
        return ip


    def check_open_port(self, host, port=22, timeout=2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)                                      #2 Second Timeout
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        else:
            return False