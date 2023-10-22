import sqlite3

con = sqlite3.connect("BD1-ES4.db")
cur = con.cursor()

es_1 = cur.execute("""
    select Titolo
    from COPIA, DATILIBRO
    where COPIA.ISBN = DATILIBRO.ISBN and julianday(DataAcquisizione) >= julianday('2010-01-01') and julianday(DataAcquisizione) <= julianday('2010-12-31')
    order by Titolo
""")

es_2 = cur.execute("""
    select count(*)
    from PRESTITO
""")

es_3 = cur.execute("""
    select count(*), sum(Costo)/1000
    from COPIA
    where julianday(DataAcquisizione) >= julianday('2018-01-01') and julianday(DataAcquisizione) <= julianday('2018-12-31')
""")

es_4 = cur.execute("""
    select count(*)
    from DATILIBRO, COPIA, PRESTITO
    where DATILIBRO.Genere = 'Giallo' and DATILIBRO.ISBN = COPIA.ISBN and COPIA.Collocazione = PRESTITO.Collocazione
""")

es_5 = cur.execute("""
    select count(distinct ISBN)
    from COPIA
    where julianday(COPIA.DataAcquisizione) >= julianday('2020-01-01') and julianday(COPIA.DataAcquisizione) <= julianday('2020-12-31')
""")

es_6 = cur.execute("""
                   select max(COPIA.Costo)
                   from COPIA, DATILIBRO
                   where COPIA.ISBN = DATILIBRO.ISBN and DATILIBRO.Titolo like 'i%'
""")



print(es_6.fetchall())