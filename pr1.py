# ==========================================
# Interactive Personal Data Collector
# Fundamental Booster Project
# ==========================================

# Welcome Message and Instructions
print("=" * 60)
print("Welcome to the Interactive Personal Data Collector!")
print("=" * 60)
print("\nThis program will collect your personal information and")
print("display it along with data type details and memory locations.")
print("\nPlease follow the prompts to enter your information.\n")

# ==========================================
# STEP 1: Collect Information from User
# ==========================================

# Collect name (string)
name = input("Please enter your name: ")

# Collect age (integer)
age_input = input("Please enter your age: ")
age = int(age_input)  # Type casting from string to integer

# Collect height (float)
height_input = input("Please enter your height in meters: ")
height = float(height_input)  # Type casting from string to float

# Collect favourite number (integer)
fav_number_input = input("Please enter your favourite number: ")
fav_number = int(fav_number_input)  # Type casting from string to integer

print("\nThank you! Processing your information...\n")

# ==========================================
# STEP 2: Data Processing
# ==========================================

# Calculate approximate birth year (current year 2026)
current_year = 2026
birth_year = current_year - age

print("=" * 60)
print("Your Information Summary")
print("=" * 60)

# ==========================================
# STEP 3: Display Results with Data Types and Memory Info
# ==========================================

# Display name information
print(f"\nName: {name} (Type: {type(name)}, Memory Address: {id(name)})")

# Display age information
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")

# Display height information
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")

# Display favourite number information
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)}, Memory Address: {id(fav_number)})")

# Display calculated birth year
print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

# Display type conversions explanation
print("\n" + "=" * 60)
print("Type Conversion Information:")
print("=" * 60)
print(f"Input age '{age_input}' (string) was converted to integer: {age}")
print(f"Input height '{height_input}' (string) was converted to float: {height}")
print(f"Input favourite number '{fav_number_input}' (string) was converted to integer: {fav_number}")

print("\n" + "=" * 60)
print("Thank you for using the Personal Data Collector. Goodbye!")
print("=" * 60)
