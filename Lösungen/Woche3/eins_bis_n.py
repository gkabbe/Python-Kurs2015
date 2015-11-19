def helper_range(i, n):
    print i
    if i < n:
        helper_range(i+1, n)


def rekursive_range(n):
    helper_range(1, n)
