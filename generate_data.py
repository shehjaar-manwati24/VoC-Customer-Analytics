import pandas as pd
import random

# We are simulating an "OTP Service Outage" scenario
problems = [
    "OTP code never arrives on my phone",        # The Main Incident (60% of cases)
    "OTP sms is delayed by 10 minutes",          # Related to main incident
    "app crashing when opening scanner",         # Minor bug
    "transaction failed but money deducted",     # Severe but rare
    "login timeout is too fast",                 # Usability issue
    "interface is confusing and slow"            # General noise
]

# We force 'OTP' issues to appear 6x more often than others
weights = [60, 20, 5, 5, 5, 5]

data = []

# Generate 150 Negative Reviews (skewed towards OTP issues)
for _ in range(150):
    # random.choices allows us to use weights
    chosen_problem = random.choices(problems, weights=weights, k=1)[0]
    review = chosen_problem + " " + random.choice(["fix it", "terrible", "help", "useless"])
    data.append([review, 1])

# Generate 50 Positive Reviews (just for noise)
for _ in range(50):
    data.append(["great app works well", 5])

# Save to CSV
df = pd.DataFrame(data, columns=['review', 'rating'])
df.to_csv('reviews.csv', index=False)
print("Success! Dataset created.")