from flask import Flask, render_template, request
from game import snowman, MIN_WORD_LENGTH, MAX_WORD_LENGTH, MAX_WRONG_GUESSES
from wonderwords import RandomWord
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    snowman_word = RandomWord().word(word_min_length=MIN_WORD_LENGTH, word_max_length=MAX_WORD_LENGTH)
    return snowman_game(snowman_word)

@app.route('/guess', methods=['POST'])
def guess():
    snowman_word = request.form['word']
    guessed_letter = request.form.get('guess')
    guessed_letters = json.loads(request.form.get('guessed_letters', '[]'))
    if guessed_letter:  # Make sure the guessed letter is not None
        guessed_letters.append(guessed_letter)
    return snowman_game(snowman_word, guessed_letters)

# ... Rest of your code remains the same, just ensure to send guessed_letters as JSON
def snowman_game(snowman_word, guessed_letters=None):
    # your logic remains the same till template rendering
    
    return render_template('game.html', word_progress=word_progress, snowman_graphic=snowman_graphic,
                            wrong_guesses=wrong_guesses_str, guesses_left=guesses_left,
                            snowman_word=snowman_word, guessed_letters=json.dumps(guessed_letters))

# ... Rest of your functions

if __name__ == '__main__':
    app.run(debug=True)
