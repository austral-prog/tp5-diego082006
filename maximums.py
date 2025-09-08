def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    return max(x, y)

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    return max(x, y, z)

result1 = max_of_two(5, 4)
print(result1)   
result2 = max_of_two(-2, -3) 
print(result2)  
result3 = max_of_two(0, 0)
print(result3)    
result4 = max_of_three(5, 4, 7)
print(result4)  
result5 = max_of_three(-2, -3, -1) 
print(result5) 
result6 = max_of_three(0, 0, 0)
print(result6)  
