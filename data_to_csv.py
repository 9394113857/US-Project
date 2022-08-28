data = [["var112"],
        ["var234"],
        ["var356"]]
with open('csvfile.csv', 'w') as file:
    for line in data:
        for cell in line:
            file.write(cell)
        file.write("\n")
