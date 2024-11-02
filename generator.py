import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker and random seed
fake = Faker()
random.seed(42)

# Function to generate random company names
def generate_company_name():
    company_name = fake.company().upper()
    return company_name.strip("@ ")

# Create data for 500 users
data = []
for _ in range(500):
    # Generate random user data
    user_data = {
        "login": fake.user_name(),
        "name": fake.name(),
        "company": generate_company_name(),
        "location": "Toronto",
        "email": fake.email(),
        "hireable": random.choice([True, False]),
        "bio": fake.sentence(nb_words=10),
        "public_repos": random.randint(10, 200),
        "followers": random.randint(101, 1000),  # Ensuring over 100 followers
        "following": random.randint(10, 500),
        "created_at": (datetime.now() - timedelta(days=random.randint(365, 3650))).strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    data.append(user_data)

# Write data to users.csv
with open("users.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["login", "name", "company", "location", "email", "hireable", "bio", "public_repos", "followers", "following", "created_at"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("users.csv has been created with 500 rows of mock data.")
