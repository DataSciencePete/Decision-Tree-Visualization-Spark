
from decision_tree import tree_json

with open('data/decision_tree.txt') as fin:
    tree_text = fin.read()

tree_json(tree_text)
