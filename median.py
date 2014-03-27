lst = raw_input("please enter a list of numbers surrounded by brackets with commas in between each number")
def median(lst):
    sort = sorted(lst)
    length = len(sort)
    if length % 2 == 0:
        result = (sort[length/2] + sort[length/2-1]) / 2.0
    else:
        result = sort[length/2]
    print "the median is " + str(result)
median(lst)
