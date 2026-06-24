# Q1: Why do you think companies analyze large volumes of data?
"""
Companies analyze large volumes of data mainly to make better decisions
faster and with more confidence. Specifically, data analysis helps them to understand customer behavior — what people buy, when, and why
so they can personalize offers for them.
In addition to that, companies can follow trends and patterns early, before they become costly problems.
They can optimize operations by reducing waste in supply chains, staffing,
inventory, and marketing spend.
"""

# Question 2: If analyzing and sorting large data manually in Excel
# is difficult, how do you think Python can help solve this problem?

"""
Excel struggles with large datasets because of its limited ability to combine data from
many different sources.
Python solves these problems by:
 1)Handling millions of rows efficiently in memory.
 2)Making it easy to clean, filter, group, and merge data from multiple
  files or databases in a few lines of code.
 3)Reducing human error since the same logic is applied consistently
  every time.

Even with just basic variables and data types, we can already see the
idea. In Excel we'd manually scroll, sort, and filter. In Python, the
data can be stored in a list, and basic operations can already process
it instantly
"""


# Question 3: Imagine you work at a sales company that receives data
# about 10,000 customer transactions daily. How would you analyze it?
"""

Right now, as it is only the first lesson with just variables and data types, I can already calculate
basic daily numbers manually as an example
"""

transaction_1 = 120
transaction_2 = 340
transaction_3 = 75
transaction_4 = 980

total_revenue = transaction_1 + transaction_2 + transaction_3 + transaction_4
average_order_value = total_revenue / 4

print("Total revenue today:", total_revenue)
print("Average order value:", average_order_value)
#This specific code isn't really effective, but later on after watching
#other lessons, I would use more effective ways of accomplishing this task.


# Question 4: What tasks can Python be useful for in BI processes?
# (e.g., data cleaning, visualization, etc.)

"""
Python is useful across almost every stage of a BI workflow. 
It can be used for data extraction: pulling data from databases, APIs, or files.
Then, there is data cleaning: handling missing values, duplicates, wrong formats,.
Furthermore, there is data analysis: statistical summaries, trend detection, correlations.

It is really efficient in terms of automation: scheduling recurring reports instead of doing them
manually (e.g., with cron jobs or Airflow).
For reporting: automatically generating Excel/PDF/PowerPoint reports, such as
openpyxl, python-docx, and python-pptx.
"""


# Question 5: If you wanted to compare a company's profit year by year,
# how could this be done using Python?

"""
At the moment, I will try doing it by using just basic variables (since we've only learned variables
and data types so far :
"""

profit_2024 = 50000
profit_2025 = 62000

profit_change = profit_2025 - profit_2024

print("Profit 2024:", profit_2024)
print("Profit 2025:", profit_2025)
print("Change in profit:", profit_change)


# Question 6: If you don't know Python, what difficulties might you
# face when working with large datasets?
"""
Without Python, working with large datasets becomes much harder.

It sets me performance limits, as tools like Excel slow down or crash with
very large files, and have hard row limits.
There will be repetitive manual work - every new dataset requires repeating the
same filtering  steps by hand, which is slow and error-prone.

Another complexity would be a limited statistical power, as advanced analysis like
forecasting, correlation analysis, or machine learning isn't
realistically possible in spreadsheet tools alone.
Lastly, I would say there is a higher risk of human error without the knowledge of Python manual copy-pasting and formula-
dragging across thousands of rows increases the chance of mistakes
that are hard to catch.

Overall, without Python, analysis becomes slower, less scalable, more
error-prone, and harder to automate or reproduce.
"""
