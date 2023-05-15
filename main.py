guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, "r")
    while True:
        line_data = text_file.readline().strip().split(",")
        yield line_data
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age


my_obj = read_guestlist("guest_list.txt")
# for i in range(1, 50):
#     if i == " ":
#         raise StopIteration
#     print(next(my_obj))

# my_obj.send("Jane, 35")

exp = (key for key, value in guests.values() if value >= 21)


def table1():
    table_num = 1
    for i in range(1, 6):
        yield ("Chicken", f"Table {table_num}", f"Seat {i}")


def table2():
    table_num = 2
    for i in range(1, 6):
        yield ("Beef", f"Table {table_num}", f"Seat {i}")


def table3():
    table_num = 3
    for i in range(1, 6):
        yield ("Fish", f"Table {table_num}", f"Seat {i}")


all_tables = [table1(), table2(), table3()]
all_meals = []

for table in all_tables:
    for meal in table:
        all_meals.append(meal)

print(all_meals)


def assign_seating(guests, tables):
    for name, age in guests.items():
        meal = next(tables)
        yield (name, meal)


seating = assign_seating(guests, all_tables)

for guest, meal in seating:
    print(f"{guest} has been assigned {meal[0]} at {meal[1]}, {meal[2]}")
