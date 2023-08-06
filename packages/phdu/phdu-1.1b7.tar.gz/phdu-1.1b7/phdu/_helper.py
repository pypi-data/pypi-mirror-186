"""
Helper functions.
"""

def sequence_or_stream(x, maxlen=None):
    """
    if maxlen is None => returns a stream
    else              => returns sequence of elements of x repeated up to the desired len.
    
    Attrs:
        - x (iterable)
        - maxlen (int|None)
    """
    x = list(x)
    x_len = len(x)
    if maxlen is None: # stream
        def stream():
            n = 0
            while True:
                yield x[n]
                n = (n + 1) % x_len
        return stream()
    else:
        mod = maxlen % x_len
        return x * (maxlen // x_len) + ([] if mod == 0 else x[:mod])

def getopt_printer(opts):
    """Prints getopt input in a readable way."""
    print('\n'.join(f'{opt} => {arg}' for opt, arg in (("Args", "Values"), *opts)))