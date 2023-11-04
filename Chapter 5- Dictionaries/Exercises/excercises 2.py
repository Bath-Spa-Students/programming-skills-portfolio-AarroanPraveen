#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output


glossary = {'string':'string is a collection of words or characters and are immutable',
            'variable':'variable is memory location to store the values',
            'list':'ordered sequence of elements and are mutable',
            'argument':'argument is a way to provide more information to a function',
            'comments':'the lines in the code that are ignored by the interpreter during the execution of the program'}
programmingwords = 'string'
print("\n" + programmingwords.title() + ": " + glossary[programmingwords])

programmingwords = 'variable'
print("\n" + programmingwords.title() + ": " + glossary[programmingwords])

programmingwords = 'list'
print("\n" + programmingwords.title() + ": " + glossary[programmingwords])

programmingwords = 'argument'
print("\n" + programmingwords.title() + ": " + glossary[programmingwords])

programmingwords = 'comments'
print("\n" + programmingwords.title() + ": " + glossary[programmingwords])