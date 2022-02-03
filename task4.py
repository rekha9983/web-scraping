from task1 import* 
url= "https://www.rottentomatoes.com//m/spider_man_into_the_spider_verse"
def one_movie(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    li=soup.find_all('li',class_='meta-row clearfix')
    heading=soup.find('h1',class_='scoreboard__title').text
    details={}
    details["name"]=heading
    for i in li:
        data=i.text
        x=data.split()
        # print(x)
        if 'Rating:' in x:
            details["rating"]=x[1]
        elif 'Language:' in x:
            details['language']=x[2].split()
        elif 'Runtime:' in x:
            h=0
            for i in x:
                if i>='0' and i<='9' and 'h' in i:
                    h=h+int(i[0])*60
                elif i>='0' and i<='9' and 'm'  in i :
                    s=""
                    for j in i:
                        if j>='0' and j<='9':
                            s=s+j
                    h=h+int(s)
            details["runtime"]=h
        elif 'Release' in x:
            details["release(steaming)"]=x[3]+" "+x[4]+x[5]
        elif 'Director:' in x:
            y=x[1:]
            h=" "
            i=0
            while i<len(y):
                h=h+y[i]
                i+=1
            l=h.strip().split(",")
            details['director']=l
        elif 'Genre:' in x:
            y=x[1:]
            h=" "
            i=0
            while i<len(y):
                h=h+y[i]
                i+=1
            l=h.strip().split(",")
            details["genre"]=l      
        elif 'Producer:' in x:
            y=x[1:]
            h=" "
            i=0
            while i<len(y):
                h=h+y[i]
                i+=1
            l=h.split(",")
            details['producer']=l 
    myfile=open("task4.json","w")
    json.dump(details,myfile,indent=4)
    myfile.close()
    return details
one_movie(url)