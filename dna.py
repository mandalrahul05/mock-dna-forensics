from sys import *
import csv
import re


def main():
    """Main Driver function"""

    # Checks for the valid arguments
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    samples = []
    # Loads the database to a list of dictionary
    with open(argv[1], "r") as file:
        reader = csv.DictReader(file)

        # Iterate over the file and append to tha list
        for row in reader:
            # Converts the count to integer
            for key in row:
                if key != "name":
                    row[key] = int(row[key])

            samples.append(row)

    # List of all STR's according to the database
    keys = list(samples[0].keys())
    keys.pop(0)

    # Loads the dna sequence
    with open(argv[2], "r") as file:
        sequence = file.read()

    # Counts the number of all str sequences
    str_count = counter(sequence, keys)

    # Retrieves the answer
    person = checker(str_count, samples, keys)

    # Prints the name
    print(person)


def counter(sequence, keys):
    """Counts the number of all STR sequnces and returns a dictionary"""

    # Declare a dictionary for STR count
    counts = {}

    # Iterate over the STRs from database
    for key in keys:
        # Finds the occurence
        c = re.findall(f'(?:{key})+', sequence)
        length = [len(i) // len(key) for i in c]

        # Adds to count
        if len(length) != 0:
            l = max(length)
            counts[key] = l

    # if any key missed out
    for key in keys:
        if key in counts.keys():
            continue
        else:
            counts[key] = 0

    return counts


def checker(counts, database, keys):
    """Matches the DNA in the database and returns the answer"""

    # Checks in the database
    for person in database:
        flag = 0
        # Checks every keys
        for key in keys:
            # If the counts match with database
            if person[key] == counts[key]:
                flag += 1
        # Checks if it matches with the person
        if flag == len(keys):
            return person["name"]

    # If no match found
    return "No match"


if __name__ == "__main__":
    main()
