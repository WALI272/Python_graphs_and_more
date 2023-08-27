# Precipitaciones en MM (contando nieve derretida)
import matplotlib.pyplot as plt 

año = [1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983,
        1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994,
          1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
            2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
              2017, 2018, 2019, 2020, 2021, 2022]
# Dias de granizo
Dias_de_granizo= [10, 3, 9, 4, 4, 4, 4, 4, 5, 5, 6, 7, 7, 6, 8, 9, 10,
                  7, 3, 2, 4, 3, 3, 2, 7, 6, 2, 1, 3, 7, 3, 3,
                  2, 1, 7, 4, 2, 3, 11, 5, 2, 0, 4, 6, 8, 3, 2,
                  2, 2, 2]
    
fig, ax = plt.subplots()

ax.plot(año, Dias_de_granizo)

ax.set_xlabel('Year')
ax.set_ylabel('Dias_de_granizo')

plt.show()