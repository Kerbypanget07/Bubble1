def bubble_sort(names):
    length = len(names)
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(1, length):
            if names[i - 1] > names[i]:
                names[i - 1], names[i] = names[i], names[i - 1]
                is_swapped = True

num = 1
names = ["Adia, Paul", "Maddagan, Jan Kerby","Villanueva, Carmelo","Ling, Ian",
         "Acodili, Lawrence", "Caguioa, Rizalino", "Macatangga, Juan",
         "Echevaria, John Leo", "Catalla, Johann","Pabellano, Nino"]

print("UNSORTED LIST OF AUTHORS:")
for unsorted in names:
    print(str(num) + ".", unsorted)
    num += 1

num = 1
print("\n\n")
bubble_sort(names)
print("SORTED LIST OF AUTHORS:")
for ssorted in names:
    print(str(num) + ".", ssorted)
    num += 1
