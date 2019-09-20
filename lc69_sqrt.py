# bit manipulation
def mySqrt(x):
    mask = 1 << 15
    res = 0
    while mask > 0:
        next = res or mask
        if next <= x / next:
            res = next
        mask >>= 1
    return res

print(mySqrt(26))