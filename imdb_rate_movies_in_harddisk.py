# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:58:13 2020

@author: Admin
"""

#rate all my movies from IMDB

#pip install imdbpy

import imdb
import os

moviesDB = imdb.IMDb()

movies_list=[]
failed_movie_list=[]
video_types=[".avi",".mp4"]
path='H:\English movies'
files = os.listdir(path)
for name in files:
    movies_list.append(name)

print("\n".join(movies_list))
print("No of movies in directory:", len(movies_list))

print('Movies from my hard disk', movies_list)
print("\n-------------------------")

for movie in movies_list:
    # to handle rerun
    if movie.find("imdb-")>0:
        continue
    endIndex=[]
    movie_name_ending_index_1 = movie.find('[')
    if movie_name_ending_index_1>=0:
        endIndex.append(movie_name_ending_index_1)
    movie_name_ending_index_2 = movie.find('(')
    if movie_name_ending_index_2>=0:
        endIndex.append(movie_name_ending_index_2)
    movie_name_ending_index_3 = movie.find('.')
    if movie_name_ending_index_3>=0:
        endIndex.append(movie_name_ending_index_3)
    if(len(endIndex)>0):
        movie_name = movie[0:min(endIndex)]
    else:
        movie_name=movie[0]
    print("movie_name used for searching :", movie_name)
    result = moviesDB.search_movie(movie_name)
    #print('result',result)
    try:
        if result:
            imdb_movie_id=result[0].getID()
            imdb_movie=moviesDB.get_movie(imdb_movie_id)
            title=imdb_movie['title']
            rating=imdb_movie['rating']
            print(title +":",  rating)
            rating = str(rating)
        else:
            print("no result fetched for:", movie_name)
        
        if rating and title:
            os.rename(path+"\\"+movie, path+"\\"+movie+"imdb-"+rating                                                                                                                                  )
            print('renamed', movie)
    except:
        print("Exception for movie", movie)
        failed_movie_list.append(movie)
    


print("No of movies failed in directory:", len(failed_movie_list))
print("\n".join(failed_movie_list))