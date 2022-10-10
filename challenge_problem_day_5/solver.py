# Adapted the solver template from the TMYC repo

class Week1Solver(): # week1 solver class for parts 1 and 2
    def __init__(self, file_path: str):
        with open(file_path) as f: # reading in the data
            self.raw_input = [num for x in f.readlines() for num in x.strip().split(',')] # storing data as list of strings

    def part_1_solver(self, num_1: int, num_2: int) -> int:
        '''
        The Part 1 Solver:
           replace numbers in position 1 and position 2
           and return the number in position 0 after performing
           the operations
        '''
        nums_copy = self.raw_input.copy() # copying the number list so we don't overwrite it when checking different values
        nums_copy[1] = int(num_1)
        nums_copy[2] = int(num_2)

        i = 0
        while True:
            num_0 = int(nums_copy[i])
            if num_0 == 3:
                
                i += 2
            elif num_0 == 4:

                i += 2
            else:
                i += 4
            try: # do things if indices are in the range of nums_copy
                num_1_ind = int(nums_copy[i + 1])
                num_2_ind = int(nums_copy[i + 2])
                replace_ind = nums_copy[i + 3]
                num_0_str = str(nums_copy[i])
                if nums_copy[i] == 1: # instructions if value is 1
                    new_num = nums_copy[noun_ind] + nums_copy[verb_ind]
                    nums_copy[replace_ind] = new_num
                elif nums_copy[i] == 2: # instructions if value is 2
                    new_num = nums_copy[noun_ind] * nums_copy[verb_ind]
                    nums_copy[replace_ind] = new_num
                elif nums_copy[i] == 3: # instructions if value is 2
                    new_num = nums_copy[noun_ind] * nums_copy[verb_ind]
                    nums_copy[replace_ind] = new_num
                elif nums_copy[i] == 99: # instructions if value is 99
                    return nums_copy[0] # return the first value in nums_copy
            except IndexError: # stop doing things if IndexError
                continue # try again
        return nums_copy[0] # return the first value in nums_copy

    def part_2_solver(self, n_check: int) -> int:
        '''
        The Part 2 Solver:
           replace numbers in position 1 and position 2
           with numbers between 0-99 and return the these
           2 numbers if the number in position 0 equals
           n_check
        '''
        for noun in range(100): # checking all numbers between 0-99 for the noun
            for verb in range(100): # checking all numbers between 0-99 for the verb
                output = self.part_1_solver(noun, verb) # calling part_1_solver function
                if output == n_check: # if output is equal to n_check
                    return (100 * noun) + verb # return this
                else:
                    pass
        return 'NO VALID SOLUTION!' # if output never equals n_check then return this
