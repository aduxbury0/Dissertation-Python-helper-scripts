inputFile = open("input.txt", "r")
outputFile = open("output.txt","w")


for line in inputFile:
    data = line
    data = data.strip()
    data = data.strip('[],')
    data = data.strip()
    outputFile.write(data + "\n")


inputFile.close()
outputFile.close()