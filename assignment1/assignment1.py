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
    grade = sum(args) / len(args)
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

def repeat(str, count):
  result = ""
  for i in range(count):
    result = str * count
  return result

def student_scores(*args, **kwargs):
  if args[0] == "mean":
    sum = 0
    for value in kwargs.values():
      sum += value
    return sum / len(kwargs)
  elif args[0] == "best":
    num = 0
    name = ""
    for key, value in kwargs.items():
      if num < value:
        num = value
        name = key
    return name

def titleize(str):
  words = str.split()
  arr_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
  capital_letter = ""
  new_words = []
  for i, word in enumerate(words):
    if i == 0:
      capital_letter = word[0].capitalize()
      updated_word = capital_letter + word[1:]
      new_words.append(updated_word)
    elif i == len(words) - 1:
      capital_letter = word[0].capitalize()
      updated_word = capital_letter + word[1:]
      new_words.append(updated_word)
    elif word not in arr_words:
      capital_letter = word[0].capitalize()
      updated_word = capital_letter + word[1:]
      new_words.append(updated_word)
    else:
      new_words.append(word)
  return " ".join(new_words)

def hangman(secret, guess):
  result = ""
  for i, letter in enumerate(secret):
    if letter in guess:
      result += letter
    else:
      result += "_"
  return result

def pig_latin(text):
  vowels = ["a", "e", "i", "o", "u"]
  words = text.split()
  result_words = []

  for word in words:
    if word[0] in vowels:
      result_word = word + "ay"
    else:
      consonants = ""
      idx = 0
      while idx < len(word) and word[idx] not in vowels:
        
        if word[idx] == "q" and idx + 1 < len(word) and word[idx + 1] == "u":
          consonants += "qu"
          idx += 2
        else:
          consonants += word[idx]
          idx += 1
          
        result_word = word[idx:] + consonants + "ay"
    result_words.append(result_word)
  return " ".join(result_words)
