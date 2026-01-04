from pathlib import Path
import logging

logging.basicConfig(
    filename='csv_analysis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Starting CSV analysis")

def analyse_scores(filename):
    import csv
    scores = []

    data_path = Path(__file__).resolve().parent / filename
    with data_path.open("r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            scores.append(int(row["score"]))

    average = sum(scores) / len(scores)
    return average, max(scores), min(scores)

try:
    avg, max_score, min_score = analyse_scores("data.csv")
except FileNotFoundError:
    print ("CSV file not found.")
except ValueError:
    print("Error processing CSV data.")
logging.info(f"Average score: {avg:.2f}")
print(f"Average score: {avg:.2f}")
print(f"Max score: {max_score}")
print(f"Min score: {min_score}")