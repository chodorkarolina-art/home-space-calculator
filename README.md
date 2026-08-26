# HomeSpace Calculator

HomeSpace Calculator to aplikacja webowa napisana w Django, która pomaga
oszacować minimalną i rekomendowaną powierzchnię mieszkania na podstawie
liczby mieszkańców, stylu życia oraz dodatkowych potrzeb użytkownika.

## Główne funkcje

Aplikacja umożliwia:

- obliczenie minimalnej powierzchni funkcjonalnej,
- obliczenie rekomendowanej powierzchni mieszkania,
- określenie rekomendowanej liczby pokoi,
- uwzględnienie liczby dorosłych i dzieci,
- uwzględnienie zwierząt,
- uwzględnienie pracy zdalnej,
- uwzględnienie hobby i sportu,
- uwzględnienie liczby rowerów,
- uwzględnienie potrzeb związanych z przechowywaniem,
- wyświetlenie podziału powierzchni na główne funkcje,
- wyświetlenie szczegółów i założeń dla pomieszczeń,
- rejestrację i logowanie użytkowników,
- zapis obliczeń zalogowanego użytkownika,
- przeglądanie historii obliczeń,
- edycję zapisanych obliczeń,
- usuwanie zapisanych obliczeń,
- ochronę danych pomiędzy użytkownikami.

## Technologie

Projekt wykorzystuje:

- Python 3.12
- Django 6.1
- PostgreSQL 17
- HTML
- CSS
- python-dotenv
- psycopg2-binary
- Git
- GitHub
- Docker
- Docker Compose
- GitHub Actions

## Baza danych

Aplikacja korzysta z PostgreSQL.

Dane połączenia do bazy są pobierane ze zmiennych środowiskowych,
a nie przechowywane bezpośrednio w kodzie projektu.

Przykładowa konfiguracja znajduje się w pliku:

```text
.env.example