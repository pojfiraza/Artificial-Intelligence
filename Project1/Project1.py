"""
CAP4640/5605
Project 1 - Python Basics 
Author: Paul Firaza
Version: 1/15/2018
Email: n01388082@ospreys.unf.edu
"""

import csv

class State:
    """
    State class contains:
    - __init__ creates a State object with 6 different datas( State Name, City,Abrv,Population,Region and House Seats )
    - setters and getters for each individual data
    - __gt__ that compares 2 State Object's Name Alphabetically
    -__str__ pertains different variations of prints which are( 1.)Print Title Format 2.)Print State Format 3.) Searched State Format )
    """
    def __init__ (self,newname,newcity,newabrv,newpopu,newregion,newseat):
        """
        __init__ Function:
        - Creates a State Object.
        Param:
        - Self(calls itself) - newname(define State's name) - newcity(define State's City) -newabrv(define State Abrv) -newpopu(Define Population) -newregion(Define House Seat No.)
        """
        self.name = newname
        self.city = newcity
        self.abrv = newabrv
        self.popu = newpopu
        self.region = newregion
        self.seat = newseat
    def getName(self):
        """
        getName Function:
        - Gets the State object's State Name.
        Param:
        - Self(calls itself)
        """
        return self.name
    def getCity(self):
        """
        getCity Function:
        - Gets the State object's State City.
        Param:
        - Self(calls itself)
        """
        return self.city
    def getAbrv(self):
        """
        getAbrv Function:
        - Gets the State object's State Abrreviation.
        Param:
        - Self(calls itself)
        """
        return self.abrv
    def getPopu(self):
        """
        getPopu Function:
        - Gets the State object's Population.
        Param:
        - Self(calls itself)
        """
        return self.popu
    def getRegion(self):
        """
        getRegion Function:
        - Gets the State object's State Region.
        Param:
        - Self(calls itself)
        """
        return self.region
    def getSeat(self):
        """
        getSeat Function:
        - Gets the State object's State House Seat No.
        Param:
        - Self(calls itself)
        """
        return self.seat
    def setName(self,newname):
        """
        setName Function:
        - Replace the State object's State Name.
        Param:
        - Self(calls itself) - newname(replacement for current name)
        """
        self.name = newname
    def setCity(self,newcity):
        """        
        setCity Function:
        - Replace the State object's State City.
        Param:
        - Self(calls itself) - newcity(replacement for current city)
        """
        self.city = newcity
    def setAbrv(self,newabrv):
        """
        setAbrv Function:
        - Replace the State object's State Abbreviation.
        Param:
        - Self(calls itself) - newcity(replacement for current abbreviation)
        """
        self.abrv = newabrv
    def setPopu(self,newpopu):
        """
        setPopu Function:
        - Replace the State object's State Population.
        Param:
        - Self(calls itself) - newcity(replacement for current population)
        """
        self.popu = newpopu
    def setRegion(self,newregion):
        """
        setRegion Function:
        - Replace the State object's State Region.
        Param:
        - Self(calls itself) - newcity(replacement for current region)
        """
        self.region = newregion
    def setSeat(self,newseat):
        """
        setSeat Function:
        - Replace the State object's State House Seat Numbers.
        Param:
        - Self(calls itself) - newcity(replacement for current numbers)
        """
        self.seat = newseat

    def comma(self):
        string = "{:,}".format(int(self.popu))
        return string
    
    def __gt__(self,operator,self2):
        """
        __gt__ Function:
        - Compare 2 State objects by their State Names
        Param:
        - Self(calls itself/1st StateObject) - operator(operator used to compare) - self2(2nd StateObject)
        """
        if(operator == '>'):
            return self.getName()>self2.getName()
        elif(operator == '<'):
            return self.getName()<self2.getName()
        elif(operator == '='):
            return self.getName() == self2.getName()
    def __str__(self,option):
        """
        __str__ Function:
        - Prints the State objects with various modes based on option which are( 1.)Print Title Format 2.)Print State Format 3.) Searched State Format )
        Param:
        - Self(calls itself/1st StateObject) - option(defines the print style it chooses)
        """
        if(option == 1):
            print(self.name + ((16-len(self.getName()))*" ")+ self.city + ((14 -len(self.getCity()))*" ") + self.abrv +"  " + str(self.popu) + ((16 -len(self.getPopu()))*" ") + self.region + ((16-len(self.getRegion()))*" ") + self.seat)            
        elif(option == 2):
            print(self.name + ((16-len(self.getName()))*" ")+ self.city + ((14 -len(self.getCity()))*" ") + (5*" ") + self.abrv + (7 *" ") + self.comma() + ((16 - (len(self.getPopu()) + (len(self.getPopu())-1)/3))*" ") + self.region + ((16-len(self.getRegion()))*" ") +(6*" " ) + self.seat)
        elif(option == 3):
            print("State Name: " +(7*" ") + self.getName())
            print("Capital City: "+(5*" ") + self.getCity())
            print("State Abrv: "+ (7*" ") +self.getAbrv())
            print("State Population:  " + self.comma())
            print("Region: "+(11*" ") + self.getRegion())
            print("US House Seats: " +(3*" ") +self.getSeat())

