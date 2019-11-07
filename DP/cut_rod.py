def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q


# Top (p, n)down DP solution
def memoized_cut_rod(p, n):
    r = [i for i in range(n+1)]
    for i in range(n+1):
        r[i] = float('-inf')
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q


# Bottom up DP solution
def bottom_up_cut_rod(p, n):
    r = [i for i in range(n + 1)]
    r[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p, n):
    r = [i for i in range(n+1)]
    s = [i for i in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print(cut_rod(p, 10))
print(memoized_cut_rod(p, 10))
print(bottom_up_cut_rod(p, 10))

print(extended_bottom_up_cut_rod(p, 10))

print_cut_rod_solution(p, 10)
