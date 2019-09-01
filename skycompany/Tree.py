class Tree:
    root = {
        'value': None,
        'children': []
    }
    def __init__(self, val):
        self.root = self._create_node(val)
        return self.root

    def _create_node(self, val):
        return {
                'value': val,
                'children': []
                }

    def create_child(self, val):
        new_node = self._create_node(val)
        self.root.append(new_node)
        return new_node

    def print_tree(node):
        print(node['value'])
        if len(node['children'] == 0):
            return None
        print('\/\/')
        for child_node in node['children']:
            self.print_tree(child_node)

    def traverse_bfs(node):





if __name__ == '__main__':
    root = Tree(3)
    root.create_child(2)
    Tree.create_child(root, 4)
    Tree.print_tree(root)
