def get_even(numb_list):
    for x in numb_list:
        if x % 2 != 0:
            numb_list.remove(x)
    return numb_list
dummy_list = [1,2,3,4,5,6]
print(dummy_list)
print(get_even(dummy_list))