from flask import render_template
from app import app
from .request import get_movies, get_movie


@app.route('/')
def index():
     """
    View root page function that returns the index page and its data

    """
     popular_movies=get_movies('popular')
     upcoming_movie = get_movies('upcoming')
     now_showing_movie = get_movies('now_playing')
     print(popular_movies)
     title = 'Home - Welcome to the best Movie Website'
     return render_template('index.html',popular = popular_movies,title = title, upcoming = upcoming_movie, now_showing = now_showing_movie )

@app.route('/movie/<int:id>')
def movie(id):

     movie = get_movie(id)
     title = f'{movie.title}'
     return render_template('movie.html',movie = movie, title = title)
