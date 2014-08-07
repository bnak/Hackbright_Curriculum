from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
import correlation

ENGINE = create_engine("sqlite:///ratings.db", echo=False)
db_session = scoped_session(sessionmaker(bind=ENGINE,
                                       autocommit = False,
                                       autoflush = False))

Base = declarative_base()
Base.query = db_session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable = True)
    gender = Column(String(10), nullable = True)
    occupation = Column(String(64), nullable = True)
    zipcode = Column(String(15), nullable= True)
    email = Column(String(50), nullable = True)
    password = Column(String(50), nullable = True)
    first_name = Column(String(50), nullable = True)
    last_name = Column(String(50), nullable = True)


    def similarity(user1, user2):
        u_ratings = {}
        paired_ratings = []
        for r in user1.data:
            u_ratings[r.item_id] = r

        for r in user2.data:
            u_r = u_ratings.get(r.item_id)
            if u_r:
                paired_ratings.append( (u_r.rating, r.rating) )

        if paired_ratings:
            return correlation.pearson(paired_ratings)
        else:
            return 0.0

    def predict_rating(self, movie):
        ratings = self.ratings
        other_ratings = movie.ratings
        other_users = [ r.user for r in other_ratings ]
        similarities = [ (self.similarity(other_user), other_user) \
            for other_user in other_users ]
        similarities.sort(reverse = True)
        top_user = similarities[0]  #highest correlated user
        matched_rating = None
        for rating in other_ratings:
            if rating.user_id == top_user[1].id:
                matched_rating = rating
                break
        return matched_rating.rating * top_user[0]

class Rating(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id = Column(Integer, ForeignKey('item.movie_id'))
    rating = Column(Integer, nullable = False)
    timestamp = Column(Integer, nullable = True)

    user = relationship("User",
            backref=backref("data", order_by=id))

    movie = relationship("Movie",
            backref=backref("data", order_by=id))

class Movie(Base):
    __tablename__ = "item"

    movie_id = Column(Integer, primary_key = True)
    movie_title = Column(String(64), nullable = True)
    release_date = Column(DateTime, nullable = True)
    video_release_date = Column(String(64), nullable = True)
    IMDb_URL = Column(String(140), nullable = True)
    unknown = Column(Integer, nullable = True)
    action = Column(Integer, nullable = True)
    adventure = Column(Integer, nullable = True)
    animation = Column(Integer, nullable = True)
    childrens = Column(Integer, nullable = True)
    comedy = Column(Integer, nullable = True)
    crime = Column(Integer, nullable = True)
    documentary = Column(Integer, nullable = True)
    drama = Column(Integer, nullable = True)
    fantasy = Column(Integer, nullable = True)
    film_noir = Column(Integer, nullable = True)
    horror = Column(Integer, nullable = True)
    musical = Column(Integer, nullable = True)
    mystery = Column(Integer, nullable = True)
    romance = Column(Integer, nullable = True)
    sci_fi = Column(Integer, nullable = True)
    thriller = Column(Integer, nullable = True)
    war = Column(Integer, nullable = True)
    western = Column(Integer, nullable = True)

### End class declarations

# def connect():
#     global ENGINE
#     global Session

#     ENGINE = create_engine("sqlite:///ratings.db", echo=False)
#     Session = sessionmaker(bind=ENGINE)

#     return Session()


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
