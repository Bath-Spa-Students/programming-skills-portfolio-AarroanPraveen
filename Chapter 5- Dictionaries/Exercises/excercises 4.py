#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

majorrivers = {'nile': 'egypt','indus': 'India','congo river': 'Democratic Republic of Congo', }

for river, country in majorrivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

