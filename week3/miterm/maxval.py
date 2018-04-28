def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    if isinstance(t, int):
        return t
    else:

        return max_val(t[1:]) +

        # for b in t:
        #    if isinstance(b,tuple) or isinstance(b,list):
        #        return max_val(b)


value = max_val((5, (1, 2), [[1], [2]]))