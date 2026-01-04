areas = ["health","family", "career", "friends", "learning", "fun"]
scores = []
for area in areas:
    score = input (f"Rate your {area} 1 to 10: ")
    scores.append(int(score))

total = sum(scores)
average = total /len(scores)
print (f"your life score is {total} and the average is {average:.1f}/10") 
if average >=7:
    print ("you are awesome")
else:
    print ("keep pushing, you will get there")