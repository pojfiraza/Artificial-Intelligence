from Tkinter import *
import os
import random


attrStore = []
consStore = []
prefStore = []
objCreate = []
optiStore = []

class Attribute:
    def __init__(self,newname,newpos,newneg):
        self.name = newname
        self.pos  = newpos
        self.neg  = newneg
    def getName(self):
        return self.name
    def getPos(self):
        return self.pos
    def getNeg(self):
        return self.neg

def retrieve_input():
    main()

def clicked(num):
    Input = textBox.get(1.0,END)
    os.remove("tempo.txt")
    fd = os.open( "tempo.txt", os.O_WRONLY|os.O_CREAT )
    os.write(fd, Input)
    if num == 1: readAtr(attrStore,"tempo.txt")
    elif num == 2:readCon(consStore,attrStore,"tempo.txt")
    elif num == 3:readPrf(prefStore,attrStore,"tempo.txt")
    
    os.close(fd)


def readAtr(attrStore,value):
    count = 0
    attrStore[:] = []
    try:
        filename = str(value)
        with open(filename) as fn:
            for line in fn:
                line = line.rstrip("\n")
                temp = line.translate(None,':,')
                temp2 = temp.split()
                attrStore.insert(count,Attribute(temp2[0],temp2[1],temp2[2]))
                count+=1
        print "Attribute File Accepted."
        return
    except IOError: print("File Not Found")

def readCon(consStore,attrStore,value):
    tempo = []
    count = 0
    check = False
    consStore[:] = []
    try:
        filename = value
        with open(filename) as fn:
            for line in fn:
                temp = line.split()
                for x in range(len(temp)):
                    if (temp[x] == "NOT"):
                        tempo.append("-")
                        continue
                    elif(temp[x] == "AND"):
                        tempo.append("0\n") 
                        check = True
                        continue
                    elif(temp[x] == "OR"):
                        check = True
                        continue
                    else:
                        for y in range(len(attrStore)):
                            if(temp[x] == Attribute.getPos(attrStore[y])):
                                tempo.append(str(y+1)+ " ")
                                break
                            elif(temp[x] == Attribute.getNeg(attrStore[y])):
                                if(len(tempo) != 0 and tempo[len(tempo)-1] == "-" ):
                                    tempo.pop()
                                    tempo.append(str(y+1)+ " ")
                                    break
                                tempo.append("-" + str(y+1) +" " )
                    if (check == True):
                        tempo.append("0\n")
                        check = False
                consStore.append(''.join(tempo))
                tempo[:] = []
                count+=1
        print "Constraint File Accepted."
        return
    except IOError: print("File not Found.")

def readPrf(prefStore,attrStore,value):
    tempo = []
    count = 0
    check = False
    prefStore[:] = []
    try:
        filename = value

        with open(filename) as fn:
            for line in fn:
                temp2 = line.split(",")
                temp = temp2[0].split()
                for x in range(len(temp)):
                    if (temp[x] == "NOT"):
                        tempo.append("-")
                        continue
                    elif(temp[x] == "AND"):
                        tempo.append("0\n") 
                        check = True
                        continue
                    elif(temp[x] == "OR"):
                        check = True
                        continue
                    else:
                        for y in range(len(attrStore)):
                            if(temp[x] == Attribute.getPos(attrStore[y])):
                                tempo.append(str(y+1)+ " ")
                            elif(temp[x] == Attribute.getNeg(attrStore[y])):
                                if(len(tempo) != 0 and tempo[len(tempo)-1] == "-" ):
                                    tempo.pop()
                                    tempo.append(str(y+1)+ " ")
                                    break
                                tempo.append("-" + str(y+1) +" " )
                    if (check == True):
                        tempo.append("0\n")
                        check = False
                prefStore.append(''.join(tempo))
                prefStore.append(temp2[1])
                tempo[:] = []
                count+=1
        print "Preference File Accepted."
        return
    except IOError: print("File not Found")

def main():
    createObj(attrStore,objCreate)
    
    
    while True:
        answer = raw_input(
            "\nChoose an option: \n" + 
            "[1]Constraint Table \n" +
            "[2]Compare 2 Objects \n" +
            "[3]Find an Optimal Object \n" +
            "[4]Find all Optimal Objects \n" +
            "[5]Exit\n"
        )
        if(answer == '1'): printFea(attrStore,consStore,objCreate)
        elif(answer == '2'):randCom(objCreate,prefStore,attrStore)
        elif(answer == '3'):findOpt(objCreate,prefStore,attrStore,1)
        elif(answer == '4'):findOpt(objCreate,prefStore,attrStore,len(objCreate))
        elif(answer == '5'):
            master.destroy()
            exit()
        else: print("\nInvalid Input.Try Again")
        
    
        
