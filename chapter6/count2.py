import csv
import re

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].strip().upper()
        if re.search("^(OFFICE | THE.OFFICE)$", title):
            counter += 1

print(f"The number of people who like the Office: {counter}")