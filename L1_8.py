import math
from functools import reduce 

#inputList = input("Please enter a comma separated list of numbers to calculate mean, standard deviation, median, n-quartil and n-percentil\n")

def sanitizeInput(inputArray):
    if(not isinstance(inputArray, list)):
        raise TypeError("Input should be a list")
    for x in inputArray:
        try:
            n=float(x)
        except ValueError:
            raise ValueError("There is an invalid value ('"+str(x)+"') somewhere in the input, please make sure all input values are numbers ")

    inputArray.sort()

#print (numberArray)

def calcMean(numberList):
    sanitizeInput(numberList)
    sum = reduce(lambda a,b:float(a)+float(b), numberList)
    return sum/len(numberList)

def calcStdDev(numberList):
    sanitizeInput(numberList)
    mean = calcMean(numberList)
    sigma = 0
    for num in numberList:
        diffSqr = (float(num) - mean)**2
        sigma += diffSqr
    div = sigma / len(numberList)
    return math.sqrt(div)

def calcMedian(numberList):
    sanitizeInput(numberList)
    if (len(numberList)%2==0):
        return (numberList[int((len(numberList)-1)/2)] + numberList[int((len(numberList)-1)/2)+1]) /2 
    else:
        return numberList[int((len(numberList)-1)/2)]

#Function than calculates the quartile
def calcQuartile(numberList, q):
    sanitizeInput(numberList)
    if (int(q) != 1 and int(q)!=3):
        raise ValueError("Not a valid quartile, available options are 1 and 3  representing Q1 and Q3 respectively")
        
    n= len(numberList)
    index = ((q/4)*(n+1))-1
    #print(index - int(index))
    if (index - int(index) != 0):
        return (numberList[int(index)] + numberList[int(index+1)])/2
    else:
        return numberList[int(math.ceil(index))]

#following algorithm found in https://goodcalculators.com/percentile-calculator/
def calcPercentile(numberList, p):
    sanitizeInput(numberList)
    if (type(p) == float):
        raise ValueError("Percentile must be an integer number")
    
    try:
        p = int(p)
    except:
        raise ValueError("Percentile must be an integer number")
    
    
        
    if p < 1 or p>100:
        raise ValueError ("Percentile must be a number between 1 and 100")
      

    n= len(numberList)
    index = ((p/100)*(n))-1
    #print(index)
    if (index - int(index) == 0.5):
        return (numberList[int(index)] + numberList[int(index+1)])/2
    else:
        return numberList[int(math.ceil(index))]


#print("Mean:" +str(calcMean(numberArray)))
#print("Std Dev:" + str(calcStdDev(numberArray)))
#print("Median: " +str(calcMedian(numberArray)))
#print("Quartile Q1: "+ str(calcQuartile(numberArray, 1 )))
#print("Quartile Q2: "+ str(calcQuartile(numberArray, 3 )))

#perc = input("Please enter a percentile value to calculate\n")
#try:
 #   perc = int(perc)
  #  print(str(perc)+" percentile: "+str(calcPercentile(numberArray, perc)))
#except:
 #   print("Percentile value is not valid")'''

