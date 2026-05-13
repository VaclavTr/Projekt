import json
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)

MOZNA_JIDLA = ("Pizza", "Řízek", "Rizoto", "Hamburger", "Kebab")
HLASY_SOUBOR = Path(__file__).with_name("hlasy.json")


def nacist_hlasy():
    hlasy = {jidlo: 0 for jidlo in MOZNA_JIDLA}
    if HLASY_SOUBOR.exists():
        with HLASY_SOUBOR.open(encoding="utf-8") as soubor:
            ulozene = json.load(soubor)
        for jidlo in MOZNA_JIDLA:
            hlasy[jidlo] = ulozene.get(jidlo, 0)
    return hlasy


def ulozit_hlasy(hlasy):
    with HLASY_SOUBOR.open("w", encoding="utf-8") as soubor:
        json.dump(hlasy, soubor, ensure_ascii=False, indent=2)


@app.route("/", methods=["GET", "POST"])
def index():
    jidlo = None
    error = None
    if request.method == "POST":
        vyber = request.form.get("jidlo")
        if vyber in MOZNA_JIDLA:
            hlasy = nacist_hlasy()
            hlasy[vyber] += 1
            ulozit_hlasy(hlasy)
            jidlo = vyber
        elif not vyber:
            error = "Vyberte prosím jedno jídlo!"
        else:
            error = "Vyberte prosím platné jídlo!"
    return render_template("index.html", jidlo=jidlo, error=error)


@app.route("/vyhodnoceni", methods=["GET"])
def vyhodnoceni():
    hlasy = nacist_hlasy()
    celkem = sum(hlasy.values())
    return render_template("vyhodnoceni.html", hlasy=hlasy, celkem=celkem)


if __name__ == "__main__":
    app.run(debug=True)
