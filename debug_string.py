
from decision_tree import tree_json, tidy_tree

with open('data/decision_tree.txt') as f:
    tree_text = f.read()

tree_text = tidy_tree(tree_text, ['static_mean', 'sensitive_mean', 'btp_mean'])

tree_json(tree_text)
