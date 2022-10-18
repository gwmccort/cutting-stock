""" cutting stock using first fit """

import random

STOCK_LEN = 10


def first_fit(cuts):
    """ first fit """
    results = []  # {waste: , cuts: []}
    for cut in cuts:
        found = False
        for stock in results:
            if stock['waste'] >= cut:
                found = True
                stock['waste'] -= cut
                stock['cuts'].append(cut)

        if not found:
            results.append({'waste': STOCK_LEN - cut, 'cuts': [cut]})

    return results

    def print_results(results):
        print(f"#stock: {len(results)}")
        for r in results:
            print(f"waste: {r['waste']} cuts: {r['cuts']}")


if __name__ == '__main__':

    # random cut list (1:9)
    NUM_CUTS = 50
    cuts = [random.randrange(1, 10, 1) for i in range(NUM_CUTS)]
    # cuts = [1, 7, 3, 1, 4, 9, 2, 9, 9, 2, 9, 5, 4, 7, 6, 6, 7, 2, 1, 3, 1, 2, 7, 1, 9, 2,
    #         2, 2, 2, 6, 3, 4, 4, 2, 7, 9, 9, 4, 4, 1, 5, 8, 1, 4, 9, 1, 8, 7, 9, 8]

    results = first_fit(cuts)
    print(f"#stock: {len(results)}")

    cuts.sort(reverse=True)
    results = first_fit(cuts)
    print(f"#stock: {len(results)}")
