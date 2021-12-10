from flask import Flask, render_template, request
import numpy
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template("index.html")
@app.route('/result',methods=['POST','GET'])
def getResult():
    firstresponse = request.form.getlist('first')
    secondresponse = request.form.getlist('Second')
    listResponse = [firstresponse, secondresponse]
    listCorrect = ['Delhi','1947']
    marks = numpy.intersect1d(listResponse, listCorrect)
    return render_template("result.html", first = firstresponse, second = secondresponse, mark = len(marks))
if __name__=='__main__':
    app.run(debug=True)