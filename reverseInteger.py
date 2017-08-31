def reverse(x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    print ((r < 2 ** 31) * s * r)
reverse(-123)

# print ('asdd'[::-1])

