print("Bubblesort, sorting algorithm to sort numbers in a list from small to large")

try: 
    sorlist = []

    while True:
        sorlist.append(int(input("Add a number to the list, type x to finish your list: ")))

except:
    print(sorlist)

n = len(sorlist)
swapa = 0
swapb = 0
sortfin = False

while not sortfin :
    sortfin = True
    for i in range (n-1):
        if sorlist[i] > sorlist[i+1]:
            swapa = sorlist[i]
            swapb = sorlist[i+1]
            sorlist[i] = swapb
            sorlist[i+1] = swapa
            sortfin = False

print(sorlist)