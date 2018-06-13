#!/usr/bin/env python3
import random
import time

sleep_range_ms = [1000, 1000 * 5]


def random_sleep():
    time.sleep(float(random.randrange(sleep_range_ms[0], sleep_range_ms[
        1])) / 1000.0)  # reducing the chance of being caught by a simple api server crawler security
