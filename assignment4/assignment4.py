import pandas as pd

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
print(task1_older)