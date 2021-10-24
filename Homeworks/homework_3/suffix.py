def suffix():
    seq = tuple(float(x) for x in input().split())
    seq_copy = list(reversed(seq))
    new_seq = []
    while seq_copy:
        new_seq.append(sum(seq_copy))
        seq_copy.pop()
    return new_seq


print(suffix())
