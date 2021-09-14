secret_word = 'leak'
guess_num = 5

revealed_word = '*' * len(secret_word)
win = False
while guess_num:
  print(f'Here is the word so far : {revealed_word}')
  guess = input(f'Guess a letter ({guess_num} guess_num left):')
  new_word = ''
  for i, c in enumerate(secret_word):
    if revealed_word[i] != '*':
      new_word += revealed_word[i]
    elif secret_word[i] == guess:
      new_word += guess
    else:
      new_word += '*'
  if new_word == secret_word:
        print(f'You guessed the word!: {secret_word}')
        win = True
        break
  revealed_word = new_word
  guess_num -= 1

if not win:
    print(f'Sorry, you lose, the word was: {secret_word}')


print(f'Sorry, you lose, the word was: {secret_word}')

