
# Notebook Checker

A package to check notebook files for the use of globals inside functions. The
checker parses each cell's AST as it is run, and injects code into the AST to
ensure that when a function is called, that any free variables are only of the
type callable, type or module. If a function tries to access any other type of
variable, i.e. stored data, outside of the function's scope, then the checker
logs an error message, informing the user.

