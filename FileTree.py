# Convert strings of file paths into a tree structure
from collections import defaultdict

class FileTree:
    def __init__(self):
        self.file_mark = '<file>'
        self.tree = self._init_subtree()
        self.layout = ''

    def _init_subtree(self):
        return defaultdict(dict, ({self.file_mark: []}))

    def build_subtree(self, tree, path):
        path_parts = path.split('/', 1)
        if len(path_parts) == 1:
            tree[self.file_mark].append(path)
        else:
            node, other = path_parts
            if node not in tree:
                tree[node] = self._init_subtree()
            self.build_subtree(tree[node], other)

    def build_tree(self, input_list):
        for path in input_list:
            self.build_subtree(self.tree, path)
    
    # Version 1, indent without hierarchy label
    def prettify(self, tree, indent_level=0):
        indent = '    ' * indent_level
        for node in tree:
            if node == self.file_mark:
                if tree[node] == ['']:
                    self.layout += (indent + '<empty>' + '\n')
                else:
                    for f in tree[node]:
                        self.layout += (indent + f + '\n')
            else:
                self.layout += (indent + node + '/' + '\n')
                self.prettify(tree[node], indent_level + 1)

    def __str__(self):
        self.layout = ''
        self.prettify(self.tree)
        return self.layout
        
    # Version 2, indent with hierarchy label
    def prettify(self, tree, indent):
        for node in tree:
            if node == self.file_mark:
                if tree[node] == ['']:
                    self.layout += (indent + '<empty>' + '\n')
                else:
                    for f in tree[node]:
                        self.layout += (indent + f + '\n')
            else:
                self.layout += (indent + node + '/' + '\n')
                self.prettify(tree[node], indent.replace('L', ' ') + 'L   ')

    def __str__(self):
        self.layout = ''
        self.prettify(self.tree, '    ')
        return self.layout

inputs = '''dir/file
dir/dir2/file2
dir/file3
dir2/alpha/beta/gamma/delta
dir2/alpha/beta/gamma/delta/
dir3/file4
dir3/file5'''
input_list = inputs.split('\n')
a = FileTree()
a.build_tree(input_list)
print(a)
