import argparse
import sys
import csv
import random as rn


def obfuscate_cli():


	# set up CLI
	parser = argparse.ArgumentParser()
	#parser.add_argument('--infile', action='store')
	parser.add_argument('--infile', type=argparse.FileType('r'))
	parser.add_argument('--outfile', type=argparse.FileType('w'))

	args = parser.parse_args()

	# if args.infile:
	# 	data = csv.reader(args.infile)
	# 	for line in data:
	# 		print(line[2])
	# 		print(obfuscate_password(line[2]))

	# dictreader version
	if args.infile:
		data = csv.DictReader(args.infile)
		for line in data:
			print(line['password'])
			print(obfuscate_password(line['password'])) 



def obfuscate_password(pw):
	return ''.join(['*' for i in range(rn.randint(3, 20))])
	

def main():
	obfuscate_cli()


if __name__ == '__main__':
	main()