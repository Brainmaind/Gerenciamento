from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route()
def info():
    return render_template('Templates/info.html')
    #nome = request.form['username']
    #idade = request.form['idade']
    #email = request.form['email']
    #ef = pd.DataFrame({'Nome': [nome],'Idade': [idade], 'Email':[email]})
    #ef.to_excel('Gerenciamento\PYTHON\Gerenciamento.xlsx', index=False)
    #print(meno)


if __name__ == '__main__':
    app.run(debug=True)

print(ef)