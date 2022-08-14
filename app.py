from flask import Flask, render_template, request
from majorLanguages import LanguageData
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/result', methods = ["POST", "GET"])
def dataResult():
    if request.method == "POST":
        usrname = request.form.get("username")
        data, total = LanguageData(usrname)
        if len(data) > 0 :
            return render_template("result.html",
                                    data = data,
                                    total = total,
                                    username = usrname
                                    )

        else :
            return render_template("notfound.html")

if __name__ == '__main__':
   app.run(debug = True)