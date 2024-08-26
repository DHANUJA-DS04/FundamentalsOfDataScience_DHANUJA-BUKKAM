qu1 = []
qu2 = []

def enqueue(list, item):
    list.append(item)


def dequeue(list):
    print(list[1:])


friends = {"pavan":"sannaik", "Anand":"Shounat"}

enqueue(qu1, "Darshan")
enqueue(qu1, "shubham")
enqueue(qu1, "monty")
enqueue(qu1, "Anand")
enqueue(qu1, "arthi")

enqueue(qu2, "perni")
enqueue(qu2, "Shounat")
enqueue(qu2, "varad")

print(f"\nQueue 1: {qu1} Length: {len(qu1)}")
print(f"Queue 2: {qu2} Length: {len(qu2)}\n")


def insert_person(list1, list2):
    x = input("Enter name to join: ")

    found_in_friends = x in friends.values()

    if found_in_friends:
        for key, value in friends.items():
            if value == x:
                if key in list1:
                    list1.insert(list1.index(key)+1, x)
                    print(f"New Queue 1: {list1} Length: {len(list1)}")
                    print(f"New Queue 2: {list2} Length: {len(list2)}\n")
                    return
                elif key in list2:
                    list2.insert(list2.index(key) + 1, x)
                    print(f"New Queue 1: {list1} Length: {len(list1)}")
                    print(f"New Queue 2: {list2} Length: {len(list2)}\n")
                    return
    else:
        if len(list1) <= len(list2):
            enqueue(list1, x)
            print(f"New Queue 1: {list1} Length: {len(list1)}")
            print(f"New Queue 2: {list2} Length: {len(list2)}\n")
        else:
            enqueue(list2, x)
            print(f"New Queue 1: {list1} Length: {len(list1)}")
            print(f"New Queue 2: {list2} Length: {len(list2)}\n")

insert_person(qu1, qu2)