from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")
@app.route("/")
def renderIndexPage():
    return render_template('index.html')
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return json.dumps(translator.translate(textToTranslate, 'en', 'fr'))  # returns a JSON string with the
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return json.dumps(translator.translate(textToTranslate, 'fr', 'en'))  # returns a JSON string with the      

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
