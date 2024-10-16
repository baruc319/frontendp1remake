from flask import Flask, render_template
from artigo import Artigo
from autor import Autor
from categoria import Categoria
from comentario import Comentario

app = Flask(__name__)


artigo_list = [
    Artigo(1, 'Colunista1', 'Tecnologia', '1.jpg', '1/1/2001', 'Temas sobre tecnologia importantes sobre Impacto da inteligência artificial no mercado de trabalho. A importância da privacidade na era digital. O papel da internet na disseminação de informações. Ética no desenvolvimento de biotecnologia. Inclusão digital e desigualdade social. A influência das redes sociais na vida moderna.'),
    Artigo(2, 'Colunista2', 'Ciência ', '2.jpg', '2/2/2002', 'Ciência é um sistema que adquire conhecimento baseado em um método, conhecido como método científico. É construída com atitudes racionais, visando à obtenção de conhecimento específico, com base na observação, na realização de métodos experimentais e no desenvolvimento de teorias e leis.'),
    Artigo(3, 'Colunista3', 'Energia ', '3.jpg', '3/3/2003', 'As energias renováveis que não causam poluição pela emissão de substâncias são chamadas de energias limpas e incluem: solar, eólica, geotérmica, maremotriz e hidráulica. Um modo de geração de energia mecânica ou elétrica é considerado limpo se não liberar substâncias poluentes para o meio ambiente.'),
    Artigo(4, 'Colunista4', 'Sustentabilidade ', '4.jpg', '4/4/2004', 'É o desenvolvimento que não esgota os recursos para o futuro. Essa definição surgiu na Comissão Mundial sobre Meio Ambiente e Desenvolvimento, criada pelas Nações Unidas para discutir e propor meios de harmonizar dois objetivos: o desenvolvimento econômico e a conservação ambiental.'),
    Artigo(5, 'Colunista5', 'Ambiente', '5.jpg', '5/5/2005', 'O meio ambiente diz respeito ao conjunto de elementos e processos biológicos, químicos e físicos responsáveis pela vida no planeta Terra. Compreende os seres humanos e as transformações que eles impõem aos espaços naturais. É composto pela biosfera, hidrosfera, atmosfera e litosfera.'),
]

autor_list = [
    Autor(1, 'Autor1', 'autor1.jpg'),    
    Autor(2, 'Autor2', 'autor2.jpg'),
    Autor(3, 'Autor3', 'autor3.jpg'),
    Autor(4, 'Autor4', 'autor4.jpg'),
    Autor(5, 'Autor5', 'autor5.jpg'),
]

categoria_list = [
    
    Categoria('Tecnologia'),    
    Categoria('Ciência'),
    Categoria('Energia'),
    Categoria('Sustentabilidade'),
    Categoria('Ambiente'),

]

@app.route("/")
def home():
    return render_template("home.html", artigo_list=artigo_list, autor_list=autor_list, categoria_list=categoria_list)

@app.route("/artigo/<int:id>")
def artigo(id):
    for artigo in artigo_list:
        if artigo.get_id() == id:
            return render_template("artigo.html", artigo=artigo, artigo_list=artigo_list, autor_list=autor_list, categoria_list=categoria_list)
    return '<h1>Ops!</h1>'

@app.route("/autor")
def autor():
    return render_template("autor.html", autor_list=autor_list)