''' Loop test to examine whether the iterator in a loop
    ('x' in 'for x in list:') is a pointer to the list element
    or a copy of the element value in a separate variable'''

mylist = [20, 18, 16]
for nr in mylist:
    if (nr == 18):
        nr = 300
if (mylist[1] == 300):
    print('iterator is a POINTER!')
elif (mylist[1] == 18):
    print('iterator is a COPY!')
else:
    print('ALARM! UNKNOWN ERROR!!')


# Now, make sure the list can be edited using an index iterator in a loop:
mylist = [20, 18, 16]
for i in range(0, len(mylist)):
    if (mylist[i] == 18):
        mylist[i] = 300
if (mylist[1] == 300):
    print('BUT index iterator WORKS!')
elif (mylist[1] == 18):
    print('AND index iterator is BROKEN!')
else:
    print('ALARM! UNKNOWN ERROR!!')
