from .array_stack import ArrayStack

def reverse_file(filename):
    """Overwrite given file with its content line-by-line reverse."""
    filestack = ArrayStack()

    with open(filename) as original:
        for line in original:
            filestack.push(line.rstrip('\n'))

    with open(filename, 'w') as output:
        while not filestack.is_empty():
            output.write(filestack.pop() + '\n')