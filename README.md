# Aprendendo-Flask
Repositório feito para aprender o Flask

## 1° Instalar um ambiente virtual, ativar ele e instalar o Flask

### Ambiente virtual > python -m venv .venv
#### Ativando: ".\.venv\Scripts\activate"

### Como instalar o flask?
#### pip install flask


## Como criar uma rota no Flask?
### Exemplo:
@app.route('/')
def index():
  return 'Olá, mundo!'

## Usando o template do Flask?
importando do proprio flask o render_template

Obs: Tem que ser criadouma pasta com o nome templates, pois ele busca os arquivos 
direto nessa pasta
Exemplo de como chamar o arquivo:
@app.route('/')
def index():
  return render_template('exemplo_template.html')

Enviando com parametro:
@app.route('/')
def index():
  return render_template('exemplo_template.html', nome="Gabriel")

Criando uma condição no html:
'<p>Olá {{nome|default('sem nome')}}</p>'
Caso a variavel nome não seja informada no render_template, ele vai renderizar na tela
a informação 'sem nome'

Passando uma imagem para o html:
Temos que criar a pasta chamada static e dentro dela vamos colocar as imagens.
'<img src="{{url_for('static', filename='cachorro.jpg')}}" alt="">'
Passamos o endereço da imagem dessa forma