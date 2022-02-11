# The lexer (the lexer identifies everything)

from frontend.styles import *


def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        g.append(el)
    yield g


class IoLexer:
    def __init__(self, data, lexing=True):
        if lexing == True:
            global cline
            global ltokens
            file = data# f.read()
            content = file.split("\n")
            content2 = file.split()
              # print(content)

            for i in content:
                if i.startswith("#"):
                    i = ""
                elif "#" in i:
                    findcom = i.find("#")
                    if findcom != -1:
                        i = i[:findcom]  # This discards comments
                line = i

            self.line = line
        else:
            exception = "lexing is not allowed!"
            error = "error: <invalid lexing>".center(40)
            print(f"{bold}{Red}{error}{reset}{Red}\n\t-> line {cline}: {underline}{exception}{reset}")
    # exit()

    def return_value(self):
      return self.line