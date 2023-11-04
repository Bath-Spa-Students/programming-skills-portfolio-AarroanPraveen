#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {'string':'string is a collection of words or characters and are immutable',
            'variable':'variable is memory location to store the values',
            'list':'ordered sequence of elements and are mutable',
            'argument':'argument is a way to provide more information to a function',
            'comments':'the lines in the code that are ignored by the interpreter during the execution of the program',
            'float':'Floating point numeric values',
            'boolean':'checks if true or false',
            'integer':"whole number",
            'dictionaries':'an abstract data type that defines an unordered collection of data as a set of key-value pairs',
            'functions': 'a block of code when runs only called'}
for programmingwords,definition in glossary.items():
    print("\n" + programmingwords.title() + ": " + definition)