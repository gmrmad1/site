import pandas as pd

# ---------------------------
# Pandas Series practice
# ---------------------------

# Create a Series
ser = pd.Series(
    [88, 92, 79, 85, 90],
    index=["Maths", "Physics", "Chemistry", "Biology", "English"]
)

# Naming the Series and its index
ser.name = "Marks"
ser.index.name = "Subject"

print("Series:")
print(ser)
print()

# Accessing Series elements
print("Marks in Chemistry:", ser["Chemistry"])
print("First three subjects:")
print(ser[:3])
print()


# ---------------------------
# Pandas DataFrame practice
# ---------------------------

# Create a larger DataFrame (20 rows, 7 columns)
data = {
    "RollNo": list(range(1, 21)),
    "Name": [
        "Madhav", "Keshav", "Abhir", "Riya", "Aarav",
        "Ananya", "Vihaan", "Ishita", "Arjun", "Kavya",
        "Rahul", "Sneha", "Aditya", "Pooja", "Rohan",
        "Neha", "Siddharth", "Meera", "Varun", "Nisha"
    ],
    "Class": [12, 7, 12, 10, 9, 11, 8, 10, 12, 9,
              11, 10, 12, 9, 8, 11, 10, 12, 9, 8],
    "Section": [
        "A", "B", "A", "C", "B",
        "A", "C", "B", "A", "C",
        "B", "A", "C", "B", "A",
        "C", "B", "A", "C", "B"
    ],
    "Maths": [88, 76, 91, 84, 79, 90, 73, 86, 92, 81,
              77, 89, 94, 78, 75, 88, 83, 91, 80, 76],
    "Science": [90, 74, 93, 82, 81, 92, 75, 85, 94, 83,
                78, 88, 95, 79, 76, 89, 84, 92, 82, 77],
    "Attendance": [95, 88, 98, 90, 85, 96, 87, 92, 99, 89,
                   86, 94, 97, 88, 84, 93, 91, 98, 90, 87]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print()


# ---------------------------
# Accessing DataFrame data
# ---------------------------

# Accessing a column (Series)
maths_col = df["Maths"]
maths_col.name = "Maths Marks"
maths_col.index.name = "Student Index"

print("Maths column:")
print(maths_col)
print()

# Accessing multiple columns
print("Name and Science columns:")
print(df[["Name", "Science"]])
print()

# Accessing rows using loc
print("Row with index 0:")
print(df.loc[0])
print()

print("Rows from index 5 to 10:")
print(df.loc[5:10])
print()

# Accessing specific value using loc
print("Science marks of student at index 3:")
print(df.loc[3, "Science"])
print()
