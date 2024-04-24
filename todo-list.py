import os
import json
import shutil

st_path = os.path.expanduser("~/.tr2nk/todo.json")
st_dir = os.path.expanduser("~/.tr2nk/")

if os.path.exists(st_dir) and not os.path.isdir(st_dir):
    os.remove(st_dir)
if not os.path.exists(st_dir):
    os.mkdir(st_dir)

if os.path.isdir(st_path):
    shutil.rmtree(st_path)
if not os.path.exists(st_path):
    open(st_path, "w").write("[]")

store = json.loads(open(st_path, "r").read())

def get_num_input(input_text: str=">>> ") -> int:
    num = ""
    valid = False

    while not valid:
        num = input(input_text)
        print(num)
        valid = True

        if num == "c":
            continue

        for i in num:
            if valid and i not in "0123456789":
                valid = False

        if valid and len(num) == 0:
            valid = False

        if valid and int(num) > len(store) or int(num) < 0:
            valid = False

        if not valid:
            print("Invalid number!")

    return False if num == "c" else int(num) - 1

def save_list():
    f = open(st_path, "w")
    f.write(json.dumps(store))
    f.close()

x = ""
print_list = lambda: print("\n".join([f"{i + 1}. {store[i]}" for i in range(len(store))]) if len(store) else "You have nothing on your todo list!")

while x != "5":
    os.system('cls' if os.name == 'nt' else 'clear')
    print_list()
    x = input("\nWhat action do you want to do?\n1. Check item off of list\n2. Add item to list\n3. Swap two items\n4. Sort list alphabetically\n5. Close program\n>>> ")

    if x == "1":
        x = get_num_input("Which item do you want to remove? ('c' to cancel)\n>>> ")
        if x is False:
            continue

        store.pop(x)

    elif x == "2":
        store.append(input("What do you want to add to your list?\n>>> "))

    elif x == "3":
        num1 = get_num_input("What is the first item you want to swap? ('c' to cancel)\n>>> ")
        if num1 is False:
            continue

        num2 = get_num_input("What is the second item you want to swap? ('c' to cancel)\n>>> ")
        if num2 is False:
            continue

        store[num1], store[num2] = store[num2], store[num1]

    elif x == "4":
        store = sorted(store, key=lambda x: x.lower())

    elif x == "5":
        continue

    else:
        print("Invalid action!")

    save_list()

print("Bye bye!")
