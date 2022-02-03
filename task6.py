from task5 import scrap_all_movies
import json
all_data=scrap_all_movies()
def analyse_movies_language():
    language_list=[]
    for i in all_data:
        if "language" in i:
            for j in i["language"]:      
                language_list.append(j)
        language_dic={}
        for i in language_list:
            if i in language_dic:
                language_dic[i]=language_dic[i]+1
            else:
                language_dic[i]=1
    myfile=open("task6.json","w")
    json.dump(language_dic,myfile,indent=4)
    myfile.close()
    return language_dic
analyse_movies_language()


