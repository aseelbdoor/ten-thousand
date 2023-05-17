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
    #return tuble of random number from 1 to 6 that have input length
      return tuple(random.randint(1, 6) for _ in range(number))
    def string_to_tuple(string):
      tuple_value = tuple(int(digit) for digit in string)
      return tuple_value
    @classmethod
    def startGame(cls):
      print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
      userInputs=input("> ")
      while userInputs.strip()!="y" and userInputs.strip()!="n":
         print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline you can't enter other thing")
         userInputs=input("> ")
      roun=0
      if userInputs.strip()!="n":
        roun+=1
        dice=cls.roll_dice()
        dices="*** "
        for i in dice:
          dices+=str(i)+" "
        else:
          dices+="***"
        print(f"Starting round {roun}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
        userInputs=input("> ")
        total=0
        while userInputs.strip()!="q":
          score1=cls.calculate_score(dice)
          if not userInputs.strip().isdigit() and userInputs.strip()!="q":
            print(f"You can't enter any thing untile the dices")
            userInputs=input("> ")
          elif userInputs.strip()=="q":
            break
          else:
            iinput=cls.string_to_tuple(userInputs.strip())
            score2=cls.calculate_score(iinput)
            if score2<=score1:
              print(f"You have {score2} unbanked points and {6-len(iinput)} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
              userInputs=input("> ")
              if userInputs.strip()=="b":
                total+=score2
                dice=cls.roll_dice()
                dices="*** "
                for i in dice:
                  dices+=str(i)+" "
                else:
                  dices+="***"
                print(f"You banked {score2} points in round {roun}\nTotal score is {total} points\nStarting round {roun+1}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
                roun+=1
                userInputs=input("> ")
        return f"Thanks for playing. You earned {total} points"
      else:
        return "OK. Maybe another time"
      
if __name__=="__main__":
   print(GameLogic.startGame())