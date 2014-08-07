from flask import Flask, request, session, render_template, g, redirect, url_for, flash
import model, collections
import jinja2


app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.before_request
def setup_session():
    session['user'] = session.get('user', None)
    session['cart'] = session.get('cart', [])
    session['total'] = session.get('total', 0)

@app.route("/")
def index():
    """This is the 'cover' page of the ubermelon site"""
    return render_template("index.html")

@app.route("/melons")
def list_melons():
    """This is the big page showing all the melons ubermelon has to offer"""
    melons = model.get_melons()

    return render_template("all_melons.html",
                           melon_list = melons)

@app.route("/melon/<int:id>")
def show_melon(id):
    """This page shows the details of a given melon, as well as giving an
    option to buy the melon."""
    melon = model.get_melon_by_id(id)

    return render_template("melon_details.html",
                  display_melon = melon)

@app.route("/cart")
def shopping_cart():
    """TODO: Display the contents of the shopping cart. The shopping cart is a
    list held in the session that contains all the melons to be added. Check
    accompanying screenshots for details."""

    tally = collections.Counter(session['cart'])
    purchased_melons = {m_id: model.get_melon_by_id(m_id) for m_id in tally}

    if not purchased_melons:
        flash("Buy melons!")

    return render_template("cart.html", melon_list=purchased_melons, qty=tally, total_price=session['total'])
    
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """TODO: Finish shopping cart functionality using session variables to hold
    cart list.
    
    Intended behavior: when a melon is added to a cart, redirect them to the
    shopping cart page, while displaying the message
    "Successfully added to cart" """
    
    session['cart'] = session.get('cart', []) + [id]
    session['total'] += model.get_melon_by_id(id).price

    print session

    flash("Successfully added to cart")
    return redirect("/cart")
    # return "Oops! This needs to be implemented!"


@app.route("/login", methods=["GET"])
def show_login():

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """TODO: Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""
    email = request.form["email"]
    password = request.form["password"]
    customer = model.get_customer_by_email(email)

    if not customer:
        flash("Sorry! Login Error.")
        return redirect("/login")

    session['user'] = customer.givenname
    return redirect("/melons")


@app.route("/checkout")
def checkout():
    """TODO: Implement a payment system. For now, just return them to the main
    melon listing page."""
    
    flash("Sorry! Checkout will be implemented in a future version of ubermelon.")
    return redirect("/melons")

@app.route("/logout")
def logout(): 
    session.clear()

    flash("User has logged out.")
    return redirect("/melons")  

if __name__ == "__main__":
    app.run(debug=True)
