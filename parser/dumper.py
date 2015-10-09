from ast.nodes import *
from utils.visitor import *


class Dumper(Visitor):

    def __init__(self, semantics=False):
        """Initialize a new Dumper visitor. If semantics is True,
        additional information will be printed along with declarations
        and identifiers."""
        self.semantics = semantics

    @visitor(None)
    def visit(self, node):
        raise Exception("unable to dump %s" % node)

    @visitor(IntegerLiteral)
    def visit(self, i):
        return str(i.intValue)

    @visitor(BinaryOperator)
    def visit(self, binop):
        # Always use parentheses to reflect grouping and associativity,
        # even if they may be superfluous.
        return "(%s %s %s)" % \
               (binop.left.accept(self), binop.op, binop.right.accept(self))

    @visitor(Type)
    def visit(self, type):
        return "%s" % type.typename

    @visitor(Let)
    def visit(self, let):
        ret_str = "let "
        for decl in let.decls:
            ret_str += decl.accept(self)
        ret_str += "in "
        for exp in let.exps:
            ret_str += exp.accept(self)
        ret_str += " end"
        return ret_str
    
    @visitor(Identifier)
    def visit(self, id):
        if self.semantics:
            diff = id.depth - id.decl.depth
            scope_diff = "{%d}" % diff if diff else ''
        else:
            scope_diff = ''
        return '%s%s' % (id.name, scope_diff)

    @visitor(IfThenElse)
    def visit(self, ite):
        return "if %s then %s else %s" % (ite.condition.accept(self),
                                           ite.then_part.accept(self),
                                           ite.else_part.accept(self))

    @visitor(VarDecl)
    def visit(self, vdecl):
        if (vdecl.type == None):
            return "var %s := %s" % (vdecl.name, vdecl.exp.accept(self))
        else:
            return "var %s : %s %s" % (vdecl.name, vdecl.type.accept(self), vdecl.exp)
