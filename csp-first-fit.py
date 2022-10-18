""" cutting stock using first fit """

import random
import time

STOCK_LEN = 10


def first_fit(cuts: list) -> list:
    """ first fit packing """
    results = [[]]
    for cut in cuts:

        # find stock to accept cut
        found = False
        for stock in results:
            if (sum(stock) + cut) <= STOCK_LEN:
                found = True
                stock.append(cut)

        # add new piece of stock
        if not found:
            results.append([cut])

    return results


def print_stock(results: list, header: str, time, detailed=False):
    """ print stock cutting details """
    print(f">>>>>>>>>> {header} <<<<<<<<<<<<<<<<<")
    total_waste = 0
    for i, item in enumerate(results):
        total_waste += STOCK_LEN - sum(item)
        if detailed: print(f"stock: {i} waste: {STOCK_LEN - sum(item)} cuts: {item}")
    print(f"time: {time:.2f} #stock: {len(results):,} total waste: {total_waste:,}")


if __name__ == '__main__':
    detailed = False

    # create random cut list [(1:9), ...]
    NUM_CUTS = 10000
    cuts = [random.randrange(1, 10, 1) for i in range(NUM_CUTS)]
    # cuts = [1, 7, 3, 1, 4, 9, 2, 9, 9, 2, 9, 5, 4, 7, 6, 6, 7, 2, 1, 3, 1, 2, 7, 1, 9, 2,
    #         2, 2, 2, 6, 3, 4, 4, 2, 7, 9, 9, 4, 4, 1, 5, 8, 1, 4, 9, 1, 8, 7, 9, 8]
    print(f"#cuts: {len(cuts):,} lower bound: {NUM_CUTS/STOCK_LEN:,}")

    # random
    start = time.time()
    results = first_fit(cuts)
    end = time.time()
    print_stock(results, 'Random', end - start, detailed)

    # descending
    start = time.time()
    cuts.sort(reverse=True)
    results = first_fit(cuts)
    end = time.time()
    print_stock(results, 'Descending Non opt', end - start, detailed)

    # ascending
    start = time.time()
    cuts.sort()
    results = first_fit(cuts)
    end = time.time()
    print_stock(results, 'Ascending No opt', end - start, detailed)

