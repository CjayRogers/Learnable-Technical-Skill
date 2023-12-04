def nth_most_rare(lst, n):
    # Count occurrences of each element
    count_dict = {}
    for num in lst:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Sort the unique elements based on their occurrence count
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1])
    
    # Return the nth rarest item
    if n <= len(sorted_items):
        return sorted_items[n - 1][0]
    else:
        return None  # Return None if n is greater than the number of unique elements

# Example usage
lst = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n = 2
result = nth_most_rare(lst, n)
print(result)
