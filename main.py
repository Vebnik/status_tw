#!/bin/python

from data.items import items
from src.tree_store import TreeStore


def main() -> None:
    store = TreeStore(items)

    # print(store.get_item(8))
    # print(store.get_children(4))
    # print('Search', store.get_all_parents(8))
    print(store.get_all())
    print(items)


if __name__ == '__main__':
    main()
