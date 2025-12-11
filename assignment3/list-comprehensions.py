import csv

all_names = []
all_names_contain_e = []

with open("../csv/employees.csv", "r") as file:
  reader = csv.reader(file)
  all_names = [" ".join(row[1:-1]) for i, row in enumerate(reader) if i != 0]
  print(all_names)
  all_names_contain_e = [name for name in all_names if "e" in name]
  print(all_names_contain_e)