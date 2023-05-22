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
    
    def hotdices():
        pass

    def zilch():
        pass
    
if __name__=="__main__":
    a=(1,2,2,3,4)
    b=(1,2,2,5)
    print(Printed.cheater(a,b,5))