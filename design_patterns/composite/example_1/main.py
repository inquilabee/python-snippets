"""Composite pattern

Adapted from: https://github.com/jackdbd/design-patterns/blob/master/composite.py
"""

from composite import Composite
from leaf import Leaf


def main():
    """
    Make this directory structure.

    /
        hello.txt
        readme.txt
        home
            notes.txt
            todo.txt
            documents
                draft.txt
    """

    root = Composite("/")
    dir_1 = Composite("home")
    dir_2 = Composite("documents")

    leaf_0 = Leaf("hello.txt")
    leaf_1 = Leaf("readme.txt")
    leaf_2 = Leaf("notes.txt")
    leaf_3 = Leaf("todo.txt")
    leaf_4 = Leaf("draft.txt")

    root.append_child(leaf_0)
    root.append_child(leaf_1)
    root.append_child(leaf_1)  # Add again to same parent? No errors.

    root.append_child(dir_1)

    dir_1.append_child(leaf_2)
    dir_1.append_child(leaf_3)
    dir_1.append_child(dir_2)

    # dir_1.append_child(leaf_1)  # Add again to another parent? Error.

    dir_2.append_child(leaf_4)

    print("Traverse the entire directory tree")
    root.traverse()
    print()

    print("Move documents to root")
    # run either of the two statements below
    dir_2.detach()  # the child knows/finds their parent
    # dir_1.remove_child(dir_2) # Explicitly mention parent

    root.append_child(dir_2)
    root.traverse()

    print('Remove "todo.txt" and traverse the tree once again')
    dir_1.remove_child(leaf_3)
    root.traverse()

    print('Remove "home" and traverse the tree once again')
    root.remove_child(dir_1)
    root.traverse()


if __name__ == "__main__":
    main()
