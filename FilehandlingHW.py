file1 = open('example.txt', 'r')
content = file1.read()
print("FULL CONTENT")
print(content)
file1.close()

# --- PART 2: READ LINE BY LINE ---
# Open again, read just the first line, and close
file2 = open('example.txt', 'r')
line = file2.readline()
print("FIRST LINE")
print(line)
file2.close()

# --- PART 3: READ AS A LIST ---
# Open again, read into a list, and close
file3 = open('example.txt', 'r')
x = file3.readlines()
print("LIST OF STRINGS")
print(x)
file3.close()