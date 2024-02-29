Answer = input("do you want to play this game?[Yes/NO]:")

if Answer == "yes":
   print("welcome to the game!")
   Answer = input("do you want to go jungle or cave?[jungle/cave]:")
   if Answer == "jungle":
       print("you see the hungry tiger tiger will ear you.game clode!")
   elif Answer == "cave":
        print("you seen the bear in front of cave")
        Answer = input("do you want to fight with bear or run away!")
        if Answer == "fight":
            print("bear is too much strong ! you loss the game!")
        else:
            print("WOW! still you are alive!")

else:
    print("The Game closed")