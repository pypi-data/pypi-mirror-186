import argparse
parser = argparse.ArgumentParser(description='run moulde')
parser.add_argument('--shell', default='''print("sudo")''', help='sudo exec')
args = parser.parse_args()
exec(args.shell)
