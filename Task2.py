def generate_squares(start,end):
    squares = [x**2 for x in range(start,end + 1)]
    return squares

start_num = 1
end_num = 10
squares_list = generate_squares(start_num, end_num)

print(squares_list)

