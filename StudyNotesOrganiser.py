import os

print("=== English Notes ===")
with open(r"C:\Users\PC\OneDrive - Wellington College India\Desktop\Python Classes\P-Lesson 15\english-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word Count ===")
with open(r"C:\Users\PC\OneDrive - Wellington College India\Desktop\Python Classes\P-Lesson 15\music-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

print("=== Merging Notes ===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists - overwriting")
else:
    print("all-notes.txt not found - creating now")

content = ""
with open(r"C:\Users\PC\OneDrive - Wellington College India\Desktop\Python Classes\P-Lesson 15\english-notes.txt", "r") as f:
    content += "--- english-notes.txt--- \n"
    content += f.read() + "\n"
with open(r"C:\Users\PC\OneDrive - Wellington College India\Desktop\Python Classes\P-Lesson 15\music-notes.txt", "r") as f:
    content += "--- music-notes.txt --- \n"
    content += f.read() + "\n"
with open("all-notes.txt", "w") as out:
    out.write(content)

if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("all-notes.txt deleted.")
else:
    print("all-notes.txt does not exist.")