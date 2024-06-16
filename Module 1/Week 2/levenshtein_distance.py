def levenshtein_distance(inp, target):
    # Step 1: Create MxN matrix
    matrix = [[None] * (len(target) + 1) for _ in range(len(inp) + 1)]

    # Step 2: Complete 1st row and 1st column
    matrix[0] = list(range(len(target) + 1))
    for i in range(1, len(inp) + 1):
        matrix[i][0] = i

    # Step 3: Complete the matrix
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            del_entry = matrix[r - 1][c] + 1
            ins_entry = matrix[r][c - 1] + 1
            sub_entry = matrix[r - 1][c - 1]
            if inp[r - 1] != target[c - 1]:
                sub_entry += 1
            matrix[r][c] = min(del_entry, ins_entry, sub_entry)

    # Step 4: Return the Levenshtein distance
    return matrix[-1][-1]


print(levenshtein_distance('yu', 'you'))
