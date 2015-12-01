

#Open and read 2 file to be compared
fname1 = raw_input("Enter first file name: ")
fname2 = raw_input("Enter second file name: ")

fh1 = open(fname1)
fh2 = open(fname2)

#Split to list
lst1 = []
lst2 = []
for line in fh1:

    ###Extract names from lists (ONLY FOR FB)

    if line.startswith("Close") or line.startswith("FriendFriends") or line.startswith("AcquaintanceFriends") or line.startswith("Add") or line.startswith("Respond"): continue
    if "mutual" in line: continue
    line = line.rstrip()
    lst1 = lst1 + line.splitlines()
    
for line in fh2:

    ###Extract names from lists (ONLY FOR FB)

    if line.startswith("Close") or line.startswith("FriendFriends") or line.startswith("AcquaintanceFriends") or line.startswith("Add") or line.startswith("Respond"): continue
    if "mutual" in line: continue
    line = line.rstrip()
    lst2 = lst2 + line.splitlines()
    

#Compare lenght

diff = len(lst2) - len(lst1)


#Find common items, items that only appear in lst1 and items that only appear in lst2
common = []
exclu1 = []
exclu2 = []


for item in lst1:
    if item in lst2:
        common.append(item)
    else:
        exclu1.append(item)

for item in lst2:
    if item not in lst1:
        exclu2.append(item)



#Print result: 

print "File 2 contain", diff, "more item than file 1 \n"

print "Common items are: \n"
for item in common:
    print item
print "\n"

print "Items exclusively found in file 1: \n"
for item in exclu1:
    print item
print "\n"

print "Items exclusively found in file 2: \n"
for item in exclu2:
    print item
