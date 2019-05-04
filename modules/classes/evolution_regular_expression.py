from __future__ import division

class eVoX:

    # Initialization
    def __init__(self, s1, s2, initial_population_size):
        self.s1 = s1
        self.s2 = s2
        self.ip_size = initial_population_size

    # Measure distance between user example and current individual's chromosome
    def editDistance(self):
        if len(self.s1) > len(self.s2):
            self.s1, self.s2 = self.s2, self.s1

        distances = range(len(self.s1) + 1)
        for i2, c2 in enumerate(self.s2):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(self.s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    # Evaluate the fitness of current individual's search pattern
    def evaluate(self):
        distance = self.editDistance()
        bigger = max(len(self.s1), len(self.s2))

        pct = (bigger - distance) / bigger
        return pct*100

    def spawn_individual(self):
        individual = object()

        basic_elements_of_life = {
            "Character Escapes": ["\a", "\b", "\t", "\r", "\v", "\f", "\n", "\e", "\ ", "\c","\u"],
            "Character Classes": ["[group]", "[^ group]", "[first - last]", "\p{name}", "\w", "\s", "\S", "\d", "\D"],
            "Anchors": ["^", "$", "\A", "\Z", "\z", "\G", "\b", "\B"],
            "Grouping Constructs": ["(subexpression)", "(?< name > subexpression)",
                                    "(?< name1 - name2 > subexpression)",
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
        return individual

    # Creates first generation of individuals
    def initialPopulation(self):
        population = []

        for i in range(0, self.ip_size):
            population.append(i)

        return population



