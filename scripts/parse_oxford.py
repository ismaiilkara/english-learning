#!/usr/bin/env python3
"""
Parse Oxford 3000-5000 word list and create JSON for flashcards
"""
import json
import re

# Raw data from Oxford website
raw_data = """a indefinite articlea1  
abandon verbb2  
ability nouna2  
able adjectivea2  
about adverba1  
about prepositiona1  
above adverba1  
above prepositiona1  
abroad adverba2  
absolute adjectiveb2  
absolutely adverbb1  
academic adjectiveb1  
academic nounb2  
accept verba2  
acceptable adjectiveb2  
access nounb1  
access verbb1  
accident nouna2  
accommodation nounb1  
accompany verbb2  
according to prepositiona2  
account nounb1  
account verbb2  
accurate adjectiveb2  
accuse verbb2  
achieve verba2  
achievement nounb1  
acknowledge verbb2  
acquire verbb2  
across adverba1  
across prepositiona1  
act nounb1  
act verba2  
action nouna1  
active adjectivea2  
activity nouna1  
actor nouna1  
actress nouna1  
actual adjectiveb2  
actually adverba2  
ad nounb1  
adapt verbb2  
add verba1  
addition nounb1  
additional adjectiveb2  
address nouna1  
address verbb2  
administration nounb2  
admire verbb1  
admit verbb1  
adopt verbb2  
adult adjectivea2  
adult nouna1  
advance adjectiveb2  
advance nounb2  
advance verbb2  
advanced adjectiveb1  
advantage nouna2  
adventure nouna2  
advertise verba2  
advertisement nouna2  
advertising nouna2  
advice nouna1  
advise verbb1  
affair nounb2  
affect verba2  
afford verbb1  
afraid adjectivea1  
after adverba2  
after conjunctiona2  
after prepositiona1  
afternoon nouna1  
afterwards adverbb2  
again adverba1  
against prepositiona2  
age nouna1  
age verbb1  
aged adjectiveb1  
agency nounb2  
agenda nounb2  
agent nounb1  
aggressive adjectiveb2  
ago adverba1  
agree verba1  
agreement nounb1  
ah exclamationa2  
ahead adverbb1  
aid nounb2  
aid verbb2  
aim nounb1  
aim verbb1  
air nouna1  
aircraft nounb2  
airline nouna2  
airport nouna1  
alarm nounb1  
alarm verbb2  
album nounb1  
alcohol nounb1  
alcoholic adjectiveb1  
alive adjectivea2  
all adverba2  
all determinera1  
all pronouna1  
all right adjectivea2  
all right adverba2  
all right exclamationa2  
allow verba2  
almost adverba2  
alone adjectivea2  
alone adverba2  
along adverba2  
along prepositiona2  
already adverba2  
also adverba1  
alter verbb2  
alternative adjectiveb1  
alternative nouna2  
although conjunctiona2  
always adverba1  
amazed adjectiveb1  
amazing adjectivea1  
ambition nounb1  
ambitious adjectiveb1  
among prepositiona2  
amount nouna2  
amount verbb2  
analyse verbb1  
analysis nounb1  
ancient adjectivea2  
and conjunctiona1  
anger nounb2  
angle nounb2  
angry adjectivea1  
animal nouna1  
ankle nouna2  
anniversary nounb2  
announce verbb1  
announcement nounb1  
annoy verbb1  
annoyed adjectiveb1  
annoying adjectiveb1  
annual adjectiveb2  
another determinera1  
another pronouna1  
answer nouna1  
answer verba1  
anxious adjectiveb2  
any adverba2  
any determinera1  
any pronouna1  
any more adverba2  
anybody pronouna2  
anyone pronouna1  
anything pronouna1  
anyway adverba2  
anywhere adverba2  
anywhere pronouna2  
apart adverbb1  
apartment nouna1  
apologize verbb1  
app nouna2  
apparent adjectiveb2  
apparently adverbb2  
appeal nounb2  
appeal verbb2  
appear verba2  
appearance nouna2  
apple nouna1  
application nounb1  
apply verba2  
appointment nounb1  
appreciate verbb1  
approach nounb2  
approach verbb2  
appropriate adjectiveb2  
approval nounb2  
approve verbb2  
approximately adverbb1  
April nouna1  
architect nouna2  
architecture nouna2  
area nouna1  
argue verba2  
argument nouna2  
arise verbb2  
arm nouna1  
armed adjectiveb2  
arms nounb2  
army nouna2  
around adverba1  
around prepositiona1  
arrange verba2  
arrangement nouna2  
arrest nounb1  
arrest verbb1  
arrival nounb1  
arrive verba1  
art nouna1  
article nouna1  
artificial adjectiveb2  
artist nouna1  
artistic adjectiveb2  
as adverba2  
as conjunctiona2  
as prepositiona1  
ashamed adjectiveb2  
ask verba1  
asleep adjectivea2  
aspect nounb2  
assess verbb2  
assessment nounb2  
assignment nounb1  
assist verbb1  
assistant adjectivea2  
assistant nouna2  
associate verbb2  
associated adjectiveb2  
association nounb2  
assume verbb2  
at prepositiona1  
athlete nouna2  
atmosphere nounb1  
attach verbb1  
attack nouna2  
attack verba2  
attempt nounb2  
attempt verbb2  
attend verba2  
attention exclamationa2  
attention nouna2  
attitude nounb1  
attract verbb1  
attraction nounb1  
attractive adjectivea2  
audience nouna2  
August nouna1  
aunt nouna1  
author nouna2  
authority nounb1  
autumn nouna1  
available adjectivea2  
average adjectivea2  
average nouna2  
average verbb1  
avoid verba2  
award nouna2  
award verbb1  
aware adjectiveb1  
away adverba1  
awful adjectivea2  
baby nouna1  
back adjectivea2  
back adverba1  
back nouna1  
back verbb2  
background nouna2  
backwards adverbb1  
bacteria nounb2  
bad adjectivea1  
badly adverba2  
bag nouna1  
bake verbb1  
balance nounb1  
balance verbb1  
ball nouna1  
ban nounb1  
ban verbb1  
banana nouna1  
band nouna1  
bank nouna1  
bar nouna2  
bar verbb2  
barrier nounb2  
base nounb1  
base verbb1  
baseball nouna2  
based adjectivea2  
basic adjectiveb1  
basically adverbb2  
basis nounb1  
basketball nouna2  
bath nouna1  
bathroom nouna1  
battery nounb1  
battle nounb1  
battle verbb2  
be verba1  
be auxiliary verba1  
beach nouna1  
bean nouna2  
bear nouna2  
bear verbb2  
beat nounb2  
beat verba2  
beautiful adjectivea1  
beauty nounb1  
because conjunctiona1  
become verba1  
bed nouna1  
bedroom nouna1  
bee nounb1  
beef nouna2  
beer nouna1  
before adverba2  
before conjunctiona2  
before prepositiona1  
beg verbb2  
begin verba1  
beginning nouna1  
behave verba2  
behaviour nouna2  
behind adverba1  
behind prepositiona1  
being nounb2  
belief nounb1  
believe verba1  
bell nounb1  
belong verba2  
below adverba1  
below prepositiona1  
belt nouna2  
bend nounb1  
bend verbb1  
benefit nouna2  
benefit verbb1  
bent adjectiveb2  
best adjectivea1  
best adverba2  
best nouna2  
bet nounb2  
bet verbb2  
better adjectivea1  
better adverba2  
better nounb1  
between adverba2  
between prepositiona1  
beyond adverbb2  
beyond prepositionb2  
bicycle nouna1  
big adjectivea1  
bike nouna1  
bill nouna1  
bill verbb2  
billion numbera2  
bin nouna2  
biology nouna2  
bird nouna1  
birth nouna2  
birthday nouna1  
biscuit nouna2  
bit nouna2  
bite nounb1  
bite verbb1  
bitter adjectiveb2  
black adjectivea1  
black nouna1  
blame nounb2  
blame verbb2  
blank adjectivea2  
blank nouna2  
blind adjectiveb2  
block nounb1  
block verbb1  
blog nouna1  
blonde adjectivea1  
blood nouna2  
blow verba2  
blue adjectivea1  
blue nouna1  
board nouna2  
board verbb1  
boat nouna1  
body nouna1  
boil verba2  
bomb nounb1  
bomb verbb1  
bond nounb2  
bone nouna2  
book nouna1  
book verba2  
boot nouna1  
border nounb1  
border verbb2  
bored adjectivea1  
boring adjectivea1  
born verba1  
borrow verba2  
boss nouna2  
both determinera1  
both pronouna1  
bother verbb1  
bottle nouna1  
bottom adjectivea2  
bottom nouna2  
bowl nouna2  
box nouna1  
boy nouna1  
boyfriend nouna1  
brain nouna2  
branch nounb1  
brand nounb1  
brand verbb1  
brave adjectiveb1  
bread nouna1  
break nouna1  
break verba1  
breakfast nouna1  
breast nounb2  
breath nounb1  
breathe verbb1  
breathing nounb1  
bride nounb1  
bridge nouna2  
brief adjectiveb2  
bright adjectivea2  
brilliant adjectivea2  
bring verba1  
broad adjectiveb2  
broadcast nounb2  
broadcast verbb2  
broken adjectivea2  
brother nouna1  
brown adjectivea1  
brown nouna1  
brush nouna2  
brush verba2  
bubble nounb1  
budget nounb2  
build verba1  
building nouna1  
bullet nounb2  
bunch nounb2  
burn nounb2  
burn verba2  
bury verbb1  
bus nouna1  
bush nounb2  
business nouna1  
businessman nouna2  
busy adjectivea1  
but conjunctiona1  
but prepositionb2  
butter nouna1  
button nouna2  
buy verba1  
"""

