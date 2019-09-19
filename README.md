# count-the-list-inside-the-list-using-function


def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
        else:
            count = 0
    return count

mixer = [1,2,3,4,[7,5,4,2,5],[2,3,5,8,5,4],[9,6,5,3,6]]
print(sublist_counter(mixer))
