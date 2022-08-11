from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 57, number2 = 34)

@app.route('/mult')
def number():
    var1 = 888
    var2 = 111
    return render_template('body.html', num1 = var1, num2 = var2, multiplication = var1*var2)



if __name__ == '__main__':
    app.run(debug=True) # debug=True'dan sonra ", port=1000" gibi bir port tanımlayabiliriz. default olarak port:5000 dir.