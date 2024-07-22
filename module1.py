def tanishtir(ism: str):
    print(f"Salom {ism.capitalize()}")


class Validate_Product:

    @staticmethod
    def check_title(check_title):
        if type(check_title) == str and len(check_title) >= 5:
            return True
        else:
            raise ValueError("5 tadan kam bo'lmagan satir kutilmoqda ")

    @staticmethod
    def check_rating(check_rating):
        if type(check_rating) == int or type(check_rating) == float and (check_rating > 0):
            return True
        else:
            raise ValueError


    
