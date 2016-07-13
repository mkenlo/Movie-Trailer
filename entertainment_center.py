import media
import fresh_tomatoes
import os

# get the path for my tvShow images
img_path=os.getcwd()+"\images"

# create tvShow object
empire =media.TvShow(
    "Empire",
    "The show centers around a hip hop music and entertainment company,"
    "Empire Entertainment, and the drama among the members of the founders' "
    "family as they fight for control of the company.",
    img_path+"\Empire_Logo.png",
    "https://www.youtube.com/watch?v=dBzu_jKLJek",
    3,36,"HBO")
being_mary_jane = media.TvShow(
    "Being Mary Jane",
    "The series centers on successful broadcast journalist Mary Jane Paul and"
    " her professional and private family life while searching for 'Mr. Right'",
    img_path+"\Being_Mary_Jane_logo.png",
    "https://www.youtube.com/watch?v=UqZICwnqf4k",
    4,32,"dont know")
games_of_thrones=media.TvShow(
    "Games of Thrones",
    "Game of Thrones is an American fantasy drama television series",
    img_path+"\Game_of_Thrones_title_card.jpg",
    "https://www.youtube.com/watch?v=iGp_N3Ir7Do",
    6,48,"HBO")
scandal=media.TvShow(
    "Scandal",
    "Scandal is an American political thriller television series",
    img_path+"\Scandal_logo.png",
    "https://www.youtube.com/watch?v=PhOR6DIS_Ho",
    6,120,"ABC")
house_of_cards=media.TvShow(
    "House of Cards",
    "story of Frank Underwood, a Democrat from South Carolina's 5th"
    " congressional district and House Majority Whip who, after being passed"
    " over for appointment as Secretary of State, initiates an elaborate plan"
    " to get himself into a position of greater power, aided by his wife, Claire Underwood",
    img_path+"\House_of_Cards_title_card.png",
    "https://www.youtube.com/watch?v=ULwUzF1q5w4",
    4,28,"Netflix")
blacklist=media.TvShow(
    "the BlackList",
    "",
    img_path+"\The-Blacklist-logo.png",
    "https://www.youtube.com/watch?v=JGBIimq1I3A",
    5,75,"NBC")
orange_black=media.TvShow(
    "Orange is the new Black",
    "The series revolves around Piper Chapman, a woman in her 30s living in New York"
    " City, who is sentenced to 15 months in Litchfield Penitentiary, "
    "a minimum-security women's federal prison (operated by the 'Federal Department of"
    " Corrections') in upstate New York",
    img_path+"\Orange_is_the_new_Black.png",
    "https://www.youtube.com/watch?v=vY0qzXi5oJg",
    4,60,"")
# create an array with tvShow objects previously created
tvshows=[empire,being_mary_jane,scandal,house_of_cards,blacklist,orange_black]

# this code will rendered a html page with my tvShow information
fresh_tomatoes.open_movies_page(tvshows)
