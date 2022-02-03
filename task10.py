from task5 import scrap_all_movies
import json
l=scrap_all_movies()
def director_language():
    director_list=[]
    dic={} 
    for i in l:
        if "director" in i:
            m=i["director"]
            for director in m:
                if director not in director_list:
                    director=director
                    director_list.append(director)
    dic={}
    for director in director_list:
        d={}
        for i in l:
            if director in i["director"]:
                if "language" in i:
                    for j in i["language"]:
                        if j in d:
                            d[j]=d[j]+1
                        if j not in d:
                            d[j]=1
        dic[director]=d
    myfile=open("task10.json","w")
    json.dump(dic,myfile,indent=4)
    myfile.close()
                                   
        
director_language()