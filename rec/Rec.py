
def permuteString(s):
    return recPerm(list(s), 0)

def recPerm(s, i):
    if i == len(s):
        print ''.join(s)
    for index in range(i, len(s)):
        s[i], s[index] = s[index], s[i]
        recPerm(s, i + 1)
        s[i], s[index] = s[index], s[i]


permuteString('ABCD')
