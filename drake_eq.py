__author__ = "Vincent Moore"

import math

#Drake equation welcome
multiline_str = """
The Drake equation or SETI equation, was created by astronomer Frank Drake in 1961.

The equation attempts to estimate how many advanced civiliations may exist in the Milky Way.

The equation is as follows:
N = R* x fp x ne x fl x fi x fc x L 

N  : The number of civilizations in the Milky Way galaxy whose electromagnetic emissions are detectable.
R* : The rate of formation of stars suitable for the development of intelligent life (number per year).
fp : The fraction of those stars with planetary systems.
ne : The number of planets, per star system, with an environment suitable for life.
fl : The fraction of suitable planets on which life actually appears.
fi : The fraction of life bearing planets on which intelligent life emerges.
fc : The fraction of civilizations that develop a technology that produces detectable signs of their existence.
L  : The average length of time such civilizations produce such signs (years).
"""
print(multiline_str)
print("This program gives you the opportunity to enter specific values to create an estimate of intelligent civilizations.")
print("Percentages should be entered as integer values and not decimals (eg 40, not .40).")
print()

#get inputs
fp = int(input('What percentage of stars have planets? '))
print()
if fp > 100:
    print("Value is more than 100 percent")
    print()
    fp = int(input('What percentage of stars have planets? '))
    print()
else:
    pass

ne = int(input('How many stars with planets can support life? '))
print()

fl = int(input('What percentage of planets produce life? '))
print()
if fl > 100:
    print("Value is more than 100 percent")
    print()
    fl = int(input('What percentage of planets produce life? '))
    print()
else:
    pass

fi = int(input('What percentage of planets produce intelligent life? '))
print()
if fi > 100:
    print("Value is more than 100 percent")
    print()
    fi = int(input('What percentage of planets produce intelligent life? '))
    print()
else:
    pass

fc = int(input('What percentage of civilizations produce detectable signals? '))
print()
if fc > 100:
    print("Value is more than 100 percent")
    print()
    fc = int(input('What percentage of civilizations produce detectable signals? '))
    print()
else:
    pass

L = int(input('How many years will these civilizations produce these signals? '))
print()

#calculate values
detectable_civilizations = (7 * (fp/100) * ne * (fl/100) * (fi/100) * (fc/100) * L)

#display results
print("Based on the values entered....")
print(f"there are an estimated {math.floor(detectable_civilizations)} potential detectable civilizations in the Milky Way")
print()
