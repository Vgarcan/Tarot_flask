
from flask import Flask,render_template
import requests
import random

app=Flask(__name__)


chosen_number = 6
cards= requests.get('https://tarot-api-es.vercel.app/api/v1/cards').json()
# selected_cards = random.sample(cards['cards'], chosen_number)

# for card in selected_cards:
#     print (card['name'],'\n', card['meaning_rev'])



@app.route('/')
def principal():
    selected_cards = random.sample(cards['cards'], chosen_number)
    return render_template('index.html', cards=selected_cards)





if __name__ == '__main__':
    app.run(debug=True)
