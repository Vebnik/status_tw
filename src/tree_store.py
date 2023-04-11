import logging


class Node:

    __slots__ = ('id', 'parents', 'children', 'type')

    def __init__(self, _id, parents, children, _type):
        self.id = _id
        self.parents = parents
        self.children = children
        self.type = _type

    def __str__(self) -> str:
        return f'{self.id} {self.type}'

    def __repr__(self) -> str:
        return f'{self.id} {self.type}'


class TreeStore:

    data: list[dict]
    node_list: list[Node] = []
    root: Node

    def __init__(self, data: list[dict]) -> None:
        try:
            self.data = data
            root = self._get_root()
            self.root = Node(_id=root.get('id'), parents=None, children=[], _type=None)
            self.node_list.append(self.root)

            for item in data[1:]:
                parent_node = self.get_item(item.get('parent'), self.root)
                new_node = Node(_id=item.get('id'), parents=parent_node, children=[], _type=item.get('type'))
                parent_node.children.append(new_node)
                self.node_list.append(new_node)

        except Exception as ex:
            logging.critical(ex)

    def get_all(self) -> list[dict]:
        """
        Возвращает изначальный массив элементов.
        """
        data = [
            {
                "id": node.id, "parent": node.parents.id, "type": node.type
            } for node in self.node_list[1:]
        ]
        data.insert(0, {"id": self.root.id, "parent": "root"})

        return data

    def get_item(self, _id, current_node: Node = None) -> Node | None:
        """
        Принимает id элемента и возвращает сам объект элемента.
        """

        if current_node is None:
            current_node = self.root

        if _id == 1:
            return self.root

        if current_node.id == _id:
            return current_node

        if current_node.children:
            for node in current_node.children:
                target_node = self.get_item(_id, node)
                if target_node:
                    return target_node

    def get_children(self, _id) -> list[Node] | list[None]:
        """
        Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
        чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив.
        """
        target_node = self.get_item(_id)

        if target_node:
            return target_node.children
        return []

    def get_all_parents(self, _id):
        """
        Принимает id элемента и возвращает массив из цепочки родительских элементов.
        """
        target_node = self.get_item(_id)
        parents = []

        if target_node is None:
            return []

        if target_node.parents:
            current_parents = target_node.parents
            parents.append(current_parents)

            while current_parents.parents:
                parents.append(current_parents.parents)
                current_parents = current_parents.parents
            return parents
        return []

    def _get_root(self) -> dict:
        for item in self.data:
            if item.get('parent') == 'root':
                return item
