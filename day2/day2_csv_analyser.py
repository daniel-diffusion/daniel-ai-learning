import csv
from pathlib import Path


scores = []
data_path = Path(__file__).resolve().parent / "data.csv"
with data_path.open("r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        scores.append(int(row["score"]))

average = sum(scores) / len(scores)
max_score = max(scores)
min_score = min(scores)

print(f"Average score: {average:.2f}")
print(f"Max score: {max_score}")
print(f"Min score: {min_score}")

with data_path.open("r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["score"]) >=8:
            print(f"Name {row['name']}, has an awesome score {row['score']}")
        else:
            print(f"Name {row['name']}, score {row['score']}")
print("Data analysis complete.")

#new_rows = [
#    ["John", 9],
#    ["Maria", 4],
#    ["Zoe", 7]
#]
#with open("data.csv", "a", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerows(new_rows)
