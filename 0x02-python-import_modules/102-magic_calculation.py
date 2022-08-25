<<<<<<< HEAD
#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

=======
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
>>>>>>> 96b768bfdec1c700b431ed01245443064e60230e
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
<<<<<<< HEAD
        return (c)

    else:
        return(sub(a, b))
=======
        return(c)

    return(sub(a, b))
>>>>>>> 96b768bfdec1c700b431ed01245443064e60230e
