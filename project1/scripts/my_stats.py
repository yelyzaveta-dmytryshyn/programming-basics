def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def maximum(numbers):
    if not numbers:
        return None
    return max(numbers)