
def quantum_splitter(mylist):
    lst = [0, 0, 0, 0]

    for element in mylist:
        for i in range(4):
            if element == i:
                lst[i] += 1
                break
    final_list = []

    while lst[0] != 0 or lst[1] != 0 or lst[2] != 0 or lst[3] != 0:
        for i in range(4):
            if lst[i] != 0:
                final_list.append(i)
                lst[i] -= 1
    return final_list