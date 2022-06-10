def tribonacci(signature, n):
    if n < 1:
        return []
    if n < len(signature):
        return signature[0:n]
    counter = 0
    sequence = signature[:]
    while counter <= n - 4:
        nextNumber = sum(sequence[counter:counter+3])
        sequence.append(nextNumber)
        counter += 1
    return sequence