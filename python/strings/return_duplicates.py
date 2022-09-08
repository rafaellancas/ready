def return_duplicates(the_list):
    dups = []
    a_ser = set()
    for item in the_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)
        if length_one == length_two:
            dups.append(item)
    return dups
    