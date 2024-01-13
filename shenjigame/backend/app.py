from flask import Flask, jsonify, render_template
from shenjigame.main import game_state, update_game_state

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update_game')
def update_game():
    update_game_state()
    return jsonify(success=True)

@app.route('/game_state')
def get_game_state():
    return jsonify({
        'population': game_state.population,
        'resources': {
            'food': game_state.food,
            'wood': game_state.wood,
            'stone': game_state.stone
        },
        'technology_level': game_state.technology_level,
        'buildings': game_state.buildings,
        'technologies': game_state.technologies
    })

if __name__ == '__main__':
    app.run(debug=True)