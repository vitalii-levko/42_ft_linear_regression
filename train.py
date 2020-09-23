#!/usr/bin/env python

import argparse
import pandas as pd
import matplotlib.pyplot as plt

def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def linear_regression(mileage, price, m, theta0, theta1, learning_rate, epoch, plot):
    m = float(m)
    x = mileage
    y = price
    mileage = (mileage-min(mileage))/(max(mileage)-min(mileage))
    price = (price-min(price))/(max(price)-min(price))
    for i in range(epoch):
        hypothesis = estimate_price(mileage, theta0, theta1)
        tmp_theta0 = learning_rate * 1/m * sum(hypothesis - price)
        tmp_theta1 = learning_rate * 1/m * sum((hypothesis - price) * mileage)
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    theta0 = theta0*(max(y)-min(y)) + min(y) + (theta1*min(x)*(min(y)-max(y)))/(max(x)-min(x))
    theta1 = theta1*(max(y)-min(y)) / (max(x)-min(x))
    if plot:
        price_predicted = estimate_price(x, theta0, theta1)
        plt.ylabel('price')
        plt.xlabel('mileage (km)')
        plt.scatter(x, y, label='data point')
        plt.plot(x, price_predicted, label='linear regression')
        plt.legend()
        plt.show()
    return theta0, theta1

def _train(args):
    try:
        dataset = pd.read_csv(args.data)
        mileage = dataset.km
        price = dataset.price
        m = dataset.shape[0]
    except:
        exit(1)
    theta0, theta1 = linear_regression(mileage, price, m, 0, 0, 1.7, 1000, args.plot)
    pd.DataFrame([theta0, theta1]).to_csv(args.save, header=['theta'], index=False)

def _parse_args():
    parser = argparse.ArgumentParser(
        description='Train weights to predict car price')
    parser.add_argument(
        '-p', '--plot',
        action='store_true',
        help='plot the result')
    parser.add_argument(
        'data',
        nargs='?',
        metavar='FILE',
        type=argparse.FileType('r'),
        default='data.csv',
        help='load dataset from file; "data.csv" by default')
    parser.add_argument(
        '-s', '--save',
        metavar='FILE',
        type=argparse.FileType('w'),
        default='weights.csv',
        help='save weights to file; "weights.csv" by default')
    return parser.parse_args()

def _main():
    args = _parse_args()
    _train(args)

if __name__ == '__main__':
    _main()
