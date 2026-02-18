import socket
from banner import grab_banner

COMMON_PORTS = [21, 22, 25, 80, 443, 3306]

def scan_target(host):
    open_services = []

    for port in COMMON_PORTS:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                banner = grab_banner(host, port)
                open_services.append({
                    "port": port,
                    "banner": banner
                })
            sock.close()
        except:
            pass

    return open_services
