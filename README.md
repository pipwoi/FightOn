# Fighton Lexical Analyzer

Able to:
Accept Alphanumeric comments that start with $<space>
Accept ID that starts with lowercase then alphanumeric (no upper)

Issues:
234ehjjk is not considered as error (no lookahead, lookbehind)
Only the first character of error is printed
After an error the next 'paragraph' is not tokenized

Clock (Int) only accepts 5 digits but not delimited by space
Hover (Float is accepted despite having more than 5 digits

Notable Regex

 ('COMMENT', r'\$[ a-zA-Z0-9]\w*'),
 ('ID', r'(?=[a-z])(?=.*[a-z(\d)*])\w*'),        # IDENTIFIERS

            ('HOVER_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            ('CLOCK_CONST', r'\d{1,5}'),          # INT



Sample
$ A1AwHA23 HEADS  -23453 
123.122323

int main() esdf123g6 234ehjjk


## Original Code Source
https://github.com/christianrfg/lexical-analyzer
