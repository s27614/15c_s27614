

class SquareGenerator:

    def generate_squares(self,start,end):
        squares = [x**2 for x in range(start, end + 1)]
        return squares
    square_gen = SquareGenerator()
    start_num = 1
    end_num = 10
    squares_list = square_gen.generate_squares(start_num, end_num)
    print(squares_list)


