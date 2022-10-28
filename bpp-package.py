""" bin packing package example
    source:https://pypi.org/project/binpacking/
"""
import time
import binpacking
from random import randrange

STOCK_LEN = 10
NUM_CUTS = 10000

cuts = [randrange(1, 10, 1) for i in range(NUM_CUTS)]

start = time.time()
stock = binpacking.to_constant_volume(cuts, STOCK_LEN)
end = time.time()
print(f"time: {end-start:.2f}")

# for i, item in enumerate(stock):
#     print(f"stock: {i} waste: {STOCK_LEN - sum(item)} cuts: {item}")
