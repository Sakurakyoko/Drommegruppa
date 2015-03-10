# -*- coding: utf-8 -*-
import random 
import math
import itertools
from collections import defaultdict

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    print hands
    print "Vinner:"
    return allmax(hands, key = hand_rank)

def allmax(iterable, key=lambda x:x):
    "Return a list of all items equal to the max of the iterable."
    maxi = max(iterable, key=key)
    return [element for element in iterable if key(element) == key(maxi)]

# hand_rank funksjonen tar en hånd og returnerer en hånd med kort.
def hand_rank(hand):
    ranks = card_ranks(hand)
    # Sjekk om hånden har straight flush.
    if straight(ranks) and flush(hand):
       return (8, max(ranks))
    # Sjekk on hånden har fire like.
    elif kind(4, ranks):
       return (7, kind(4, ranks), kind(1, ranks))
    # Sjekk om hånden har fullt hus.
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    # Sjekk om hånden har flush.
    elif flush(hand):
        return (5, ranks)
    # Sjekk om hånden har en straight.
    elif straight(ranks):
        return (4, max(ranks))
    # Sjekk om hånden har tre like.
    elif kind(3, ranks):
        return (3, kinds(3, ranks), ranks)
    # Sjekk om hånden har to par.
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    # Sjekk om hånden har to like.
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    # Sjekk om hånden har den høyeste kortet.
    else:
        return (0, ranks)

def group(items):
    "Return a list of [(count, x)...], highest count first, the highest x first"
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)

# card_ranks funksjonen tar en hånd og returnerer hvilken rangering hvert kort i hånden.
def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    # For at man skal få alle mulige straight så må vi sørge for at ESS har to verdier 14 og 1.
    if ranks == [14,5,4,3,2]:
        return [5,4,3,2,1]
    return ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return sum(ranks) - min(ranks)*5 == 10

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    result = [r for r in set(ranks) if ranks.count(r) == 2]
    if len(result) == 2:
        return (max(result), min(result))

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in set(ranks):
        if ranks.count(r) == n:
            return r
    return None

deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n = 5, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Return a list of numhands hands consisting of n cards each"
    random.shuffle(deck)
    deck = iter(deck)
    return [[next(deck) for card in range(n)] for hand in range(numhands)]

def test():
    "Tester funksjonene i poker programmet"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
    s3 = "TC JC QC KS AS".split() # 10-A straight    
    tp = "5S 5D 9H 9C 6S".split() # two pair
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "2S 3S 4S 6C 7D".split() # 7 high
    #Tester riktig vinner
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert poker([s1, s2]) == [s2]
    assert poker([s1, tp]) == [s1]

    # assert hand_rank(sf) == (8, 10)
    # assert hand_rank(fk) == (7, 9, 7)
    # assert hand_rank(fh) == (6, 10, 7)
    # assert hand_rank(s1) == (4, 5)
    # assert hand_rank(s3) == (4, 14)    

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]

    # Ace-high slår 7-high
    assert (card_ranks(['AS', '2C', '3D', '4H', '6S']) >
            card_ranks(['2D', '3S', '4C', '6H', '7D']))
    # Straight fra 1-5 er dårligere enn straight 2-6
    assert (card_ranks(['AS', '2C', '3D', '4H', '5S']) <
            card_ranks(['2D', '3S', '4C', '5H', '6D']))

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(tpranks) == (9, 5)
    assert two_pair([10, 10, 5, 5, 2]) == (10, 5)    

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    return 'tests pass'
    print "Test"
#Navn på alle mulige vinner hånd
hand_names = [
    'High Card',
    'Pair',
    '2 Pair',
    '3 Kind',
    'Straight',
    'Flush',
    'Full House',
    '4 Kind',
    'Straight Flush',
    ]
    
#Alt fra og med her er kopiert fra Udacity kurset "Shuffling", ettersom det staar at vi skal gjore det i oppgaven.
    
def hand_percentages(n = 700*1000):
    "Sample n random hands and print a table of percentages for each type of hand"
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %6.3f'%(hand_names[i], 100.*counts[i]/n))

def all_hand_percentages():
    "Print an exhaustive table of frequencies for each type of hand"
    counts = [0]*9
    n = 0
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    for hand in itertools.combinations(deck, 5):
        n += 1
        ranking = hand_rank(hand)[0]
        counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %7d %6.3f'%(hand_names[i], counts[i], 100.*counts[i]/n))

def shuffle1(deck):
    # O(N**2)
    # incorrect distribution
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2(deck):
    # O(N**2)
    # incorrect distribution?    
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2a(deck):
    # http://forums.udacity.com/cs212-april2012/questions/3462/better-implementation-of-shuffle2
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        j = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle3(deck):
    # O(N)
    # incorrect distribution    
    N = len(deck)
    for i in range(N):
        j = random.randrange(N)
        deck[i], deck[j] = deck[j], deck[i]

def shuffle(deck):
    # Knuth method
    n = len(deck)
    for i in range(n-1):
        j = random.randrange(i, n)
        deck[i], deck[j] = deck[j], deck[i]        

def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1./factorial(len(deck))  ## expected count
    ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
    name = shuffler.__name__
    print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** bad ***'))
    print '    ',
    for item, count in sorted(counts.items()):
        print "%s:%4.1f" % (item, count*100./n),
    print

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc','ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n*factorial(n-1)

print poker(deal(3))
