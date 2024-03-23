import math


class SquareGenerator:
    def generate_squares(self, start, end):

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots


square_gen = SquareGenerator()
start_num = 1
end_num = 10
squares_list = square_gen.generate_squares(start_num, end_num)

print(squares_list)

square_roots_list = square_gen.calculate_square_roots(squares_list)

print(square_roots_list)
