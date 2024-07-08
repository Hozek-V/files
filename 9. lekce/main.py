

"""
file = open("test.txt", "w")

file.write("Ahoj světe! Jak se máš?")

file.close()

file = open("test.txt", "r")
data = file.read()
file.close()
print(data)
"""
#Task 1
source_file = open("task_1_help.txt", "r")
source_data = source_file.read()
source_file.close()

new_file_1 = open("new_file_1.txt", "w")
new_file_1.write(source_data)
new_file_1.close()

#Task