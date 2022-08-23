def birthday(s, d, m):
    result = 0
    nums = None
    for i in range(len(s)):
        if sum(s[i:(i+m)]) == d:
            result +=1

    return result