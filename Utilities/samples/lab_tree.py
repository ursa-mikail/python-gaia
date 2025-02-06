from ete3 import Tree, TreeStyle

t = Tree()
t.populate(10, random_branches=True)
ts = TreeStyle()
ts.show_leaf_name = True
# ts.rotation = 90 # -30
ts.show_branch_length = True
ts.show_branch_support = True
t.show(tree_style=ts)

t.populate(30)
ts = TreeStyle()
ts.show_leaf_name = True
ts.mode = "c"
ts.arc_start = -180 # 0 degrees = 3 o'clock
ts.arc_span = 180
t.show(tree_style=ts)

# ref: http://etetoolkit.org/docs/2.3/tutorial/tutorial_drawing.html

rand_data = 'ABCDEFGHIJKL' # "((((a,b), c), d), (e,f));"

t = Tree()
t.populate(8, names_library=list(rand_data), random_branches=True)

print(t.get_ascii(attributes=['name', 'support'], show_internal=True))


ts = TreeStyle()
ts.show_branch_length = True # show branch length
ts.show_branch_support = True # show support

# rotate the tree by 30 degree
ts.rotation = -30
# t.render('tree2.png', tree_style=ts)
ts.show_branch_length = True
ts.show_branch_support = True
t.show(tree_style=ts)

# https://mrnoutahi.com/2016/01/09/Tree-manipulation-with-ETE/
# http://etetoolkit.org/docs/latest/tutorial/tutorial_trees.html

# Loads a tree with internal node names
t = Tree("(1.0:22,(2.1:1,(3.1:1,3.2:1)Internal_1:3.0)Internal_2:2.0)Root;", format=1)

# And prints its newick using the default format

print (t.write()) # (A:1.000000,(B:1.000000,(E:1.000000,D:1.000000)1.000000:0.500000)1.000000:0.500000);

# To print the internal node names you need to change the format:

print (t.write(format=1)) # (A:1.000000,(B:1.000000,(E:1.000000,D:1.000000)Internal_1:0.500000)Internal_2:0.500000);

# We can also write into a file
t.write(format=1, outfile="new_tree.nw")
ts = TreeStyle()
ts.show_branch_length = True # show branch length
ts.show_branch_support = True # show support

ts.rotation = 90
# t.render('tree2.png', tree_style=ts)
ts.show_branch_length = True
ts.show_branch_support = True
t.show(tree_style=ts)