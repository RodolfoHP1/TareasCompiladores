# En esta tarea comenzaremos a trabajar con el API de ANTLR para Python3. Toma como modelo el ejemplo de HTML.

# 1. Descarga la gramática de Java del repositorio público de ANTLR, son dos archivos y guárdalos en el
#    directorio antlr
#    https://github.com/antlr/grammars-v4
# 2. Configura la generación de código.
# 3. Prueba un programa sencillo de Java usando el ANTLR preview.

# 4. Resuelve las siguientes tareas:
#     1. Imprimir los nombres de todas las clases
#     2. Imprimir los nombres y tipos de todos los métodos
#     3. Imprimir todos los strings

# Puedes hacer 1 solo listener e ir guardando en una lista lo que vayas encontrando, para al final imprimirlo,
# o bien hacer 3 listeners y mandarlos llamar uno tras otro con el objeto walker.
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from gen.JavaParserListener import JavaParserListener

import sys


class TreePrinter(JavaParserListener):
    #     1. Imprimir los nombres de todas las clases
    def enterClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        print('Nombres de las clases')
        if ctx.identifier():
            print(ctx.identifier().getText())
    #     2. Imprimir los nombres y tipos de todos los métodos
    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        print('Nombres y tipos de los métodos')
        if ctx.identifier():
            print(ctx.identifier().getText())
            print('///')
            print(ctx.typeTypeOrVoid().getText())
    #     3. Imprimir todos los strings
    def enterLiteral(self, ctx: JavaParser.LiteralContext):
        print('Strings')
        if ctx.STRING_LITERAL():
            print(ctx.STRING_LITERAL().getText())


def main(argv):
    parser = JavaParser(CommonTokenStream(JavaLexer(FileStream("test.java"))))
    tree = parser.compilationUnit()

    print(tree)

    walker = ParseTreeWalker()
    walker.walk(TreePrinter(), tree)


if __name__ == '__main__':
    main("test.java")

