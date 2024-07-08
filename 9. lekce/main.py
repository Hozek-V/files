


file = open("test.txt", "w")

file.write("Ahoj světe! Jak se máš?")

file.close()

file = open("test.txt", "r")
data = file.read()
file.close()
print(data)