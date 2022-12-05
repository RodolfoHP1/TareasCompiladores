from antlr.coolListener import coolListener
from antlr.coolParser import coolParser
from util.asm import *
from util.structure import allClasses, lookupClass

"""
Los tipos quedarán así:
object 0
IO 1
Int 2
String 3
Boolean 4"""


class Literales(coolListener):
    def __init__(self):
        self.idx = 0
        self.result = ""

    def enterInt(self, ctx: coolParser.IntContext):
        self.result += cTplInt.substitute(idx=self.idx, tag=2, value=ctx.getText())
        ctx.constantIdx = self.idx
        self.idx = self.idx + 1

    def enterStr(self, ctx: coolParser.StrContext):
        strValue = ctx.getText()[1:-1]
        self.result += cTplInt.substitute(idx=self.idx, tag=2, value=len(strValue()))
        self.idx = self.idx + 1

        self.result += cTplStr.substitute(idx=self.idx, tag=3, size=4 + (len(strValue()) + 1) % 4,
                                          sizeIdx=(self.idx - 1), value=strValue())
        ctx.constantIdx = self.idx
        self.idx = self.idx + 1


class CodeGen():
    def __init__(self, walker, tree):
        self.result = ""
        self.tree = tree
        self.walker = walker
        self.idx = 0

    def generar(self):
        self.segDatos()
        self.segTexto()

    def segDatos(self):
        literales = Literales()
        self.walker.walk(literales, self.tree)

        # nombre de todas las clases, #direccion de objetos modelo como template, itera sobre lista de clases y el init, #itera sobre las clases y después por cada nombre de metodos que hay en la clase incluyendo herencia, #itera sobre cada objeto y cada
        self.result = literales.result + \
                      self.tablaNombres(literales.idx) + \
                      self.tablaModelosConstructores() + \
                      self.tablaMetodos() + \
                      self.objetosModelos()

    def tablaNombres(self, idx):
        r = "class_nameTab:\n"
        for k in allClasses().values():
            self.result += cTplInt.substitute(idx=idx, tag=2, value=len(k.name))
            idx = idx + 1

            self.result += cTplStr.substitute(idx=idx, tag=3, size=4 + (len(k.name) + 1) % 4,
                                              sizeIdx=(idx - 1), value=k.name)
            r += "    .word str_const{}\n".format(idx)
            idx = idx + 1
        return r

    def tablaModelosConstructores(self):

        r = "class_objTab:\n"
        for k in allClasses().values():
            r += k.name + "_protObj:\n"
            r += "  .word {}.{}\n".format(k.name, k)
            r += k.name + "_init:\n"
            r += "  .word {}.{}\n".format(k.name, k)
        return r

    def tablaMetodos(self):
        r = ""
        for k in allClasses().values():
            r += k.name + "_dispTab:\n"
            for k1 in k.methods:
                # Indice y Valores, se itera en cada método y clase
                r += "    .word {}.{}\n".format(k.name, k1)
            k = lookupClass(k.inherits)
        return r

    def objetosModelos(self):
        r = "_protObj:\n"
        idx = 0
        for k in allClasses().values():
            if k.name != "Main":
                r += k.substitute(name="{}_protObj".format(k.name), tag=idx, size=3 + len(k.attributes),
                                  name_dispTab="{}_dispTab".format(k.name))
            # Se imprimen y cambia el nombre dentro del if
            r += "    .word 0\n"
        return r

    def segTexto(self):
        pass

