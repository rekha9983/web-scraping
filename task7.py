from task5 import scrap_all_movies
import json
all_data=scrap_all_movies()
def analyse_movies_director():
    director_list=[]
    for i in all_data:
        if "director" in i:
            for j in i["director"]:      
                director_list.append(j)
        director_dic={}
        for i in director_list:
            if i in director_dic:
                director_dic[i]=director_dic[i]+1
            else:
                director_dic[i]=1
    myfile=open("task7.json","w")
    json.dump(director_dic,myfile,indent=4)
    myfile.close()
    return director_dic
analyse_movies_director()