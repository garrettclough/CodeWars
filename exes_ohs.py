# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):

    o = s.lower().count('o')
    x = s.lower().count('x')

    if o == x : return True
    elif o != x : return False
    else:
        return True

#FIRST PASS
# def xo(s):
#     s = s.lower()
#     x_list = []
#     o_list = []
#     for i in s:
#         if i == 'x':
#             x_list.append(i)
#         elif i == 'o':
#             o_list.append(i)
#         else:
#             break
#     if len(x_list) == len(o_list):
#         return True
#     else:
#         return False
            