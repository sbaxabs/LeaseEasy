from flask import Flask, redirect, url_for,  render_template

app = Flask(__name__)
app.static_folder = 'static'  # Folder where your static files are located
app.static_url_path = '/static'  # URL path for static files

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

# from flask import Flask, render_template, jsonify

# app = Flask(__name__)
# app.static_folder = 'static'
# app.static_url_path = '/static'

# # Include your scraping code here to get the ugroup_json_data

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/apartments")
# def get_apartments():
#     # Return the JSON data from the scraper
#     return jsonify(ugroup_json_data)

# if __name__ == "__main__":
#     app.run()
