from itertools import zip_longest


class Category:
    def __init__(self, cat):
        self.cat = cat
        self.ledger = []
        self.balance = 0
        self.withdrawals = 0
    # making string representation of budget
    def __str__(self):
        string_representation = ""
        # centering title of category on a line of length thirty and filling all spaces on each side with asterisks
        string_representation += self.cat.center(30, "*") + "\n"
        for transaction in self.ledger:
            # this adjust value will be used to correctly adjust the price value to the right 
            adjust = 30-len(transaction['description'][:23])
            # for amounts input without cents, this will add a .00 to the end of the amount, and adjust the adjust value accordingly to suit the now longer amount string. [:23] and [:7] cap description and amount at the max length that they can be according to the directions
            if "." not in str(transaction["amount"]):
                string_representation += transaction['description'][:23] + str(transaction['amount'])[:7].rjust(adjust-3) + ".00" + "\n"
            # this creates the line for each transaction input with an amount with cents
            else:
                string_representation += transaction['description'][:23] + str(transaction['amount'])[:7].rjust(adjust) + "\n"

        string_representation += f"Total: {self.balance}"
        return string_representation
    # this method checks if there is enough mony left in the account to afford an expense. returns True if yes and False if no
    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else: 
            return True
    # this method adds funds to the account
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
    # this method checks if their are enough funds in the account to withdraw (using the check_funds method from earlier), and if there are enough funds, it withdraws them from the account. returns True if withdrawal goes through and False if not 
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -abs(amount), "description":description})
            self.balance -= amount
            self.withdrawals += amount
            return True
        else:
            return False
    # pretty self explatanatory, returns the current balance
    def get_balance(self):
        return self.balance
    # works like withdraw method, but also deposits to specified different account
    def transfer(self, amount, cat2):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -abs(amount), "description": f"Transfer to {cat2.cat}"})
            cat2.ledger.append({"amount": amount, "description": f"Transfer from {self.cat}"})
            self.balance -= amount
            cat2.balance += amount
            self.withdrawals += amount
            return True
        else:
            return False

def create_spend_chart(categories):
    percentages = {}
    total_withdrawals = 0
    number_of_os = {}
    y_axis_values = ["100|", " 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]
    final_graph = "Percentage spent by category\n"
    # adding up withdrawals from each category to get total amount withdrawed 
    for category in categories:
      total_withdrawals += category.withdrawals
    # finding the percentage of total withdrawals that each account is responsible for. multiplying that decimal by 10 and then casting that float as an integer to essentially round down to the nearest tenth, then multiplying by 10 again to get a round multiple of 10 "percentage"
    for category in categories:  
      percentages[category.cat] = int(10*int((category.withdrawals/total_withdrawals)*10))
    
    for key, value in percentages.items():
        # creating dictionary where each key is a category name and each value is a list which holds the spaces and o's for the percentage chart
        number_of_os[key] = []
        # calculating number of spaces needed by subracting the percent of total withdrawals from 100 and dividing by 10, then appending that number of spaces to the list for each category. (so if a category was responsible for 60% of withdrawals, there will be 7 o's (one extra because the first o corresponds to 0%, not 10%) and (100-60)/10 spaces, or 4 spaces)
        for i in range(int((100-value)/10)):
            number_of_os[key].append(" ")
        # calculating number of o's needed. dividing percentage (already rounded down in the dictionary) by 10 and then adding an o for ever number in that range (inclusive of top number, so actually in the range of that number plus 1)
        for i in range(0, int((value/10+1))):
            number_of_os[key].append("o")
    # zipping the strings we created of spaces and os for every category so that we have an iterator of tuples where each tuple contains the spaces and/or o's for each row on the y axis (each tuple will be the number of categories given to the function long and there will be 11 of them as there are 11 rows on the y-axis)
    zipped_os = list(zip(*list(number_of_os.values())))
    # adding each row of output to final string (y-axis values and spaces and o's)
    for index, value in enumerate(y_axis_values):
        final_graph += value + " " + "  ".join(zipped_os[index]) + "  \n"
    # adding necessary number of dashes under graph to final string
    final_graph += "    " + "-"*(3*len(categories)+1) + "\n"
    #making a list of the names of the categories (sourced from the keys of the percentages dictionary) and zipping those keys so that we have an iterator of tuples with each tuple containing the letters for each category at the same index. this will enable us to print them so that the x-axis labels read vertically. then I convert that iterator to a list so that I can index it in the next section
    zipped_x_labels = list(zip_longest(*list(percentages.keys()), fillvalue=" "))
    # iterating through the list of tuples I just created to add each one (each tuple being a row in the output) to the final string
    for row in zipped_x_labels:
      # not adding a newline if it is the last row so that my output matches the expected output
      if row == zipped_x_labels[-1]:
        final_graph += "     " + "  ".join(row) + "  "
      else:
        final_graph += "     " + "  ".join(row) + "  \n"
    return final_graph
