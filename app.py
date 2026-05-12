from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET"])
def page():
	

    
    
    return render_template("page.html")


if __name__=="__main__":
	app.run(debug=True)