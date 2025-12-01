from flask import Flask, render_template,jsonify
import json
import pandas as pd

app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    dfDataset = pd.read_json("static/data/dataset.json")
    kecList =  sorted(dfDataset["Kecamatan"].unique())

    dfTrainVal = pd.read_json("static/data/trainvalloss.json")
    trainvals = dfTrainVal.to_dict(orient="records")

    dfMetrik = pd.read_json("static/data/metrik-model.json")
    metriks = dfMetrik.to_dict(orient="records")

    dfAktual = pd.read_json("static/data/actual-prediksi.json")
    aktuals = dfAktual.to_dict(orient="records")

    return render_template('index.html', kecs = kecList, trainvals = trainvals, metriks = metriks, aktuals = aktuals)

@app.route('/data')
def get_data():
    dfDataset = pd.read_json("static/data/dataset.json")
    kecList =  sorted(dfDataset["Kecamatan"].unique())

    dfTrainVal = pd.read_json("static/data/trainvalloss.json")
    trainvals = dfTrainVal.to_dict(orient="records")

    dfMetrik = pd.read_json("static/data/metrik-model.json")
    metriks = dfMetrik.to_dict(orient="records")

    dfAktual = pd.read_json("static/data/actual-prediksi.json")
    aktuals = dfAktual.to_dict(orient="records")

    return render_template('data.html', kecs = kecList, trainvals = trainvals, metriks = metriks, aktuals = aktuals)

@app.route('/data-aktual')
def get_data_aktual():
    dfDataset = pd.read_json("static/data/dataset.json")
    kecList =  sorted(dfDataset["Kecamatan"].unique())
    dataReturn = []
    dfAktual = pd.read_json("static/data/actual-prediksi.json")
    aktuals = dfAktual.to_dict(orient="records")

    for i, item in enumerate(aktuals):
        dataReturn.append({
            "Kecamatan": kecList[item["Index"]],
            "Aktual": item["Aktual"],
            "Prediksi": item["Prediksi"],
            "Selisih": item["Selisih"],
        })
    return jsonify(dataReturn)

@app.route('/data-cabai')
def get_data_cabai():
    # df = pd.read_excel("Datasett.xlsx")
    # df = df.where(pd.notnull(df), None)
    # return app.response_class(
    #     response=df.to_json(orient='records'),
    #     mimetype='application/json'
    # )
    with open('static/data/dataset.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
