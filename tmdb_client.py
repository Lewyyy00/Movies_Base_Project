import requests
import random

api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMjc0YzFjMTU0YTIzOWFiYWIyZmFlMGM0MzZlNTJkYyIsInN1YiI6IjY1YTAzNTNjNzI2ZmIxMDEyYmY4YWY1MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PXi-g7fUum3wzL60J2bq3bzFe6XuKwZML7GqWlXYvjQ'

#Stworzyłem jeden szablon get_api żeby nie powtrzac cały czas kodu 
def get_api(endpoint):
    url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type):
    return get_api(f"movie/{list_type}")

def get_single_movie(movie_id):
    return get_api(f"movie/{movie_id}")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_title_url(movie_id):
    return get_api(f"movie/{movie_id}/title")

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type=list_type)
    random_data = random.sample(data["results"], how_many)
    return random_data

def get_image(movie_id):
    return get_api(f"movie/{movie_id}/images")

def get_single_movie_cast(movie_id):
    return get_api(f"movie/{movie_id}/credits")["cast"]

