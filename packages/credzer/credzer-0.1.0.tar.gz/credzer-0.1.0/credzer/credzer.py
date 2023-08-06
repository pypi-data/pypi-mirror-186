from credzer.lib.display import display
from credzer.lib.args import args_parser
#from credzer.lib.conf import get_conf
from credzer.lib.router import router

def main():
    args=args_parser()
    #get_conf(args)
    router(args)

