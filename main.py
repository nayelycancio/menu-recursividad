from flask import Flask, render_template
 
app = Flask(__name__)
 
menu = {
    "Inicio":{},
    "Oferta Educativa": {
        "Licenciaturas e Ingenierias": {
            "Ing. Sistemas Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
           },
            "Ing.Electronica": {
               "Plan de Estudios": {},
               "Programa":{}
           },
           "ing.Quimica":{
            "Plan de Estudios": {},
            "Programa":{}
           },
           "ing.Industrial":{
            "Plan de Estudios": {},
           }
        },
        "Posgrado":{

        }
    },
    "contacto": {}
}


@app.route("/")
def mostrar_menu_flask():
    return render_template("menu.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
 
