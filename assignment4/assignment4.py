import pandas as pd

# Task 1

task1_data_frame = pd.DataFrame({
  "Name": ['Alice', 'Bob', 'Charlie'],
  "Age": [25, 30, 35],
  "City": ['New York', 'Los Angeles', 'Chicago']
})

task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

task1_older = task1_with_salary.copy()
task1_older["Age"] += 1

task1_older.to_csv("employees.csv", index=False)

# Task 2
task2_employees = pd.read_csv("employees.csv")

json_employees = pd.read_json("./additional_employees.json")

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)