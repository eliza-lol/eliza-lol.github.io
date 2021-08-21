from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Haunted House"
    
    text = """Little Red Riding Hood lived in a wood with her mother. 
    One day Little Red Riding Hood went to visit her granny. 
    She had a nice cake in her basket.
    On her way Little Red Riding Hood met a wolf.
    ‘Hello!’ said the wolf. ‘Where are you going?’"""

    picture_url= url_for('static', filename='29067311.png')

    choices = [
        ('enter_house',"I’m going to see my grandmother. She lives in a house behind those trees."),
        ('happy_end', "don't talk to strangers")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)



@app.route("/inside")
def enter_house():
    title = "After..."

    picture_url= url_for('static', filename='29067404.jpg')

    text = """The wolf ran to Granny’s house and ate Granny up. He got into Granny’s bed. 
    A little later, Little Red Riding Hood reached the house. She looked at the wolf."""

    choices = [
        ('teeth',"Granny, what big eyes you have!"),
        ('run_away',"‘Granny, what big teeth you have!’!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)


@app.route("/woodcutterr")
def woodcutter():
    
    picture_url= url_for('static', filename='29067299.png')

    text = """A woodcutter was in the wood. He heard a loud scream and ran to the house.
    The woodcutter hit the wolf over the head. The wolf opened his mouth wide and shouted and Granny jumped out.
    The wolf ran away and Little Red Riding Hood never saw the wolf again. """

    choices = []

    return render_template('adventure.html', text=text, choices=choices, picture_url=picture_url)

@app.route("/teeee")
def teeth():
    
    picture_url= url_for('static', filename='29067311.png')

    text = """‘All the better to see you with!’ said the wolf. """

    choices = [
        ('run_away',"‘Granny, what big teeth you have!"),
        ('woodcutter',"Where is my grandmother, wolf!!!")
    ]

    return render_template('adventure.html', text=text, choices=choices, picture_url=picture_url)

@app.route("/escape")
def run_away():
    #title = "You run away!"

    picture_url= url_for('static', filename='29067420.jpg')
    
    text = """‘All the better to eat you with!’ shouted the wolf."""

    choices = []

    return render_template('adventure.html', text=text, choices=choices, picture_url=picture_url)


@app.route("/happy")
def happy_end():
    #title = "You run away!"

    picture_url= url_for('static', filename='29067403.jpg')
    
    text = """You delivered the cake to your grandmother and the wolf didn't eat her"""

    choices = []

    return render_template('adventure.html', text=text, choices=choices, picture_url=picture_url)



