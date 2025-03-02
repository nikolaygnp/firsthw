import requests
import json
from flask import Flask



def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    lengthlist = [8, 8, 8, 8, 40, 8, 8]
    keytxt = [key for key in valutes[0].keys()]
    fchar = '_'
    for k in range(7):
        text += f'<th>{str(keytxt[k]).center(lengthlist[k])}</th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        valuelist = list(valute.values())
        for v in range(7):
            text += f'<td>{str(valuelist[v]).ljust(lengthlist[v])}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
#    print(type(valutes[0].values()))
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()
