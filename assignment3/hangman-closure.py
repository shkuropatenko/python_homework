def make_hangman(secret_word):
  guesses = []
  idx = 0
  result = ""

  def hangman_closure(letter):
    if letter in secret_word[idx]:
      guesses.append(letter)
    else:
      guesses.append("_")

  while idx < len(secret_word):
    user_input = input("Type your letter ")
    hangman_closure(user_input)
    idx += 1

  result = "".join(guesses)
  print(result)

  if result == secret_word:
    return True
  else:
    return False


print(make_hangman("alphabet"))