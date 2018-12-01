import pandas
import matplotlib

frame2014 = pandas.read_csv('2014.csv')

short2014 = pandas.DataFrame({
    'ER': frame2014['ER'],
    'Pit': frame2014['Pit'],
})

short2014['HQS'] = (short2014['ER'] < 2) & (short2014['Pit'] > 60)

print(short2014)
