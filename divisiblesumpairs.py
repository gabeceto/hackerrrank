def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(len(ar)):
        for j in range(i):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
                
    return result