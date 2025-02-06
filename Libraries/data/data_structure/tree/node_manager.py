

"""
as base support for tree
"""
class node_manager:
    """ Template model of Gaia """
    id = "node_manager"

    def __init__(self, id, left_node = None, right_node = None, depth = None, data = None):
        self.id = id
        self.left_node = left_node
        self.right_node = right_node
        self.data = data
        self.depth = depth
        print("_gaia object [%s] is born\n" % self.id)


    def add_node_objects_to_node (self, left_node = None, right_node = None):
        self.left_node = left_node
        self.right_node = right_node

        return self

    def add_data_to_node (self, data):
        self.data = data

        return self
    def add_depth_data_to_node (self, depth):
        self.depth = depth

        return self

    def get_data_of_node_by_id (self, root, id):
        search_status = 'not_found'
        data, search_status = self.search_inorderTraversal(root, id)

        return data

    # search Inorder traversal
    # Left -> Root -> Right
    def search_inorderTraversal(self, root, id):
        search_status = 'not_found'
        res = []
        if root:
            if (root.id == id):
                search_status = 'found'
                print('================')
                print('Found')
                print('================')
                print('id: ', root.id)
                print('data: ', root.data)
                print('depth: ', root.depth)
                print('================')
                return root.data, search_status
            else:
                print('id: ', root.id)
                print('data: ', root.data)
                print('depth: ', root.depth)
                search_status = 'not_found'

            if (search_status == 'not_found'):
                res, search_status = self.search_inorderTraversal(root.left_node, id)
            else:
                return res, search_status

            if (search_status == 'not_found'):
                res, search_status = self.search_inorderTraversal(root.right_node, id)
            else:
                return res, search_status

        return res, search_status

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left_node)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right_node)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left_node)
            res = res + self.PreorderTraversal(root.right_node)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left_node)
            res = res + self.PostorderTraversal(root.right_node)
            res.append(root.data)
        return res

    # print the Tree
    def print_tree(self):
        if self.left_node:
            self.left_node.print_tree()
        print(self.data),
        if self.right_node:
            self.right_node.print_tree()

    def who_am_i(self):  #
        """ Introspection """
        self.line_storage = [];

        print("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <node_manager>"
    print("=====[" + id + " Start]===== \n")

    root = node_manager('0')  #
    root.add_depth_data_to_node('0')
    root.add_data_to_node('0') # root.data = '0'
    """
    root.left = node_manager('0.0')
    root.left.data = "0.0"
    root.right = node_manager('0.1')
    root.right.data = "0.1"
    
    root.left.left = node_manager('0.0.0')
    root.left.left.data = "0.0.0'"
    root.left.right = node_manager('0.0.1')
    root.left.right.data = '0.0.1'
    """
    root_left, root_right = node_manager('0.0'), node_manager('0.1')
    root_left.add_depth_data_to_node('1')
    root_right.add_depth_data_to_node('1')
    root_left.add_data_to_node('0.0')
    root_right.add_data_to_node('0.1')
    root.add_node_objects_to_node(root_left, root_right)

    root_left_left, root_left_right = node_manager('0.0.0'), node_manager('0.0.1')
    root_left_left.add_depth_data_to_node('2')
    root_left_right.add_depth_data_to_node('2')
    root_left_left.add_data_to_node('0.0.0')
    root_left_right.add_data_to_node('0.0.1')
    #root_left_right.add_data_to_node('found me yet?')
    root_left.add_node_objects_to_node(root_left_left, root_left_right)

    root_left_left_left, root_left_left_right = node_manager('0.0.0.0'), node_manager('0.0.0.1')
    root_left_left_left.add_depth_data_to_node('3')
    root_left_left_right.add_depth_data_to_node('3')
    root_left_left_left.add_data_to_node('0.0.0.0')
    root_left_left_right.add_data_to_node('0.0.0.1')
    root_left_left.add_node_objects_to_node(root_left_left_left, root_left_left_right)

    root_left_right_left, root_left_right_right = node_manager('0.0.1.0'), node_manager('0.0.1.1')
    root_left_right_left.add_depth_data_to_node('3')
    root_left_right_right.add_depth_data_to_node('3')
    root_left_right_left.add_data_to_node('0.0.1.0')
    # root_left_right_right.add_data_to_node('0.0.1.1')
    root_left_right_right.add_data_to_node('found me yet?')
    root_left_right.add_node_objects_to_node(root_left_right_left, root_left_right_right)

    print(root.inorderTraversal(root))
    root.print_tree()

    id_to_hunt = '0.0.1.1' # '0.0.1' # '0.1' # '0.0.0.1' # '0.0.x' #
    data = root.get_data_of_node_by_id(root, id_to_hunt)

    if (len(data) != 0):
        print('Data found for id_to_hunt: ', id_to_hunt)
        print(data)
    else:
        print('Data not found for id_to_hunt: ', id_to_hunt)

    # import _Gaia._gaia
    # help(node_manager) # introspect

    print("=====[" + id + " End]===== \n");

"""
# version: 2018-06-05_0050hr_20sec
"""