# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
data = []
try: 
    with open("sales.csv", "r") as file:
        header = file.readline()
        # 2D array 
        # [Date,Product,Sales_Amount,Units_Sold,Region]
        for line in file:
            data.append(line.split(","))
except FileNotFoundError:
    print("Error: File can't be found")

# Find largest sale day
def largestSaleDay():
    dates = {}
    for i in data:
        
        revenue = int(i[2]) * int(i[3]) # sales amount multiplied by units sold
        dates[i[0]] = dates.get(i[0], 0) + revenue # If date not in dictionary, default to 0

    return max(dates.items())

# Find average revenue per sale
def averageSaleAmount():
    sold = 0
    revenue = 0

    for i in data:
        sold += int(i[3])
        revenue += int(i[2])

    average = revenue / sold
    return(average)


def mostSoldWidget():
    widgetSales = {}
    for i in data:
        widgetSales[i[1]] = widgetSales.get(i[1], 0) + int(i[3])

    return max(widgetSales.items())

if data:
    print(f"Largest Sales Day: {largestSaleDay()}")
    print(f"Average Sale Amount: {averageSaleAmount()}")
    print(f"Most Sold Widget: {mostSoldWidget()}")
# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows