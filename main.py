#!/bin/python

from data.items import items
from src.tree_store import TreeStore


def main() -> None:
    store = TreeStore(items)

    print(store.get_item(8))
    print(store.get_children(4))
    print(store.get_all_parents(7))
    print(store.get_all())


if __name__ == '__main__':
    main()
