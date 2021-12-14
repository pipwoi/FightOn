
import re

class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, code):
        rules = [
            # FightOn
            # negative lookahead
            # generic delimiter (?=.*[ \n\t])
            ('COMMENT', r'\$(?=.*[\sa-zA-Z0-9])\w*( \w+)*(?=.*[\n])'),

            ('RUNE_LIT', r'\'[\s!a-zA-Z0-9_\(\),]\''),                      # RUNELIT
            ('ROPE_LIT', r'\"(?=.*[\sa-zA-Z0-9_\(\)])\w*( \w+)*(\s*)\"'),   # ROPELIT

            ('HOVER_ERROR', r'\d{1,10}\.\d{1,5}(?=[a-zA-Z\"\'])'),
            ('HOVER_LIT', r'\d{1,10}\.\d{1,5}(?=.*[ \n\t\+\-\/\%\*])'),    # FLOAT

            ('CLOCK_ERROR', r'\d{1,10}(?=[a-zA-Z\"\'\_\^\&\#\@\?])'),
            ('CLOCK_LIT', r'\d{1,10}(?=[\s\n\t\+\-\/\%\*])'),              # INT


            ('clock', r'clock(?=.*[ \n\t])'),
            ('hover', r'hover(?=.*[ \n\t])'),
            ('rune', r'rune(?=.*[ \n\t])'),
            ('rope', r'rope(?=.*[ \n\t])'),
            ('coin', r'coin(?=.*[ \n\t])'),
            ('COIN_VAL', r'heads(?=.*[ \n\t])'),
            ('party', r'party(?=.*[ \n\t])'),
            ('quest', r'quest(?=.*[ \n\t])'),
            ('job', r'job(?=.*[ \n\t])'),
            ('listen', r'listen(?=.*[ \n\t])'),
            ('say', r'say(?=.*[ \n\t])'),
            ('tower', r'tower(?=.*[ \n\t])'),
            ('STOCK', r'STOCK(?=.*[ \n\t])'),

            #('OR', r'OR'),
            #('OR', r'\|\|'),
            ('AND', r'AND(?=.*[ \n\t])'),
            ('NOT', r'NOT(?=.*[ \n\t])'),
            ('START', r'START(?=.*[ \n\t])'),
            ('END', r'END(?=.*[ \n\t])'),
            ('while', r'while(?=.*[ \n\t:])'),
            ('break', r'break(?=.*[ \n\t;])'),
            ('case', r'case(?=.*[ \n\t])'),
            ('continue', r'continue(?=.*[ \n\t])'),
            ('default', r'default(?=.*[ \n\t])'),
            ('do', r'do(?=.*[ \n\t:])'),
            ('elif', r'elif(?=.*[ \n\t:])'),
            ('else', r'else(?=.*[ \n\t:])'),
            ('for', r'for'),
            ('if', r'if'),
            ('switch', r'switch'),

            ('ID_ERROR', r'(?=[a-z])[a-z0-9_]{1,15}(?=.*[?@&\#\'\"\~\^])'),  # IDENTIFIERS
            ('ID', r'(?=[a-z])[a-z0-9_]{1,15}(?=[\s\n\t(])'),  # IDENTIFIERS

            ('CASE_ERROR', r'(?=[a-zA-Z])[a-zA-Z0-9_]{1,16}'),  # IDENTIFIERS
            # ('SQUOTE', r'\''),
            #('DQUOTE', r'\"(?=.*[ \n\t])'),
            #('TQUOTE', r'\'\'\''),
            ('BSLASH', r'\\(?=.*[ \n\t])'),

            ('INV_SYM', r'[\~\'\"\#\&\^\?\_]'),
            ('L_PARENTH', r'\((?=.*[ \n\t\(\)a-z0-9\'\"])'),   # check (
            ('R_PARENTH', r'\)(?=.*[ \n\t)\+\-\*\/%;])'),    # check )
            ('LBRACKET', r'\[(?=.*[ \n\t])'),                 # { check?
            ('RBRACKET', r'\](?=.*[ \n\t()a-z0-9])'),         # } check
            ('LBRACE', r'\{(?=.*[ \n\t])'),                 # { check?
            ('RBRACE', r'\}(?=.*[ \n\t()a-z0-9])'),         # } check
            ('COMMA', r',(?=.*[ \n\ta-z])'),                #check ,
            ('SEMICOL', r';(?=.*[ \n\ta-z])'),              #check :
            ('COLON', r':(?=.*[ \n\ta-z0-9])'),             # ; ????

            # operational delimiter (?=.*[ \n\ta-z0-9])
            ('EQ', r'==(?=[\s\n\ta-z0-9])'),              # ==
            ('ASSIGN', r'=(?=[\s\n\ta-z0-9])'),           # =
            ('NE', r'!=(?=.*[ \n\ta-z0-9])'),              # !=
            ('LE', r'<=(?=.*[ \n\ta-z0-9])'),              # <=
            ('GE', r'>=(?=.*[ \n\ta-z0-9])'),              # &&
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
            ('PERIOD', r'\.'),         # ANOTHER CHARACTER

            ('MODULO', r'%(?=.*[ \n\ta-z0-9])'),           # %
            ('AT', r'@(?=.*[ \n\t])'),               # @
            ('DOLLAR', r'\$(?=.*[ \n\t])'),          # $
            ('EXCLA', r'!(?=.*[ \n\t])'),            # !


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
                elif token_type == 'CLOCK_ERROR' or token_type == 'HOVER_ERROR':
                    lexerror.append('\n  Invalid Value on Line {} : {}'.format(self.lin_num, token_lexeme))

                elif token_type == 'ID_ERROR':
                    lexerror.append('\n  Invalid ID on Line {} : {}'.format(self.lin_num, token_lexeme))

                elif token_type == 'INV_SYM':
                    lexerror.append('\n  Invalid Symbol on Line {} : {}'.format(self.lin_num, token_lexeme))

                elif token_type == 'CASE_ERROR':
                    lexerror.append('\n  Case Error on Line {} : {}'.format(self.lin_num, token_lexeme))

                elif token_type == 'MISMATCH':
                    raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
                else:

                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token

                    if token_type == 'CLOCK_LIT' or token_type == 'HOVER_LIT':
                        token_lexeme = token_lexeme.strip("0")
                        print(token_lexeme)

                    tab_row.append('{:>5}, {:>3}{:>15} {:>15}\n'
                                   .format(self.lin_num, col, token_lexeme, token_type))


        except:
            lexerror.append('\n  Lexical Error on Line {} : {}'.format(self.lin_num, token_lexeme))
            self.lin_num += 1


        return token, lexeme, row, column, lexerror, tab_row

