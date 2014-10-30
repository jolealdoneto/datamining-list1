seq_db = [ "ACGTCACG", "TCGA", "GACTGCA", "CAGTC", "AGCT", "TGCAGCTC", "AGTCAG" ]
alf = [ "A", "C", "G", "T" ]

def is_present(seq, phrase):
    last = 0
    for l in seq:
        spot = phrase.find(l, last)
        if spot == -1:
            return False
        last = spot+1
    return True
def sup(seq):
    return sum(map(lambda s: 1 if is_present(seq, s) else 0, seq_db))

def get_frequent(item, last, minsup):
    freq_items = []
    for l in last:
        gen_item = item + l[-1]
        if sup(gen_item) >= minsup:
            freq_items.append(gen_item)
    return freq_items + reduce(lambda acc, a: acc + a, map(lambda i: get_frequent(i, freq_items, 4), freq_items), [])
def get_all_permutations(seq, start):
    return map(lambda s: seq[start:s], range(start+1, len(seq)+1))
def sup_substr(sub):
    return sum(map(lambda s: 1 if s.find(sub) > -1 else 0, seq_db))




# A
all_frequent = get_frequent("", ["A", "C", "G", "T"], 4)
max_freq = []
for seq, i in zip(all_frequent, range(len(all_frequent))):
    if len(filter(lambda x: is_present(seq, x), all_frequent[i+1:])) == 0:
        max_freq.append(seq)
print "Max: ", max_freq
# B
closed_freq = []
for seq, i in zip(sorted(all_frequent, lambda a, b: len(a) - len(b)), range(len(all_frequent))):
    closed = True
    for pair in all_frequent[i+1:]:
        if is_present(seq, pair) and sup(seq) == sup(pair):
            closed = False
            break
    if closed:
        closed_freq.append(seq)
print "closed: ", closed_freq
#C
substr = {}
for seq in seq_db:
    for i in range(len(seq)):
        for perm in get_all_permutations(seq, i):
            if sup_substr(perm) >= 4:
                if perm not in substr:
                    substr[perm] = 1
                else:
                    substr[perm] += 1
max_subs = substr.keys()
print "frequent:"
for s, i in zip(max_subs, range(len(max_subs))):
    if len(filter(lambda j: j.find(s) > -1, max_subs[i+1:])) == 0:
        print s, substr[s]



