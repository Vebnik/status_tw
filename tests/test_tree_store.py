from data.items import items
from src.tree_store import TreeStore, Node


def test_get_all():
    store = TreeStore(items)

    assert items == store.get_all()


def test_get_item():
    store = TreeStore(items)
    test_node = Node(
        _id=items[7].get('id'),
        parents=items[7].get('parent'),
        _type=items[7].get('type'),
        children=[]
    )
    target_node = store.get_item(8)

    assert target_node.id == test_node.id and target_node.children == test_node.children


def test_get_children():
    store = TreeStore(items)
    test_node = Node(
        _id=items[7].get('id'),
        parents=items[7].get('parent'),
        _type=items[7].get('type'),
        children=[]
    )
    target_node = store.get_children(8)

    assert target_node == test_node.children


def test_get_all_parents():
    store = TreeStore(items)
    target_node = store.get_all_parents(8)

    assert [node.id for node in target_node] == [4, 2, 1]

