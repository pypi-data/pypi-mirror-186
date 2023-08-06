"""
Name: _trees.py
Author: Oliver B. Gaither
Date: 1/16/2023
Description: tree-based data structures
"""

class _bstnode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent: _bstnode = None
        self.left: _bstnode = None
        self.right: _bstnode = None
        self.height = 0
    
    def find(self, k):
        if k == self.key:
            return self
        if k < self.key:
            if self.left is None: return None
            return self.left.find(k)
        else:
            if self.right is None: return None
            return self.right.find(k)
    
    def find_min(self):
        cur = self
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def find_max(self):
        cur = self
        while cur.right is not None:
            cur = cur.right
        return cur
    
    def successor(self):
        if self.right is not None:
            return self.right.find_min()
    
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max()
    
    def insert(self, node):
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)
    
    def delete(self):
        """
        delete this current node
        :return:
        """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            
            return self
        else:  # has both children
            # get successor node
            tmp = self.successor()
            self.key, tmp.key = tmp.key, self.key  # swap keys
            return tmp.delete()
    
    def __str__(self):
        if self.key == self.val:
            return str(self.key)
        
        return str(self.val)


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class bst:
    def __init__(self):
        self.root = None
    
    def insert(self, k, v=None):
        if v is None:
            v = k
        node = _bstnode(k, v)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node
    
    def find(self, k):
        if self.root is None: return None
        return self.root.find(k)
    
    def remove(self, k):
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            tmp = _bstnode(0)
            tmp.left = self.root
            self.root.parent = tmp
            deleted = self.root.delete()
            self.root = tmp.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()
    
    def rotateLeft(self, x):
        """ perform a left rotation about a given node """
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)
    
    def rotateRight(self, x):
        """ perform a right rotation about a given node """
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)
    
    @staticmethod
    def inorder(root):
        """
        returns an iterable of an inorder sorting
        of the binary search tree rooted at root
        :param root: root node
        :return: iterable
        """
        data = list()
        
        def _inorder(node, nodes):
            if node is None: return
            _inorder(node.left, nodes)
            nodes.append(node)
            _inorder(node.right, nodes)
        
        _inorder(root, data)
        
        return iter(data)
    
    @staticmethod
    def preorder(root):
        """
        returns an iterable of an preorder sorting
        of the binary search tree rooted at root
        :param root: root node
        :return: iterable
        """
        data = list()
        
        def _preorder(node, nodes):
            if node is None: return
            nodes.append(node)
            _preorder(node.left, nodes)
            _preorder(node.right, nodes)
        
        _preorder(root, data)
        return iter(data)
    
    @staticmethod
    def postorder(root):
        """
        returns an iterable of an postorder sorting
        of the binary search tree rooted at root
        :param root: root node
        :return: iterable
        """
        data = list()
        
        def _postorder(node, nodes):
            if node is None: return
            _postorder(node.left, nodes)
            _postorder(node.right, nodes)
            nodes.append(node)
        
        _postorder(root, data)
        
        return iter(data)
    
    def __str__(self):
        return ', '.join(map(str, bst.preorder(self.root)))


class splay(bst):
    def __init__(self):
        super(splay, self).__init__()
    
    def insert(self, element, value=None):
        node = bst.insert(self, element, value=None)
        self.root = self.splay(node)
    
    def get(self, k):
        node = bst.find(self, k)
        self.root = self.splay(node)
        return None if node is None else node.val
    
    def __contains__(self, item):
        return self.find(item) != None
    
    def splay(self, node):
        while node.parent is not None:
            x = node
            y = node.parent
            z = y.parent
            if y is self.root:  # node does not have grandparent
                if z is not None:
                    raise RuntimeError("splay.splay(x): node relationship error")
                if x is y.left:
                    self.rotateRight(node.parent)
                else:
                    self.rotateLeft(node.parent)
            
            else:  # current node has a grand parent
                # Case 1 - x is left child of y, and y is also left child of z (Zig zig right right)
                if ((x is y.left) and (y is z.left)):
                    self.rotateRight(node.parent.parent)
                    self.rotateRight(node.parent)
                # Case 3 - x is the right child of y, and y is right child of z (zig zig left left)
                elif x is y.right and y is z.right:
                    self.rotateLeft(node.parent.parent)
                    self.rotateLeft(node.parent)
                
                # Case 2 - x is left child of y, but y is right child of z (Zig Zag right left)
                elif x is y.left and y is z.right:
                    self.rotateRight(node.parent)
                    self.rotateLeft(node.parent)
                
                # Case 4 - x is right of y and y is left of z (zig zag left right)
                else:
                    self.rotateLeft(node.parent)
                    self.rotateRight(node.parent)
        return node
