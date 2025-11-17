import os

files = os.listdir('.')
for f in files:
    if f.endswith('.txt'):
        os.rename(f, f.replace('.txt', '_backup.txt'))
