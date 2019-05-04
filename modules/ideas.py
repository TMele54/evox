import sys, re

# elements of life are genes in GA, combining genes into a chain will make a regex pattern ie a chromosome
basic_elements_of_life = {
    "Character Escapes":            ["\a", "\b", "\t", "\r", "\v", "\f", "\n", "\e", "\ ", "\ x (this is joined)", "\c", "\u"],
    "Character Classes":            ["[group]", "[^ group]", "[first - last]", "\p{name}", "\w", "\s", "\S", "\d", "\D"],
    "Anchors":                      ["^", "$", "\A", "\Z", "\z", "\G", "\b", "\B"],
    "Grouping Constructs":          ["(subexpression)", "(?< name > subexpression)", "(?< name1 - name2 > subexpression)", "(?: subexpression )", "(?imnsx-imnsx: subexpression )", "(?= subexpression )", "(?! subexpression )", "(?<= subexpression )", "(?<! subexpression )", "(?> subexpression )"],
    "Quantifiers":                  ["*", "+", "?", "{n, }", "{n, m}", "*?", "+?", "??", "{ n }?", "{ n , }?", "{ n , m }?"],
    "Backreference Constructs":     ["\number", "\k< name >"],
    "Alternation Constructs":       ["|", "(?( expression ) yes | no )", "(?( name ) yes | no )"],
    "Substitutions":                ["$", "${name}", "$$", "$&", "$", "$`", "$'", "$+", "$_", "", "", "", ""],
    "Regular Expression Options":   ['i','m','n','s','x'],
    "Miscellaneous Constructs":     ['(?imnsx-imnsx)','(?# comment )','#']
}

str = '''
I say
I say 
that college boy
up yonder with
them
71.127.215.54
college books
over there
ain't
smarter
than
a
ten watt
lightbulb
said
the
Rhode Island Red Rooster
tonymelerutgers@gmail.com
'''

#re.search()
#re.findall()
p = re.compile('\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}')
p2 = re.compile('^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')

print p.findall(str)
print p2.findall(str)

# some combination of the above chromosomes will yield better and better matches to the intended search string
# if i create an initial population of parents that carry individual elements and they are combined at random
# eventually they will accidentally find the above or other pattern that satisfies a fitness function
# but if i can structure these elements into more complex types that are often found then it may be faster
# looking for database of common regex strings.

# seems regex strings are too wildly random to have definite patterns, but common subcomponents do exist such as
# \w+ or {int,int}+ or [a-z]
# some rules must be adhere'd to in general structure.. that can be forced without losing evolutionary form


###### fitness function
# individuals of a generation will output potential regex patterns, the results of those patterns can be compared to the
# target output and could use 'edit distance' to evaluate progress toward goal..

combination_patterns = {

"Character Classes": "Quantifiers"

}
