import os

verbose = True


def delete_file(path):
    if verbose:
        print(f"deleting file {path}")
    os.remove(path)
