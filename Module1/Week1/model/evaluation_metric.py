def evaluation(tp, fp, fn):
    if (not (is_int('tp', tp) and is_int('fp', fp) and is_int('fn', fn))) or (
            not (is_positive('tp', tp) and is_positive('fp', fp) and is_positive('fn', fn))):
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    print(f"precision is {precision}\n"
          f"recall is {recall}\n"
          f"f1 is {f1}")


def is_int(name, val):
    if not isinstance(val, int):
        print(f"{name} must be int")
        return False
    return True


def is_positive(name, val):
    if val <= 0:
        print(f"{name} must be greater than zero")
        return False
    return True
