

"""
file = open("test.txt", "w")

file.write("Ahoj světe! Jak se máš?")

file.close()

file = open("test.txt", "r")
data = file.read()
file.close()
print(data)
"""
# Task 1


def load_data(file_name):
    try:
        source_file = open(file_name, "r")
        source_data = source_file.read()
        return source_data
    except:
        print("Došlo k chybě")
    finally:
        source_file.close()


def processing_data_1(source_data):
    words = source_data.split(" ")
    long_words = []
    for w in words:
        if len(w) > 6:
            long_words.append(w)
    return long_words


def save_data(new_file_name, long_words):
    new_file_1 = open(new_file_name, "w")
    new_file_1.write(str(long_words))
    new_file_1.close()


data = load_data("task_1_help.txt")
new_data = processing_data_1(data)
save_data("new_file_1.txt", new_data)

# Task 2


def processing_data_2(data):
    processed_data = data.split("\n")
    return (processed_data)


def save_data_2(file_name, data):
    with open(file_name, "w") as new_file:
        for line in data:
            new_file.write(line + "\n")


data_2 = load_data("task_2_help.txt")
new_data_2 = processing_data_2(data_2)
save_data_2("new_file_2.txt", new_data_2)

# Task 3


def processing_data_3(data):
    source_data_lines = data.split("\n")
    reversed_source_data_lines = reversed(source_data_lines)
    return (reversed_source_data_lines)


data_3 = load_data("task_2_help.txt")
new_data_3 = processing_data_3(data_3)
save_data_2("new_file_3.txt", new_data_3)
