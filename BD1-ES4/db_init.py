import sqlite3
import subprocess

subprocess.run(['rm', 'BD1-ES4.db'])

data_utente = [
    (1, 'Mario', 'Rossi', 'Via Roma 123', '123-4567890'),
    (2, 'Laura', 'Bianchi', 'Via Milano 456', '987-6543210'),
    (3, 'Giovanni', 'Verdi', 'Corso Italia 789', '555-1234567'),
    (4, 'Elena', 'Neri', 'Viale Europa 321', '333-7890123'),
    (5, 'Alessia', 'Marroni', 'Piazza Garibaldi 567', '777-2345678'),
    (6, 'Luca', 'Gialli', 'Via Napoli 890', '444-8765432'),
    (7, 'Francesca', 'Verdi', 'Corso Roma 234', '999-3456789'),
    (8, 'Marco', 'Blu', 'Viale Milano 567', '111-9876543'),
    (9, 'Anna', 'Rosa', 'Piazza Venezia 876', '666-5432109'),
    (10, 'Paolo', 'Giallo', 'Corso Napoli 123', '222-6789012')
]

data_prestito = [
    ('A1', 1, '2023-03-01', '2023-03-15'),
    ('B2', 2, '2023-04-10', '2023-04-25'),
    ('C3', 3, '2023-05-20', '2023-06-05'),
    ('D4', 4, '2023-06-02', '2023-06-20'),
    ('E5', 5, '2023-07-15', '2023-08-01'),
    ('F6', 6, '2023-08-20', '2023-09-05'),
    ('G7', 7, '2023-09-05', '2023-09-20'),
    ('H8', 8, '2023-10-02', '2023-10-15'),
    ('I9', 9, '2023-11-10', '2023-11-25'),
    ('J10', 10, '2023-12-15', '2023-12-30'),
    ('J10', 5, '2023-12-15', '2023-12-30'),
    ('K11', 1, '2024-01-05', '2023-09-20'),
    ('L12', 2, '2024-02-10', '2023-09-20')
]

data_copia = [
    ('A1', '978-1234567890', '2010-01-15', 20.50),
    ('B2', '978-0987654321', '2012-02-20', 18.75),
    ('C3', '978-0123456789', '2014-03-10', 15.00),
    ('D4', '978-5678901234', '2016-04-05', 25.99),
    ('E5', '978-6789012345', '2018-05-12', 22.50),
    ('F6', '978-3456789012', '2020-06-18', 19.99),
    ('G7', '978-8901234567', '2022-07-25', 17.50),
    ('H8', '978-2345678901', '2024-08-30', 23.75),
    ('I9', '978-9012345678', '2026-09-05', 21.00),
    ('J10', '978-4567890123', '2029-10-10', 18.25)
]

data_libro = [
    ('978-1234567890', 'Il Libro Magico', 2022, 'Editore XYZ', 'Autore A', 'Fantasy'),
    ('978-0987654321', 'Programmazione in Python', 2021, 'LibriTech', 'Guido van Rossum', 'Informatica'),
    ('978-0123456789', 'Storia di una Famiglia', 2023, 'LibriUni', 'Autore B', 'Romanzo'),
    ('978-5678901234', 'Guida alla Fotografia', 2020, 'FotoEdizioni', 'Fotografo C', 'Fotografia'),
    ('978-6789012345', 'La Cucina Italiana', 2019, 'GustoLibri', 'Chef D', 'Cucina'),
    ('978-3456789012', 'Viaggio nel Tempo', 2022, 'AvventuraEd', 'Scrittore E', 'Avventura'),
    ('978-8901234567', 'Le Origini dell\'Universo', 2021, 'CosmoLibri', 'Astronomo F', 'Scienza'),
    ('978-2345678901', 'Arte Moderna', 2020, 'ArteEdizioni', 'Artista G', 'Arte'),
    ('978-9012345678', 'Poesie d\'Amore', 2023, 'CuoreEd', 'Poeta H', 'Poesia'),
    ('978-4567890123', 'Il Segreto del Successo', 2022, 'SapienzaLibri', 'Mentor I', 'Motivazionale'),
    ('978-1111222233', 'Il Mistero del Caso Giallo', 2015, 'GialloEd', 'Detective J', 'Giallo')
]

con = sqlite3.connect("BD1-ES4.db")
cur = con.cursor()

cur.execute("CREATE TABLE UTENTE(Codice primary key, Nome, Cognome, Indirizzo, Telefono)")
cur.execute("CREATE TABLE PRESTITO(Collocazione, CodUtente, DataPrestito date, DataResa date, primary key(Collocazione, CodUtente, DataPrestito), foreign key (CodUtente) references UTENTE (Codice))")
cur.execute("CREATE TABLE COPIA(Collocazione primary key references PRESTITO, ISBN, DataAcquisizione date, Costo)")
cur.execute("CREATE TABLE DATILIBRO(ISBN primary key references COPIA, Titolo, AnnoPub, CasaEd, PrimoAut, Genere)")

cur.executemany("INSERT INTO UTENTE VALUES(?, ?, ?, ?, ?)", data_utente)
cur.executemany("INSERT INTO PRESTITO VALUES(?, ?, ?, ?)", data_prestito)
cur.executemany("INSERT INTO COPIA VALUES(?, ?, ?, ?)", data_copia)
cur.executemany("INSERT INTO DATILIBRO VALUES(?, ?, ?, ?, ?, ?)", data_libro)

for i in range(1, 101):
    isbn = f'978-{str(i).zfill(10)}'
    titolo = f'Libro Giallo {i}'
    anno_pub = i+1920
    casa_ed = 'CasaEdizioneUnica'
    primo_aut = f'AutoreGiallo{i}'
    genere = 'Giallo'

    cur.execute('''
        INSERT INTO DATILIBRO (ISBN, Titolo, AnnoPub, CasaEd, PrimoAut, Genere)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (isbn, titolo, anno_pub, casa_ed, primo_aut, genere))

con.commit()
