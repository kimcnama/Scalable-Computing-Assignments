import pandas as pd
import sys
import argparse

def usage():
    print("Usage: " + sys.argv[0] + " -len1 <Length of wordlist 1>")
    sys.exit(1)

parser = argparse.ArgumentParser(description='Create Wordlist. Max 3 seperate word lists')

parser.add_argument('--len1', type=int,
                    help='Length of wordlist 1')
parser.add_argument('--pos1', metavar='N', type=int,
                    help='Number of letter (positionally) that can be capital or lowercase')


args = parser.parse_args()

if args.len1 == None:
    usage()

dictionary = '/usr/share/dict/american-english'
dictionary2 = '/usr/share/dict/british-english'

with open(dictionary) as a:
    wordlist = a.readlines()

with open(dictionary2) as b:
    british_dict = b.readlines()

wordlist.extend(british_dict)

wordlist = [str(w).lower() for w in wordlist]

wordlist = [w.rstrip() for w in wordlist]

wordlist = list(pd.unique(wordlist))

newlist = []

for w in wordlist:
    if len(w) == 4 and w.isalpha() == True:
        newlist.append(w)

newlist = [w + '\n' for w in newlist]

wordlist = newlist

wordlist2 = [str(w[0]).upper() + w[1:] for w in wordlist]

wordlist.extend(wordlist2)

out_file = '/home/kieran/junk/wordlist1.txt'
out_file2 = '/home/kieran/junk/wordlist2.txt'

with open(out_file, 'w+') as f:
    f.writelines(wordlist)

with open(out_file2, 'w+') as f2:
    f2.writelines(wordlist2)
