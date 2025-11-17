def hello():
  return "Hello!"

def greet(name):
  return f"Hello, {name}!"

def calc(val1, val2, operator = "multiply"):
  match operator:
    case "add":
      return val1 + val2
    case "subtract":
      return val1 - val2
    case "multiply":
      try:
        int(val1)
      except:
        return "You can't multiply those values!"
      else:
        return val1 * val2
    case "divide":
      try:
        val1 / val2
      except ZeroDivisionError:
        return "You can't divide by 0!"
      else:
        return val1 / val2
    case "modulo":
      return val1 % val2

def data_type_conversion(value, type):
  match type:
    case "int":
      try:
        int(value)
      except:
        return f"You can't convert {value} into a {type}."
      else:
        return int(value)
    case "float":
      try:
        float(value)
      except:
        return f"You can't convert {value} into a {type}."
      else:
        return float(value)
    case "str":
        return str(value)

def grade(*args):
  try:
    sum(args)
  except:
    return "Invalid data was provided."
  else:
    grade = sum(args) / 3
    
    if grade >= 90:
      return "A"
    elif (grade >= 80) and (grade < 90):
      return "B"
    elif (grade >= 70) and (grade < 80):
      return "C"
    elif (grade >= 60) and (grade < 70):
      return "D"
    else:
      return "F"

