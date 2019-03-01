import csv

class sortingData(object):
    def __init__(self):
        self.lst=[]
    
    def setInputData(self,path):
        try:
            with open(path+'.csv')as f:
                reader=csv.reader(f)
                for row in reader:
                    for item in row:
                        try:
                            item=float(item)
                            self.lst.append(item)
                        except ValueError:
                            pass
        except FileNotFoundError:
            raise FileNotFoundError("File was not found")
        return self.lst
    
    def set_output_data(self,nameFile):
        with open(nameFile+'.csv','w') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow(self.lst)
        csvFile.close()
    
    def mergeSort(self,lista):
        alist=lista
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
    
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)
    
            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1
    
            while i < len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1
    
            while j < len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
    

#srtDt=sortingData()
#lista=srtDt.setInputData("Book1")
#srtDt.mergeSort(lista)
#srtDt.set_output_data("SortedBook1")
#print(srtDt.lst)
