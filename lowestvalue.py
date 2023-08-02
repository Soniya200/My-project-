def find_lowest_total_sublist(sublists):
    if not sublists:
        return None
    
    lowest_total = float('inf')
    lowest_sublist = None

    for sublist in sublists:
        total = sum(sublist)
        if total < lowest_total:
            lowest_total = total
            lowest_sublist = sublist

    return lowest_sublist

# Example usage:
sublists = [[1, 2, 3], [4, 5], [70,80,67], [3, 1, 78]]
result = find_lowest_total_sublist(sublists)
print("Sublist with the lowest total values:", result)
