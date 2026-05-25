from requests_toolbelt import SourceAddressAdapter


class whereRequest:
    def __init__(self, ip, port, host):
        self.ip = ip
        self.port = port
        self.host = host

    def ip_request(self):
        session = requests.Session()
        source = SourceAddressAdapter(self.ip)
        session.mount('http://', source)
        session.mount('https://', source)
        return session

    def proxy_request(self):
        proxy = {
            "http": f"socks5://{self.proxy_host}:{self.proxy_port}",
            "https": f"socks5://{self.proxy_host}:{self.proxy_port}"
        }
        session = requests.Session()
        session.proxies.update(proxy)
        return session


