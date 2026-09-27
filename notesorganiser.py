import os

print("*=======Notes Organiser=======*")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())

print()
print("======Word Count=======")
with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words))

print()
print("======Merging Notes=======")
if os.path.exists("merged_notes.txt"):
    print("All notes already exists")
else:
    print("file not found")

content = ""
with open("science-notes.txt", "r") as f:
    content += "========Science Notes=======\n"
    content += f.read() + "\n"

with open("maths-notes.txt", "r") as f:
    content += "========Maths Notes=======\n"
    content += f.read() + "\n"

with open("merged_notes.txt", "w") as f:
    f.write(content)

print("All notes merged")
print("Printing merged notes")

with open("merged_notes.txt", "r") as f:
    print(f.read())

if os.path.exists("merged_notes.txt"):
    os.remove("merged_notes.txt")
    print("All merged notes deleted")
else:
    print("Merged notes not found")