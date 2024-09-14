import pandas as pd
import re

# Load the dataset
file_path = '/Users/pratikluitel/Desktop/Calories_data/Food_calories_Sheet1.csv'
data = pd.read_csv(file_path)

# Function to classify whether the serving is in grams (g) or milliliters (ml)
def classify_food(serving):
    if 'g' in serving:
        return 'Solid'
    elif 'ml' in serving:
        return 'Liquid'
    else:
        return 'Unknown'

# Function to extract the weight or volume in grams or milliliters
def extract_weight_volume(serving):
    match = re.search(r'(\d+)\s*(g|ml)', serving)
    if match:
        return int(match.group(1))
    else:
        return None

# Function to extract the calorie value
def extract_calories(calories):
    match = re.search(r'(\d+)\s*cal', calories)
    if match:
        return int(match.group(1))
    else:
        return None

# Add new columns to classify food, extract weight/volume, and calories
data['Type'] = data['Serving'].apply(classify_food)
data['Weight_Volume'] = data['Serving'].apply(extract_weight_volume)
data['Calories'] = data['Calories'].apply(extract_calories)

# Standardize calories per 100g for solid foods and per 100ml for liquid foods
data['Calories_per_100'] = (data['Calories'] / data['Weight_Volume']) * 100

# Save the standardized data to a new CSV file
standardized_file_path = '/Users/pratikluitel/Desktop/Calories_data/Standardized_Food_calories.csv'
data.to_csv(standardized_file_path, index=False)

print(f"Standardized data saved to {standardized_file_path}")
