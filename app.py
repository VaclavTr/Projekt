from flask import Flask, render_template, request

app = Flask(__name__)

MOZNA_JIDLA = ("Pizza", "Řízek", "Rizoto", "Hamburger", "Kebab")
hlasy = {jidlo: 0 for jidlo in MOZNA_JIDLA}


@app.route("/", methods=["GET", "POST"])
def index():
    jidlo = None
    error = None
    if request.method == "POST":
        vyber = request.form.get("jidlo")
        if vyber in hlasy:
            hlasy[vyber] += 1
            jidlo = vyber
        elif not vyber:
            error = "Vyberte prosím jedno jídlo!"
        else:
            error = "Vyberte prosím platné jídlo!"#když uživatel vybere jídlo, které není v hlasech
    return render_template("index.html", jidlo=jidlo, error=error)


@app.route("/vyhodnoceni", methods=["GET"])
def vyhodnoceni():
    return render_template("vyhodnoceni.html", hlasy=hlasy)


if __name__ == "__main__":
    app.run(debug=True)
