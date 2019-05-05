from classes.eVoXCls import eVoX


def generate(user_string, initial_population_size, corpus, elite_size, mutation_rate, generations):

    fitness = eVoX(s1=user_string, document=corpus, initial_population_size=initial_population_size)

    initial_population = fitness.initial_population()

    fitness_matrix = fitness.evaluate_generation(initial_population)















'''

combination_patterns = {"Character Classes": "Quantifiers"}

# elements of life are genes in GA, combining genes into a chain will make a regex pattern ie a chromosome
basic_elements_of_life = {
    "Character Escapes": ["\a", "\b", "\t", "\r", "\v", "\f", "\n", "\e", "\ ", "\ x (this is joined)", "\c", "\u"],
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
    "Regular Expression Options": ['i', 'm', 'n', 's', 'x'],
    "Miscellaneous Constructs": ['(?imnsx-imnsx)', '(?# comment )', '#']
}

'''
'''
    The goal of this project is to generate a regular expression search pattern, given a target chuck of free text. The search pattern will be constructed by using a custom Genetic Algorithm (GA). The GA will use various Regex string 
     subcomponents as genes concatinated sets of these genes will become chromosomes. The fitness function will evaluate
      an individual's chromosome against the user define example string(s). The workflow is as follows, a user will provide the 
     algorithm an initial string, such as an ip address [71.127.215.54]. From generation to generation, individuals will
     pass on successful genes (regex components) to their offspring and as this race evolves a better and better regular 
     expression search string will be defined. Once this pattern has converged via the fitness function, the expression can be 
     optimized using a number of open source tools.

     The search space for a regex search pattern is enourmous, but by structuring a chromosome and properly leveraging
     mutations, elitism, CRISPR, and other items, I believe that the code will be fast enough for use by a Data Scientist. 

'''
'''
hypo = re.sub(" +", " ", hypo.replace("\n", " "))
print hypo

# 123.432.345.768
# re.search()
# re.sub()
# re.findall()
p1 = re.compile('\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}')
p2 = re.compile('^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')

print p1.findall(hypo)
print p2.findall(hypo)

'''