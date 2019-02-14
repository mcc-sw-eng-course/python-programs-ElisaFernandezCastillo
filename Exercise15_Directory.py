'''
Created on 2019 M01 30

@author: A01221781
'''

class userDirectory(object):
    def __init__(self):
        self.listRecords=[]
    """def __str__(self):
        allRecords=""
        for i in self.listRecords:
            user=i
            userInfo=""
            for x in user.values():
                try:
                    userInfo=userInfo+x+"\n"
                except TypeError:
                    pass
            userInfo=userInfo+"\n"
            allRecords=allRecords+" "+userInfo
        return allRecords"""
            
    
    def createNewRecord(self,name,address=None,phone=None,email=None):
        newUser={"name":name,"address":address,"phone":phone,"email":email}
        self.listRecords.append(newUser)
        return newUser
        
    def saveToTextFile(self,filename):
        fileName=filename+".txt"
        with open(fileName,'w') as f:
            for i in self.listRecords:
                f.write(i.__str__()+"\n")
        
    def loadRecordsFromFile(self,filename):
        fileName=filename+".txt"
        openedFile=False
        try:
            openFile=open(fileName,'r')
            openedFile=True
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        listLine=listLine=openFile.readline().strip('\n')
        newRecord=None
        while (listLine): 
            #print("Line read from file:",listLine)
            listLine=listLine.strip('[]\n' '')
            if(listLine.find(',')!=-1):
                elements=listLine.split(",")
            elif(listLine.find(';')!=-1):
                elements=listLine.split(";")
            elif(listLine.find(':')!=-1):
                elements=listLine.split(":")
            else:
                elements=listLine.split(" ")
            #print("Elements:",elements)
            name=""
            address=""
            phone=""
            email=""
            for i in elements:
                i=i.strip(" ")
                item=i.split(":")
                #print(item)
                if(item[0].lower()==("name")):
                    name=item[-1]
                elif(item[0].lower()==("address")):
                    address=item[-1]
                elif(item[0].lower()==("phone")):
                    phone=item[-1]
                elif(item[0].lower()==("email")):
                    email=item[-1] 
            if(address==""):
                address=None
            if(phone==""):
                phone=None
            if(email==""):
                email=None
            #print("Name:",name)
            #print("Address:",address)
            #print("Phone:",phone)
            #print("Email:",email)
            #Create the new record
            newRecord=self.createNewRecord(name,address,phone,email)
            #print("New Record",newRecord)
            newRecord=None
            listLine=openFile.readline().strip('\n')
        #print(userDict)
        return self
    def searchDataFromRecord(self,toSearch):
        for i in self.listRecords:
            if(toSearch in i.values()):
                return i

               
    
    
    
    
"""userDict=userDirectory() 
userDict.createNewRecord("Elisa")
userDict.createNewRecord("Carolina","R.Laureles 2068")
userDict.createNewRecord("Marisol",None,"3310389654")
userDict.createNewRecord("Pedro","R.Crisantemos Pte. 2644","39874513","pedro.tre@gmail.com")
print("Creation of records for Elisa, Carolina, Marisol and Pedro\nThe program accepts different types of input:\n\n",userDict)
userDict.saveToTextFile("records_4users")
userDict.loadRecordsFromFile("contactos")
userDict.saveToTextFile("records")
print("Searching for 'Marisol': ",userDict.searchDataFromRecord("Marisol"))
print("Searching for '3316457891': ",userDict.searchDataFromRecord("3316457891"))
print("Searching for 'Cesar': ",userDict.searchDataFromRecord("Cesar"))"""