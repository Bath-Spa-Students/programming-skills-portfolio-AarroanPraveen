#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner. •Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner. •Print a message to each of the two people still on your list, letting them know they’re still invited.

guests = ['ALEN JOBY', 'ANIRUDH', 'FAHEEM']

name = guests[0].title()
print(name + ", I WOULD LIKE TO INVITE YOU FOR MY DINNER.")

name = guests[1].title()
print(name + ", I WOULD LIKE TO INVITE YOU FOR MY DINNER.")

name = guests[2].title()
print(name + ", I WOULD LIKE TO INVITE YOU FOR MY DINNER.")

name = guests[2].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[2])
guests.insert(1,'REZIN')

name = guests[0].title()
print("\n" + name + ", I WOULD LIKE TO INVITE YOU FOR MY DINNER.")

name = guests[1].title()
print(name + ", I WOULD LIKE TO INVITE YOU FOR MY DINNER.")

name = guests[2].title()
print(name + ", I WOULD LIKE TO INVITE YOU FOR MY DINNER.")

print("\nSorry, I can only invite two people to dinner.")

name = guests.pop(0)
print("Sorry, " + name.title() + " there is no space for the dinner.")


