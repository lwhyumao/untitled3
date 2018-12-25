import csv

# filename = 'sitka_weather_07-2017.csv'
with open('C:/Users/muyua/PycharmProjects/untitled3/sitka_weather_07-2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs = []
    for row in reader:
        highs.append(row[1])
    print(highs)
filename = 'sitka_weather_07-2017.csv'

