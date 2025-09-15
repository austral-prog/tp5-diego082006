def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        return x
    else:
        y

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y 
    else:
        return z

print(max_of_two(5,4))   
print(max_of_two(-2,-3)) 
print(max_of_two(0,0))   

print(max_of_three(5,4,7))   
print(max_of_three(-2,-3,-1)) 
print(max_of_three(0,0,0))    
