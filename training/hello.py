def visit_If(self, node):
    vars.function_def += 'if ('
    vars.is_if = True  # visit_Call inserts a ';' if NOT set to True.
    self.visit(node.test)
    vars.is_if = False
    vars.function_def += ') {\n'
    for statement in node.body:
        self.visit(statement)
    vars.function_def += '} '
    if (len(node.orelse) > 0):
        for i in range(0, len(node.orelse)):
            statement = node.orelse[i]
            if (type(statement) == ast.If):
                vars.function_def += 'else '
                self.visit(statement)
                if (i == len(node.orelse) - 1):
                    vars.function_def += '\n'

            else:
                vars.function_def += 'else {\n'
                self.visit(statement)
                vars.function_def += '}\n'
    print(strings.NODE_IF + str(type(node)) + ' ' + str(vars.brackets) + ' ' + str(node.orelse) + ' ' + str(
        vars.has_else_part) + ' ' + str(node.body))