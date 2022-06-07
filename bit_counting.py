def count_bits(n):
    bits = f'{n:08b}'
    res = [int(x) for x in str(bits)]
    for i in res:
        x += i
    return(x)


# n = 4
# bits = f'{n:08b}'

# print(bits)git

# res = [int(x) for x in str(bits)]

# print(res)

# x = 0
# for i in res:
#     x += i

# print(x)