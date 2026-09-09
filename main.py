distinctions = []
pass_list = {}
fail_list = {}
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
        distinctions.append(grades[key])


print("\nFailed")
for key, val in fail_list.items():
     print(f'Name:{key}| grade {val}')

print("\nPassed: ")
for key, val in pass_list.items():
     print(f'Name:{key}| grade {val}')


print("Learners with distinctions: ")
for i in range(len(distinctions)):
    print(i)

class_avarage = round(sum(grades.values())/len(grades),2)
print(f"Class avarage:{class_avarage} ")

