import os
import time


while True:
  print("\033[32m HIGH SCORE TABLE\033[0m")
  print()
  initials = input("Input your initials > ").upper()
  score = input("Input your score > ")
  print()

  # File creation(new)
  f = open("high.score", "a+")
  f.write(f"{initials} {score}\n")
  f.close()
  print("Added to high score table.")
  time.sleep(1)
  os.system("clear")
  