import webbrowser

class Movie():
    """This class enables to create movie instances. A movie
    has a title, a storyline, an official poster image and an official trailer"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """This function construct a movie object; it is the class's constructor
        Inputs: the movie's title, its storyline,
        the link of its poster image and the link to its youtube trailer
        Output: a movie object"""
        self.title =movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube


    def show_trailer(self):
        """this function is called upon a movie object and launch the youtube trailer
        of the object
        Input: none
        Output: a web page"""
        webbrowser.open(self.trailer_youtube_url)
        
# class TvShow herited from class Movie
class TvShow(Movie):
    """This class described a tv show;
    Some attributes were added, since a tv show is a type of movie"""
    
    def __init__(self,title,storyline,poster_image,trailer,season,episode,tv_station):
        """This is the class constructor
        Inputs: the tv show's title, its storyline, the link to a poster image,
        a link to a youtube trailer, the number of seasonsm the number of total episodes,
        the tv station who promote the show
        Ouput: a tvShow object"""
        Movie.__init__(self,title,storyline,poster_image,trailer);
        self.season=season
        self.episode=episode
        self.tv_station=tv_station
