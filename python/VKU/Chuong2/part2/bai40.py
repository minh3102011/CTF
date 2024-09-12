def print_tuple_halves(input_tuple):
    mid_index = len(input_tuple) // 2
    first_half = input_tuple[:mid_index]
    second_half = input_tuple[mid_index:]
    
    print("Nửa đầu tiên:", first_half)
    print("Nửa còn lại:", second_half)

input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print_tuple_halves(input_tuple)
