def make_hangman(secret_word):
  guesses = []

  def hangman_closure(letter):
    guesses.append(letter)
    display = ""

    for ch in secret_word:
      if ch in guesses:
        display += ch
      else:
        display += "_"
    print(display)

    if "_" not in display:
      return True
    else:
      return False

  return hangman_closure

if __name__ == "__main__":
  secret = input("Enter secret word: ")
  game = make_hangman(secret)
  finished = False

  while not finished:
    letter = input("Guess a letter: ")
    finished = game(letter)
  print("You guessed the word!")