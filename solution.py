from flask import render_template, Flask, redirect

from forms.loginfrom import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/training/<prof>')
def training(prof):
    prof = prof.split()
    return render_template('simulator.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                   'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
                   'киберинженер', 'штурман', 'пилот дронов']
    return render_template('profs.html', list=list, prof=professions)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(port=88, host='127.0.0.1')
