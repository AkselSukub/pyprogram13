#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import prod


def calculate_geometric_mean(*args):
    if not args:
        return None

    product = prod(args)
    geometric_mean = product ** (1 / len(args))
    return geometric_mean