# sets
fruits = {'orange', 'apple', 'banana'}  # indexlenemez liste:çıktısını alırken karma sırada veriyor
print(fruits)
for x in fruits:
    print(x)

fruits.add('cherry')
print(fruits)

fruits.update(['mango', 'grape', 'cherry'])
print(fruits)  # set list olduğu için

fruits.add('cherry')
print(fruits)  # set list olduğu için

myList = ['orange', 'apple', 'banana']
print("old ", myList)

myList.append('cherry')
myList.insert(0, 'cherry')  # neden çıktı olarak listenin son hali yerine NONE veriyor bu 3 satır
#action ayrı,obje ayrıdır
# methodun yazılıp en sondaki return ; edilen değerin error olmaması için none olduğunu düşünebilirsin

print("new ", myList)
print(set(myList))

# discard:elementin listede olup olmadığından emin değilken listeden kaldırır
# remove:elementin listede olduğuna eminken listeden kaldırır eğer listede değilse error verecektir
