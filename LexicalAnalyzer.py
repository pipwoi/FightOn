import re


class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, code):
        rules = [
            # FightOn
            ('clock', r'clock'),
            ('hover', r'hover'),
            ('rope', r'rope'),
            ('coin', r'coin'),
            ('party', r'party'),
            ('quest', r'quest'),
            ('job', r'job'),
            ('listen', r'listen'),
            ('say', r'say'),
            ('tower', r'tower'),


            ('OR', r'\|\|'),
            ('AND', r'&&'),
            ('NOT', r'NOT'),
            ('START', r'START'),
            ('END', r'END'),
            ('while', r'while'),
            ('break', r'break'),
            ('case', r'case'),
            ('continue', r'continue'),
            ('default', r'default'),
            ('do', r'do'),
            ('elif', r'elif'),
            ('else', r'else'),
            ('for', r'for'),
            ('if', r'if'),
            ('switch', r'switch'),

            # ('', r''),

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
            ('ID', r'[a-z]\w*'),     # IDENTIFIERS
            ('HOVER_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            ('CLOCK_CONST', r'\d(\d)*'),          # INT
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

        try:
            print('\n<LEXEME>___________<TOKEN>______________<LINE> ')

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
                        print('{:>16} {:>16} {:>8}, {:>3}'.format(token_lexeme, token_type,  self.lin_num, col))

        except: print('\nLexical Error on Line {}'.format( self.lin_num, col))


        return token, lexeme, row, column
