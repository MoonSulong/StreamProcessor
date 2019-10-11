import ast
from flask import Flask, jsonify, request
from flask import render_template

# create app and define global var to store labels and values
app = Flask(__name__)
words = []
counts = []

# parse data sent from spark and codes according to request form
@app.route('/updateData', methods=['POST'])
def update_data_from_spark():
    global words, counts
    if not request.form or 'words' not in request.form:
        return "error",400
    words = ast.literal_eval(request.form['words'])
    counts = ast.literal_eval(request.form['counts'])
    print("current words: " + str(words))
    print("current counts: " + str(counts))
    return "success",201

# update hashtag labels and counts
@app.route('/updateChart')
def refresh_hashtag_data():
    global words, counts
    print("current words: " + str(words))
    print("current data: " + str(counts))
    return jsonify(sWords=words, sCounts=counts)

# binds to homepage
@app.route("/")
def showChart():
    global words,counts
    counts = []
    words = []
    return render_template('chart.html', counts=counts, words=words)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

