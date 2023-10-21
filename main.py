
from flask import Flask,render_template, request, redirect
import requests
import random

app=Flask(__name__)


add_number = 3
chosen_number = 5
cards= requests.get('https://tarot-api-es.vercel.app/api/v1/cards').json()



@app.route('/')
def principal():
    selected_cards = random.sample(cards['cards'], add_number)
    display_cards = random.sample(cards['cards'], chosen_number)
    return render_template('index.html', cards=selected_cards, c_display=display_cards)


@app.route('/reading/<q1>/<q2>')
def principal2(q1,q2):
    selected_cards = random.sample(cards['cards'], chosen_number)
    return render_template('index_copy.html', cards=selected_cards, q1=q1, q2=q2)





if __name__ == '__main__':
    app.run(debug=True)
