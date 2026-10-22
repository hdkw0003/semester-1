# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

with open("images/feep.pgm", "r") as file:
    text = file.readlines()
    text = [line.strip().split() for line in text]
    if text[1][0] == "#":
     print(f"dimension: {text[1][0]} x {text[1][1]}")
     print(f"max gray: {text[2][0]}")
    else:
     print(f"dimension: {text[2][0]} x {text[2][1]}")
     print(f"max gray: {text[3][0]}")

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)