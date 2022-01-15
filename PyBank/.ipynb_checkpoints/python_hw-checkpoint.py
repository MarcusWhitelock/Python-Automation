import csv

# declare variables
month_count = 0
total = 0
greatest_inc_mon = None
greatest_inc = None
greatest_dec_mon = None
greatest_dec = None

# open the file containing the budget dataset
with open("budget_data.csv") as company_data:
    company_data_reader = csv.reader(company_data)

    # loop over every row in the budget dataset
    # index represents the position, at which the row is located in the array
    for index, row in enumerate(company_data_reader):
        # The first row contains only the column headers, so skip it
        if index == 0:
            continue

        val = int(row[1])
        month = row[0]
        month_count += 1
        total += val

        if val < 0:
            # Val is considered a decrease.
            # If the 'greatest_dec' hasn't been initialized with a real value yet or the current row
            # contains a larger loss in profit than the saved one, set variables to current row's data
            if (greatest_dec is None) or (val < greatest_dec):
                greatest_dec = val
                greatest_dec_mon = month
        else:
            # val is considered an increase
            # If the 'greatest_inc' hasn't been initialized with a real value yet or the current row
            # contains a larger profit than the saved one, set variables to current row's data
            if (greatest_inc is None) or (val > greatest_inc):
                greatest_inc = val
                greatest_inc_mon = month

# Calculate the average profit
avg = total / month_count

# Format the log.
log = ''
log += f'Financial Analysis\n----------------------------\n'
log += f'Total Months: {month_count}\n'
log += f'Total: ${total}\n'
log += f'Average Change: ${avg}\n'
log += f'Greatest Increase in Profits: {greatest_inc_mon} (${greatest_inc})\n'
log += f'Greatest Decrease in Profits: {greatest_dec_mon} (${greatest_dec})\n'

print(log)

# Print the log to a file. 'w' means overwrite the existing content from the file
file = open("log.txt", "w")
file.write(log)
file.close()
