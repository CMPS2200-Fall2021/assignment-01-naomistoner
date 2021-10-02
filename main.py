"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        return (foo(x-1) + foo(x-2))

def longest_run(mylist, key):
    counter = 0
    prev = mylist[0]
    for i in mylist:
        if i == key:
            if prev == key:
                counter += 1
        prev = i
    return counter


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def longest_helper(left, right):
    #simply adding l1 and l2 gives the total num of keys

    isEntTot = False
    longestMid = 0
    #This does work if the entire thing is 12 or not 12
    if left.is_entire_range == True and right.is_entire_range == True:
        leftTot = left.left_size + right.left_size
        rightTot = right.right_size + left.right_size
        longestTot = left.longest_size + right.longest_size
        isEntTot = True
    elif right.is_entire_range == True and left.right_size > 0:
        # I may have to deal with a case where the left has a longer run
        # 1 12  12 12
        leftTot = left.left_size

        rightTot = right.longest_size + left.right_size
        if rightTot > leftTot:
            longestTot = rightTot
        #otherwise pick longest side
        else:
            longestTot = leftTot
    elif left.is_entire_range == True and right.left_size > 0:

        rightTot = right.right_size

        leftTot = left.longest_size + right.left_size
        if leftTot > rightTot:
            longestTot = leftTot
        #otherwise pick longest side
        else:
            longestTot = rightTot

    elif left.longest_size > 0 or right.longest_size > 0:
        #determine if there is a middle run

        #for nothing down the middle
        if (left.right_size == 0 or right.left_size == 0):
            leftTot = left.left_size
            rightTot = right.right_size

            if right.longest_size > left.longest_size:
                longestTot = right.longest_size
            else:
                longestTot = left.longest_size
        #this is if there is a run in the middle
        #for something down the middle
        else:
            midTot = left.right_size + right.left_size
            leftTot = left.left_size
            rightTot = right.right_size
            if midTot > leftTot and midTot > rightTot:
                longestTot = midTot
            else:
                if leftTot > rightTot:
                    longestTot = leftTot
                else:
                    longestTot = rightTot
    #if everything is 0
    else:
        leftTot = 0
        rightTot = 0
        longestTot = 0
    if left.longest_size > longestTot:
        return Result(leftTot, rightTot, left.longest_size, isEntTot)
    if right.longest_size > longestTot:
        return Result(leftTot, rightTot, right.longest_size, isEntTot)
    #print(Result(leftTot, rightTot, longestTot, isEntTot))
    return Result(leftTot, rightTot, longestTot, isEntTot)

def longest_run_recursive(mylist, key):

    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1,1,1,True)
        else:
            return Result(0,0,0,False)
    else: #recursive case
        mid = len(mylist)//2
        left = longest_run_recursive(mylist[:mid], key)
        right = longest_run_recursive(mylist[mid:], key)
        #moved this down here
        #attempting with one res for each side
        return longest_helper(left, right)
        return l1 + l2

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([2,2,2,8,12,12,12,0,12,1], 2) == 3

print(longest_run_recursive([2,1,2,1,2,2,1,2,2,2,1,1], 2))
