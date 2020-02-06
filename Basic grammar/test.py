

def numbers(input_list):
    max_sum = input_list[0]
    current_sum = input_list[0]
    for i in range(1, len(input_list)):
        current_sum = max(current_sum + input_list[i], input_list[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


input_list = [-1, 3, -1, 5]
numbers(input_list)

input_list = [-5, -3, -1]
numbers(input_list)

input_list = [2, 4, -2, -3, 8]
numbers(input_list)