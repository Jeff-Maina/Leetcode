'''
2303. Calculate Amount Paid in Taxes
Easy

You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti] means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti. The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).

Tax is calculated as follows:

The first upper0 dollars earned are taxed at a rate of percent0.
The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
And so on.
You are given an integer income representing the amount of money you earned. Return the amount of money that you have to pay in taxes. Answers within 10-5 of the actual answer will be accepted
'''


def calculateTax(brackets, income):

        total_tax = 0

        for i in range(len(brackets)):
            current_bracket = brackets[i]

            if i == 0:
                diff = min((current_bracket[0] - 0), (income-0))

                tax = current_bracket[1]/100 * diff

                total_tax += tax
            else:
                diff = min((current_bracket[0] - brackets[i-1][0]), (income - brackets[i-1][0]))
                
                if diff < 0:
                    break

                tax = current_bracket[1]/100 * diff
                total_tax += tax

        return total_tax

print(calculateTax([[3,50],[7,10],[12,25]], 10))
