from flask import Flask, render_template, redirect, request, session, flash
import model
import jinja2





app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'

@app.before_request
def setup_session():
    session['user_id'] = session.get('user_id', None)

@app.route("/")
def index():
    user_list = model.db_session.query(model.User).limit(5).all()

    return render_template("user_list.html", users=user_list)

@app.route("/signup", methods = ["GET"])
def show_signup():

    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():

    user = model.User(age=request.form["age"], gender = request.form["gender"], 
            occupation = request.form["occupation"], zipcode = request.form["zipcode"],
            first_name = request.form["first_name"], last_name = request.form["last_name"],
            email = request.form["email"], password = request.form["password"])  
    model.db_session.add(user)
    model.db_session.commit()

    return redirect("/")

@app.route("/login", methods = ["GET"])
def show_login():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def process_login():
    email = request.form["email"]
    password = request.form["password"]

    query = model.db_session.query(model.User)
    user = query.filter_by(email = email).one()


    if user.password != password:

        print "Password incorrect, unable to login"
        return render_template("login.html")

    else:

        print "entered else"
        session['user_id'] = user.id
        print session
 
        return redirect("/")

@app.route("/movies", methods = ["GET"])
def show_movies():
    if session['user_id'] == None:
        print "Please login"
        return render_template("login.html")
    else:
        user_id = session['user_id']
        ratings = model.db_session.query(model.Rating).filter_by(user_id=user_id).all()

        return render_template("movies.html", ratings = ratings)
        # ratings=model.db_sessions.query(model.User).filter_by(id=session['user'].id).all()

        # print ratings

    #return render_template("movies.html")

@app.route("/update_movies", methods = ["POST"])
def update_movies():
    
    # new_rating = request.form[]
    model.db_session.execute(update(data, values))

    print "Your ratings have been updated"
    return render_template("movies.html")

# @app.route("/user_ratings")
# def ratings_by_user(user_id):
#     query = model.db_session.query(model.User).get(user_id)
#     user = query.user
#     ratings = user.data
#     print ratings

if __name__ == "__main__":
    app.run(debug = True, port = 5000)