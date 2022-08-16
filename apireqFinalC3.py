"""     FINAL ASSESSMENT
             PART 1 
"""

import requests_with_caching

def get_movies_from_tastedive(names):
        
    d = {'q': names,'type':'movies','limit': 5}
    results = requests_with_caching.get("https://tastedive.com/api/similar", params=d)
    print(results.url)
    data=results.json()
    return data

def extract_movie_titles(res_dict):
    return [x['Name'] for x in res_dict['Similar']['Results']]


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
#extract_movie_titles(get_movies_from_tastedive("Black Panther"))

def get_related_titles(movies_list):
    movies=[]
    for movie in movies_list:
        movies+=(extract_movie_titles(get_movies_from_tastedive(movie)))
    movies = list(set(movies))
    return movies
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#get_related_titles(["Black Panther", "Captain Marvel"])
#get_related_titles([])

"""                  PART 2 
"""

def get_movie_data(title):
    d = {'t':title,'r':'json'}
    result = requests_with_caching.get("http://www.omdbapi.com/",params=d)
    data = result.json()
    return data
def get_movie_rating(res_dict):
    #['Ratings'][1] contais dict Sourse : Rotton Tomatoes  and Value : __%
    if len(res_dict['Ratings']) == 0:
        return 0
    else:    
        for k in res_dict['Ratings']:
            if 'Rotten Tomatoes' in k['Source']:
                rating = k['Value']
                return int(rating[:-1])
        return 0
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#print(get_movie_rating(get_movie_data("Deadpool 2")))
#print(get_movie_rating(get_movie_data("Black Panther")))
#print(get_movie_rating(get_movie_data("Venom")))



def get_sorted_recommendations(movies_l):

    ratings = []
    titles = get_related_titles(movies_l)
    print(titles)
    for title in titles:
        ratings.append(get_movie_rating(get_movie_data(title)))
    print(ratings)
    movies = dict(zip(titles, ratings)) 
    print(movies)
    sorted_movies = sorted(movies,key=lambda x:(movies[x],-len(x)),reverse = True)
    print(sorted_movies)
    return sorted_movies

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
