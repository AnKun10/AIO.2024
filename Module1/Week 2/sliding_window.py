def is_positive_int(numb):
    if numb >= 1 and type(numb) is int:
        return True
    return False


def sliding_window(arr, k):
    if not is_positive_int(k):
        print("Invalid k.")
        return None
    ans = []
    for i in range(len(arr) - k + 1):
        ans.append(max(arr[i:i + k]))
    return ans


lst = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
print(sliding_window(lst, 3))
