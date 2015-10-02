from ast.nodes import *
from utils.visitor import *


class Binder(Visitor):
    """The binder takes care of linking identifier uses to its declaration."""

    self.scopes = []

    def __init__(self):
        # Push an initial scope for top-level declarations
        self.push_new_scope()

    def push_new_scope(self):
        """Push a new scope on the scopes stack."""
        self.scopes.append({})

    def pop_scope(self):
        """Pop a scope from the scopes stack."""
        del self.scopes[-1]

    def current_scope(self):
        """Return the current scope."""
        return self.scopes[-1]

    def lookup(self, name):
        """Return the declaration associated with a name, looking
        into the closest scope first. If no declaration is found,
        raise an exception."""
        for scope in reversed(scopes):
            if name in scope:
                return scope[name]
        else:
            return None
