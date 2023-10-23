rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Hello User , Welcome to the world of \n \n \t \t\t ℝ𝕆ℂ𝕂 ℙ𝔸ℙ𝔼ℝ 𝕊ℂ𝕀𝕊𝕊𝕆ℝ𝕊 \n")
user_val= int(input("What do you choose? Tpye 0 for Rock,1 for Paper or 2 for Scissiors \n"))
computer_val= random.randint(0,2)
print(f"\n Your chose -> {user_val} ")

if user_val == 0 :
    print(rock)
elif user_val == 1:
    print(paper)
else :
    print(scissors)

print(f"The computer chose -> {computer_val} ")
if computer_val == 0 :
    print(rock)
elif computer_val == 1:
    print(paper)
else :
    print(scissors)

if user_val == computer_val:
    print("Well, well, well, it's a tie! \n The universe couldn't decide who's cooler.")
elif user_val > computer_val and computer_val != 0:
    print("Congratulations! You're officially cooler than the computer.  \n It's probably sulking in a corner now.")
else:
    print("Ha, ha, ha! The computer is doing its victory dance. \n Don't worry, you're still a rock star in our book!")


