import socket
from bettersocket import BetterSocketIO

# Blessed be those who have ascended from built-in socket library to bettersocket.
# I was so fortunate today.  

encoding = 'utf-8'

# TIL how to get rid of them 'b's in the beginning.  They  signify bytes.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('wiki.wcsc.usf.edu', 17648))

bs = BetterSocketIO(s)

# Using BetterSocketIO(s) groups together all subclasses - writing, reading, etc...


# Check if the word is a palindrome, if yes : "Y", in not then "N".
def palindrome_check(word):
    checkem = ""
    # Decode from bytes to string.  Also initiate an empty string for
    # where our reversed word will go.
    
    word = word.decode(encoding)
    word = str(word)
    for char in word:
        checkem = str(char) + checkem
    print(checkem)
    
    # if word is the same backwards and forwards - we gang now.
    
    if str(checkem) == str(word):
        bs.sendframe(str.encode("Y"))
    else:
        bs.sendframe(str.encode("N"))
        
# CTF challenge script that required you to connect to a socket.  Receive a word.
# Evaluate its palindrominity and respond in approval or disappointment.
        
while True:
    word = bs.readframe()
    if word == None:
        continue
    print(word.decode(encoding))
    if word == (str.encode("Send me a 'Y' if the following is a palindrome, 'N' if not. Do it 100 times and you'll get a flag")):
        continue
    else:
        palindrome_check(word)
    
    # Keep checking until that flag spills out.
    # Thanks for reading!!
        
    
