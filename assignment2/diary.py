import traceback

try:
  with open("diary.txt", "a") as file:
    first_time = True

    while True:
      if first_time:
        enterText = "What happened today? "
        user_input = input(enterText)
        file.write(f"{user_input}\n")
        first_time = False
      else:
        enterText = "What else? "
        user_input = input(enterText)
        file.write(f"{user_input}\n")
      print(user_input)
      if user_input == "done for now":
        break
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