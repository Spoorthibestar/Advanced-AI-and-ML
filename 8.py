import random, math
from collections import Counter

text = "the cat sat on the mat the cat lay on the rug"
words = text.split()

n = 2
ngrams = Counter(zip(words, words[1:]))
context = Counter(words[:-1])

print("Learned Bigrams:")
for (a, b), c in ngrams.items():
    print(f"{a} → {b}  (count={c})")

def generate(start="the", length=8):
    s = [start]
    for _ in range(length):
        choices = [(b, c) for (a, b), c in ngrams.items() if a == s[-1]]
        if not choices:
            break
        words_list, counts = zip(*choices)
        s.append(random.choices(words_list, counts)[0])
    return " ".join(s)

print("\nGenerated:", generate())

def perplexity(sentence):
    w = sentence.split()
    logp = 0
    for a, b in zip(w, w[1:]):
        p = ngrams[(a, b)] / context[a] if context[a] else 1e-9
        logp += math.log(p)
    return math.exp(-logp / (len(w) - 1))

print("\nPerplexity:", perplexity("the cat sat on the mat"))
