import sqlite3

con = sqlite3.connect("BD1-ES4.db")
cur = con.cursor()

# es_1
cur.execute("""
            select Titolo
            from COPIA, DATILIBRO
            where COPIA.ISBN = DATILIBRO.ISBN and date(DataAcquisizione) >= date('2010-01-01') and date(DataAcquisizione) <= date('2010-12-31')
            order by Titolo
""")

# es_2
cur.execute("""
            select count(*)
            from PRESTITO
""")

# es_3
cur.execute("""
            select count(*), sum(Costo)/1000
            from COPIA
            where date(DataAcquisizione) >= date('2018-01-01') and date(DataAcquisizione) <= date('2018-12-31')
""")

# es_4
cur.execute("""
            select count(*)
            from DATILIBRO, COPIA, PRESTITO
            where DATILIBRO.Genere = 'Giallo' and DATILIBRO.ISBN = COPIA.ISBN and COPIA.Collocazione = PRESTITO.Collocazione
""")

# es_5
cur.execute("""
            select count(distinct ISBN)
            from COPIA
            where date(COPIA.DataAcquisizione) >= date('2020-01-01') and date(COPIA.DataAcquisizione) <= date('2020-12-31')
""")

# es_6
cur.execute("""
            select max(COPIA.Costo)
            from COPIA, DATILIBRO
            where COPIA.ISBN = DATILIBRO.ISBN and DATILIBRO.Titolo like 'i%'
""")

# es_7
cur.execute("""
            select min(date(DataAcquisizione))
            from COPIA
""")

# es_8
cur.execute("""
            select Codice
            from UTENTE
            where Nome like '%o' or Cognome like '_o%'
""")

# es_9
cur.execute("""
            select CodUtente, count(*)
            from PRESTITO
            group by CodUtente
""")

# es_10
cur.execute("""
            select CodUtente, Nome, count(*)
            from UTENTE, PRESTITO
            where UTENTE.Codice = PRESTITO.CodUtente
            group by CodUtente
""")

# es_11
cur.execute("""
            select Nome, CodUtente, count(distinct ISBN)
            from PRESTITO, COPIA, UTENTE
            where COPIA.Collocazione = PRESTITO.Collocazione and PRESTITO.CodUtente = UTENTE.Codice
            group by CodUtente
""")

# es_12
cur.execute("""
            select min(AnnoPub)
            from DATILIBRO
            where Genere = 'Giallo' and 
                CasaEd = (
                    select CasaEd
                    from DATILIBRO
                    where Genere = 'Giallo'
                    group by CasaEd
                    having count(distinct ISBN) >= 100
                )
""")

# es_13
cur.execute("""
            select ISBN
            from COPIA
            where date(DataAcquisizione) = date('2022-05-01') 
                intersect 
            select ISBN
            from COPIA
            where date(DataAcquisizione) = date('2022-06-01')
""")

# es_14
cur.execute("""
            select PrimoAut as Nome
            from DATILIBRO
                union 
            select Nome
            from UTENTE
""")

# es_15 
cur.execute("""
            select PrimoAut as Nome
            from DATILIBRO
                except
            select Nome 
            from UTENTE
""")

print(cur.fetchall())