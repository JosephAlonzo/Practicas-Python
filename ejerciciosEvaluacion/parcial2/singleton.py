class SoyUnico(object):

    class __SoyUnico:
        def __init__(self):
            self.nombre = None

        def __str__(self):
            return 'self' + ' ' + self.nombre

    instance = None

    def __new__(cls):
        if not SoyUnico.instance:
            SoyUnico.instance = SoyUnico.__SoyUnico()
        return SoyUnico.instance

    def __getattr__(self, texto):
        return getattr(self.instance, texto)

    def __setattr__(self, texto, valor):
        return setattr(self.instance, texto, valor)


ricardo = SoyUnico()
ricardo.nombre = "Ricardo Moya"
print(ricardo)
ramon = SoyUnico()
ramon.nombre = "Ramón Invarato"
print(ramon)
print(ricardo)
print(ramon)