count = [i for i in range(1, 100)]
count = count[::-1]

for num in count:
    if num != 1:
        print("{0} bottles of beer on the wall, {0} bottles of beer.".format(num))
        print("Take one down and pass it around, {0} bottles of beer on the wall!\n".format(num - 1))
    if num == 1:
        print("{0} bottle of beer on the wall, {0} bottle of beer.".format(num))
        print("Take one down and pass it around, no more bottles of beer on the wall!\n")

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall!\n")