def findOpt(objCreate,prefStore,attrStore,num):
    tempo = []
    print (" Models List:" )
    for x in range(len(objCreate)):
        ext = 99999
        total = 0
        print str(bin(x)[2:].zfill(4))+ " = ",
        for y in range(len(prefStore)/2):
            f = open('tmp.txt','w')
            f.write("p cnf " + str(len(attrStore)) + " 22\n")
            f.write(str(prefStore[(y*2)]))
            f.write(str(objCreate[x]))
            f.close()
            os.system( "clasp "+ "tmp.txt" + " > tmp")
            line  = (open('tmp', 'r').read()).split()
            for z in range(len(line)):
                if line[z] == "SATISFIABLE":
                    if (float(prefStore[(y*2)+1])<1):
                        if(ext>(1-float(prefStore[(y*2)+1]))):
                            total = 1-float(prefStore[(y*2)+1])
                            ext = 1-float(prefStore[(y*2)+1])
                    else:total += float(prefStore[(y*2)+1])
                    break
        tempo.append(total)
        print total
    Min = min(tempo)
    print ("Models that fit")
    for y in range(len(objCreate)):
        if(tempo[y] == Min):
            if(num == 0): break
            print str(bin(y)[2:].zfill(4))
            num-=1

def randCom(objCreate,prefStore,attrStore):
    tempo = []
    print (" Models That Fit:" )
    for x in range(2):
        ext = 99999
        total = 0
        val = random.randint(0,len(objCreate)-1)
        print str(bin(val)[2:].zfill(4))+ " = ",
        for y in range(len(prefStore)/2):
            f = open('tmp.txt','w')
            f.write("p cnf " + str(len(attrStore)) + " 22\n")
            f.write(str(prefStore[(y*2)]))
            f.write(str(objCreate[val]))
            f.close()
            os.system( "clasp "+ "tmp.txt" + " > tmp")
            line  = (open('tmp', 'r').read()).split()
            for z in range(len(line)):
                if line[z] == "SATISFIABLE":
                    if (float(prefStore[(y*2)+1])<1):
                        if(ext>(1-float(prefStore[(y*2)+1]))):
                            ext = 1-float(prefStore[(y*2)+1])
                            total = 1-float(prefStore[(y*2)+1])
                    else: total += float(prefStore[(y*2)+1])
                    break
        tempo.append(total)
        print total
    if(tempo[0]== tempo[1]): print " Equivalence "
    else: print " Strict Preference "
        
    
def printFea(attrStore,consStore,objCreate):
    print "\nConstraint Table: 0 = Negative 1 = Positive O = SAT X = UNSAT"
    print "______" * (len(consStore)+1)
    for y in range(len(objCreate)):
        print " "+str(bin(y)[2:].zfill(4)) + " |",
        for x in range(len(consStore)):
            f = open('tmp.txt','w')
            f.write("p cnf " + str(len(attrStore)) + " 22\n")
            f.write(str(consStore[x]))
            f.write(str(objCreate[y]))
            f.close()
            os.system( "clasp "+ "tmp.txt" + " > tmp")
            line  = (open('tmp', 'r').read()).split()
            for z in range(len(line)):
                if line[z] == "UNSATISFIABLE":
                    print " X  |",
                    break
                elif line[z] == "SATISFIABLE":
                    print " O  |",
                    break
        print
    print "------" * (len(consStore)+1)    
        
def createObj(attrStore,objCreate):
    tempo2 = []
    for x in range(pow(2,len(attrStore))):
       tempo = list(bin(x)[2:].zfill(4))
       for y in range(len(tempo)):
           if(tempo[y] == '0'): tempo2.append("-"+str(y+1) + " 0\n")
           else: tempo2.append(str(y+1) + " 0\n")
       objCreate.append(''.join(tempo2))
       tempo2[:] = []

master = Tk()

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

textBox=Text(master, height=20, width=60)
Button(master,text="Load", command = lambda:clicked(1)).grid(row = 1, column = 0)
Button(master,text="Load", command = lambda:clicked(2)).grid(row = 1, column = 1)
Button(master,text="Load", command = lambda:clicked(3)).grid(row = 1, column = 2)
textBox.grid(row = 0 , columnspan = 3)
buttonCommit=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input()).grid(row = 4, columnspan =3)
Button(master, text='Save', command=lambda:readAtr(attrStore,str(e1.get()))).grid(row=3, column=0)
Button(master, text='Save', command=lambda:readCon(consStore,attrStore,str(e2.get()))).grid(row=3, column=1)
Button(master, text='Save', command=lambda:readPrf(prefStore,attrStore,str(e3.get()))).grid(row=3, column=2)



e1.grid(row=2, column=0)
e2.grid(row=2, column=1)
e3.grid(row=2, column=2)

master.mainloop()
if __name__ == "__main__": main()

