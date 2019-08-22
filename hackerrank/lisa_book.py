N, K = map(int, input().split())
T = list(map(int, input().split()))
cnt = 0 # special problems
i = 0   # chapter number
j = 1   # page number
m = 1   # problem number
while i < N:
    if m <= j and j <= min(m + K - 1, T[i]):
        cnt += 1
        print("special",cnt)
    j += 1
    m += K
    print("page",j)
    print("problem",m)
    if m > T[i]: # next chapter
        i += 1
        m = 1
print(cnt)
