import random

class GameLogic:
    def __init__(self):
        pass
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
        
    def string_to_tuple(string):
      # Convert each character in the string to an tuble of integer using a generator expression
      tuple_value = tuple(int(digit) for digit in string)
      return tuple_value
    
    @classmethod
    def roll(cls,score,digit2,roun):
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
      total=score #assign total score for this re-roll round
      dice=cls.roll_dice(digit2) # roll the remining dices coming fron digit2
      dices="*** "
      for i in dice:
        dices+=str(i)+" "
      else:
        dices+="***"
      score1=cls.calculate_score(dice) # calculate the defult score for remining dices
      print(f"Rolling {len(dice)} dice...\n{dices}\nEnter dice to keep, or (q)uit:")
      # print to the user enter dices messege and sugisst to quit
      userInputs=input("> ")
      if userInputs.strip()=="q":
        return 0 # if the user need to quit the method will return 0 as total score for re-roll round
      while not userInputs.strip().isdigit(): # to order not to allow the user to enter anything until dices
        print(f"You can't enter any thing untile the dices")
        userInputs=input("> ")
      iinput=cls.string_to_tuple(userInputs.strip()) # convert string input dices to tuble of integar
      score2=cls.calculate_score(iinput) # calculate input score
      if score2>score1: # check from the score if it more defult score the user are cheating
         print("Cheater!! oh no")
         return 0 # return 0 as total becouse the user cheating in this round as first time
      if score1>0: # if the defult score is 0 the user will lose his score in this round
        total+=score2 # add the score to total score for this round
        while userInputs.strip()!="b": # loop untile bank
          digit=digit2 # assign digit for calculate digit for every re-roll time
          print(f"You have {total} unbanked points and {digit-len(iinput)} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
          digit2=digit-len(iinput) #assign the remining digit of dices
          userInputs=input("> ")
          if userInputs.strip()=="q":
            return 0 # if user need to quit without bank his score the total will be 0
          if userInputs.strip()=="b": # if user need to bunk his score
            return total # return the total score for this round(total re-roll times)
          if userInputs.strip()=="r": # if user need to re-roll remining dices
            dice=cls.roll_dice(digit2) # roll remining dices
            dices="*** " # made good formate for dices
            for i in dice:
              dices+=str(i)+" "
            else:
              dices+="***"
            score1=cls.calculate_score(dice) # calculate the defult score for remining dices
            if score1==0: # if defult score is 0 the user lose his score in this round 
              return 0 # return 0 as total score in this round
            print(f"Rolling {len(dice)} dice...\n{dices}\nEnter dice to keep, or (q)uit:")
            userInputs=input("> ")
            if userInputs.strip()=="q": # if user needto quit without bank his score
              return 0
            iinput=cls.string_to_tuple(userInputs.strip()) # convert remining string of dices
            score2=cls.calculate_score(iinput) # calculate user input score for remining dices
            if score2<=score1: # check from cheating
              total+=score2 # the user does not cheating , add win score to the total
            else: # if the user is cheater
               print("Cheater!! oh no")
               return 0 # lose his score
      else: # return 0 as score becouse the user lose on it
          return 0
      

    @classmethod
    def play(cls,userInputs):
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
      dices="*** " # made good format for dices 
      for i in dice:
        dices+=str(i)+" "
      else:
        dices+="***"
      print(f"Starting round {roun}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")# start messege for game
      userInputs=input("> ") # first input my dices or q for quit
      total=0 # assign total variable to calculate the total score
      digit=6 # first digit to play with out reroll dices
      while userInputs.strip()!="q": # if the user input in any part will be q the game will end
        score1=cls.calculate_score(dice) # defult score to compare it with user input score to avoid cheating
        if not userInputs.strip().isdigit() and userInputs.strip()!="q": # user input should be the dices or q
          print(f"You can't enter any thing untile the dices")
          userInputs=input("> ")
        elif userInputs.strip()=="q": # if user input == q the loop will stop
          break
        else: # this when user input = dices
          iinput=cls.string_to_tuple(userInputs.strip()) # convert string dices to tuble  of integer 
          score2=cls.calculate_score(iinput) # calculate the score of  user inpput
          if score2<=score1: # check if the user dose not cheating
            print(f"You have {score2} unbanked points and {6-len(iinput)} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
            # print to the  user messege to till him about unbank score he is have and the remaining dices and ask him to roll again or bank his score or quit
            digit2=digit-len(iinput) # assign digit2 to calculate the remaining dices
            userInputs=input("> ")
            if userInputs.strip()=="b": # if user choose bank
              total+=score2 # save his score to thetotal score
              dice=cls.roll_dice() # roll defult digit of dices for new round
              dices="*** "
              for i in dice:
                dices+=str(i)+" "
              else:
                dices+="***"
              print(f"You banked {score2} points in round {roun}\nTotal score is {total} points\nStarting round {roun+1}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
              # print to the user the score he banked and the round of this score and his total score and start new round whit its number and the dices and suggist to quit
              roun+=1 # rrassign the round number for nrw round
              userInputs=input("> ")
            elif userInputs.strip()=="r": # if user need to re-roll the remaining dices
              total2=cls.roll(score2,digit2,roun) # cull roll method to re-roll remining  dices and return the total value of score from re-roll time
              total+=total2 # add the re-roll score to the total score
              dice=cls.roll_dice() # roll defult dices
              dices="*** "
              for i in dice:
                dices+=str(i)+" "
              else:
                dices+="***"
              print(f"You banked {total2} points in round {roun}\nTotal score is {total} points\nStarting round {roun+1}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
              # print bank messege 
              roun+=1 # reassign for new round
              userInputs=input("> ")
          else: # if user are cheating the game will stop and tell him cheater
             return "Cheater!! oh no"
      return f"Thanks for playing. You earned {total} points" # in the end of game this will return
    @classmethod
    def startGame(cls):
      print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
      # Prompt the user for input and validate it
      userInputs=input("> ")
      while userInputs.strip()!="y" and userInputs.strip()!="n": # the user cant enter any think from his mind
         print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline you can't enter other thing")
         userInputs=input("> ")
      if userInputs.strip()!="n":
        # Start the game if the user chooses to play
        return cls.play(userInputs)
      else:
        # Return a message if the user declines to play
        return "OK. Maybe another time"
        

if __name__=="__main__":
  print(GameLogic.startGame())