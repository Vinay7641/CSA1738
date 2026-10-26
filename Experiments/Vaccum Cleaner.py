rooms = {"A": 1, "B": 1}
position = "A"
while 0 in rooms.values():
    print("Position:", position, "Rooms:", rooms)
    if rooms[position] == 1:
        rooms[position] = 0
        print("Cleaned", position)
    else:
        position = "B" if position == "A" else "A"
print("All rooms are clean")
