from flask import Flask, jsonify, request, abort

app = Flask(__name__)

data = [{
    "codigo" : 123,
    "identificacion": "02938219391",
    "nombres" : "Ariel Sebastian",
    "apellidos" : "Idrovo Pacheco",
    "telefono" : "0984612392",
    "direccion" : "Ricaurte",
    "perfilCompra" : 2,
    "valorCompra" : 568.90
}]

@app.route('/persona', methods=['GET'])
def listarpersonas():
    if(request.method == 'GET'):
        return jsonify(data)
     
@app.route('/persona', methods=['POST'])
def addpersona():
    if(request.method == 'POST') and (request.headers.get('Content-Type')=='application/json'):
        person = request.json
        data.append(person)
        return "OK"
    else:
        abort(440, "No Valido")
    

if __name__=='__main__':
    app.run(debug=True)
