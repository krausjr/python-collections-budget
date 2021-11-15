import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expenses()
expenses.read_expenses(data/spending_data.csv)

spendingCategories = []
for expense in expenses:
    spendingCategories.append(expense.category)

spendingCounter = collections.Counter(spendingCategories)

top5 = spendingCounter.most_common(5)

categories, count = zip(*top5)

fig,ax=plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()