# import random
# # print("welcome to the coin gussing game!\nchose a mothed to toss the coin:\n1- using random.random()\n2- using random.randint()")

# choce=int(input("enter your choce(1 or 2):\n"))

# if choce==1:
#   coin=random.random()
#   if coin>=0.5:
#     computer_ruselt="Heads"
#   else:
#     computer_ruselt="Tails"


# elif choce==2:
#   coin=random.randint(0,1)
#   if coin==0:
#     computer_ruselt="Heads"
#   else:
#     computer_ruselt="Tails"

# else:
#   print("invaild choce. please selct eithor 1 or 2")


# user_choce=input("Enter your choce (Heads or Tails):\n").capitalize()

# if user_choce==computer_ruselt:
#   print("congratulations you win!")

# else:
#  print("sorry you lose!")

# print(f"the computer choce was {computer_ruselt}")

# name=["marwa","menaa","mohamed","mona","magda"]
# # print(f"the first name is {name[0]} and last name is {name[-1]}")
# name[-1]="lola"
# print(name)
# library=["books","noteboks","markers","pens","pants"]
# library[3]="new pen"
# print(library)

# name=["nour","menaa","mohamed","lola"]

# print(name[3])
# print(name)

# colors=[]
# colors.append("black")
# colors.append("red")
# print(colors)
# colors=[]
# color=input("add the first color you like:\n")
# add_color=input("Do you want to add colors? (yes or no)\n")
# if add_color=="yes":
#   color2=input("add anthor color to the list:\n")
#   colors.append(color)
#   colors.append(color2)
#   print(f"the colors you like are:\n {colors}")

# else:
#   print(color)
# all_students=[]
# class_a=["marwa","mona","lola","menaa"]
# class_b=["mohamed","ahmed","ali","noha"]
# all_students.extend(class_a)
# all_students.extend(class_b)
# print(all_students)

# number=[4,6,7,2]
# number.remove(7)
# print(number)
# name=input("what is your name?\n")
# if name:
#   print(f"hello {name}")
# else:
#   print("you forget to enter name")

# bassket=["apples","mango","orange"]
# guess=input("guess the name of the friute salate:\n")
# if guess in bassket:
#   print("good guss")
  

# else:
#   print("sorry puteer try agin")



# books=input("enter the name of the book you own:\n")
# add_books=input("enter the name of a nother book you own (or press enter to skip):\n")
# library =[]
# if add_books:
#   library.append(books)
#   library.append(add_books)
#   print(f"you library :{library}")
  
# else:
#   print(f"you library: {books}")

# book_future=input("enter the name of a book you wish to have in the future:\n")
# add_book_future=input("enter the name of anthor book you wish to have in the future (or press enter to skip)\n")
# wishlist=[]
# if add_book_future:
#   wishlist.append(book_future)
#   wishlist.append(add_book_future)
#   print(f"your wishlist is: {wishlist}")

# else:
#   print(f"your wishlist is {book_future}")

# book_wishlist=input("enter the name of a book from your wishlist that you have aquired: (or press enter to skip):\n")
# if book_wishlist:
#   wishlist.remove(book_wishlist)
#   library.append(book_wishlist)
#   print(f"update library {library}")
#   print(f"update wishlist {wishlist}")
# else: 
#   print(f"update library {library}")
#   print(f"update wishlist {book_future}")


# library_wish=input("enter the name of a book from your library you wish to donat a friend:(or press enter to skip):\n")
# if library_wish:
#   library.remove(library_wish)
#   print(f"fainal library after donat {library}")
# else:
#   print(f"fainal library {library}")
# item=[]
# item_shopping=input("enter an item to add to your shopping list:\n")
# add_item_shopping=input("add anthor item? (press enter to skip):\n")
# if add_item_shopping:
#   item.append(item_shopping)
#   item.append(add_item_shopping)
#   print(f"\nyour shopiing list is {item}")
# else:
#   item.append(item_shopping)
#   print(f"\nyour shopiing list is {item_shopping}")

