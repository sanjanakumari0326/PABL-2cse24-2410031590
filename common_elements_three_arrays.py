def common_elements(a, b, c):
    i = j = k = 0
    result = []
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1; j += 1; k += 1
        else:
            minimum = min(a[i], b[j], c[k])
            if a[i] == minimum: i += 1
            if b[j] == minimum: j += 1
            if c[k] == minimum: k += 1
    return result if result else [-1]
