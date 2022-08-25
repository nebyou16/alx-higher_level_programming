#!/usr/bin/python3
<<<<<<< HEAD

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
=======
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    sum = 0
    for i in range(1, n):
        sum += int(sys.argv[i])
    print(sum)
>>>>>>> 96b768bfdec1c700b431ed01245443064e60230e
