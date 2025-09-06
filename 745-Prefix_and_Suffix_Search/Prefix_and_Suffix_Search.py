class WordFilter:
    def __init__(self, words):
        self.lookup = {}
        
        for index, word in enumerate(words):
            for i in range(len(word)+1):
                prefix = word[:i]
                for j in range(len(word)+1):
                    suffix = word[j:]
                    self.lookup[(prefix, suffix)] = index

    def f(self, pref, suff):
        return self.lookup.get((pref, suff), -1)