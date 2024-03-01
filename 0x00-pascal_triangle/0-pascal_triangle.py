#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.
    
    Args:
        n (int): The number of rows in the Pascal's triangle.
        
    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Generate Pascal's Triangle using nested list comprehension
    triangle = [[1] * (i + 1) for i in range(n)]
    
    # Populate the triangle except for the first row
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    return triangle
