class Artigo:

    def __init__(self, id, palestrante, tema, img, data, noticia):
        self.__id = id
        self.__palestrante = palestrante
        self.__tema = tema
        self.__img = img
        self.__data = data
        self.__noticia = noticia

    def get_id(self):
        return self.__id
    
    def get_palestrante(self):
        return self.__palestrante
    
    def get_tema(self):
        return self.__tema
    
    def get_img(self):
        return self.__img    
    
    def get_data(self):
        return self.__data
    
    def get_noticia(self):
        return self.__noticia
    

