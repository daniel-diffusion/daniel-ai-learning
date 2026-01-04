name = "Daniel"
age = 45
is_learning_ai = True
print(f"Name: {name}, Age: {age}, Learning AI: {is_learning_ai}")
skills = ["AI", "Leadership", "Python", "Curiosity","Change", "Adaptability","Ideation", "Learning", "Critical Thinking"]
print (skills[7])
profile = {
    "name": "Daniel",
    "role": "Support Engineering Manager",
    "company": "Microsoft",
    "goal": "Become a power user for AI tool and python programming"
}
print(profile["goal"])
for skill in skills:
    print("Learning:", skill)

def greet(name):
    print(f"hello {name}, welcome to AI era)")
greet("Daniel")