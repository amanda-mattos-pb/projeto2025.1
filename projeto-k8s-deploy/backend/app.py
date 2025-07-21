from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Mensagem
import os

app = Flask(__name__)
CORS(app)

# Configuração do banco via variáveis de ambiente
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'mensagensdb')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def cria_tabelas():
    db.create_all()

@app.route('/api/mensagens', methods=['GET'])
def listar_mensagens():
    mensagens = Mensagem.query.all()
    return jsonify([{'id': m.id, 'texto': m.texto} for m in mensagens])

@app.route('/api/mensagens', methods=['POST'])
def adicionar_mensagem():
    dados = request.get_json()
    nova = Mensagem(texto=dados['texto'])
    db.session.add(nova)
    db.session.commit()
    return jsonify({'id': nova.id, 'texto': nova.texto}), 201

#@app.route("/health")
#def health():
#    return "OK", 200

if __name__ == '__main__':
    FLASK_HOST = os.getenv('API_HOST', '0.0.0.0')#ver o que seria esse ip
    FLASK_PORT = int(os.getenv('API_PORT', '5000'))#verqual seria a porta
    app.run(host=FLASK_HOST, port=FLASK_PORT)