def main():
    """
    Main Function:
    - Reads a File specified by user input.
    - Shows the Menu Choices by which they are activated here.
    Exceptions: IOError - will return "File not Found"
    """
    while True:
        try:
            filename = raw_input("Insert File Name: ")
            f = open(filename)
            csv_f = csv.reader(f)
            break
        except IOError:
            print("File not Found.")
    x = 1
    count = 0
    lexi = False

    
    title = []   
    pjList = [] 
    for row in csv_f:
        temp = State(row[0],row[1],row[2],row[3],row[4],row[5])
        if(count == 0):
            title.insert(count,temp)
        else:
            pjList.insert(count-1,temp)
        count+=1

    while(x != '5'):

        print("\n1.State Report")
        print("2.Sort Alphabetically")
        print("3.Sort by Population")
        print("4.Find State")
        print("5.Quit \n")


        while(count > -1):
            x = raw_input("Choose an Option: ")
            if x == '1':
                State.__str__(title[0],1)
                option1(pjList)
            elif x == '2':
                option2(pjList,0,(len(pjList)-1))
                print("\nList ordered by Name.")
                lexi = True
            elif x == '3':
                option3(pjList)
                print("\nList ordered by Population.")
                lexi = False
            elif x == '4':
                option4(pjList,lexi)
            elif x == '5':
                break
            else:
                print("Invalid Key")
                continue
            break
            
    print("Goodbye.Have a NICE DAY!!")

def option1(pjList):
    """
    Option 1 Function:
    - It loops a given list based on its length using the __str__ function in the State Class
    Param:
    - pjList: A State object List which contains data from the given file
    """
    print(94 *"-")
    for row in range(len(pjList)):
        State.__str__(pjList[row],2)
def option2(pjList, low, high):
    """
    Option 2 Function:
    - A QuickSort variant that organizes the list into alphabetical order
    Param:
    - pjList: A State object List which contains data from the given file
    Return?:
    - returns an organized list by State Name
    """
    if(low < high):
        pi = partition(pjList,low,high)

        option2(pjList,low,pi - 1)
        option2(pjList,pi+1,high)

def option3(pjList):
    """
    Option 3 Function:
    - A Radix variant that organizes the list into numerical order
    Param:
    DLLs pjList: A State object List which contains data from the given file
    Return?:
    - returns an organized list by population
    """
    repeat = 0
    for w in range(1,len(pjList)):
        if repeat < int(State.getPopu(pjList[w])):
            repeat = int(State.getPopu(pjList[w]))
    pos = 1
    while (repeat/pos )> 0:
        CSort(pjList,pos)
        pos *= 10     
def option4(pjList,lexi):
    """
    Option 4 Function:
    - Searches States Name in the list and Finds the match. Exact Match Only(Prefixes incompatible)
    - Uses Binary/Sequential Sort based on the lexi Boolean
    Param:
    - pjList: A State object List which contains data from the given file
    - lexi: boolean that returns true when option 2 is used last
    Return?:
    - returns a match ( if not found: Prints error and ends option 4)
    """  
    choice = raw_input("\nInsert State Name:")
    count= 0
    print("")
    if(lexi == False):
    
        print("Sequential Search:\n")
        while(count<len(pjList)):
            if(State.getName(pjList[count]) == choice):
                State.__str__(pjList[count],3)
                break
            count+=1
            if(count == len(pjList)):
                print("Error: " + choice + " is not found." )
    else:
    
        print("Binary Search:\n")
        n = len(pjList)-1
        l = 0
        stop = 0
        while(stop != 5):
            loop = l+(n-l)/2
            if(loop == 49):
                stop +=1
                if(stop == 5):
                    print("Error: " + choice + " is not found.")
            if(State.getName(pjList[loop]) == choice):
                State.__str__(pjList[loop],3)
                break
            elif(State.getName(pjList[loop]) > choice):
                n = loop-1
            else:
                l = loop+1

def partition(pjList,low,high):
    """
    Partition Function:
    - An extention for option 2 quicksort algorithm that organize data based upon the pivot point
    Param:
    - pjList: A State object List which contains data from the given file
    - low : start of the list
    - high : end of the list
    Return?:
    - returns a partition sorted list,which will eventually be repartitioned by option2 function
    """
    count = (low -1)
    pivot =  pjList[high]

    for x in range(low,high):
        if (State.__gt__(pjList[x],'<',pivot) == True | State.__gt__(pjList[x],'=',pivot) == True):
            count += 1
            pjList[count],pjList[x] = pjList[x],pjList[count]

    pjList[count + 1],pjList[high] = pjList[high],pjList[count + 1]
    return(count + 1)    

def CSort(pjList,pos):
    """
    CSort Function:
    - An extention for option 3 radix algorithm that organize data based upon the counting sort algorithm
    Param:
    - pjList: A State object List which contains data from the given file
    - pos : an int used to divide the population variable in order to get a specific digit's modulus 10 ( Ex: 1234/pos(10) = 123 -> 123%10 = 3 )
    Return?:
    - returns a counting sorted list,which will eventually be repeated in increasing pos in order to complete option 3's radix sort.
    """
    pjList2 = [0] * (len(pjList))
    temp  = [0] * 10
    
    for x in range(len(pjList)):
        index = (int(State.getPopu(pjList[x]))/pos)
        temp[ (index)%10 ] += 1
    for y in range(1,10):
        temp[y] += temp[y-1]

    i = len(pjList) -1
    while i >= 0:
        index =(int(State.getPopu(pjList[i]))/pos)
        pjList2[ temp[(index) %10] - 1 ]=  State.getPopu(pjList[i])
        temp[index % 10] -= 1
        i -= 1

    for g in range(len(pjList)):
        tempo = pjList[g]
        for h in range(len(pjList)):
            if  int(pjList2[g]) == int(State.getPopu(pjList[h])) :
                pjList[g] = pjList[h]
                pjList[h] = tempo
                break
                       
    for z in range(len(pjList)):
        State.setPopu(pjList[z],pjList2[z])
        

if __name__ == "__main__": main()

