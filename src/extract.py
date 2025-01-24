import csv


def read_csv(csv_file: str) -> list[str]:
    """Read the CSV file and return a list of dictionaries"""
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