def parse_word_line(line):
    """Parse a single line of word data"""
    line = line.strip()
    if not line:
        return None
    
    # Pattern: word type+level (e.g., "abandon verbb2")
    # Handle multi-word entries like "all right"
    pattern = r'^(.+?)\s+(noun|verb|adjective|adverb|preposition|conjunction|determiner|pronoun|exclamation|ordinal number|number|indefinite article|auxiliary verb|modal verb|linking verb|infinitive marker|definite article)([ab][12])$'
    
    match = re.match(pattern, line, re.IGNORECASE)
    if match:
        word = match.group(1).strip()
        word_type = match.group(2).strip()
        level = match.group(3).upper()
        return {
            "word": word,
            "type": word_type,
            "level": level
        }
    return None

def main():
    words = []
    seen = set()  # Track unique word+type combinations
    
    for line in raw_data.strip().split('\n'):
        result = parse_word_line(line)
        if result:
            key = f"{result['word']}_{result['type']}"
            if key not in seen:
                seen.add(key)
                words.append(result)
    
    # Group by level
    levels = {"A1": [], "A2": [], "B1": [], "B2": []}
    for w in words:
        level = w["level"]
        if level in levels:
            levels[level].append(w)
    
    # Create output structure
    output = {
        "title": "Oxford 3000-5000",
        "description": "Core vocabulary for English learners from Oxford",
        "totalWords": len(words),
        "levels": {
            "A1": len(levels["A1"]),
            "A2": len(levels["A2"]),
            "B1": len(levels["B1"]),
            "B2": len(levels["B2"])
        },
        "words": words
    }
    
    # Save to file
    output_path = "/Users/ismailkara/Desktop/english-learning/data/vocabulary/oxford-3000-5000.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"Parsed {len(words)} words")
    print(f"A1: {len(levels['A1'])}, A2: {len(levels['A2'])}, B1: {len(levels['B1'])}, B2: {len(levels['B2'])}")
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    main()
