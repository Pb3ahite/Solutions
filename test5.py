def is_consecutive(a_list):
    if len(a_list) <= 1:
        return True

    sorted_list = sorted(a_list)
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] + 1 != sorted_list[i + 1]:
            return False
    
    return True

numbers = [2, 3, 4, 5, 6, 7]
result = is_consecutive(numbers)
print(result)  
