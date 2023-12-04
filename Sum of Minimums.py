def sum_of_minimums(numbers):
    min_values = [min(row) for row in numbers]
    return sum(min_values)