import csv
import os
import custom_module
from datetime import datetime
import traceback

def read_employees():
  try:
    all_dict = {}
    all_rows = []

    with open("../csv/employees.csv", "r") as file:
      reader = csv.reader(file)
      for i, row in enumerate(reader):
        if i == 0:
          all_dict["fields"] = row
        else:
          all_rows.append(row)
      all_dict["rows"] = all_rows
    return all_dict
  except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
      print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
employees = read_employees()

# Task 3
def column_index(name):
  return employees["fields"].index(name)
employee_id_column = column_index("employee_id")

# Task 4
def first_name(row_number):
  first_name_col = column_index("first_name")

  return employees["rows"][row_number][first_name_col]

# Task 5
def employee_find(employee_id):
  def employee_match(row):
   return int(row[employee_id_column]) == employee_id
  
  matches=list(filter(employee_match, employees["rows"]))

  return matches

# Taks 6
def employee_find_2(employee_id):
  matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))

  return matches

# Task 7
def sort_by_last_name():
  last_name_col = column_index("last_name")
  employees["rows"].sort(key=lambda row: row[last_name_col])
  
  return employees["rows"]

# Task 8
def employee_dict(employer_row):
  dict_results = dict(
    zip(employees["fields"][1:], employer_row[1:])
  )
  return(dict_results)

# Task 9
def all_employees_dict():
  result = {}
  for row in employees["rows"]:
    employee_id = row[0]
    info = employee_dict(row)
    result[employee_id] = info

  return result

# Task 10
def get_this_value():
  return os.getenv("THISVALUE")

# Task 11
def set_that_secret(secret_key):
  custom_module.set_secret(secret_key)

# Task 12
def read_minutes():
  with open("../csv/minutes1.csv", "r") as file1, open("../csv/minutes2.csv", "r") as file2:
      v1 = csv.reader(file1)
      v2 = csv.reader(file2)

      def read_minutes_people(file): 
        minutes_dict = {}
        minutes_rows = []
        for i, row in enumerate(file):
          if i == 0:
            minutes_dict["fields"] = row
          else:
            minutes_rows.append(tuple(row))
        minutes_dict["rows"] = minutes_rows
        return minutes_dict
      minutes1 = read_minutes_people(v1)
      minutes2 = read_minutes_people(v2)
  return minutes1, minutes2
minutes1, minutes2 = read_minutes()

# Task 13
def create_minutes_set():
  set1 = set(minutes1["rows"])
  set2 = set(minutes2["rows"])
  combined = set1.union(set2)
  
  return combined
minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
  minutes_list_raw = list(minutes_set)
  mapperd = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list_raw)

  return list(mapperd)
minutes_list = create_minutes_list()

# Task 15
def write_sorted_list():
  global minutes_list
  minutes_list.sort(key=lambda x: x[1])
  converted = list(
    map(
      lambda x: (x[0], x[1].strftime("%B %d, %Y")),
      minutes_list
    )
  )

  with open("./minutes.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(minutes1["fields"])
    for row in converted:
      writer.writerow(list(row))
  minutes_list = converted

  return converted
