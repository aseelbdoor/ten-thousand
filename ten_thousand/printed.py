from sys import exit

class Printed:
    def __init__(self) -> None:
        pass

    def decorate(dice):
        dices="*** " # made good format for dices 
        for i in dice:
            dices+=str(i)+" "
        else:
            dices+="***"
        return dices
    
    def string_to_tuple(string):
      # Convert each character in the string to an tuble of integer using a generator expression
      string=string.replace(" ","")
      tuple_value = tuple(int(digit) for digit in string)
      return tuple_value

    def quit_game(message):
        exit(message)

    def end_game(total):
        print(f"Thanks for playing. You earned {total} points")
        exit()
    
    def validate(dice,user):
        for i in user:
            if i in dice:
                if dice.count(i)>=user.count(i):
                    continue
                else:
                    return False
            else:
                return False
        return True
    
    def padInput(user,per):
        while user.strip() not in per:
            if user.strip().isdigit():
                return user
            print(f"You can't enter any thing untile {per}")
            user=input("> ")
        return user
    
    @classmethod
    def cheater(cls,dice,user,total):
        dices=cls.decorate(dice)
        while not cls.validate(dice,user):
            print(f"Cheater!!! Or possibly made a typo...\n{dices}\nEnter dice to keep, or (q)uit:")
            user=input("> ")
            if user.strip()=="q":
                cls.quit_game(f"Thanks for playing. You earned {total} points")
            else:
                user=cls.string_to_tuple(user)
        return user
    
    def hotdices(dice,digit):
        if len(dice)==digit:
            dice=sorted(dice)
            if digit==6:
                for i in range(0,6,2):
                    if dice.count(dice[i])==2:
                        continue
                    else:
                        break
                else:
                    return True
                for i in range(0,5):
                    if dice[i+1]==dice[i]+1:
                        continue
                    else:
                        break
                else:
                    return True
            for i in range(len(dice)):
                if dice[i]==1 or dice[i]==5:
                    continue
                else:
                    if dice.count(dice[i])>2:
                        continue
                    else:
                        return False
            return True     
        else:
            return False
    
    @classmethod
    def zilch(cls,dice):
        dices=cls.decorate(dice)
        return f"{dices}\n****************************************\n**        Zilch!!! Round over         **\n****************************************"
    
