""" my bin packing w/ class for bin """

import logging
import random


class Bin:
    """ a bin to hold items """
    capacity = 10
    log = logging.getLogger()

    def add(self, item):
        """ add item to bin"""
        self.waste -= item
        self.cuts.append(item)

    def __init__(self):
        self.waste = self.capacity
        self.cuts = []

    def __str__(self) -> str:
        return f"w: {self.waste} cuts: {self.cuts}"

    def __repr__(self):
        return str(self)


def first_fit(requirements) -> list:
    ''' bin packing first fit '''
    bins = list()
    for item in requirements:

        # check if item can fit in bins
        found = False
        for b in bins:
            if b.waste >= item:
                found = True
                b.add(item)

        # add new bin & item to new bin
        if not found:
            nb = Bin()
            nb.add(item)
            bins.append(nb)
    return bins


def print_bins(bins):
    for i, b in enumerate(bins):
        print(f"bin[{i}] {str(b)}")


def write_bins(bins, bin_name: str):
    with open(bin_name + '.txt', 'a+') as fp:
        fp.write(
            f"total waste: {total_waste(bins)} total stock: {total_stock(bins)}\n")
        for i, b in enumerate(bins):
            fp.write(f"bin[{i}] {str(b)}\n")


def total_waste(bins) -> int:
    w = 0
    for b in bins:
        w += b.waste
    return w


def total_stock(bins) -> int:
    s = 0
    for b in bins:
        s += 10 - b.waste
    return s


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log.info('Starting')

    # random requirements
    req = [random.randrange(1, 10, 1) for i in range(200)]
    # req = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
    log.info(f'#req: {len(req)} total req: {sum(req)}')

    # first fit UNSORTED
    bins = first_fit(req)
    # print(*bins)
    # for i, b in enumerate(bins):
    #     log.info(f" bin:{i} {b}")
    # log.info(f"#bins: {len(bins)} bins: {' '.join(bins)}")
    log.info(
        f"first fit #bins: {len(bins)} total waste: {total_waste(bins)} total stock: {total_stock(bins)}")
    # print(bins)
    write_bins(bins, 'first-fit')

    # first fit UNSORTED
    bins = first_fit(req)
    # print(*bins)
    # for i, b in enumerate(bins):
    #     log.info(f" bin:{i} {b}")
    # log.info(f"#bins: {len(bins)} bins: {' '.join(bins)}")
    log.info(
        f"first fit #bins: {len(bins)} total waste: {total_waste(bins)} total stock: {total_stock(bins)}")
    # print(bins)
    write_bins(bins, 'first-fit')

    # first firt SORTED
    req.sort(reverse=True)   # sort req for first fit decreasing
    bins = first_fit(req)
    # print(*bins)
    # for i, b in enumerate(bins):
    #     log.info(f" bin:{i} {b}")
    log.info(
        f"first fit decreasing #bins: {len(bins)} total waste: {total_waste(bins)} total stock: {total_stock(bins)}")
    # print(bins)
    write_bins(bins, 'ff-sorted')

    log.info('End')
