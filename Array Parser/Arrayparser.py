inputFile = open("./input.txt", "r")
outputfile = open("./output.txt", "w")

for line in inputFile:
    currentLine = ""
    for char in line:
        if char == "]":
            currentLine = currentLine[1:len(currentLine)]
            currentLine = currentLine.strip("[")
            outputfile.write(currentLine + "\n")
            currentLine = ""
            continue
        currentLine = currentLine + char

print("Complete")
