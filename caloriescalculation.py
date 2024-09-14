import pandas as pd

# Load the standardized dataset
file_path = '/Users/pratikluitel/Desktop/Calories_data/Standardized_Food_calories.csv'
data = pd.read_csv(file_path)

# Function to search for a food item and return its calories per 100g/ml
def get_calories(food_item):
    food_data = data[data['Food'].str.contains(food_item, case=False, na=False)]
    
    if not food_data.empty:
        return food_data[['Food', 'Calories_per_100']]
    else:
        print(f"Food item '{food_item}' not found.")
        return pd.DataFrame()  # Return an empty DataFrame if food not found

# Example usage
while True:
    user_input = input("Enter food items separated by commas (or type 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        break
    
    # Split the user input into individual food items
    food_items = [food.strip() for food in user_input.split(',')]
    
    total_calories = 0
    all_food_data = pd.DataFrame()

    for food in food_items:
        # Get individual food calorie data
        food_data = get_calories(food)
        if not food_data.empty:
            # Add the calories from the current food item to the total
            total_calories += food_data['Calories_per_100'].sum()
            all_food_data = pd.concat([all_food_data, food_data])

    if not all_food_data.empty:
        print("\nIndividual Calories for Each Food Item:")
        print(all_food_data)

        # print(f"\nTotal Calories for all food items: {total_calories:.2f} cal\n")
