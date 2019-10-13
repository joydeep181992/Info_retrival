from flask import Flask, render_template, url_for
app = Flask(__name__)

bs_group = [
    {
        'name': 'Srilata',
        'nick_name': 'Pikachu',
        'role': 'portable charger',
    },
    {
        'name': 'Monika',
        'nick_name': 'Mosi Tosi Meowsi',
        'role': 'says meow meow all the time',
    },
    {
        'name': 'Nirupama',
        'nick_name': 'Chuhiya',
        'role': 'eats all the time',
    },
    {
        'name': 'Sachin',
        'nick_name': 'Kuttu',
        'role': 'does bhau bhau',
    },
    {
        'name': 'Garima',
        'nick_name': 'Hari Bhai aka Hulk',
        'role': 'smash/break everything',
    }
]

# decorator
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', bs_group=bs_group)

@app.route('/about')
def about():
    return render_template('about.html', title='Bs group About')

if __name__ == '__main__':
    app.run(debug=True)