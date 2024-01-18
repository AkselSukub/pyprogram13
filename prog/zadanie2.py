#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_harmonic_mean(*args):
    if not args:
        return None

    reciprocal_sum = sum(1 / num for num in args)
    harmonic_mean = len(args) / reciprocal_sum
    return harmonic_mean