

class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start.")

        squares = [x**2 for x in range(start, end + 1)]
        return squares

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start.")

        cubes = [x**3 for x in range(start, end + 1)]
        return cubes


cubic_gen = CubicGenerator()
start_num = 1
end_num = 5


cubes_list = cubic_gen.generate_squares(start_num, end_num)

print(cubes_list)
