from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/fizzbuzz/<int:count_to>")
def fizzbuzz(count_to):

    l=[]

    for n in range(1,count_to):

        if n%3==0 and n%5==0:
            l.append("fizzbuzz")
        elif n%5==0:
            l.append("Buzz")
        elif n%3==0:
            l.append("Fizz")
        else:
            l.append(n)
        
    return render_template('home.html', numbers=n, l=l)

    

