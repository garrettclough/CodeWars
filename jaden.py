
string = "How can the world be real if our eyes aren't real?"
list = string.split()
title_list = [word.capitalize() for word in list]
print(" ".join(title_list))