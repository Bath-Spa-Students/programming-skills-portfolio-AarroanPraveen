#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
#each pet
pets=[]
pet ={'animal type':'Dog',
      'owners name':'Anirudh'}
pets.append(pet)

pet = {'animal type':'Cat',
       'owners name':'Zarakkhan'}
pets.append(pet)

pet = {'animal type':'chicken',
       'owners name':'Rezin'}
pets.append(pet)
for pet in pets:
    print(f"\nHere's what I know about {pet['owners name'].title()}:")
    for key, value in pet.items():
     print(f"\t{key}: {value}")


