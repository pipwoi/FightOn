# Fighton Lexical Analyzer

Updates:
Comment is no longer one word
Rope Lit is no longer one word and apostrophe is included
Display error when float ends with decilmal point

Issues:
Only the first character of error is printed
Long errors cause the system to not tokens a few lines below it
Special Characters that arent underscore is not accepted by Rope lit

Notable Regex

            ('COMMENT', r'\$(?=.*[\sa-zA-Z0-9])\w*( \w+)*(?=.*[\n])'),
            ('ROPELIT', r'\'(?=.*[a-zA-Z0-9_])\w*( \w+)*(\s*)\''),

            ('HOVER_CONST', r'\d{1,10}\.\d{1,5}(?=.*[ \n\t])'),  # FLOAT
            ('CLOCK_CONST', r'\d{1,10}[\s](?=.*[ \n\t])'),  # INT

            ('ID', r'(?=[a-z])(?=.*[a-z(\d)*])\w*(?=.*[ \n()])'),       # ID1 not max 16
            ('ID', r'(?=[a-z])[a-z0-9]{1,10}[\s\n()]'),  # ID2 max 16 hides token below error

REQUEST!! FOR LOOP is based on C and C++

Sample
$ A1AwHA23 HEADS  -23453 
123.122323


## Original Code Source
https://github.com/christianrfg/lexical-analyzer
