"""
    MineCraft Watching Proxy
    ========================
"""

from MCRP import MCRewriteProxy, Relative
import cubelib

from ruamel.yaml import YAML
import argparse

version = '0.1.0'

BANNER = \
"""
 __  __   ____  ____   ____       __        __ ____
|  \/  | / ___||  _ \ |  _ \  _   \ \      / /|  _ \\
| |\/| || |    | |_) || |_) |(_)   \ \ /\ / / | |_) |
| |  | || |___ |  _ < |  __/  _     \ V  V /  |  __/
|_|  |_| \____||_| \_\|_|    (_)     \_/\_/   |_| v0.1
"""

def main():

    print(BANNER[1:])
    parser = argparse.ArgumentParser(description="Minecraft Watching Proxy")
    parser.add_argument(dest="conf", type=argparse.FileType("r", encoding="utf-8"), help="Path to YAML config file", metavar="config.yaml")
    parser.add_argument("-v", action="store_true", help="If passed, enables verbose logging")    
    parser.add_argument("-l", help="Proxy listen addr [default:25565]", default="127.0.0.1:25565", metavar="addr")
    parser.add_argument("-u", help="Proxy upstream server addr [default:25575]", default="127.0.0.1:25575", metavar="addr")
    args = parser.parse_args()

    yaml = YAML(typ="safe")
    conf = yaml.load(args.conf)    

    def addr_str2tuple(addr: str):
        s = addr.split(":")
        return (s[0], int(s[1]))

    proxy = MCRewriteProxy(addr_str2tuple(args.l), addr_str2tuple(args.u), args.verbose)

    ClientBoundFilterList = []
    ServerBoundFilterList = []

    @proxy.on(cubelib.proto.ServerBound.Handshaking.Handshake)
    def handler(packet):
        global ClientBoundFilterList, ServerBoundFilterList

        if packet.NextState != cubelib.NextState.Login:
            return

        proxy.logger.debug(f'Selected proto version is: {packet.ProtoVer}, building filter...')
        proto = proxy.PROTOCOL

        def find_ap_by_path(proto, path):
            obj = proto
            attrs = path.split('.')
            if attrs[-1] == "NotImplementedPacket":
                return cubelib.p.NotImplementedPacket

            for attr in attrs:
                obj = getattr(obj, attr, None)
                if not obj:
                    proxy.logger.debug(f'[WARN] Failed to resolve filter packet {proxy.PROTOCOL.__name__}.{".".join(attrs)}')
                    break
            return obj
        
        ClientBoundFilterList = [find_ap_by_path(proto, "ClientBound.Play." + packet) for packet in conf["ClientBound"]] if "ClientBound" in conf else []
        ServerBoundFilterList = [find_ap_by_path(proto, "ServerBound.Play." + packet) for packet in conf["ServerBound"]] if "ServerBound" in conf else []

        proxy.logger.debug(f"Filtering mode: {conf['mode']}, filtered packets:")

        proxy.logger.debug(f"ClientBound [{len(ClientBoundFilterList)}]:")
        for packet in ClientBoundFilterList:
            proxy.logger.debug(f"    {packet}")

        proxy.logger.debug(f"ServerBound [{len(ServerBoundFilterList)}]:")
        for packet in ServerBoundFilterList:
            proxy.logger.debug(f"    {packet}")

    def filter_(packet, mode, bound):        
        if bound is cubelib.bound.Server:
            list_ = ServerBoundFilterList
        else:
            list_ = ClientBoundFilterList

        if mode == "blacklist":
            if packet.__class__ in list_ or packet in list_:
                return False
            return True

        elif mode == "whitelist":
            if packet.__class__ in list_ or packet in list_:
                return True
            return False

    def log_clientbound(*args):
        proxy.logger.debug(f'\u001b[96m[ClientBound] {" ".join([str(a) for a in args])}\u001b[0m')

    def log_serverbound(*args):
        proxy.logger.debug(f'\u001b[95m[ServerBound] {" ".join([str(a) for a in args])}\u001b[0m')

    @proxy.ClientBound
    def handler(packet):
        if filter_(packet, conf["mode"], cubelib.bound.Client):
            log_clientbound(packet)

    @proxy.ServerBound
    def handler(packet):
        if filter_(packet, conf["mode"], cubelib.bound.Server):
            log_serverbound(packet)

    proxy.join()

if __name__ == "__main__":
    main()
