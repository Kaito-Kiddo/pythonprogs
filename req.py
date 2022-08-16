#%%
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=orange")
print(type(page))
# print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
# print("---first item in the list---")
# print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results

#%%
import requests
import json
url="http://github.com/presnick/runestone"
page=requests.get(url)
print(type(page))
print(page.headers)


# %%
""" generate following url using request.get
https://www.google.com/search?q=%22Kaito+Kid%22&tbm=isch
"""
import requests
d = {'q': '"Kaito Kid"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)
print(type(results))
print(results.status_code)
# print(results.headers)


# %%
""" generate following url using requestURL
https://www.google.com/search?tbm=isch&q=Kaito+Kid
"""
import requests
def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url
some_base_url = "https://www.google.com/search"
some_params_dictionary= {'tbm': 'isch','q': 'Kaito Kid'}

print(requestURL(some_base_url, some_params_dictionary))


# %%
""" Itunes req """
import requests
# import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters)
# print(iTunes_response.text)
data_json = iTunes_response.json()
for r in data_json['results']:
    print(r['trackName'])


# %%

""" Course 3 FINAL ASSESSMENT """
import requests

def get_movies_from_tastedive(names):
        
    d = {'q': names,'type':'movies','limit': 5}
    results = requests.get("https://tastedive.com/api/similar", params=d)
    print(results.url)
    # print(results.text)
    data=results.json()
    # return data['Similar']['Results']
    return data
res = get_movies_from_tastedive("Bridesmaids")

def extract_movie_titles(res_dict):
        return [x['Name'] for x in res_dict['Similar']['Results']]
res = extract_movie_titles(res)
print((res))

def get_related_titles(movies_list):
    movies=[]
    for movie in movies_list:
        movies+=(extract_movie_titles(get_movies_from_tastedive(movie)))
    movies = list(set(movies))
    return movies
final_movie_list = get_related_titles(["Black Panther", "Captain Marvel"])
print(final_movie_list)
# %%
