'''
This is my attempt on Diceware™ method for generating password.
You can find more about algorithm at http://world.std.com/~reinhold/diceware.html
You will be also able to download dictionary for your language from there.
Language for czech language, made by Vladimír Sedmík is uncluded in this package.
This dictionary is under GNU General Public Licence.
This code is under GNU Genereal Public License too.
Enjoy
'''

import sys, getopt, random

def getRandomWord():
    str = ''
    val = -1
    for num in range(0, 5):
        val = random.randint(1, 6)
        str += val.__str__()
    return str

def main(argv):
    dicfile = ''        # name of dictionary file - cli arg -d
    passlen = 3         # number of words to be generated - cli arg -l
    words = dict()      # internal dictionary loaded from the file
    wordlist = ''       # list of words generated with diceware algorithm


# Try read command line arguments and parse them looking fo r-d, -l -h
    try:
        opts, args = getopt.getopt(argv, "hd:l:")
    except getopt.GetoptError:
        print('diceware.py -d <dictfile> -l <passwordlenght>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('diceware.py -d <dictfile> -l <passwordlenght>')
            sys.exit()
        elif opt in ("-d"):
            dicfile = arg
        elif opt in ("-l"):
            passlen = arg

    if dicfile == '':
        print('Now dictionary included, exiting!!!')
        sys.exit()

# Ok, we succesfully parsed cli, print it out
    print('[1] Using dictionary file: ', dicfile)
    print('[2] Supposed password lenght is: ', passlen)

    try:
        fhand = open(dicfile, encoding = 'utf-8-sig') # remove BOM if present
    except:
        print("Cant'open dictionary file (", fname, ")")
        sys.exit()

    print("[3] Opening dictionary ...\n")

    for line in fhand:
        pair = line.split()
        words[pair[0]] = pair[1]

    for index in range(0, int(passlen)):
        oneword = words[getRandomWord()]
        wordlist += oneword
        if index < int(passlen)-1:
            wordlist += ' '

    print('[4] Your Diceware™ method generated password is:')
    print("...", wordlist, '...')

if __name__ == "__main__":
   main(sys.argv[1:])


