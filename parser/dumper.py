from ast.nodes import *
from utils.visitor import *


class Dumper(Visitor):

    def __init__(self, semantics):
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
 
 
    @visitor(Let)
    def visit(self, let):
        ret_str = "let "
        if (len(let.decls) != 0):
            for decl in let.decls:
                ret_str += decl.accept(self) + " "
        ret_str += "in "
        for exp in let.exps:
            ret_str += exp.accept(self)
            if (exp != let.exps[-1]):
                ret_str += ", "
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


    @visitor(Type)
    def visit(self, type):
        return "%s" % type.typename


    @visitor(VarDecl)
    def visit(self, vdecl):
        if (vdecl.type == None):
            return "var %s := %s" % (vdecl.name, vdecl.exp.accept(self))
        elif (vdecl.exp == None):
            return "var %s : %s" % (vdecl.name, vdecl.type.accept(self))
        else:
            return "var %s : %s :=  %s " % (vdecl.name, vdecl.type.accept(self),
                                                   vdecl.exp.accept(self))


    @visitor(FunDecl)
    def visit(self, fdecl):
        ret_str = "function %s(" % fdecl.name
        if (len(fdecl.args) == 1):
            for arg in fdecl.args:
                ret_str += "%s : %s" % (arg.name, arg.type.accept(self))
        elif (len(fdecl.args) != 0):
            for arg in fdecl.args:
                ret_str += "%s : %s" % (arg.name, arg.type.accept(self))
                if (arg != fdecl.args[-1]):
                    ret_str += ", "
        ret_str += ") "
        if (fdecl.type != None):
            ret_str += ": " + fdecl.type.accept(self) + " "
        ret_str += "= "
        ret_str += fdecl.exp.accept(self)
        return ret_str

    @visitor(FunCall)
    def visit(self, fcall):
        ret_str = fcall.identifier.accept(self) + "("
        if (len(fcall.params) == 1):
            for param in fcall.params:
                ret_str += "%s : %s" % (param.name, param.type.accept(self))
        elif (len(fcall.params) != 0):
            for param in fcall.params:
                ret_str += "%s : %s" % (param.name, param.type.accept(self))
                if (param != fcall.params[-1]):
                    ret_str += ", "
        ret_str += ") "
        return ret_str
