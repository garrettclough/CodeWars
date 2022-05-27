# TEST CASES
# integers = [2, 4, 6, 8, 10, 3]

# integers = [2, 4, 0, 100, 4, 11, 2602, 36]

def find_outlier(integers):
    evenlist = [i for i in integers if i % 2 == 0]
    oddlist = [i for i in integers if i % 2 != 0]
    return evenlist[0] if len(evenlist) == 1 else oddlist[0]

# print(find_outlier(integers))