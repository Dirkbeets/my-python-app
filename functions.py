FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


print(__name__)
if __name__ == "__main__":
    print(5 * 35)
    print(get_todos())

#
# def hernummer_todos(todos):
#     genummerde_todos = []
#     for i, todo in enumerate(todos, start=1):
#         if '-' in todo:
#             todo = todo.split('-', 1)[1].strip
#             genummerde_todos.append(f"{i} - {todo}")
#             return genummerde_todos