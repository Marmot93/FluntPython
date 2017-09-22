from difflib import SequenceMatcher

s = SequenceMatcher(lambda x: x == " ", "private Thread currentThread;", "private volatile Thread currentThread;")
print(round(s.ratio(), 3))