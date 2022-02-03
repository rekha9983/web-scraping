from task1 import*
import json
file=open("task1.json","r")
myfile=json.load(file)
list=[]
for i in range(len(myfile)):
    year=myfile[i]["year"]
    mod=int(year)%10
    year1=int(year)-int(mod)
    if year1 not in list:
        list.append(year1)
dict={}
for i in range(len(list)):
    list1=[]
    for j in range(list[i],list[i]+9):
        for y in myfile:
            if y["year"]==j:
                list1.append(y)
    dict[list[i]]=list1
    new=open("task3.json","w")
    file=json.dump(dict,new,indent=4) 
    new.close()