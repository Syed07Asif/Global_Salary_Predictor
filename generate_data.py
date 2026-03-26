import pandas as pd
import random

education_levels = ["Bachelor", "Master", "PhD"]
job_roles = [
    "Data Scientist", "ML Engineer", "Software Engineer",
    "Data Analyst", "Cloud Engineer", "Cybersecurity"
]

country_locations = {
    "USA": ["New York","San Francisco","Seattle","Austin","Chicago","Boston"],
    "UK": ["London","Manchester","Birmingham","Edinburgh"],
    "Germany": ["Berlin","Munich","Frankfurt","Hamburg"],
    "Australia": ["Sydney","Melbourne","Brisbane","Perth"],
    "India": ["Bangalore","Hyderabad","Mumbai","Delhi","Chennai","Pune"],
    "UAE": ["Dubai","Abu Dhabi"],
    "Singapore": ["Singapore"],
    "Malaysia": ["Kuala Lumpur"],
    "Spain": ["Madrid","Barcelona"],
    "Netherlands": ["Amsterdam","Rotterdam"],
    "Ireland": ["Dublin"],
    "Luxembourg": ["Luxembourg"],
    "Canada": ["Toronto","Vancouver","Montreal"],
    "France": ["Paris","Lyon"],
    "Switzerland": ["Zurich","Geneva"],
    "Sweden": ["Stockholm"],
    "Japan": ["Tokyo","Osaka"]
}

# Base salary (USD/year)
base_salary_country = {
    "USA": 120000,
    "UK": 65000,
    "Germany": 80000,
    "Australia": 100000,
    "India": 20000,
    "UAE": 85000,
    "Singapore": 95000,
    "Malaysia": 30000,
    "Spain": 50000,
    "Netherlands": 85000,
    "Ireland": 90000,
    "Luxembourg": 110000,
    "Canada": 90000,
    "France": 70000,
    "Switzerland": 120000,
    "Sweden": 80000,
    "Japan": 75000
}

# Role multiplier
role_multiplier = {
    "Data Scientist": 1.2,
    "ML Engineer": 1.3,
    "Software Engineer": 1.1,
    "Data Analyst": 0.9,
    "Cloud Engineer": 1.25,
    "Cybersecurity": 1.2
}

# Location multiplier
location_multiplier = {
    "San Francisco": 1.5, "New York": 1.4, "Seattle": 1.3,
    "Austin": 1.1, "Chicago": 1.1, "Boston": 1.2,

    "London": 1.4, "Manchester": 1.1, "Birmingham": 1.0, "Edinburgh": 1.1,

    "Berlin": 1.1, "Munich": 1.3, "Frankfurt": 1.2, "Hamburg": 1.1,

    "Sydney": 1.3, "Melbourne": 1.2, "Brisbane": 1.1, "Perth": 1.1,

    "Bangalore": 1.3, "Mumbai": 1.2, "Hyderabad": 1.1,
    "Delhi": 1.1, "Chennai": 1.0, "Pune": 1.1,

    "Dubai": 1.3, "Abu Dhabi": 1.2,

    "Singapore": 1.4, "Kuala Lumpur": 1.1,

    "Madrid": 1.1, "Barcelona": 1.2,

    "Amsterdam": 1.3, "Rotterdam": 1.2,

    "Dublin": 1.3,

    "Luxembourg": 1.4,

    "Toronto": 1.2, "Vancouver": 1.3, "Montreal": 1.1,

    "Paris": 1.3, "Lyon": 1.1,

    "Zurich": 1.5, "Geneva": 1.4,

    "Stockholm": 1.2,

    "Tokyo": 1.3, "Osaka": 1.2
}

data = []

for _ in range(3500):  # bigger dataset
    experience = random.randint(0, 12)
    education = random.choice(education_levels)
    job = random.choice(job_roles)

    country = random.choice(list(country_locations.keys()))
    location = random.choice(country_locations[country])

    base_salary = base_salary_country[country]

    # Role impact
    salary = base_salary * role_multiplier[job]

    # Location impact
    salary *= location_multiplier.get(location, 1.0)

    # Experience growth
    salary += experience * random.randint(3000, 10000)

    # Education impact
    if education == "Master":
        salary *= 1.1
    elif education == "PhD":
        salary *= 1.2

    annual_salary = int(salary)
    monthly_salary = int(annual_salary / 12)

    data.append([
        experience, education, job, location, country,
        monthly_salary, annual_salary
    ])

df = pd.DataFrame(data, columns=[
    "Experience", "Education", "JobRole", "Location", "Country",
    "Salary_Monthly_USD", "Salary_Annual_USD"
])

df.to_csv("salary_data.csv", index=False)

print("Dataset created!")