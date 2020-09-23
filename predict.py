#!/usr/bin/env python

import argparse
import sys
import pandas as pd

def _predict(args):
    try:
        weights = pd.read_csv(args.weights)
        theta0, theta1 = weights.theta
    except:
        theta0 = theta1 = 0
    if args.mileage:
        mileage = args.mileage
    else:
        while True:
            print('Enter mileage:')
            try:
                mileage = int(input())
                break
            except:
                pass
    price_predicted = theta0 + theta1 * mileage
    print(f'Price predicted:\n{round(price_predicted,0):.0f}')

def _parse_args():
    parser = argparse.ArgumentParser(
        description='Predict car price based on its mileage')
    parser.add_argument(
        'mileage',
        nargs='?',
        metavar='NUMBER',
        type=int,
        help='set mileage in km as integer; STDIN prompt if missed')
    parser.add_argument(
        'weights',
        nargs='?',
        metavar='FILE',
        type=argparse.FileType('r'),
        default='weights.csv',
        help='load weights from file; "weights.csv" by default, 0 if empty')
    return parser.parse_args()

def _main():
    args = _parse_args()
    _predict(args)

if __name__ == '__main__':
    _main()
