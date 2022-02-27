import operator
from sqlalchemy import false

def arithmetic_arranger(problems, show_answer = false):
    if len(problems) > 5:
        return "Error: Too many problems."
    final_string = ""
    split_problems = []
    rjust_lengths = []
    solutions = []
    ops = {"+": operator.add, "-": operator.sub}
    for problem in problems:
      split_problems.append(problem.split())
    for problem in split_problems:
        for item in problem:
            if problem.index(item)%2 != 0:
                if item != "+" and item != "-":
                    return "Error: Operator must be \'+\' or \'-\'."
            else:
                if not item.isnumeric():
                    return "Error: Numbers must only contain digits." 
            if len(item) > 4:
                return "Error: Numbers cannot be more than four digits."
    for problem in split_problems:
        solutions.append(str(ops[problem[1]](int(problem[0]), int(problem[2]))))
    #print(solutions)
    #print(split_problems)
    for row in split_problems:
        longest_item_length = 0
        for item in row:
            if len(item) > longest_item_length:
                longest_item_length = len(item)
        rjust_lengths.append(longest_item_length)
    #print(rjust_lengths)
    zipped_problems =  zip(*split_problems)
    zipped_problems_list = list(zipped_problems)
    zipped_problems_list.append(solutions)
    #print(zipped_problems_list)
    for i in range(len(zipped_problems_list)-2):
        for j in range(len(zipped_problems_list[i])):
            if i == 0:
                if j < len(rjust_lengths)-1:
                    final_string += zipped_problems_list[i][j].rjust(rjust_lengths[j] + 2) + " "*(4)
                else:
                    final_string +=zipped_problems_list[i][j].rjust(rjust_lengths[j] + 2)
                #print(zipped_problems_list[i][j] + "\t", end=" ")
                #print(str(rjust_lengths[j]) + "\t", end=" ")
                #print(str(len(zipped_problems_list[i][j])) + "\t", end = " ")
                #print(str(adjust))
            else:
                if j < len(rjust_lengths)-1:
                    final_string += zipped_problems_list[i][j] + " " + zipped_problems_list[i+1][j].rjust(rjust_lengths[j]) + "    "
                else: 
                    final_string += zipped_problems_list[i][j] + " " + zipped_problems_list[i+1][j].rjust(rjust_lengths[j])
        final_string += "\n"
    for i in range(len(problems)):
        if i < (len(problems)-1):
            final_string += ("-"*(rjust_lengths[i]+2)) + "    "
        else:
            final_string += ("-"*(rjust_lengths[i]+2))
    if show_answer == True:
        final_string += "\n"
        for j in range(len(zipped_problems_list[3])):
            if j < (len(zipped_problems_list[3])-1):
                final_string += zipped_problems_list[3][j].rjust(rjust_lengths[j] + 2) + " "*(4)
            else:
                final_string += zipped_problems_list[3][j].rjust(rjust_lengths[j] + 2)
    return final_string
