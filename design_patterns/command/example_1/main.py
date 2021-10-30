from read_file import ReadFile
from create_file import CreateFile
from rename_file import RenameFile


def main():
    orig_name, new_name = './data/original.txt', './data/other.txt'
    commands = (
        CreateFile(orig_name),
        ReadFile(orig_name),
        RenameFile(orig_name, new_name)
    )
    [c.execute() for c in commands]

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print("Error", str(e))


if __name__ == "__main__":
    main()