# remove_item=input("DID you by anything? enter item name to remove: (press enter to skip)\n")
# if remove_item:
#   if remove_item in item:
#     item.remove(remove_item)
#     print(f"\nupdate shoping list: {item}")
#   else:
#     print(f"{remove_item} is not your list.")
# else:
#   print(f"\nupdate shoping list: {item}")
# list=[]
# guess_name=input("Enter the name of the first guest:\n")
# add_name=input("\nDo tou want to add anthor guest? (press enter to skip):\n")
# if add_name:
#   list.append(guess_name)
#   list.append(add_name)
#   print(f"\nyour guset list is: {list}")
# else:
#   list.append(guess_name)
#   print(f"\nyour guset list is: {list}")
# ask_come=input("\ndid any one chanel and won't come? enter the name to remove (press enter to skip)\n")
# if ask_come:
#  if ask_come in list:
#    list.remove(ask_come)

# print(f"\nupdate guset list is: {list}")
  

# names_string=input("enter names speared by a comma")
# names=names_string.split(", ")
# print(type(names))
# print(names)
# print(len(names))

# print("welcome to 'whose wallet?\nyou well give me a list of names, and a will pick a person to pay.")
# name_string=input("if yo're ready, enter a list of names, spearted by a comma:\n").split(", ")
# import random
# print(f"please ask {random.choice(name_string)} to talk his wallet out.diiner is on him!")

# basket= ["apples","orange","milk","water"]
# basket.insert(3,"candy")
# print(basket)

# basket=[["aplles","bananes"],["Milk","water"]]
# print(basket)
# input("press enter to change the contact")
# basket[0].insert(0,"oranges")
# basket[0].insert(3,"candy")
# basket[1].insert(0,"coffee")
# basket[1].remove("water")
# basket[1].append("tea")
# basket.append(["1","2","3"])
# print(f"Here is ubdate baket:\n{basket}")

# print("welcome to place the rabit")
# faild=["☘️","☘️","☘️"],["☘️","☘️","☘️"],["☘️","☘️","☘️"]
# print(f"{faild[0]}\n{faild[1]}\n{faild[2]}")
# print("where should the rabbit Go?🐇")
# chosse=input("please chosse a raw and a cloumn")
# raw=int(chosse[0])
# cloumn=int(chosse[1])
# faild[raw -1][cloumn -1]="🐣" 
# print("\nsucces..\n")
# print(f"\n{faild[0]}\n{faild[1]}\n{faild[2]}")
# print("welcome to the shooting game")
# shooting=["♣️","♣️","♣️"],["♣️","♣️","♣️"],["♣️","♣️","♣️"]
# print(f"{shooting[0]}\n{shooting[1]}\n{shooting[2]}")
# print("where should you shoot?")
# chosse=input("please chosse a raw and choumn:")
# raw=int(chosse[0])
# cloumn=int(chosse[1])
# shooting[raw -1][cloumn-1]="♟️"
# print("\nHit!\n")
# print(f"{shooting[0]}\n{shooting[1]}\n{shooting[2]}")

# print("welcome to the dangerouse cupkake tray")
# cake=["✿","✿","✿"],["✿","✿","✿"],["✿","✿","✿"]
# print(f"{cake[0]}\n{cake[1]}\n{cake[2]}")
# print("which cupcake do you want to eat?")
# chosse=input("\nchosse a raw and cloumn:")
# raw=int(chosse[0])
# cloumn=int(chosse[1])
# if chosse[0]=="2" and chosse[1]=="2":
#   print("\nBoom! that one was a bomb! Game over☠")
#   cake[raw -1][cloumn -1]="☠"
#   print(f"\n{cake[0]}\n{cake[1]}\n{cake[2]}")

# else:
#   print("\nYummy!")
#   cake[raw -1][cloumn -1]="♛"
#   print(f"\n{cake[0]}\n{cake[1]}\n{cake[2]}")

# import random 
# rock_ascii="""

# ___
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper_ascii="""
# ______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# """

# scisoors_ascii="""


