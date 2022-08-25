#!/usr/bin/python3
<<<<<<< HEAD

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
=======
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
if argc < 2:
    print("{} arguments.".format(argc - 1))
else:
    if argc == 2:
        print("{} argument:".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))
    for n in range(1, argc):
        print("{}: {}".format(n, argv[n]))
>>>>>>> 96b768bfdec1c700b431ed01245443064e60230e
