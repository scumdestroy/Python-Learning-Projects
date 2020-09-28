import socket
from bettersocket import BetterSocketIO

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('wiki.wcsc.usf.edu', 39812))

bs = BetterSocketIO(s)

# Bless the creator of BetterSocketIO - top 10 inventions of the human race all-time
# CTF Scripting challenge where you just spit the same word back at this server until
# it squeezes out a flag. This is the way.

while True:
    line = bs.readframe()
    print(line)
    if line == "Echo DUCK or GOOSE. Do it 100 times to get the golden egg.":
        continue
    elif line == b"GOOSE":
        bs.(b"GOOSE")
    elif line == b"DUCK":
        bs.sendframe(b"DUCK")
        
    