#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# print("Welcome to the rock, paper, scissors game!:")
# help=input("press enter to countinue or type (help) to see the rules:")
# if help=="help":
#   print("""      ♥♥♥♥♥♥♥♥♥ RULES ♥♥♥♥♥♥♥♥♥
#               1- you chossse and computer chosse
#               2-rock matches scissors-> rock wins
#               3-paper matches rock-> paper wins
#               4-scissors matches paper-> scissors wins
# """)
# user_choice=input("Enter your choice (rock. paper, scissors):").lower()
# if user_choice  not in ["rock", "paper", "scissors"] :
#   print("invailed choice. please enter rock, paper, scissors")

# else: 
#   if user_choice=="rock":
#     print(f"\nyou choce:\n{rock_ascii}")
#   elif user_choice=="paper":
#     print(f"\nyou choce:\n{paper_ascii}")
#   else:
#     print(f"\nyou choce:\n{scisoors_ascii}")

# #random choice the computer
# computer_choce=random.choice(["rock","Paper","scissors"])
# if computer_choce=="rock":
#   print(f"computer choce:\n{rock_ascii}")
# elif computer_choce=="paper":
#   print(f"computer choce:\n{paper_ascii}")

# else:
#   print(f"computer choce:\n{scisoors_ascii}")


# if user_choice==computer_choce:
#   print("it's a tie!")

# elif ( 
#   ( user_choice=="rock" and computer_choce=="scissors")
# or
#   (user_choice=="paper" and compile=="rock")
# or
#   (user_choice=="scissors" and computer_choce=="paper") 

# ):
#   print(f"you win! {user_choice} beats {computer_choce}")

# else:
#   print(f"you lose! {computer_choce} beats {user_choice}")

# names=["Marwa","Mohamed","lola","Nour"]
# for x in names:
#   if x=="lola":
#     print(f"{x} she's my best friend")

# #   else:
# #     print(x)

# books=["book1","book2","book3","book5"]
# books.insert(3,"book4")
# for x in books:
#   if x=="book2":
#     print(f"i have {x} in my library")
#   else:
#     print(x)
    

# number=[1,2,3,4,5,6,7,8,9,10]
# for m in number:
#   if m%2==0:
#     print(f"\n{m}\n")

# print("finished is loop succsesfully")

# student=["Marwa","nour","Mona","lola"]
# for n in student:
#   print(n)
#   print("attendance comfaried")
#   print("___________")

# names=["Lola","Marwa","Mohamed","tito"]
# for x in names:
#   print(x)
#   ask=input("is person coming? type (yes or no):")
#   if ask=="yes":
#     print("attendance comfaried")
  
#   else: 
#     print("attendance not comfaried")
# #   print("______________")
# attendance=input("\nenter he names of attendance spearted bt a comma:\n").split(", ")
# for person in attendance:
#   print(person)
#   ask=input("\nis person coming? type yes or no")
#   if ask=="yes":
#     print("attendance comfaried")

#   else:
# #     print("attendance not comfaried") 
# #   print("\n____________________\n")
# country=input("please type the name of the countyries by a comma:\n").split(", ")
# for x in country:
#   print("\n"+ x + "\n")
#   ask=input(f"have you visitied {x} before? type(yes or No):")
#   if ask=="yes":
#     print("i hope you had a good time")
#   else:
#     print("i hope you visit it soon")
#   print("_____________________")
# input("press enter to Exit")

done_task=[]
onoging_task=[]

task_today=input("Enter your task for today spearted by a comma:\n").split(", ")
for Z in task_today:
  ask=input(f"\nDid you finish {Z}? type (yes or no):\n")
  if ask=="yes":
    print("\nnice Jop")
    done_task.append(Z)

  else:
    print("\ntry not to but it off")
    onoging_task.append(Z)
progras=input("\ndo you went to see your porgras? type (yes or no)")
if progras=="yes":
  print(f"\n         ****** Done Task *******\n{done_task}\n")
  print(f"\n         ****** Ooging Task *******\n{onoging_task}\n")
else:
  print("thanks for using the app")


















