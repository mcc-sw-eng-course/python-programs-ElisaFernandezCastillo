import csv
import timeit

class sortingData(object):
    def __init__(self):
        self.lst=[]
        self.time=0
        self.sortingMethod=None
    
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
        self.sortingMethod="Merge Sort"
        start = timeit.default_timer()
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
        stop = timeit.default_timer()
        self.time=stop-start


    def heap_sort(self):
        self.sortingMethod = "Heap Sort"
        starting = timeit.default_timer()
        end=len(self.lst)
        start=end//2-1
        for i in range(start,-1,-1):
            self.heapify(end,i)
        for i in range(end-1,0,-1):
            self.swap(i,0)
            self.heapify(i,0)
        stop = timeit.default_timer()
        self.time=stop-starting

    def swap(self,i,j):
        self.lst[i],self.lst[j]=self.lst[j],self.lst[i]

    def heapify(self,end,i):
        l=2*i+1
        r=2*i+2

        max=i
        if l<end and self.lst[i]<self.lst[l]:
            max=l
        if r<end and self.lst[max]<self.lst[r]:
            max=r
        if max !=i:
            self.swap(i,max)
            self.heapify(end,max)

    def quickSort(self):
        self.sortingMethod = "Quick Sort"
        start = timeit.default_timer()
        self.quickSortHelper(self.lst,0,len(self.lst)-1)
        stop = timeit.default_timer()
        self.time=stop-start

    def quickSortHelper(self,alist,first,last):
        if first<last:
            splitpoint=self.partition(alist,first,last)

            self.quickSortHelper(alist,first,splitpoint-1)
            self.quickSortHelper(alist, splitpoint+1, last)

    def partition(self,alist,first,last):
        pivotvalue=alist[first]

        leftmark=first+1
        rightmark=last

        done=False
        while not done:

            while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
                leftmark=leftmark+1
            while alist[rightmark]>=pivotvalue and rightmark>=leftmark:
                rightmark=rightmark-1

            if rightmark<leftmark:
                done=True
            else:
                temp=alist[leftmark]
                alist[leftmark]=alist[rightmark]
                alist[rightmark]=temp
        temp=alist[first]
        alist[first]=alist[rightmark]
        alist[rightmark]=temp

        return rightmark

    def getPerformanceData(self):
        n=len(self.lst)
        msg = "Number of sorted records: ", n, "Time spent in execution:"+str(self.time),"Sorting Method:"+self.sortingMethod
        print(msg)







#start = timeit.default_timer()
#srtDt=sortingData()
#lista=srtDt.setInputData("Book1")
#print(srtDt.lst)
#srtDt.getPerformanceData2()
#srtDt.mergeSort(lista)
#srtDt.heap_sort()
#srtDt.quickSort()
#srtDt.set_output_data("SortedBook1")
#print(srtDt.lst)
#srtDt.getPerformanceData()
#stop=timeit.default_timer()

