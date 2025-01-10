import requests
from bs4 import BeautifulSoup
import pandas as pd


Movies = []
Director = []
Year_Release = []
Liked_percentage = []


url = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"
r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text,"html.parser")
#print(soup)

for i in range(1, 3):

    np = soup.find("a", class_="post-page-numbers")


    if np:
        npl = np["href"]
        #print(npl)


        cnp = npl
        #print(cnp)


        url = cnp
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
    else:
        print("No 'post-page-numbers' link found.")
        break

    n = soup.find_all("h2")
    #print(n)
    for i in n:
        names = i.find("a")
        if names:
            Movies.append(names.text.strip())
            Movies = Movies[:301]
    print(len(Movies))


    a = soup.find_all("span",class_="subtle start-year")
    #print(a)
    for j in a:
        year = j.text.strip()
        Year_Release.append(year)
        Year_Release = Year_Release[:301]
    print(len(Year_Release))


    b = soup.find_all("span",class_="tMeterScore")
    #print(b)
    for k in b:
        rating = k.text.strip()
        Liked_percentage.append(rating)
        Liked_percentage = Liked_percentage[:301]
    print(len(Liked_percentage))

    c = soup.find_all("div",class_="info director")
    #print(c)
    for l in c:
        D = l.find("a")
        if c :
            Director.append(D.text.strip())
        Director = Director[:301]

    print(len(Director))

df = pd .DataFrame({"Movie_name": Movies, "Year": Year_Release, "Rating(%)":Liked_percentage,"Directed By":Director})
#print(df)
df.to_csv("Rotten Tomatoes.csv")





