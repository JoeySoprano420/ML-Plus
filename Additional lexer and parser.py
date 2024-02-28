from ply import lex, yacc

# Lexer
tokens = (
    'IMPORT', 'FROM', 'IDENTIFIER', 'AS', 'CLASS', 'DEF', 'WITH', 'RETURN', 'IF', 'ELSE', 'FOR', 'IN', 'TRY', 'EXCEPT',
    'COLON', 'COMMA', 'LPAREN', 'RPAREN', 'NEWLINE', 'INDENT', 'DEDENT'
)

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_INDENT(t):
    r'    '
    return t

def t_DEDENT(t):
    r'    '
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
        'import': 'IMPORT',
        'from': 'FROM',
        'as': 'AS',
        'class': 'CLASS',
        'def': 'DEF',
        'with': 'WITH',
        'return': 'RETURN',
        'if': 'IF',
        'else': 'ELSE',
        'for': 'FOR',
        'in': 'IN',
        'try': 'TRY',
        'except': 'EXCEPT'
    }
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_statement(p):
    '''
    statement : import_statement
              | tri_polar_tool_function
              | mlplus_update
    '''

def p_import_statement(p):
    'import_statement : IMPORT IDENTIFIER FROM IDENTIFIER AS IDENTIFIER NEWLINE'
    # Define actions for import statements

def p_tri_polar_tool_function(p):
    'tri_polar_tool_function : DEF IDENTIFIER LPAREN IDENTIFIER RPAREN COLON NEWLINE INDENT tri_polar_tool_body DEDENT'
    # Define actions for tri_polar_tool function

def p_tri_polar_tool_body(p):
    '''
    tri_polar_tool_body : transformed_data ruby_logic go_lang_concurrent_task
                       | transformed_data ruby_logic go_lang_concurrent_task recognition_model
    '''

def p_mlplus_update(p):
    'mlplus_update : FROM concurrent.futures IMPORT ThreadPoolExecutor NEWLINE'
    # Define actions for mlplus updates

def p_error(p):
    print(f"Syntax error at line {p.lineno}")

parser = yacc.yacc()
