from task1 import*
movies_name=(scarap_top_movies())
myfile=open("task1.json")
opened_file=json.load(myfile)  
movieName_dic={}
count=1900
for i in opened_file:
    movie_list=[]
    for j in opened_file:
        x=j["year"]
        if count==x:
            movie_list.append(j)
            movieName_dic[x]=movie_list
    count=count+1
myfile=open("task2.json","w")
json.dump(movieName_dic,myfile,indent=4)
myfile.close()
