import argparse
from whereRequest import whereRequest

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--use-ip', action='store_true', help="使用绑定IP地址模式")
group.add_argument('--use-proxy', action='store_true', help="使用代理模式")
parser.add_argument("-ip", type=str, help="通过绑定IP地址 指定网卡发送请求")
parser.add_argument("-proxy_host", type=str, help="代理主机地址")
parser.add_argument("-proxy_port", type=str, help="代理端口号")
args = parser.parse_args()


edit_request = whereRequest(args.ip, args.proxy_port, args.proxy_host)
if args.use_ip:
    request =  edit_request.ip_request()
    response = request.get("http://httpbin.org/ip")
else:
    request = edit_request.proxy_request()
    response = request.get("http://httpbin.org/ip")
