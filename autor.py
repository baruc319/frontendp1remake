class Autor:

    def __init__(self, id_autor, autor, img_autor):
        self.__id = id_autor
        self.__autor = autor
        self.__img_autor = img_autor

    def get_id_autor(self):
        return self.__id
    
    def get_autor(self):
        return self.__autor
    
    def get_img_autor(self):
        return self.__img_autor