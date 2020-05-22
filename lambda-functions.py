# Sorting by lastname

scifi_authors = ["Ray Bradbury", "Robert Heinlein", "Isaak Asimov"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

print(scifi_authors)


authors=['M. Aleksandrov','Mike Zoich', 'Alex Xander', 'Jack Black']
authors_initials=[]


for author in authors:
	first_name = author.split(' ')[0]
	last_name = author.split(' ')[1]
	authors_initials.append(last_name + ' ' + list(first_name)[0]+'.')

for name in authors_initials:
    print(name)
