# Jake Billard UHID 1582534

parts = input().split()  # puts input into parts list.
name = parts[0] # name is the 0th index.

while name != '-1':
    try:
        age = int(parts[1]) + 1 # Person's age is the 1st index
    except Exception as ex:
        age = 0

    print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]