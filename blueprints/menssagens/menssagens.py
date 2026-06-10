from flask import Blueprint, render_template

menssagens_bp = Blueprint('menssagens', __name__, template_folder='templates', 
static_folder='static', static_url_path='/menssagens/static')

@menssagens_bp.route('/ola')
def ola():
  return render_template('ola.html')

@menssagens_bp.route('/oi')
def oi():
  return 'Oi'