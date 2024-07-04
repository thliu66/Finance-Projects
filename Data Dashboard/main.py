import pandas as pd
from flask import Flask, render_template, request, redirect, session


df = pd.read_csv("constituents-financials.csv")
sectors = list(df['Sector'].unique())

app = Flask(__name__)
# app.config["SERVER_NAME"] = "www.snp500dashboard.com:5000"

@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/Sector')
def Show_Sectors():
   return sectors


@app.route('/EBITDA', methods=['GET'])
def Show_EBITDA_of_Sector():
    sector = request.args['Sector']
    print(sector)
    if sector in sectors:
        res = df[df['Sector'] == sector]['EBITDA']
        return list(res)
    else:
        return f'<h1>Invalid Sector: {sector}</h1>'

if __name__ == '__main__':
   app.run(debug=True)

