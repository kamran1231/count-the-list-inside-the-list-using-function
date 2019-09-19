
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
        else:
            count = 0

mixer = [1,2,3,4,[8,7,5,3],[9,6,3,6],[2,6,8,4]]
print(sublist_counter(mixer))