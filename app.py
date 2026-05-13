from flask import Flask, render_template, request

app = Flask(__name__)

MOZNA_JIDLA = ("Pizza", "Řízek", "Zmrzlina", "Hamburger", "Kebab")
hlasy = {jidlo: 0 for jidlo in MOZNA_JIDLA}


@app.route("/", methods=["GET", "POST"])
def index():
    jidlo = None
    if request.method == "POST":
        jidlo = request.form.get("jidlo")
        if jidlo in hlasy:
            hlasy[jidlo] += 1
    return render_template("index.html", jidlo=jidlo)


@app.route("/vyhodnoceni", methods=["GET"])
def vyhodnoceni():
    return render_template("vyhodnoceni.html", hlasy=hlasy)


if __name__ == "__main__":
    app.run(debug=True)
