from email_validator import validate_email, EmailNotValidError
from faker import Faker
import csv
import random

fake = Faker("en_US")

email_domains = ["gmail.com", "yahoo.com", "example.com", "hotmail.com"]

num_records = 5


def generate_users_csv(csv_file: str):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(['user_id', 'name', 'email', 'signup_date'])

        for user_id in range(1, num_records + 1):
            name = fake.name()
            if user_id % 100 == 0:
                email = f"{fake.user_name()}@gmail"
            else:
                email = f"{fake.user_name()}@{random.choice(email_domains)}"
            signup_date = fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([user_id, name, email, signup_date])


def _format_date(date: str) -> str:
    """Format the date from timestamp to YYYY-MM-DD"""
    
    return date.split(" ")[0]


def is_valid_email(email: str) -> bool:
    """Check if an email is valid"""
    
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def get_email_domain(email: str) -> str:
    """Extract the domain from an email address"""
    
    return email.split("@")[1]
