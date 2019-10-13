def permute_original(a, lo):
    hi = len(a)
    if lo == hi:
        print(a)
        return
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]


# Q1
def permute(a, lo):
    hi = len(a)
    if lo == hi:
        if a[0] != 'A' and a[1] != 'B' and a[2] != 'C' and a[3] != 'D':
            print(a)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]


# Q3
def permute2(a, lo):
    hi = len(a)
    indexA = a.index('A')
    indexB = a.index('B')
    indexC = a.index('C')
    indexD = a.index('D')
    if lo == hi:
        if abs(indexA - indexB) == 1 and abs(indexC - indexD) > 1:
            print(a)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute2(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]


# Q2


# Q4
# def combination(c, d, lo):
#    hi = len(c)
#    if lo == hi:
#        if len(d) == 3:
#            if 'A' in d and 'B' in d:
#                print(d)
#            if 'C' in d and 'D' not in d:
#                print(d)
#            if 'D' in d and 'C' not in d:
#                print(d)
#    else:
#        e = d[:]
#        d.append(c[lo])
#        combination(c, d, lo + 1)
#        combination(c, e, lo + 1)


def combination(c, d, lo):
    hi = len(c)
    if lo == hi:
        if len(d) == 3:
            if 'A' in d and 'B' in d:
                print(d)
            if 'C' in d and 'D' not in d:
                print(d)
            if 'D' in d and 'C' not in d:
                print(d)
    else:
        e = d[:]
        d.append(c[lo])
        combination(c, d, lo + 1)
        combination(c, e, lo + 1)


#def subsets(remain, chosen):
#    if len(remain) == 0:
#        print(chosen)
#    else:
#        remain = remain[1:]
#        subsets(remain, chosen)
#        subsets(remain, chosen + remain[0])


# Q5
def sub_sets(a, b, lo):
    hi = len(a)
    if lo == hi:
        if sum(b) == 50:
            print(b)

    else:
        c = b[:]
        b.append(a[lo])
        sub_sets(a, b, lo + 1)
        sub_sets(a, c, lo + 1)


def main():
    a = ['A', 'B', 'C', 'D']
    # permute(a, 0)
    # print()
    # b = ['A', 'B', 'C', 'D', 'E']
    # permute2(b, 0)
    # print()
    c = ['A', 'B', 'C', 'D', 'E', 'F']
    d = []
    # print()
    combination(c, d, 0)
    print()
    # e = [15, 9, 30, 21, 19, 3, 12, 6, 25, 27]
    # f = []
    # print(sub_sets(e, f, 0))
    permute_original(a, 0)
    # z = []
    #subsets(c, z)
main()
