print("SMART NOTES ORGANIZER")

sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n"
] 
file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("\nSample file 'class-notes.txt' created successfully.")

print("\nPreview Notes with read(n)") 
file = open("class-notes.txt", "r")
preview = file.read(40)
file.close() 
print("First 40 characters:")
print(preview)

print("\nRead All Lines with readlines()") 
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close() 
print("Total lines in file:", len(lines)) 
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())

print("\nLoop Through File Line by Line") 
file = open("class-notes.txt", "r") 
for line in file:
    print("Reading:", line.strip())
file.close()

print("\nFilter Lines with Conditions")
file = open("class-notes.txt", "r") 
for line in file:
    if line.startswith("SKIP"):
        print("Skipped:", line.strip())
    else:
        print("Kept:", line.strip()) 
file.close()

print("\nCopy Selected Lines to a New File") 
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close() 
output_file = open("organized-notes.txt", "w")
for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        output_file.write(line) 
output_file.close() 
print("Selected lines copied to 'organized-notes.txt'.")

print("\nOrganized Notes:") 
file = open("organized-notes.txt", "r") 
for line in file:
    print(line.strip()) 
file.close()

print("SMART NOTES ORGANIZER SUMMARY")
print("read(n): Previewed the first few characters.")
print("readlines(): Stored all lines in a list.")
print("Loop: Read the file line by line.")
print("Condition: Skipped lines starting with SKIP.")
print("Copy: Saved IMPORTANT and TODO lines into a new file.")