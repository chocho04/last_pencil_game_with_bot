counter = 0
print("How many pencils would you like to use:")


def evaluate():
    global counter
    counter += 1
    if pencils == 0:
        print("John wins") if counter % 2 == 1 else print("Jack wins")
        exit()
    print('|' * pencils)


while True:
    try:
        pencils = int(input())
        if pencils > 0:
            break
        else:
            print("The number of pencils should be positive")
    except ValueError:
        print("The number of pencils should be numeric")

print("Who will be the first (John, Jack):")

while True:
    name = input()
    if name == "John":
        counter = 1
        break
    elif name == "Jack":
        counter = 0
        break
    else:
        print("Choose between 'John' and 'Jack'")

print('|' * pencils)

while pencils > 0:
    if counter % 2 == 1:
        print("John's turn:")
        hand = input()
    else:
        print("Jack's turn:")

    if counter % 2 == 1:

        while hand not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            hand = input()

        while int(hand) > pencils:
            print("Too many pencils were taken")
            hand = input()
            continue
        else:
            pencils -= int(hand)
            evaluate()
    else:
        if pencils % 4 == 0:
            pencils -= 3
            print("3")
        elif pencils % 4 == 3:
            pencils -= 2
            print("2")
        elif pencils % 4 == 2:
            pencils -= 1
            print("1")
        else:
            pencils -= 1
            print("1")
        evaluate()
