'''Let's play with the *args pattern.
Create a function named multiply that takes any number of arguments. Return the product (multiplied value) of all of the supplied arguments. The type of argument shouldn't matter.
Slices might come in handy for this one.'''

def multiply(*nums):
    x = len(nums) - 1
    total = nums[x] 
    while x > 0:
        x -= 1
        total = total * nums[x]
    return total
    