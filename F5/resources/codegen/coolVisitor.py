# Generated from C:/Users/rodol/Desktop/tareasCompiladores/tareas/F5/semantic3/antlr\cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete generic visitor for a parse tree produced by coolParser.

class coolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by coolParser#program.
    def visitProgram(self, ctx:coolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#klass.
    def visitKlass(self, ctx:coolParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#method.
    def visitMethod(self, ctx:coolParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#attribute.
    def visitAttribute(self, ctx:coolParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#formal.
    def visitFormal(self, ctx:coolParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#add.
    def visitAdd(self, ctx:coolParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#new.
    def visitNew(self, ctx:coolParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#sub.
    def visitSub(self, ctx:coolParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#mul.
    def visitMul(self, ctx:coolParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#pri.
    def visitPri(self, ctx:coolParser.PriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#isvoid.
    def visitIsvoid(self, ctx:coolParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#callobj.
    def visitCallobj(self, ctx:coolParser.CallobjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#less.
    def visitLess(self, ctx:coolParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#while.
    def visitWhile(self, ctx:coolParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#eq.
    def visitEq(self, ctx:coolParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#call.
    def visitCall(self, ctx:coolParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#div.
    def visitDiv(self, ctx:coolParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#sequence.
    def visitSequence(self, ctx:coolParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#neg.
    def visitNeg(self, ctx:coolParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#not.
    def visitNot(self, ctx:coolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#lesseq.
    def visitLesseq(self, ctx:coolParser.LesseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#callstat.
    def visitCallstat(self, ctx:coolParser.CallstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#let.
    def visitLet(self, ctx:coolParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#if.
    def visitIf(self, ctx:coolParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#case.
    def visitCase(self, ctx:coolParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#assign.
    def visitAssign(self, ctx:coolParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#case_stat.
    def visitCase_stat(self, ctx:coolParser.Case_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#let_decl.
    def visitLet_decl(self, ctx:coolParser.Let_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#parens.
    def visitParens(self, ctx:coolParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#var.
    def visitVar(self, ctx:coolParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#int.
    def visitInt(self, ctx:coolParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#str.
    def visitStr(self, ctx:coolParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#bool.
    def visitBool(self, ctx:coolParser.BoolContext):
        return self.visitChildren(ctx)



del coolParser