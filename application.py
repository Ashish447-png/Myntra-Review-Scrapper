from flask import Flask, render_template, request
from flask_cors import cross_origin
from src.scrapper.scrape import ScrapeReviews


application = Flask(__name__)
app = application


@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route("/review", methods=['POST', 'GET'])
@cross_origin()
def review():
    columns = None
    data = None
    
    if request.method == 'POST':
        scrape = ScrapeReviews(request)
        columns, data = scrape.get_data()
    
    return render_template("results.html",
                           titles=columns,
                           rows=data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)