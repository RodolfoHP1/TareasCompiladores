from util.exceptions import *
from antlr.coolListener import coolListener
from antlr.coolParser import coolParser
from util.structure import Klass, Method, lookupClass, SymbolTableWithScopes



class SemanticListener(coolListener):
    def __init__(self):
        self.main = False

    def exitAttribute(self, ctx: coolParser.AttributeContext):
        #test_anattributenamedself
        if ctx.ID().getText() == 'self':
            raise BadAttributeName()

        #test_assignmentnoconform

    def enterKlass(self, ctx: coolParser.KlassContext):

        #test_nomain
        if ctx.TYPE(0).getText() == 'Main':
            self.main = True

        #test_badredefineint. test_redefinedobject, test_selftyperedeclared
        if ctx.TYPE(0).getText() in ['Int', 'String', 'Bool', 'SELF_TYPE', 'Object']:
            raise BadClassName()

        #test_inheritsbool, test_inheritsselftype, test_inheritsstring
        if not ctx.TYPE(1) is None and ctx.TYPE(1).getText() in ['Int', 'String', 'Bool', 'SELF_TYPE']:
            raise InvalidInheritance()

        #Crear esta clase, para este subárbol la voy a guardar en self.klass
        if ctx.TYPE(1) is None:
            self.klass = Klass(ctx.TYPE(0).getText())
        else:
            self.klass = Klass(ctx.TYPE(0).getText(), ctx.TYPE(1).getText())

        #Crear el scope de variables, se asocia a la klass para buscar también en atributos
        self.scopes = SymbolTableWithScopes(self.klass)

    def enterMethod(self, ctx:coolParser.MethodContext):
        #Se buscan variables-parámteros
        self.scopes.openScope()
        method_name = ctx.ID().getText()
        method_already_defined = False
        try:
            # Metodo del profe
            method: Method = self.klass.lookupMethod(method_name)
            method_already_defined = True
        except KeyError:
            pass
        if method_already_defined:
            for x, y in zip(method.params, ctx.params):
                if method.params.dict[x].name != y.TYPE():
                    raise InvalidOverride
            if len(method.params) != len(ctx.params):
                raise InvalidOverride
        else:
            params = []
            for p in ctx.params:
                params.append( (p.ID().getText(), lookupClass(p.TYPE().getText())) )
            type_ = ctx.TYPE().getText()
            new_method = Method(type_, params)
            self.klass.addMethod(method_name, new_method)

    def exitMethod(self, ctx:coolParser.MethodContext):
        #Cierro el scope
        self.scopes.closeScope()

        #test_selftypebadreturn

    def enterFormal(self, ctx: coolParser.FormalContext):
        #test_selfinformalparameter
        if ctx.ID().getText() == 'self':
            raise BadVariableName()

        #test_selftypeparameterposition
        if ctx.TYPE().getText() == 'SELF_TYPE':
            raise BadClassName()

        #test_dupformals
        self.scopes[ctx.ID().getText()] = lookupClass(ctx.TYPE().getText())

    def enterLet(self, ctx:coolParser.LetContext):
        #Variables locales en el let
        self.scopes.openScope()

    def exitLet(self, ctx:coolParser.LetContext):
        #Ejemplo: let x:Int <-5, y:Int <- x in x + y;
        self.scopes.closeScope()

    def enterLet_decl(self, ctx: coolParser.Let_declContext):
        #test_letself
        if ctx.ID().getText() == 'self':
            raise BadVariableName()

        self.scopes[ctx.ID().getText()] = lookupClass(ctx.TYPE().getText())

    def exitLet_decl(self, ctx:coolParser.Let_declContext):
        #test_letbadinit
        pass

    def exitProgram(self, ctx: coolParser.ProgramContext):
        #test_nomain
        if not self.main:
            raise NoMain()

    def enterAttribute(self, ctx:coolParser.AttributeContext):
        #Se declara un atributo type: Klass
        attrName = ctx.ID().getText()
        attrType: Klass = lookupClass(ctx.TYPE().getText())
        self.klass.addAttribute(attrName, attrType)
        self.scopes[attrName] = attrType

    def enterAssign(self, ctx: coolParser.AssignContext):
        #test_selfassignment
        if ctx.ID().getText() == 'self':
            raise BadVariableName()

    # Base para el algoritmo bottom-up

    def exitAdd(self, ctx:coolParser.AddContext):
        #test_badarith
        pass

    def exitCall(self, ctx:coolParser.CallContext):
        #test_badmethodcallitself
        pass

    def exitCallobj(self, ctx:coolParser.CallobjContext):
        #test_baddispatch, test_badwhilebody, test_badargs1
        pass

    def exitCallstat(self, ctx:coolParser.CallstatContext):
        #test_badstaticdispatch, test_tricyatdispatch2
        pass

    def exitEq(self, ctx:coolParser.EqContext):
        #test_badequalitytest, test_badequalitytest2
        pass

    def exitWhile(self, ctx:coolParser.WhileContext):
        #test_badwhilecond
        pass

    def exitCase(self, ctx:coolParser.CaseContext):
        #test_caseidenticalbranch
        pass

    def exitVar(self, ctx:coolParser.VarContext):
        #test_outofscope
        try:
            ctx.type = self.scopes[ctx.ID().getText()]
        except KeyError:
            raise BadVariableName

    def exitNew(self, ctx:coolParser.NewContext):
        #test_returntypenoexist
        try:
            self.type = lookupClass(ctx.TYPE().getText())
        except KeyError:
            raise BadClassName


    # Base para el algoritmo bottom-up
    def enterInt(self, ctx:coolParser.IntContext):
        # el tipo representado con un objeto
        # lookupClass('Int'): regresa el objeto que representa ese tipo
        ctx.type = lookupClass('Int')

    def enterStr(self, ctx: coolParser.StrContext):
        ctx.type = lookupClass('String')

    def enterBool(self, ctx:coolParser.BoolContext):
        ctx.type = lookupClass('Bool')

    def exitPri(self, ctx:coolParser.PriContext):
        # ¡Este paso es necesario porque en la gramática hay una regla que consolida todas las literales!
        # Es necesario para darles la misma precedencia
        # Descomentar la siguiente línea una vez que los nodos de la regla primary ya tengan tipo
        # ctx.type = ctx.primary().type
        ctx.type = ctx.primary().type

    def enterVar(self, ctx:coolParser.VarContext):
        try:
            ctx.type = self.scopes[ctx.ID().getText()]
        except KeyError:
            raise BadVariableName


    def exitAssign(self, ctx:coolParser.AssignContext):
        try:
            klassType: Klass = self.scopes[ctx.ID().getText()]
            exprType = lookupClass(ctx.expr().getText().replace("new", ""))
            if not klassType.conforms(exprType):
                raise BadType
        except KeyError:
            raise


    def exitIf(self, ctx:coolParser.IfContext):
        #test_lubtest
        pass


    def exitKlass(self, ctx: coolParser.KlassContext):
        # print(ctx.TYPE())
        pass