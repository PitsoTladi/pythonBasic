distinctions = []
pass_list = {}
fail_list = {}

# store names and grades of students in key value pairs
grades ={
    "Mpho":80,
    "Lerato":90,
    "Tshego" : 45,
    "joseph": 92,
    "Micheal": 70,
}

# print all names in list 
print("All names: ")
for key,val in grades.items():
    print(f'Name:{key}| grade {val}')

# validate and insert names into seperate dictionaries based on grade
    if val < 50:
        fail_list[key] = val

    elif val > 50 and val < 80:
       pass_list[key] = val

# add all students with grade > 50 into distinction list
    elif val >= 80:
        pass_list[key] = val
        distinctions.append(key)


print("\nFailed")
for key, val in fail_list.items():
     print(f'Name:{key}| grade {val}')

print("\nPassed: ")
for key, val in pass_list.items():
     print(f'Name:{key}| grade {val}')


print("Learners with distinctions: ")
for i in distinctions:
    print(i)

class_avarage = round(sum(grades.values())/len(grades),2)
print(f"Class avarage:{class_avarage} ")

##funtions
def fizzBuzz(num):
    if num%2 == 0:
        print('fizz')
    else:
        print('buzz')

fizzBuzz(15)

#imort module
import random

# 
hand = input('pick a rock,Paper or Sciscor: ').lower()
comp_options = ['rock','Paper','Sciscor']

#computer picks random element from list
computer_hand = random.choice(comp_options).lower()

# print winner depending on user input and random 
if computer_hand == hand:
    print('tie')

elif (computer_hand == 'rock' and hand == 'scissor') or (computer_hand == 'paper' and hand == 'rock') or (computer_hand == 'scissor' and hand == 'paper'):
    print('computer wins')

else:
    print('player wins')
