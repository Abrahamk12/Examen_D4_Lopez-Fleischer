'''
UNIVERSIDAD DE SONORA
LOPEZ FLEISCHER URIEL ABRAHAM 
DESARROLLO 4
EXAMEN 2
'''
from flask import Flask, redirect, render_template, request
app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"

@app.route("/")
def index():
    if request.method == 'GET':
        msg = ''
        return render_template('index.html')
        

@app.route("/consumo")
@app.route("/consumo/")
def consumo():
    if request.method == 'GET':
        msg = ''
        return render_template('consumo.html', msg = msg)
    else:
        if request.method == 'POST':
            gasolina = request.form['name']

            calcular_MPG_a_Kml = request.form['MPG a Kml']
            calcular_MPG_a_l_100km = request.form['MPG a l/100km']
            calcular_Kml_a_MPGl = request.form['Kml a MPG']
            calcular_Kml_a_l_100lm = request.form['Kml a l/100lm']
            calcular_l_100km_a_MPG = request.form['l/100km a MPG']
            calcular_l_100km_a_Kml = request.form['l/100km a Kml']
            #'''
            if calcular_MPG_a_Kml == 'MPG a Kml':
                resultado = gasolina * 0.425144
                print("\nEsta mierda jalo\n")
                return render_template('new_user.html',resultado=resultado)
            if calcular_MPG_a_l_100km == 'MPG a l/100km':
                resultado =  235.215 / gasolina
                return render_template('new_user.html',resultado=resultado)
            if calcular_Kml_a_MPGl == 'Kml a MPG':
                resultado = gasolina * 2.352
                return render_template('new_user.html',resultado=resultado)
            if calcular_Kml_a_l_100lm == 'Kml a l/100lm':
                resultado = 100 / gasolina
                return render_template('new_user.html',resultado=resultado)
            if calcular_l_100km_a_MPG == 'l/100km a MPG':
                resultado = 235.215 / gasolina
                return render_template('new_user.html',resultado=resultado)
            if calcular_l_100km_a_Kml == 'l/100km a Kml':
                resultado = 100 / gasolina
                return render_template('new_user.html',resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)