import random
responses = [
    "Yes, but only after coffee ☕",
    "No. And you know why.",
    "Absolutely. You’re unstoppable.",
    "Ask again after debugging.",
    "The AI gods say: maybe."
]
question = input ("What is your question? ")
answer = random.choice(responses)
print ("\n Answer:")
print (answer)
print ("\n")
