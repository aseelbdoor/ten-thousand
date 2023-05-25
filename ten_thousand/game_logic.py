
import random
from ten_thousand.printed import Printed 
# from printed import Printed

class GameLogic:
    def __init__(self,total=0,roun=0):
      self.total=total
      self.round=roun
    @staticmethod
    def calculate_score(roll):
        """
        Calculates the score based on the given roll.
    
        Args:
            roll (tuple): A tuple representing the dice roll.
    
        Returns:
            int: The calculated score.
    
        """
        score = 0
        counts = [roll.count(i) for i in range(1, 7)]
    
        if counts == [1, 1, 1, 1, 1, 1]:
            # Check for a straight (1, 2, 3, 4, 5, 6)
            score = 1500
            return score
    
        if counts.count(2) == 3:
            # Check for three pairs
            score += 1500
            return score
    
        if counts[0] <= 2:
            # Check for individual 1s
            score += counts[0] * 100
    
        if counts[4] <= 2:
            # Check for individual 5s
            score += counts[4] * 50
    
        if 3 in counts:
            # Check for three of a kind
            if counts.count(3) == 2:
                # Two sets of three of a kind
                location = counts.index(3) + 1
                location2 = counts[location::1].index(3) + location + 1
                if location == 1:
                    score += location * 1000
                else:
                    score += location * 100
                score += location2 * 100
            else:
                location = counts.index(3) + 1
                if location == 1:
                    score += location * 1000
                else:
                    score += location * 100
    
        elif 4 in counts or 5 in counts or 6 in counts:
            # Check for four, five, or six of a kind
            maxx = max(counts)
            a = 0
            location = counts.index(maxx) + 1
            if location == 1:
                for i in range(3, maxx + 1):
                    a += 1000
            else:
                for i in range(3, maxx + 1):
                    a += (location * 100)
            score += a
    
        return score

      
    def roll_dice(number=6):
        # Generate a sequence of random numbers between 1 and 6 using a generator expression
        return tuple(random.randint(1, 6) for _ in range(number))
    
    @classmethod
    def roll(cls,score,digit2,roun,total):
      """
      Rolls the remaining dice and calculates the score.

      Parameters:
          cls (class): The class representing the game.
          score (int): The score obtained from previous rolls.
          digit2 (int): The number of dice to roll in the current round.
          roun (int): The current round number.

      Returns:
        int: The total score obtained after rolling the dice.
      """
      total2=score #assign total score for this re-roll round
      dice=cls.roll_dice(digit2) # roll the remining dices coming fron digit2
      dices=Printed.decorate(dice)
      score1=cls.calculate_score(dice) # calculate the defult score for remining dices
      if score1==0: # if defult score is 0 the user lose his score in this round 
        print(Printed.zilch(dice))
        return 0 # return 0 as total score in this round
      print(f"Rolling {len(dice)} dice...")
      print(f"{dices}")
      print("Enter dice to keep, or (q)uit:")
      # print to the user enter dices messege and sugisst to quit
      userInputs=input("> ")
      if userInputs.strip()=="q":
        Printed.end_game(total) # if the user need to quit the method will return 0 as total score for re-roll round
      while not userInputs.strip().isdigit(): # to order not to allow the user to enter anything until dices
        print(f"You can't enter any thing untile the dices")
        userInputs=input("> ")
      iinput=Printed.string_to_tuple(userInputs.strip()) # convert string input dices to tuble of integar
      if  not Printed.validate(dice,iinput):
             iinput=Printed.cheater(dice,iinput,total)
      score2=cls.calculate_score(iinput) # calculate input score
      if score1>0: # if the defult score is 0 the user will lose his score in this round
        total2+=score2 # add the score to total score for this round
        while userInputs.strip()!="b": # loop untile bank
          digit=digit2 # assign digit for calculate digit for every re-roll time
          if digit==0:
             return 0
          print(f"You have {total2} unbanked points and {digit-len(iinput)} dice remaining")
          print("(r)oll again, (b)ank your points or (q)uit:")
          digit2=digit-len(iinput) #assign the remining digit of dices
          userInputs=input("> ")
          if userInputs.strip()=="q":
            Printed.end_game(total) # if user need to quit without bank his score the total will be 0
          if userInputs.strip()=="b": # if user need to bunk his score
            return total2 # return the total score for this round(total re-roll times)
          if userInputs.strip()=="r": # if user need to re-roll remining dices
            if Printed.hotdices(dice,digit):
              dice=cls.roll_dice(digit)
              digit2=digit
            else:
              dice=cls.roll_dice(digit2) # roll remining dices
            dices=Printed.decorate(dice)
            score1=cls.calculate_score(dice) # calculate the defult score for remining dices
            if score1==0: # if defult score is 0 the user lose his score in this round 
              print(Printed.zilch(dice))
              return 0 # return 0 as total score in this round
            print(f"Rolling {len(dice)} dice...")
            print(f"{dices}")
            print("Enter dice to keep, or (q)uit:")
            userInputs=input("> ")
            if userInputs.strip()=="q": # if user needto quit without bank his score
              Printed.end_game(total)
            iinput=Printed.string_to_tuple(userInputs.strip()) # convert remining string of dices
            score2=cls.calculate_score(iinput) # calculate user input score for remining dices
            if not Printed.validate(dice,iinput):
               Printed.cheater(dice,iinput,total)
            else:
               total2+=score2 # the user does not cheating , add win score to the total
      else: # return 0 as score becouse the user lose on it
          print(Printed.zilch(dice))
          return 0
      
    @classmethod
    def startGame(cls,userInputs,a):
      """
      Plays the game of Ten Thousand.

      Parameters:
        cls (class): The class representing the game.
        userInputs (str): The user's input to start the game.

      Returns:
        str: A message indicating the total score earned in the game.
      """
      roun=1 #assign roun variable to calculate the round
      dice=cls.roll_dice() # first dice as defult
      dices=Printed.decorate(dice) # made good format for dices 
      print(f"Starting round {roun}")# start messege for game
      print("Rolling 6 dice...")
      print(f"{dices}")
      print("Enter dice to keep, or (q)uit:")
      userInputs=input("> ") # first input my dices or q for quit
      total=0 # assign total variable to calculate the total score
      digit=6 # first digit to play with out reroll dices
      while userInputs.strip()!="q": # if the user input in any part will be q the game will end
        
        if userInputs.strip()=="q": # if user input == q the loop will stop
          Printed.end_game(total)
        else: # this when user input = dices
          iinput=Printed.string_to_tuple(userInputs.strip()) # convert string dices to tuble  of integer 
          if not Printed.validate(dice,iinput): # check if the user dose not cheating
            iinput=Printed.cheater(dice,iinput,total)
          score2=cls.calculate_score(iinput) # calculate the score of  user inpput
          print(f"You have {score2} unbanked points and {6-len(iinput)} dice remaining")
          print("(r)oll again, (b)ank your points or (q)uit:")
          # print to the  user messege to till him about unbank score he is have and the remaining dices and ask him to roll again or bank his score or quit
          digit2=digit-len(iinput) # assign digit2 to calculate the remaining dices
          userInputs=input("> ")
          if userInputs.strip()=="b": # if user choose bank
            total+=score2 # save his score to thetotal score
            dice=cls.roll_dice() # roll defult digit of dices for new round
            dices=Printed.decorate(dice)
            print(f"You banked {score2} points in round {roun}")
            print(f"Total score is {total} points")
            print(f"Starting round {roun+1}")
            print("Rolling 6 dice...")
            print(f"{dices}")
            print("Enter dice to keep, or (q)uit:")
            # print to the user the score he banked and the round of this score and his total score and start new round whit its number and the dices and suggist to quit
            roun+=1 # rrassign the round number for nrw round
            userInputs=input("> ")
          elif userInputs.strip()=="r": # if user need to re-roll the remaining dices
            if Printed.hotdices(dice,digit):
               total2=cls.roll(score2,digit,roun,total)
            else:
               total2=cls.roll(score2,digit2,roun,total) # cull roll method to re-roll remining  dices and return the total value of score from re-roll time
            total+=total2 # add the re-roll score to the total score
            dice=cls.roll_dice() # roll defult dices
            dices=Printed.decorate(dice)
            print(f"You banked {total2} points in round {roun}")
            print(f"Total score is {total} points")
            print(f"Starting round {roun+1}")
            print("Rolling 6 dice...")
            print(f"{dices}")
            print("Enter dice to keep, or (q)uit:")
            # print bank messege 
            roun+=1 # reassign for new round
            userInputs=input("> ")
        if roun==20:
          Printed.end_game(total)
      Printed.end_game(total) # in the end of game this will return
    
    @classmethod
    def get_scorers(cls ,dice):
      total=cls.calculate_score(dice)
      if total==0:
        return tuple()
      scorers=[]
      for i,val in enumerate(dice):
        sub_roll=dice[:i]+dice[i+1:]
        sub_score=cls.calculate_score(sub_roll)
        if sub_score != total:
           scorers.append(val)
      return tuple(scorers)
       
if __name__=="__main__":
   print("")