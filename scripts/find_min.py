import numpy as np
import argparse
import os
import csv

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--test', action='store_true')
	parser.add_argument('--filter_b', action='store_true')
	parser.add_argument('--b', type=int)
	parser.add_argument('--filter_lr', action='store_true')
	parser.add_argument('--filter_x', action='store_true')
	parser.add_argument('--filter_l2', action='store_true')
	parser.add_argument('--lr', type=float)
	return parser.parse_args()

def main():
	args = parse_args()
	min_value = None
	min_file = None
	max_value = None
	max_file = None
	type_ = 'train' if not args.test else 'test'
	for filename in os.listdir('.'):
		if type_  not in filename or 'max_min' in filename:
			continue

		if args.filter_b:
			if 'b_{}'.format(args.b) not in filename:
				continue
		if args.filter_lr:
			if 'lr_{}'.format(args.lr) not in filename:
				continue
		# Includes momentum and weight decay
		if args.filter_x:
			if '_x' not in filename:
				continue
		if args.filter_l2:
			if 'l2_5e-4' not in filename:
				continue
		with open(filename) as f:
			value = np.mean([float(line[0]) for line in list(csv.reader(f))[-3:]])
			if min_file is None or min(min_value, value) == value:
				min_file = filename
				min_value = value
			if max_file is None or max(max_value, value) == value:
				max_file = filename
				max_value = value

	print("min: {}".format(min_file))
	print("max: {}".format(max_file))

if __name__ == "__main__":
    main()