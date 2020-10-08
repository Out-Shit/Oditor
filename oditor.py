import random , os
import fileinput
import re
S10 = '\033[91m'#yellow
S11 = '\033[94m'#clearblue
S12 = '\033[93m'#pink
def draw():
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"""+S11)
def clear(numlines=100):
  print(S10)
  if os.name == "posix":
    print('\n' * numlines)
    os.system('clear')
    draw()
  elif os.name in ("nt", "dos", "ce"):
    print('\n' * numlines)
    os.system('CLS')
    draw()
  else:
    print('\n' * numlines)
    draw()
clear()
def randooo():
    clear()
    inpu = input('From:\n\nODITOR~>>>')
    input('To ranline.txt')
    f = open('ranline.txt', 'w')
    lines = open(inpu).readlines()
    random.shuffle(lines)
    f.writelines(lines)
    print('done!!!')
    exit()
def Editor():
    clear()
    inpuut6=input('File to change:\n\nODITOR~>>>')
    inpuuut6='edited.txt'
    clear()
    print(S12+'From: '+inpuut6+'\nTo: edited.txt'+S11)
    Chang=input('\nWorld to Change:\n\nODITOR~>>>')
    clear()
    print(S12+'From: '+inpuut6+'\nTo: edited.txt\nChange: '+Chang+S11)
    Repla=input('\nReplace per:\n\nODITOR~>>>')
    clear()
    print(S12+'From: '+inpuut6+'\nTo: edited.txt\nReplace: '+Chang+'\nFor: '+Repla+S11)
    Repla=input('\nOk?\n\nODITOR~>>>')
    pri=open(inpuut6, 'r')
    pru=open(inpuuut6, 'w')
    stu=pri.read()
    Gada=str(stu).replace(Chang,Repla)
    pru.write(Gada)
    pru.close()
    clear()
    print('done!!!')
    exit()
def NumberFinder():
    clear()
    F1L3 = '.plugin'
    F1L33 = 'data.txt'
    inpuut = input('From:\n\nODITOR~>>>')
    input('To data.txt')
    pri = open(inpuut, 'r')
    stu= pri.read()
    finaalA = str(stu).replace(")",'')
    finaalB = str(finaalA).replace("(",'')
    finaalC = str(finaalB).replace("-",'')
    finaalD = str(finaalC).replace(" ",'')
    clear()
    va = input('Choose an option:\n#1- +1(514) 444 6666 (12 letters)\n#2- (514)444-6666 (10 letters)\n\nODITOR~>>>')
    if va == '2':
        accro='\d{10}'
        Nor='+1'
        N=10
    else:
        accro='[+]\d{11}'
        Nor=''
        N=12
    def filterNumber(n):
    	if(len(n)==N):
    		return True
    	else:
    		return False
    x=re.findall(accro, finaalD)
    finalx=list(filter(filterNumber, x))
    finaallA=str(finalx).replace("]",'')
    finaallB=str(finaallA).replace("[",'')
    finaallC=str(finaallB).replace(" ",'\n'+Nor)
    finaallD=str(finaallC).replace("'",'')
    finaallE=str(finaallD).replace(",",'')
    pru = open(F1L3, 'a')
    pru.write('\n'+Nor+finaallE)
    pru.close()
    clear()
    print('Done!')
    os.system('sort -u '+F1L3+' > '+F1L33)
    os.system('rm .plugin')
    exit()
def Main():
    clear()
    print('Welcome to Oditor.  Made by Out-Shit\n')
    print('Choose whats you wanna do:')
    print('1-Search Number in a file')
    print('2-Randomize Lines in a list')
    print('3-Search and Change worlds in a file')
    print('\n')
    try:
        v = input('ODITOR~>>>')
    except:
        input(v+' is not an anwser!')
        Main()
    if v == '1':
        print('Number Finder')
        NumberFinder()
    if v == '2':
        print('Randomizer')
        randooo()
    if v == '3':
        print('Editor')
        Editor()
    else:
        input(v+' is not an anwser!')
        Main()

Main()
