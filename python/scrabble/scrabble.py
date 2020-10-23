letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letter: point for letter, point in zip(letters, points)}

for letter, point in zip(letters, points):
  letters_to_points[letter.lower()] = point

letters_to_points[" "] = 0


def score_word(word):
  point_total = 0
  if(isinstance(word, str)):
    for letter in word:
      point_total += letters_to_points.get(letter, 0)
    return point_total
  else:
    return 0


#print("BROWNIE")
#print(score_word("BROWNIE"))


player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": [
  "EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BEllY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
#print(player_to_words)

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

#print(player_to_points)


def play_word(player, word):
  player_to_words[player].append(word)


play_word("Lexi Con", "JUST")

#print(player_to_words)


def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points


update_point_totals()

print(letters_to_points)
