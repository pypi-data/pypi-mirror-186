import argparse 
import sys
from credzer.lib.static import version, codename, supported

def args_parser():
    parser = argparse.ArgumentParser(exit_on_error=False,description=f"""
    Credzer - $$$
    Version : {version} Codename : {codename}
    """, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--database','-db',action="store",required=True,help="the final db")
    parser.add_argument('--source','-s',nargs=1,choices=supported)
    parser.add_argument('--file','-f',action="store",help="File containing creds to be add to the database")
    parser.add_argument('--search',action="store",help="Search content in the database")
    #parser.add_argument('-a',)

    try:
        args=parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    except SystemExit:
        exit(-1)
    return args
