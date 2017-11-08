'''Let's play with the *args pattern.
Create a function named multiply that takes any number of arguments. Return the product (multiplied value) of all of the supplied arguments. The type of argument shouldn't matter.
Slices might come in handy for this one.'''

#Revised function
def multiply(*nums):
    total = 1
    for num in nums:
        total *= num
    return total

#If you use slices maybe? (the function is correct--but don't know if that's what he meant. https://teamtreehouse.com/community/slices-issue https://teamtreehouse.com/community/is-this-how-you-would-use-slices-in-the-twople-challenge
def multiply(*nums):
    total = nums[0]
    for num in nums[1:]:
        total *= num
    return total

#my original function
def multiply(*nums):
    x = len(nums) - 1
    total = nums[x] 
    while x > 0:
        x -= 1
        total = total * nums[x]
    return total
