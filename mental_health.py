# GAD-7 scoring example
gad7_questions = [
    "Feeling nervous, anxious, or on edge",
    "Not being able to stop or control worrying",
    "Worrying too much about different things",
    "Trouble relaxing",
    "Being so restless that it's hard to sit still",
    "Becoming easily annoyed or irritable",
    "Feeling afraid as if something awful might happen"
]

# User responses: 0 (not at all) to 3 (nearly every day)
responses = [2, 1, 2, 3, 1, 2, 2]  # Example input

score = sum(responses)

if score <= 4:
    level = "Minimal anxiety"
elif score <= 9:
    level = "Mild anxiety"
elif score <= 14:
    level = "Moderate anxiety"
else:
    level = "Severe anxiety"

print(f"GAD-7 Score: {score} → {level}")