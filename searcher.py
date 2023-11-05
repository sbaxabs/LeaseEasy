from flask import Flask, redirect, url_for,  render_template

app = Flask(__name__)
app.static_folder = 'static'  # Folder where your static files are located
app.static_url_path = '/static'  # URL path for static files

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()