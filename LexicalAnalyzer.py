
import re

class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, code):
        rules = [
            # FightOn

            # generic delimiter (?=.*[ \n\t])
            ('COMMENT', r'\$[ a-zA-Z0-9]\w*(?=.*[\n])'),
            ('CLOCK', r'clock(?=.*[ \n\t])'),
            ('HOVER', r'hover(?=.*[ \n\t])'),
            ('ROPE', r'rope(?=.*[ \n\t])'),
            ('COIN', r'coin(?=.*[ \n\t])'),
            ('COIN_VAL', r'HEADS|TAILS(?=.*[ \n\t])'),
            ('PARTY', r'party(?=.*[ \n\t])'),
            ('QUEST', r'quest(?=.*[ \n\t])'),
            ('JOB', r'job(?=.*[ \n\t])'),
            ('LISTEN', r'listen(?=.*[ \n\t])'),
            ('SAY', r'say(?=.*[ \n\t])'),
            ('TOWER', r'tower(?=.*[ \n\t])'),
            ('STOCK', r'STOCK(?=.*[ \n\t])'),

            #('OR', r'OR'),
            ('AND', r'AND(?=.*[ \n\t])'),
            ('NOT', r'NOT(?=.*[ \n\t])'),
            ('START', r'START(?=.*[ \n\t])'),
            ('END', r'END(?=.*[ \n\t])'),
            ('WHILE', r'while(?=.*[ \n\t:])'),
            ('BREAK', r'break(?=.*[ \n\t;])'),
            ('CASE', r'case(?=.*[ \n\t])'),
            ('CONTINUE', r'continue(?=.*[ \n\t])'),
            ('DEFAULT', r'default(?=.*[ \n\t])'),
            ('DO', r'do(?=.*[ \n\t:])'),
            ('ELIF', r'elif(?=.*[ \n\t:])'),
            ('ELSE', r'else(?=.*[ \n\t:])'),
            ('FOR', r'for'),
            ('IF', r'if'),
            ('SWITCH', r'switch'),

            #('OR', r'\|\|'),

            ('CLOCK_CONST', r'\d{1,10}(?=.*[ \n\t])'),  # INT
            # ('ROPELIT', r'\'(?=[a-z])\''),  # ROPELIT
            # ('SQUOTE', r'\''),
            ('DQUOTE', r'\"(?=.*[ \n\t])'),
            ('TQUOTE', r'\'\'\''),
            ('BSLASH', r'\\(?=.*[ \n\t])'),
            ('TILDE', r'~(?=.*[ \n\t])'),

            ('LBRACKET', r'\((?=.*[ \n\t()a-z0-9\'\"])'),   # check (
            ('RBRACKET', r'\)(?=.*[ \n\t)\+\-\*\/%;])'),    # check )
            ('LBRACE', r'\{(?=.*[ \n\t])'),                 # { check?
            ('RBRACE', r'\}(?=.*[ \n\t()a-z0-9])'),         # } check
            ('COMMA', r',(?=.*[ \n\ta-z])'),                #check ,
            ('SEMICOL', r';(?=.*[ \n\ta-z])'),              #check :
            ('COLON', r':(?=.*[ \n\ta-z0-9])'),             # ; ????

            # operational delimiter (?=.*[ \n\ta-z0-9])
            ('EQ', r'==(?=.*[ \n\ta-z0-9])'),              # ==
            ('ASSIGN', r'=(?=.*[ \n\ta-z0-9])'),           # =
            ('NE', r'!=(?=.*[ \n\ta-z0-9])'),              # !=
            ('LE', r'<=(?=.*[ \n\ta-z0-9])'),              # <=
            ('GE', r'>=(?=.*[ \n\ta-z0-9])'),              # &&
            ('ATTR', r'\=(?=.*[ \n\ta-z0-9])'),            # =
            ('LT', r'<(?=.*[ \n\ta-z0-9])'),               # <
            ('GT', r'>(?=.*[ \n\ta-z0-9])'),               # >
            ('PLUSEQ', r'\+\=(?=.*[ \n\ta-z0-9;])'),       # +
            ('INC', r'\+\+(?=.*[ \n\ta-z0-9;])'),          # ++
            ('PLUS', r'\+(?=.*[ \n\ta-z0-9])'),            # +
            ('MINEQ', r'\-\=(?=.*[ \n\ta-z0-9;])'),        # -=
            ('DEC', r'\-\-(?=.*[ \n\ta-z0-9;])'),          # --
            ('MINUS', r'-(?=.*[ \n\ta-z0-9])'),            # -
            ('MULT', r'\*(?=.*[ \n\ta-z0-9])'),            # *
            ('DIV', r'\/(?=.*[ \n\ta-z0-9])'),             # /

            ('MODULO', r'%(?=.*[ \n\ta-z0-9])'),           # %
            ('AT', r'@(?=.*[ \n\t])'),               # @
            ('DOLLAR', r'\$(?=.*[ \n\t])'),          # $
            ('EXCLA', r'!(?=.*[ \n\t])'),            # !



            ('ID', r'(?=[a-z])(?=.*[a-z(\d)*])\w*(?=.*[ \n()])'),        # IDENTIFIERS

            #('HOVER_CONST', r'\d(\d)*\.\d(\d)*'),  # FLOAT
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

                    tab_row.append('{:>10} {:>16} {:>8}, {:>3}\n'
                                   .format(token_lexeme, token_type, self.lin_num, col))


        except:
            lexerror.append('\n  Lexical Error on Line {} : {}'.format(self.lin_num, token_lexeme))
            self.lin_num += 1


        return token, lexeme, row, column, lexerror, tab_row

