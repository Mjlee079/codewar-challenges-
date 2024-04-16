def find_it(seq):
    from collections import Counter
    count = Counter(seq)

    for num in count:
        if count[num] % 2 != 0:
            return num
    return None