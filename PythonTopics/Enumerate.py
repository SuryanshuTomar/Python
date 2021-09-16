list1 = ["Bhindi", "Aloo", "Choopssticks", "Chowmein"]

for i in list1[::2]:
    print(i)

for index, item in enumerate(list1):
    if index % 2 == 0:
        print(f"Jarvis Please buy these items : {index, item}")
