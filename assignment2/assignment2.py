import csv
import os

try:
  def read_employees():
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
  employees = read_employees()
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