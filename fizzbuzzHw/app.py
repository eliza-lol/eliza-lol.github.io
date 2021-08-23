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

@app.route('/words/<string:word>')
def words(word):

    anagrams_list=[]
    
    w = open('words.txt')
    word_list = w.read().splitlines()
    real_word = word.upper() in word_list
    
    a =sorted(word.upper())

    for an in word_list:
        if sorted(an) == a:
            anagrams_list.append(an)

    return render_template('words.html', word=word, word_list=word_list, real_word=real_word, anagrams_list=anagrams_list)


    

  


    

