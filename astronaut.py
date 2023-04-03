from flask import Flask, url_for, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('astronaut_data.html')


@app.route("/question")

def render_question():
    ct = 0
    if 'yearfind' not in request.args:
        return render_template('astronaut_data2.html')
    else:
        with open('astronauts.json') as astro_data:
            data = json.load(astro_data)
        year = request.args["yearfind"]
        for d1 in data:
            if str(d1["Profile"]["Selection"]["Year"]) == year:
                print(d1)
                ct += 1
        return render_template('astronaut_data2.html', astronaut = ct)
        
        
@app.route("/statistics")
def render_statistics():
    return render_template('astronaut_data3.html')

if __name__=="__main__":
    app.run(debug=False)