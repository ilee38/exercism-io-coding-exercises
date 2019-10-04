"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
  #sort the dice
  dice.sort()

  if category == YACHT:
    return _score_yacht(dice)

  if category >= ONES and category <= SIXES:
    return _score_face_value(dice, category)

  if category == FULL_HOUSE:
    return _score_full_house(dice)

  if category == FOUR_OF_A_KIND:
    return _score_four_of_a_kind(dice)

  if category == LITTLE_STRAIGHT:
    return _score_little_straight(dice)

  if category == BIG_STRAIGHT:
    return _score_big_straight(dice)

  if category == CHOICE:
    return _score_choice(dice)

  return 0


def _score_yacht(dice):
  if dice.count(dice[0]) == 5:
    return 50
  return 0


def _score_face_value(dice, category):
  return category * dice.count(category)


def _score_full_house(dice):
  """ dice are in sorted order
  """
  #case1: first 3 are equal and last 2 are equal
  if dice[0:3].count(dice[0]) == 3 and dice[3:].count(dice[3]) == 2:
    if dice[0] != dice[3]:
      return sum(dice)
  #case 2: first 2 are equal and last 3 are equal
  elif dice[0:2].count(dice[0]) == 2 and dice[2:].count(dice[2]) == 3:
    if dice[0] != dice[2]:
      return sum(dice)
  return 0


def _score_four_of_a_kind(dice):
  """ dice are in sorted order
  """
  if dice[0:4].count(dice[0]) == 4:
    return dice[0] * 4
  if dice[1:].count(dice[1]) == 4:
    return dice[1] * 4
  return 0


def _score_little_straight(dice):
  if dice == [1, 2, 3, 4, 5]:
    return 30
  return 0


def _score_big_straight(dice):
  if dice == [2, 3, 4, 5, 6]:
    return 30
  return 0


def _score_choice(dice):
  return sum(dice)