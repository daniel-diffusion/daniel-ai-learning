name = input("Enter your name: ")
mood = input("How are you feeling today (1-10)? ")
mood = int(mood)

print (f"hello {name}!")
if mood >=7:
    print (f"You are feeling great today, {name}, awesome day to build AI!")
else:
    print (f"No worries for today, {name}. Hope things get better!")