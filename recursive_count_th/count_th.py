'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # setting the target
    target = 'th'
    # if length of the word is less than length of target
    # it can't contain the target
    if len(word) < 2:
        return 0
    # checks the beginning of the word for target
    # and if it has the target value, adds 1 to the counter and recalls the function
    # with the beginning of the word moved up 1
    else:
        if word[:2] == target:
            return count_th(word[1:]) +1
        if word[:2] != target:
            return count_th(word[1:])

# def prob(n):
#     sum = 0
#     for i in range(n): # this is linear
#       j = 1            # this is constant
#       while j < n:     
#         j *= 2         # j gets multiplied by 2
#         sum += 1
#         print(i, j, sum)

# prob(5)
# prob(10)