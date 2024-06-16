def count_chars(inp):
    ans = {}
    for c in inp:
        if c in ans:
            ans[c] += 1
        else:
            ans[c] = 1
    ans = sorted(ans.items(), key=lambda x: x[1], reverse=False)
    return ans


string = 'Happiness'
print(count_chars(string))
