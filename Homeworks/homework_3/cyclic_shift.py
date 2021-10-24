def shift():
    n = int(input("Length of sequence: "))
    seq = list()
    for _ in range(n):
        seq.append(int(input("Number: ")))
    k = int(input("Number of shifts: "))
    new_seq = seq[:]
    i = 0
    while i < len(seq):
        if i + k < len(seq):
            new_seq[i + k] = seq[i]
        else:
            new_seq[(i + k) % len(seq)] = seq[i]
        i += 1
    return new_seq


print(shift())
