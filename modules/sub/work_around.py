import pickle

basic = {
    "template": {
        "Character Escapes": ["\a", "\b", "\t", "\r", "\v", "\f", "\n", "\e", "\ ", "\c", "\u"],
        "Character Classes": ["[group]", "[^ group]", "[first - last]", "\p{name}", "\w", "\s", "\S", "\d", "\D"],
        "Anchors": ["^", "$", "\A", "\Z", "\z", "\G", "\b", "\B"],
        "Grouping Constructs": ["(subexpression)", "(?< name > subexpression)", "(?< name1 - name2 > subexpression)",
                                "(?: subexpression )", "(?imnsx-imnsx: subexpression )", "(?= subexpression )",
                                "(?! subexpression )", "(?<= subexpression )", "(?<! subexpression )",
                                "(?> subexpression )"],
        "Quantifiers": ["*", "+", "?", "{n, }", "{n, m}", "*?", "+?", "??", "{ n }?", "{ n , }?", "{ n , m }?"],
        "Backreference Constructs": ["\number", "\k< name >"],
        "Alternation Constructs": ["|", "(?( expression ) yes | no )", "(?( name ) yes | no )"],
        "Substitutions": ["$", "${name}", "$$", "$&", "$", "$`", "$'", "$+", "$_", "", "", "", ""],
        "Options": ['i', 'm', 'n', 's', 'x'],
        "Miscellaneous Constructs": ['(?imnsx-imnsx)', '(?# comment )', '#']
    },
    "real": {
        "Escapes": ["\a", "\b", "\t", "\r", "\v", "\f", "\n", "\e", "\ ", "\c", "\u"],
        "Classes": ["\w", "\s", "\S", "\d", "\D", "[a-z]", "[A-Z]", "[0-9]", "[^ a-z]", "[^ A-Z]", "[^ 0-9]"],
        "Anchors": ["^", "$", "\A", "\Z", "\z", "\G", "\b", "\B"],
        "Quantifiers": ["*", "+", "?", "{n, }", "{n, m}", "*?", "+?", "??", "{ n }?", "{ n , }?", "{ n , m }?"],
        "Options": ['i', 'm', 'n', 's', 'x']
    },
    "simple": {
        "Escapes": [],
        "Classes": ["\w", "\s", "\S", "\d", "\D", "[a-z]", "[A-Z]", "[0-9]", "[^ a-z]", "[^ A-Z]", "[^ 0-9]"],
        "Anchors": [],
        "Quantifiers": ["*", "+", "?", "{0, }"],
        "Options": ["i", ""]
    }
}

pth = 'data/basic_elements.pym'

with open(pth, 'wb') as handle:
    pickle.dump(basic, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(pth, 'rb') as handle:
    b = pickle.load(handle)

print basic == b
