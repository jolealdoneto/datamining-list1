seq_db = [ "ACGTCACG", "TCGA", "GACTGCA", "CAGTC", "AGCT", "TGCAGCTC", "AGTCAG" ]
alf = [ "A", "C", "G", "T" ]

def is_present(seq, phrase, last):
    for l in seq:
        spot = phrase.find(l, last)
        if spot == -1:
            return -1
        last = spot+1
    return last

def get_pos(seq, phrase, last):
    last_pos = is_present(seq, phrase, last+1)
    if last_pos != -1:
        return [last_pos] + get_pos(seq, phrase, last_pos)
    return []

class Spade:
    def __init__(self, seq, spade = None, spade2 = None):
        if seq is not None:
            self.seq = seq
        if spade is None:
            self.calc_occurrences()
        else:
            self.seq = spade.seq + spade2.seq[-1]
            self.join(spade, spade2)

    def join(self, spade1, spade2):
        self.occurrences = {}
        for k, v in spade2.occurrences.items():
            if k in spade1.occurrences:
                for pos in v:
                    if len(filter(lambda p: pos > p, spade1.occurrences[k])) > 0:
                        if k not in self.occurrences:
                            self.occurrences[k] = []
                        self.occurrences[k].append(pos)

    def calc_occurrences(self):
        self.occurrences = {}
        for seq, i in zip(seq_db, range(len(seq_db))):
            pos = get_pos(self.seq, seq, -1)
            if pos:
                self.occurrences[i] = pos
    def sup(self):
        return len(self.occurrences)

def get_frequent(item, last, minsup):
    freq_items = []
    for l in last:
        spade = Spade(None, item, l)
        if spade.sup() >= minsup:
            freq_items.append(spade)
    return freq_items + reduce(lambda acc, a: acc + a, map(lambda i: get_frequent(i, freq_items, 4), freq_items), [])

freq_spades = reduce(lambda acc, a: acc + a, map(lambda start: get_frequent(Spade(start), map(lambda s: Spade(s), alf), 4), alf))
for spade in freq_spades:
    print spade.seq, spade.sup(), spade.occurrences
