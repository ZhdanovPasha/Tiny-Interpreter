import sys
from LanguageVisitor import LanguageVisitor
from LanguageParser import LanguageParser


class MyVisitor(LanguageVisitor):

    def __init__(self):
        self.memory = {}
        self.line_counts = 1

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        print('{} = {}'.format(name, value))
        self.line_counts += 1
        return value

    def visitBlank(self, ctx):
        self.line_counts += 1
        return self.visitChildren(ctx)

    def visitComparatorExpr(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == LanguageParser.GT:
            return left > right
        if ctx.op.type == LanguageParser.GE:
            return left >= right
        if ctx.op.type == LanguageParser.LT:
            return left < right
        if ctx.op.type == LanguageParser.LE:
            return left <= right
        if ctx.op.type == LanguageParser.EQ:
            return left == right
        if ctx.op.type == LanguageParser.NE:
            return left != right

    def visitUnaryMinus(self, ctx):
        value = int(self.visit(ctx.expr()))
        return -value

    def visitNotExpr(self, ctx):
        value = bool(self.visit(ctx.expr()))
        return not value

    def visitBoolExpr(self, ctx):
        return str(ctx.BOOL()) == 'TRUE'

    def visitBinaryExpr(self, ctx):
        left = bool(self.visit(ctx.expr(0)))
        right = bool(self.visit(ctx.expr(1)))
        if ctx.op.type == LanguageParser.AND:
            return left and right
        else:
            return left or right

    def visitNum(self, ctx):
        num = ctx.NUM().getText()
        return num

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        else:
            print('unknown variable {} in line {}'.format(name, self.line_counts))
            sys.exit(1)

    def visitMulDiv(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == LanguageParser.MUL:
            return left * right
        if right == 0:
            print('zero division in line {}'.format(self.line_counts))
            sys.exit(1)
        return left // right

    def visitAddSub(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == LanguageParser.ADD:
            return left + right
        return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
