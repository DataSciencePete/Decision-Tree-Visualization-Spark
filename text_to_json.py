
from decision_tree import tree_json, tidy_tree
import sys

with open(sys.argv[1]) as f:
    tree_text = f.read()

tree_text = tidy_tree(tree_text, ['static_mean', 'sensitive_mean', 'btp_mean', 'num_neighbours'])

tree_json(tree_text, 'data/structure.json')
