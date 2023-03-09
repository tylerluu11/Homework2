import datetime

currentDate = datetime.datetime.now().date()
parsed_dates = []

with open('inputDates.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == '-1':
            break
        try:
            date = datetime.datetime.strptime(line, "%B %d, %Y").date()
            if date <= currentDate:
                parsed_dates.append(date.strftime("%-m/%-d/%Y"))
        except ValueError:
            pass
with open('parsedDates.txt', 'w') as output:
    for line in parsed_dates:
        output.write(line + "\n")
