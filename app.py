from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home_page():
    with open('genealogie.csv', 'r', encoding='utf-8-sig') as csvfile:
        forebears = []
        csv_reader = csv.reader(csvfile)
        keys = next(csv_reader)
        for row in csv_reader:
            forebear = {}
            for index_col in range(len(row)):
                forebear[keys[index_col]] = row[index_col]
            forebears.append(forebear)
    return render_template('base.html', forebears=forebears, keys=keys)


@app.route('/forebears', methods=['POST'])
def add_new_forebear():
    # Add a new line to the CSV
    print(request.form['Branche'])
    # Can update data

    # Can show the data depending on the name of the branch
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
