import solver

file_path = 'data.txt' # path/to/data/file

if __name__ == "__main__": # do all the things
    solution = solver.Week1Solver(file_path)
    print('The solution to part 1 is', solution.part_1_solver(12, 2))
    print('The solution to part 2 is', solution.part_2_solver(19690720))
