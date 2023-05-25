from ten_thousand.game_logic import GameLogic
from ten_thousand.printed import Printed 

# from game_logic import GameLogic
# from printed import Printed

class Game:
    def __init__(self) -> None:
        pass
    def play(a=1):
      print("Welcome to Ten Thousand")
      print("(y)es to play or (n)o to decline")
      # Prompt the user for input and validate it
      userInputs=input("> ")
      userInputs=Printed.padInput(userInputs,["y","n"]) # the user cant enter any think from his mind
      if userInputs.strip()!="n":
        # Start the game if the user chooses to play
        return GameLogic.startGame(userInputs,a)
      else:
        # Return a message if the user declines to play
        Printed.quit_game("OK. Maybe another time") 


if __name__=="__main__":
  print(Game.play())