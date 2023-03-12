import os
import shutil


with open("friends.txt", "w") as f:
    f.write("Viktor\n")
    f.write("Vlatko\n")
    f.write("Filip\n")

# Display the contents of friends.txt on the console.
with open("friends.txt", "r") as f:
    print(f.read())

input("Press Enter to rename the file...")

# Rename file friends.txt to bestfriends.txt
os.rename("friends.txt", "bestfriends.txt")

input("Press Enter to make a copy of the file...")

# Make a copy of bestfriends.txt under the name sysadmins.txt
shutil.copy("bestfriends.txt", "sysadmins.txt")

input("Press Enter to list all files with specific names and extensions...")

# List all files whose name begins with letter 'b' and ends with extension txt.
for filename in os.listdir("."):
    if filename.startswith("b") and filename.endswith(".txt"):
        print(filename)

input("Press Enter to get the size of the file...")


print(os.path.getsize("sysadmins.txt"))

input("Press Enter to create a file with a list of cars...")

# Create file cars.txt with a list of 5 brands of cars on separate lines.
with open("cars.txt", "w") as f:
    f.write("Toyota\n")
    f.write("BMW\n")
    f.write("Ford\n")
    f.write("Yugo\n")
    f.write("Nissan\n")

input("Press Enter to get the size of the file...")

# Check the size
print(os.path.getsize("cars.txt"))

input("Press Enter to copy the file to /tmp directory...")

# Copy the file cars.txt into directory /tmp
shutil.copy("cars.txt", "/tmp")

input("Press Enter to list all .txt files in /tmp directory...")

# List all files with extension *.txt in directory /tmp.
for filename in os.listdir("/tmp"):
    if filename.endswith(".txt"):
        print(filename)

input("Press Enter to exit...")

