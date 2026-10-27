def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here

    new_matrix = []
    new_row = []

    for i in range(len(a[0])):
        for row in a:
            new_row.append(row[i])
        new_matrix.append(new_row)
        new_row = []

    return new_matrix



    pass