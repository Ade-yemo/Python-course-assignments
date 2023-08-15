print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1= name1.lower()
lower_name2= name2.lower()
name1_2=lower_name1+lower_name2
t=name1_2.count("t")
r=name1_2.count("r")
u=name1_2.count("u")
e=name1_2.count("e")
l=name1_2.count("l")
o=name1_2.count("o")
v=name1_2.count("v")
e=name1_2.count("e")
true=str(t+r+u+e)
love=str(l+o+v+e)
score=true+love
score_int=int(score)
if score_int<10 or score_int>90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int>40 and score_int<50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")    