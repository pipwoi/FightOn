import re


class LexicalAnalyzer:
    # Token row
    lin_num = 1
    def tokenize(self, code):
        rules = [
            # FightOn
            ('CLOCK', r'clock'),
            ('HOVER', r'hover'),
            ('ROPE', r'rope'),
            ('COIN', r'coin'),
            ('PARTY', r'party'),
            ('QUEST', r'quest'),
            ('JOB', r'job'),
            ('LIST', r'listen'),
            ('SAY', r'say'),
            ('TOWER', r'tower'),

            ('OR', r'\|\|'),
            ('AND', r'&&'),
            ('NOT', r'NOT'),
            ('START', r'START'),
            ('END', r'END'),
            ('WHILE', r'while'),
            ('BREAK', r'break'),
            ('CASE', r'case'),
            ('CONTINUE', r'continue'),
            ('DEFAULT', r'default'),
            ('DO', r'do'),
            ('ELIF', r'elif'),
            ('ELSE', r'else'),
            ('FOR', r'for'),
            ('IF', r'if'),
            ('SWITCH', r'switch'),

            ('MAIN', r'main'),          # while
            ('READ', r'read'),          # read
            ('PRINT', r'print'),        # print
            ('LBRACKET', r'\('),        # (
            ('RBRACKET', r'\)'),        # )
            ('LBRACE', r'\{'),          # {
            ('RBRACE', r'\}'),          # }
            ('COMMA', r','),            # ,
            ('PCOMMA', r';'),           # ;
            ('EQ', r'=='),              # ==
            ('NE', r'!='),              # !=
            ('LE', r'<='),              # <=
            ('GE', r'>='),              # &&
            ('ATTR', r'\='),            # =
            ('LT', r'<'),               # <
            ('GT', r'>'),               # >
            ('PLUS', r'\+'),            # +
            ('MINUS', r'-'),            # -
            ('MULT', r'\*'),            # *
            ('DIV', r'\/'),             # /

            ('ID', r'[a-z]\w*'),        # IDENTIFIERS
            ('HOVER_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            ('CLOCK_CONST', r'\d(\d)*'),            # INT
            ('NEWLINE', r'\n'),         # NEW LINE
            ('SKIP', r'[ \t]+'),        # SPACE and TABS
            ('MISMATCH', r'.'),         # ANOTHER CHARACTER
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        # Lists of output for the program
        token = []
        lexeme = []
        row = []
        column = []
        lexerror = []
        tab_row = []

        try:


        # It analyzes the code to find the lexemes and their respective Tokens

            for m in re.finditer(tokens_join, code):
                token_type = m.lastgroup
                token_lexeme = m.group(token_type)

                if token_type == 'NEWLINE':
                    lin_start = m.end()
                    self.lin_num += 1
                elif token_type == 'SKIP':
                    continue
                elif token_type == 'MISMATCH':
                    raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
                else:
                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token
                    tab_row.append('{:>8} {:>16} {:>8}, {:>3}\n'
                                         .format(token_lexeme, token_type,  self.lin_num, col))

        except: lexerror.append('\nLexical Error on Line {:>3}, {:>3}'.format(self.lin_num, col))


        return token, lexeme, row, column, lexerror, tab_row

