from task1 import*
from task4 import*
import json
t1=scarap_top_movies()
movie=t1
def scrap_all_movies():
    list=[]
    for i in movie:
        list.append(one_movie(i["url"]))
    file=open("task5.json","w")
    json.dump(list,file,indent=4)
    file.close()
    return list
scrap_all_movies()