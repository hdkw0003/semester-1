# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading
name = input("Please enter your name. ")
age = input("Please enter your age. ")
colour = input("Please enter your favourite colour. ")
# Write each piece of information to the file, each on a new line.

with open("user_info.txt", "w") as f:
    f.write(f"name: {name}\n")
    f.write(f"age: {age}\n")
    f.write(f"favourite colour: {colour}\n")

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
