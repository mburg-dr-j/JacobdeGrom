import pandas

# I am assuming you've gotta throw a minimum number of pitches before calling it
# a real start.  This is obviously not how baseball is doing things yet, but
# maybe it should.
minPit = 60

# I will call it a High Quality Start if the pitcher throws a minimum number
# of pitches and allows 1 or 0 earned runs.

# Read in 2014 data
frame2014 = pandas.read_csv('2014.csv')
short2014 = pandas.concat([ frame2014['ER'], frame2014['Pit'], frame2014['Inngs'] ], axis=1)
# Calculate 2014 Real Starts (>= minimum number of pitches)
short2014['RealS'] = short2014['Pit'] > minPit
# Calculate 2014 High Quality Starts
short2014['HQS'] = (short2014['ER'] < 2) & (short2014['RealS'])

# Read in 2015 data
frame2015 = pandas.read_csv('2015.csv')
short2015 = pandas.concat([ frame2015['ER'], frame2015['Pit'], frame2015['Inngs'] ], axis=1)
# Calculate 2015 Real Starts (>= minimum number of pitches)
short2015['RealS'] = short2015['Pit'] > minPit
# Calculate 2015 High Quality Starts
short2015['HQS'] = (short2015['ER'] < 2) & (short2015['RealS'])

# Read in 2016 data
frame2016 = pandas.read_csv('2016.csv')
short2016 = pandas.concat([ frame2016['ER'], frame2016['Pit'], frame2016['Inngs'] ], axis=1)
# Calculate 2016 Real Starts (>= minimum number of pitches)
short2016['RealS'] = short2016['Pit'] > minPit
# Calculate 2016 High Quality Starts
short2016['HQS'] = (short2016['ER'] < 2) & (short2016['RealS'])

# Read in 2017 data
frame2017 = pandas.read_csv('2017.csv')
short2017 = pandas.concat([ frame2017['ER'], frame2017['Pit'], frame2017['Inngs'] ], axis=1)
# Calculate 2017 Real Starts (>= minimum number of pitches)
short2017['RealS'] = short2017['Pit'] > minPit
# Calculate 2017 High Quality Starts
short2017['HQS'] = (short2017['ER'] < 2) & (short2017['RealS'])

# Read in 2018 data
frame2018 = pandas.read_csv('2018.csv')
short2018 = pandas.concat([ frame2018['ER'], frame2018['Pit'], frame2018['Inngs'] ], axis=1)
# Calculate 2018 Real Starts (>= minimum number of pitches)
short2018['RealS'] = short2018['Pit'] > minPit
# Calculate 2018 High Quality Starts
short2018['HQS'] = (short2018['ER'] < 2) & (short2018['RealS'])

# Concatenate all seasons to get career totals
shortAll = pandas.concat([short2014, short2015, short2016, short2017, short2018], ignore_index=True)

print ("I am defining High Quality Start as throwing at least", minPit, "pitches, and allowing 1 or 0 earned runs.")

# Compute ratio of High Quality Starts for 2014
hqs2014 = len(short2014['HQS'].nonzero()[0])
all2014 = len(short2014['RealS'].nonzero()[0])
print('High Quality Starts, 2014:', hqs2014, "out of", all2014, "or", round(hqs2014 * 100 / all2014), "%" )

# Compute ratio of High Quality Starts for 2015
hqs2015 = len(short2015['HQS'].nonzero()[0])
all2015 = len(short2015['RealS'].nonzero()[0])
print('High Quality Starts, 2015:', hqs2015, "out of", all2015, "or", round(hqs2015 * 100 / all2015), "%" )

# Compute ratio of High Quality Starts for 2016
hqs2016 = len(short2016['HQS'].nonzero()[0])
all2016 = len(short2016['RealS'].nonzero()[0])
print('High Quality Starts, 2016:', hqs2016, "out of", all2016, "or", round(hqs2016 * 100 / all2016), "%" )

# Compute ratio of High Quality Starts for 2017
hqs2017 = len(short2017['HQS'].nonzero()[0])
all2017 = len(short2017['RealS'].nonzero()[0])
print('High Quality Starts, 2017:', hqs2017, "out of", all2017, "or", round(hqs2017 * 100 / all2017), "%" )

# Compute ratio of High Quality Starts for 2018
hqs2018 = len(short2018['HQS'].nonzero()[0])
all2018 = len(short2018['RealS'].nonzero()[0])
print('High Quality Starts, 2018:', hqs2018, "out of", all2018, "or", round(hqs2018 * 100 / all2018), "%" )

# Compute ratio of High Quality Starts for Career
hqsAll = len(shortAll['HQS'].nonzero()[0])
allAll = len(shortAll['RealS'].nonzero()[0])
print('High Quality Starts, Career:', hqsAll, "out of", allAll, "or", round(hqsAll * 100 / allAll), "%" )
