print "Welcome to my TODO app"

""" name = "Jan"
names = ["Jan, MessiSucks, RonaldoISaBitch"]
surname = "kajtebriga"

user = ["name", "lipovnik", "23", "maribor", "69.69"]

print user[2]
"""

todo_list = []

todo_dictionary = {}

while True:
    task = raw_input("Please enter TODO task: ")
    # todo_list.append(task)

    complete = raw_input("Is this task finished? (yes/no): ")

    if complete.lower() == "yes":
        todo_dictionary[task] = True
    else:
        todo_dictionary[task] = False

    print "Your task is " + task

    newTask = raw_input("Would you like to add another task? ")

    if newTask.lower() == "no":
        break

todo_file = open("todo.txt", "w+")

print "Zakljuceni taski: "
todo_file.write("Zakljuceni taski: \n")

for task in todo_dictionary:
    if todo_dictionary[task]:
        print task
        todo_file.write("- " + task + "\n")

print "Nezakljuceni primeri: "
todo_file.write("Nezakljuceni taski: \n")
for task in todo_dictionary:
    if not todo_dictionary[task]:
        print task
        todo_file.write("- " + task + "\n")

print "END"