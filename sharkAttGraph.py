import matplotlib.pyplot as plt
import numpy as np
import csv






def main():
    
    everyAttackList,totalAttacks=ListTotalOccurencesInUS()      #returns every single attack in the US along with the total # of attacks

    stateList=getNumStates()

    occurenceList=TallyOccurence(everyAttackList,stateList)     #should return the dictionary of occurence of attacks in the USA

    # for key,value in occurenceList.items():
    #     print(str(key)+': '  + str(value))          #dict contains all total attacks in each US state

    createPieChart(occurenceList,totalAttacks) #calls the function to create the pie chart




def createUSAFile():
    # plt.plot([1,2,3],[5,7,4])
    # plt.show()

    # correctly outputs USA and location of attack

    with open('attacks.csv','r',encoding="utf8",errors='ignore') as inputFile:
        reader=csv.reader(inputFile)

        with open('attacksUSA','w') as outputFile:
            writer=csv.writer(outputFile)
            for line in reader:
                counntry=line[4]  #stores the name of the country encountered

                if(line[4]=="USA"):
                    writer.writerow([line[4]]+[line[5]])


def getNumStates():
    #Gets the number of states in the USA listed from the csv file

    # stateCount=0
    arrayOfStates=[]

    with open('attacksUSA','r',encoding="utf8",errors='ignore') as inputFile:
        reader=csv.reader(inputFile)
        next(reader)    ##skips the first row of headers in the csv

        for line in reader:
            state=line[1]
            if state in arrayOfStates:  #do nothing
                pass
            else:
                arrayOfStates.append(state)
                # stateCount=stateCount+1  for debugging. 44 total according to data in USA
                
        
       

    return arrayOfStates



def ListTotalOccurencesInUS():

    everyOccurenceList=[]
    totalAttacks=0

    with open('attacksUSA','r',encoding="utf8",errors='ignore') as inputFile:
        reader=csv.reader(inputFile)
        next(reader)    ##skips the first row of headers in the csv

        for line in reader:
            state=line[1]
            everyOccurenceList.append(state);
            totalAttacks=totalAttacks+1
    print("There are a total of "+str(totalAttacks)+" attacks.")



    return everyOccurenceList,totalAttacks

def TallyOccurence(everyOccurenceList,arrayOfStates):

    index=0
    stateCount=0
    tallyStateDict={}

    while index<len(arrayOfStates):
        number=everyOccurenceList.count(arrayOfStates[index]) #gets a count of the occurence of each state in the total USA attakcs
        tallyStateDict[arrayOfStates[index]]=[number]       #adds the new tally to the list -- state : #attacks
        index=index+1

    return tallyStateDict


def createPieChart(attackDictionary,totalAttacks):

    labelArr=[]       #parrallel arrays to represent the dict
    sizeArr=[]

    for key,value in attackDictionary.items():
        labelArr.append(key)
        sizeArr.append(value)     #fills the parallel arrays
    
    # plt.pie(sizes,labels=labels,startangle=90,shadow=True,autopct='%1.1f%%')
    # plt.title("USA Shark Attacks in 2016")
    # plt.show()


    # labels = 'Python', 'C++', 'Ruby', 'Java'
    # sizes = [215, 130, 245, 210]
    # colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    # # explode = (0.1, 0, 0, 0)  # explode 1st slice

    plt.plot(labelArr, sizeArr)
    plt.xticks(labelArr,rotation='vertical')
    plt.show()



if __name__=="__main__":
    main()
    