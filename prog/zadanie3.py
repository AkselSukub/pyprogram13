#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_sum_before_last_positive(*args):
    sum_before_last_positive = 0
    last_positive_index = -1

    for i, num in enumerate(args):
        if num > 0:
            last_positive_index = i
        if i < last_positive_index:
            sum_before_last_positive += num

    if last_positive_index == -1:
        return None

    return sum_before_last_positive