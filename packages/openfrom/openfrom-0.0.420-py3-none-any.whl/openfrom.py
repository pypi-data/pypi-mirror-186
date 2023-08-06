import	os
import	argparse
import	subprocess

def	main():
	parser = argparse.ArgumentParser(prog = 'openfrom',
									description = 'openfrom is a tool that opens multiple pages from a single base URL by appending unique strings to it and opening them in separate tabs.',
									epilog = 'Report any issue at https://github.com/chozeur/openfrom')
	parser.add_argument('baseURL', metavar='baseURL', type=str,
						help='Base URL')
	parser.add_argument('endPoints', metavar='endPoints', type=str, nargs='*',
						help='list of endPoints')
	parser.add_argument('-r', '--read', dest='read', type=str,
						help='read endPoints from a file, each one separated by a white char')
	args = parser.parse_args()
	if args.read:
		if os.path.isfile(args.read):
			if os.access(args.read, os.R_OK):
				with open(args.read, 'r') as f:
					args.endPoints = f.read().split()
			else:
				parser.error("the file '{}' is not readable".format(args.read))
		else:
			parser.error("the file '{}' does not exist".format(args.read))
	if not args.endPoints:
		parser.error('endPoints must not be empty')
	for endP in args.endPoints:
		subprocess.run(["open", args.baseURL + endP])

# if __name__ == '__main__':
# 	main()
