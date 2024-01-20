from random import choice
from flask import Flask, render_template, request, redirect, url_for
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    avalible_list = ['popular', 'top_rated', 'upcoming', 'now_playing']
    selected_list = request.args.get('list_type', 'popular')

    if selected_list not in avalible_list:
        selected_list = 'popular'
        return redirect(url_for('homepage', list_type=selected_list))

    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, list=avalible_list, selected_list=selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)[:8]
    movie_images = tmdb_client.get_image(movie_id)
    if movie_images['backdrops']:
        selected_movie_images = choice(movie_images['backdrops'])
    else:
        selected_movie_images = []
    return render_template("movie_details.html", movie=details, selected_movie_images=selected_movie_images, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)
    

