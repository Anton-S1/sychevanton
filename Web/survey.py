# Данная программа реализовывает простой опрос, сохраняет результаты в документ и выдает их на отдельной странице
from flask import Flask, render_template, request

app = Flask(__name__)

survey_data = {
    'question': 'Какую фигуру Вы видите на картинке?',
    'fields': ['Овал', 'Квадрат', 'Окружность', 'Треугольник', 'Прямоугольник']
}
filename = 'data.txt'

@app.route('/survey')
def S():
    vote = request.args.get('field')

    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()

    return render_template('over.html', data=survey_data)

@app.route('/')
def root():
    return render_template('survey.html', data=survey_data)


@app.route('/results')
def results():
    votes = {}
    for f in survey_data['fields']:
        votes[f] = 0

    f = open(filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template('results.html', data=survey_data, votes=votes)

if __name__ == "__main__":
    app.run(debug=True)