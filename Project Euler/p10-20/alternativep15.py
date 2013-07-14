import numpy
 
table = numpy.zeros((21, 21), dtype=numpy.int64)
 
def rec(r, c):
    if table[r, c] != 0:
        return table[r, c]
    if r == 0 and c == 0:
        return 1
    rsum = 0
    csum = 0
    if r != 0:
        rsum = rec(r-1, c)
    if c != 0:
        csum = rec(r, c-1)
    table[r, c] = rsum + csum
    return rsum + csum
 
if __name__ == "__main__":
    n = int(raw_input("Enter n : "))
    print rec(n, n)
