# Generated from C:/Users/rodol/Desktop/tareasCompiladores/tareas/F5/semantic3/antlr\cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete listener for a parse tree produced by coolParser.
class coolListener(ParseTreeListener):

    # Enter a parse tree produced by coolParser#program.
    def enterProgram(self, ctx:coolParser.ProgramContext):
        pass

    # Exit a parse tree produced by coolParser#program.
    def exitProgram(self, ctx:coolParser.ProgramContext):
        pass


    # Enter a parse tree produced by coolParser#klass.
    def enterKlass(self, ctx:coolParser.KlassContext):
        pass

    # Exit a parse tree produced by coolParser#klass.
    def exitKlass(self, ctx:coolParser.KlassContext):
        pass


    # Enter a parse tree produced by coolParser#method.
    def enterMethod(self, ctx:coolParser.MethodContext):
        pass

    # Exit a parse tree produced by coolParser#method.
    def exitMethod(self, ctx:coolParser.MethodContext):
        pass


    # Enter a parse tree produced by coolParser#attribute.
    def enterAttribute(self, ctx:coolParser.AttributeContext):
        pass

    # Exit a parse tree produced by coolParser#attribute.
    def exitAttribute(self, ctx:coolParser.AttributeContext):
        pass


    # Enter a parse tree produced by coolParser#formal.
    def enterFormal(self, ctx:coolParser.FormalContext):
        pass

    # Exit a parse tree produced by coolParser#formal.
    def exitFormal(self, ctx:coolParser.FormalContext):
        pass


    # Enter a parse tree produced by coolParser#add.
    def enterAdd(self, ctx:coolParser.AddContext):
        pass

    # Exit a parse tree produced by coolParser#add.
    def exitAdd(self, ctx:coolParser.AddContext):
        pass


    # Enter a parse tree produced by coolParser#new.
    def enterNew(self, ctx:coolParser.NewContext):
        pass

    # Exit a parse tree produced by coolParser#new.
    def exitNew(self, ctx:coolParser.NewContext):
        pass


    # Enter a parse tree produced by coolParser#sub.
    def enterSub(self, ctx:coolParser.SubContext):
        pass

    # Exit a parse tree produced by coolParser#sub.
    def exitSub(self, ctx:coolParser.SubContext):
        pass


    # Enter a parse tree produced by coolParser#mul.
    def enterMul(self, ctx:coolParser.MulContext):
        pass

    # Exit a parse tree produced by coolParser#mul.
    def exitMul(self, ctx:coolParser.MulContext):
        pass


    # Enter a parse tree produced by coolParser#pri.
    def enterPri(self, ctx:coolParser.PriContext):
        pass

    # Exit a parse tree produced by coolParser#pri.
    def exitPri(self, ctx:coolParser.PriContext):
        pass


    # Enter a parse tree produced by coolParser#isvoid.
    def enterIsvoid(self, ctx:coolParser.IsvoidContext):
        pass

    # Exit a parse tree produced by coolParser#isvoid.
    def exitIsvoid(self, ctx:coolParser.IsvoidContext):
        pass


    # Enter a parse tree produced by coolParser#callobj.
    def enterCallobj(self, ctx:coolParser.CallobjContext):
        pass

    # Exit a parse tree produced by coolParser#callobj.
    def exitCallobj(self, ctx:coolParser.CallobjContext):
        pass


    # Enter a parse tree produced by coolParser#less.
    def enterLess(self, ctx:coolParser.LessContext):
        pass

    # Exit a parse tree produced by coolParser#less.
    def exitLess(self, ctx:coolParser.LessContext):
        pass


    # Enter a parse tree produced by coolParser#while.
    def enterWhile(self, ctx:coolParser.WhileContext):
        pass

    # Exit a parse tree produced by coolParser#while.
    def exitWhile(self, ctx:coolParser.WhileContext):
        pass


    # Enter a parse tree produced by coolParser#eq.
    def enterEq(self, ctx:coolParser.EqContext):
        pass

    # Exit a parse tree produced by coolParser#eq.
    def exitEq(self, ctx:coolParser.EqContext):
        pass


    # Enter a parse tree produced by coolParser#call.
    def enterCall(self, ctx:coolParser.CallContext):
        pass

    # Exit a parse tree produced by coolParser#call.
    def exitCall(self, ctx:coolParser.CallContext):
        pass


    # Enter a parse tree produced by coolParser#div.
    def enterDiv(self, ctx:coolParser.DivContext):
        pass

    # Exit a parse tree produced by coolParser#div.
    def exitDiv(self, ctx:coolParser.DivContext):
        pass


    # Enter a parse tree produced by coolParser#sequence.
    def enterSequence(self, ctx:coolParser.SequenceContext):
        pass

    # Exit a parse tree produced by coolParser#sequence.
    def exitSequence(self, ctx:coolParser.SequenceContext):
        pass


    # Enter a parse tree produced by coolParser#neg.
    def enterNeg(self, ctx:coolParser.NegContext):
        pass

    # Exit a parse tree produced by coolParser#neg.
    def exitNeg(self, ctx:coolParser.NegContext):
        pass


    # Enter a parse tree produced by coolParser#not.
    def enterNot(self, ctx:coolParser.NotContext):
        pass

    # Exit a parse tree produced by coolParser#not.
    def exitNot(self, ctx:coolParser.NotContext):
        pass


    # Enter a parse tree produced by coolParser#lesseq.
    def enterLesseq(self, ctx:coolParser.LesseqContext):
        pass

    # Exit a parse tree produced by coolParser#lesseq.
    def exitLesseq(self, ctx:coolParser.LesseqContext):
        pass


    # Enter a parse tree produced by coolParser#callstat.
    def enterCallstat(self, ctx:coolParser.CallstatContext):
        pass

    # Exit a parse tree produced by coolParser#callstat.
    def exitCallstat(self, ctx:coolParser.CallstatContext):
        pass


    # Enter a parse tree produced by coolParser#let.
    def enterLet(self, ctx:coolParser.LetContext):
        pass

    # Exit a parse tree produced by coolParser#let.
    def exitLet(self, ctx:coolParser.LetContext):
        pass


    # Enter a parse tree produced by coolParser#if.
    def enterIf(self, ctx:coolParser.IfContext):
        pass

    # Exit a parse tree produced by coolParser#if.
    def exitIf(self, ctx:coolParser.IfContext):
        pass


    # Enter a parse tree produced by coolParser#case.
    def enterCase(self, ctx:coolParser.CaseContext):
        pass

    # Exit a parse tree produced by coolParser#case.
    def exitCase(self, ctx:coolParser.CaseContext):
        pass


    # Enter a parse tree produced by coolParser#assign.
    def enterAssign(self, ctx:coolParser.AssignContext):
        pass

    # Exit a parse tree produced by coolParser#assign.
    def exitAssign(self, ctx:coolParser.AssignContext):
        pass


    # Enter a parse tree produced by coolParser#case_stat.
    def enterCase_stat(self, ctx:coolParser.Case_statContext):
        pass

    # Exit a parse tree produced by coolParser#case_stat.
    def exitCase_stat(self, ctx:coolParser.Case_statContext):
        pass


    # Enter a parse tree produced by coolParser#let_decl.
    def enterLet_decl(self, ctx:coolParser.Let_declContext):
        pass

    # Exit a parse tree produced by coolParser#let_decl.
    def exitLet_decl(self, ctx:coolParser.Let_declContext):
        pass


    # Enter a parse tree produced by coolParser#parens.
    def enterParens(self, ctx:coolParser.ParensContext):
        pass

    # Exit a parse tree produced by coolParser#parens.
    def exitParens(self, ctx:coolParser.ParensContext):
        pass


    # Enter a parse tree produced by coolParser#var.
    def enterVar(self, ctx:coolParser.VarContext):
        pass

    # Exit a parse tree produced by coolParser#var.
    def exitVar(self, ctx:coolParser.VarContext):
        pass


    # Enter a parse tree produced by coolParser#int.
    def enterInt(self, ctx:coolParser.IntContext):
        pass

    # Exit a parse tree produced by coolParser#int.
    def exitInt(self, ctx:coolParser.IntContext):
        pass


    # Enter a parse tree produced by coolParser#str.
    def enterStr(self, ctx:coolParser.StrContext):
        pass

    # Exit a parse tree produced by coolParser#str.
    def exitStr(self, ctx:coolParser.StrContext):
        pass


    # Enter a parse tree produced by coolParser#bool.
    def enterBool(self, ctx:coolParser.BoolContext):
        pass

    # Exit a parse tree produced by coolParser#bool.
    def exitBool(self, ctx:coolParser.BoolContext):
        pass



del coolParser