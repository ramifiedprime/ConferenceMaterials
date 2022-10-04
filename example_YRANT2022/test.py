import argparse

parser = argparse.ArgumentParser(description="Compute files in relation to conference materials preparation")
parser.add_argument("inputfiles", metavar="f", nargs="+",
                    type= str,help="files to be used")
parser.add_argument('--booklet', dest='do_booklet', action='store_const',
                    const=True, default=False,
                    help='compile conference booklet')
parser.add_argument('--badges', dest='do_booklet', action='store_const',
                    const=True, default=False,
                    help='compile name badges')
args = parser.parse_args()
print(args.inputfiles)
print(args.do_booklet)