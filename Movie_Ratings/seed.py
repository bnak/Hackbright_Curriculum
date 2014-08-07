import csv
import model
from model import *
import datetime

def load_users(db_session, user_file):
    # use u.user
    f = open(user_file)
    user_data = csv.reader(f, delimiter = "|")
    for row in user_data:
        user = User(id = row[0], age=row[1], gender = row[2], occupation = row[3], zipcode = row[4])
        db_session.add(user)
    db_session.commit()

def load_movies(db_session, user_file):
    # use u.item

    f = open(user_file)

    movie_data = csv.reader(f, delimiter = "|")

    for row in movie_data:

        if row[2]:
            release_date = datetime.datetime.strptime(row[2], "%d-%b-%Y")
        else:
            release_date = None

        movie = Movie(movie_id = row[0], 
            movie_title=row[1].decode("latin-1"), 
            release_date = release_date,
            video_release_date = row[3], 
            IMDb_URL = row[4], 
            unknown = row[5], 
            action=row[6],
            adventure=row[7], 
            animation = row[8],
            childrens = row[9],
            comedy = row[10],
            crime = row[11],
            documentary = row[12],
            drama = row[13],
            fantasy = row[14],
            film_noir = row[15],
            horror = row[16],
            musical = row[17],
            mystery = row[18],
            romance = row[19],
            sci_fi = row[20],
            thriller = row[21],
            war = row[22],
            western = row[23])
        db_session.add(movie)
    db_session.commit()


def load_ratings(db_session, data_file):
    # use u.data

    f = open(data_file)
    ratings_data = csv.reader(f, delimiter="\t")

    for row in ratings_data:
        rating = Rating(user_id = row[0], item_id = row[1], rating = row[2],
         timestamp = row[3])
        db_session.add(rating)

    db_session.commit()

def main(db_session):
    # You'll call each of the load_* functions with the session as an argument
   
    data_file = "seed_data/u.user"
    load_users(db_session, data_file)

    data_file = "seed_data/u.item"
    load_movies(db_session, data_file)

    data_file = "seed_data/u.data"
    load_ratings(db_session, data_file)

if __name__ == "__main__":
    s= model.connect()
    main(s)
