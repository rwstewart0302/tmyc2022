# Adapted the solver template from the TMYC repo

class Week1Solver(): # week1 solver class for parts 1 and 2
    def __init__(self, file_path: str):
        with open(file_path) as f: # reading in the data
            self.raw_input = [int(num) for x in f.readlines() for num in x.strip().split(',')] # storing data as list of integers

    def part_1_solver(self, noun: int, verb: int) -> int:
        '''
        The Part 1 Solver
         ---> requires 'noun' and 'verb' values to produce an output
         ---> forcing returned value to an integer
         ---> returns the initial value of the number list as our output
        '''
        nums_copy = self.raw_input.copy() # copying our number list so we don't overwrite it when checking different values
        nums_copy[1] = noun
        nums_copy[2] = verb
        for i in range(0, len(nums_copy), 4): # instruction appear every 4 values
            try: # do things if indices are in the range of nums_copy
                noun_ind = nums_copy[i + 1]
                verb_ind = nums_copy[i + 2]
                replace_ind = nums_copy[i + 3]
                if nums_copy[i] == 1: # instructions if value is 1
                    new_num = nums_copy[noun_ind] + nums_copy[verb_ind]
                    nums_copy[replace_ind] = new_num
                elif nums_copy[i] == 2: # instructions if value is 2
                    new_num = nums_copy[noun_ind] * nums_copy[verb_ind]
                    nums_copy[replace_ind] = new_num
                elif nums_copy[i] == 99: # instructions if value is 99
                    return nums_copy[0] # return the first value in nums_copy
            except IndexError: # stop doing things if IndexError
                continue # try again
        return nums_copy[0] # return the first value in nums_copy

    def part_2_solver(self, n_check: int) -> int:
        '''
        The Part 2 Solver
         ---> requires an 'n_check' value to produce an output
         ---> forcing returned value to an integer
         ---> returns the initial value of the number list as our output
         ---> uses part 1 solver functionality
         ---> brute force method...probably a more clever way to do this
        '''
        for noun in range(100): # checking all numbers between 0-99 for the noun
            for verb in range(100): # checking all numbers between 0-99 for the verb
                output = self.part_1_solver(noun, verb) # calling part_1_solver function
                if output == n_check: # if output is equal to n_check
                    return (100 * noun) + verb # return this
                else:
                    pass
        return 'NO VALID SOLUTION!' # if output never equals n_check then return this
