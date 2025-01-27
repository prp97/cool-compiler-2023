keywords = {
    'class': 'CLASS',
    'else': 'ELSE',
    'false': 'FALSE',
    'fi': 'FI',
    'if': 'IF',
    'in': 'IN',
    'inherits': 'INHERITS',
    'isvoid': 'ISVOID',
    'let': 'LET',
    'loop': 'LOOP',
    'pool': 'POOL',
    'then': 'THEN',
    'while': 'WHILE',
    'case': 'CASE',
    'esac': 'ESAC',
    'new': 'NEW',
    'of': 'OF',
    'not': 'NOT',
    'true': 'TRUE',
}


tokens = [
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'AT',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'STAR',
    'DIV',
    'ARROW',
    'EQUAL',
    'LESSEQ',
    'LESS',
    'COMPL',
    'INT',
    'ID',
    'TYPE',
    'STRING',
    'COMMENT_LINE'
]

tokens = tokens + list(keywords.values())

literals = [
    '+',
    '-',
    '*',
    '/',
    '~',
    '=',
    '<',
    ':',
    '{',
    '}',
    '@',
    ',',
    '.',
    '(',
    ')',
    ';',
]
