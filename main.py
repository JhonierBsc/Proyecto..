
from flask import Flask
from rutas import init_app


app = Flask(__name__)
init_app(app)

print('iniciando...')
print('35%')
print('63%')
print('84%')
print('97%')
print('98%')
print('99%')
print('100%')
print('Cargado!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=11795)
