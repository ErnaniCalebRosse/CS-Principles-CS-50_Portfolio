# Counts students in each house
import csv

# Dictionary to count the houses
houses = {
    "Gryffindor": 0,
    "Hufflepuff': 0,
    "Slytherin": 0,
    "Ravenclaw": 0
}
# Open the csv
with open("hogwarts.csv", "r") as house_list:
    # Read the rows and save as a variable called reader
    reader = csv.reader(house_list)
    # Skip over the title row
    next(reader)

    # Add 1 to the correct house for each row in house_list/reader
    for row in reader:
        house = 