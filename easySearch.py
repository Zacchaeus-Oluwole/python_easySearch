dictv = {
            'ace': 'of the highest quality',
            'age': 'how long something has existed',
            'agree': 'be in accord; be in agreement',
            'abate': 'make less active or intense',
            'abatement': "an interruption in the intensity or amount of something",
            'aggregate': 'the whole amount',
            'name': 'a language unit by which a person or thing is known',
            'nice': 'pleasant or pleasing in nature',
            'nominate': 'propose as a candidate for some honor',
            'seven': 7,
            'zacchaeus': 'MY NAME, LOL...'
        }

# get = input("Enter first and last letter:")
get = input("Enter first and last letter:").split()
first = get[0]
last = get[1]
numMin = int(get[-2])
numMax = int(get[-1])

for l,k in dictv.items():
    if l[0] == first and l[-1] == last and numMin <= len(l) and len(l) <= numMax:
        print(l,":",k)
