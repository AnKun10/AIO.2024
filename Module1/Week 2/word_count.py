def word_count(filename):
    f = open(filename, 'r')
    ans = {}
    for line in f:
        words = line.split()
        for word in words:
            if word not in ans:
                ans[word] = 1
            else:
                ans[word] += 1
    f.close()
    return ans


filename = "P1_data.txt"
print(word_count(filename))
