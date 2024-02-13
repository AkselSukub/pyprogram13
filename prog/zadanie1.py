#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import prod


def calculate_geometric_mean(*args):
    if not args:
        return None

    product = prod(args)
    geometric_mean = product ** (1 / len(args))
    return geometric_mean

if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10]
    result = calculate_geometric_mean(*numbers)
    print("Geometric mean:", result)
