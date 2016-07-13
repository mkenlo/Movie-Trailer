import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title =movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
#class TvShow herited from class Movie
class TvShow(Movie):
    def __init__(self,title,storyline,poster_image,trailer,season,episode,tv_station):
        Movie.__init__(self,title,storyline,poster_image,trailer);
        self.season=season
        self.episode=episode
        self.tv_station=tv_station
