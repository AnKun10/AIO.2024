def count_chars(inp):
    ans = {}
    for c in inp:
        if c in ans:
            ans[c] += 1
        else:
            ans[c] = 1
    return ans
