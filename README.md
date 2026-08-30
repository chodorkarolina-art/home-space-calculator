# **HomeSpace Calculator**

HomeSpace Calculator to aplikacja webowa napisana w Django, która pomaga
oszacować minimalną i rekomendowaną powierzchnię mieszkania na podstawie
liczby mieszkańców, stylu życia oraz dodatkowych potrzeb użytkownika.

## **Główne funkcje**

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

## **Technologie**

Projekt wykorzystuje:

- Python 3.12
- Django 6.1
- Django REST Framework
- PostgreSQL 17
- HTML
- CSS
- python-dotenv
- psycopg2-binary
- WhiteNoise
- Gunicorn
- Nginx
- Docker
- Docker Compose
- Git
- GitHub
- GitHub Actions
- AWS EC2
- Let's Encrypt
- Certbot

## **Baza danych**

Aplikacja korzysta z PostgreSQL.

Dane połączenia do bazy są pobierane ze zmiennych środowiskowych,
a nie przechowywane bezpośrednio w kodzie projektu.

Przykładowa konfiguracja znajduje się w pliku:

```text
.env.example
```

## **REST API**

Projekt wykorzystuje Django REST Framework.

API umożliwia dostęp do danych obliczeń poprzez endpoint:

```text
/api/calculations/
```

## **Testy**

Projekt posiada zestaw automatycznych testów Django.

Aktualnie aplikacja posiada:

```text
40 testów automatycznych
```

Testy można uruchomić poleceniem:

```bash
python manage.py test
```

Testy są również automatycznie uruchamiane przez GitHub Actions w ramach procesu CI.

## **Docker**

Aplikacja posiada konfigurację Docker dla środowiska deweloperskiego
oraz produkcyjnego.

Konfiguracja produkcyjna znajduje się w pliku:

```text
docker-compose.prod.yml
```

Środowisko produkcyjne składa się z trzech głównych usług:

- `db` — PostgreSQL,
- `web` — Django uruchamiane przez Gunicorn,
- `nginx` — reverse proxy obsługujący ruch HTTP i HTTPS.

## **Deployment**

Aplikacja została wdrożona na AWS EC2.

Architektura produkcyjna:

```text
Internet
   |
   v
HTTPS :443
   |
   v
Nginx
   |
   v
Gunicorn
   |
   v
Django
   |
   v
PostgreSQL
```

Nginx pełni funkcję reverse proxy i przekazuje żądania do aplikacji
Django uruchomionej przez Gunicorn.

Ruch przychodzący przez HTTP na porcie 80 jest automatycznie
przekierowywany na HTTPS.

## **HTTPS**

Połączenie z aplikacją produkcyjną jest zabezpieczone przez HTTPS.

Certyfikat TLS jest wystawiany przez Let's Encrypt przy użyciu Certbota.

Dla certyfikatu skonfigurowano:

- automatyczne odnawianie przez Certbot,
- ACME challenge obsługiwany przez Nginx,
- automatyczny reload Nginxa po odnowieniu certyfikatu.

## **CI**

Projekt wykorzystuje GitHub Actions do Continuous Integration.

Po wysłaniu zmian do repozytorium wykonywane są automatyczne testy
aplikacji przed dalszym wdrażaniem zmian.

## **Bezpieczeństwo**

W konfiguracji produkcyjnej:

- `DEBUG` jest wyłączony,
- `SECRET_KEY` jest przechowywany w zmiennych środowiskowych,
- dane dostępowe PostgreSQL nie znajdują się w kodzie,
- prywatny klucz TLS nie jest przechowywany w repozytorium,
- Django działa za reverse proxy Nginx,
- aplikacja korzysta z HTTPS,
- Django obsługuje ochronę CSRF,
- dane poszczególnych użytkowników są od siebie odseparowane.

## **Status projektu**

Aplikacja działa w środowisku produkcyjnym na AWS EC2.

Aktualnie działają:

- kalkulator powierzchni,
- system rekomendacji powierzchni,
- rejestracja i logowanie,
- historia obliczeń,
- edycja i usuwanie obliczeń,
- PostgreSQL,
- Django Admin,
- REST API,
- Docker,
- Docker Compose,
- Gunicorn,
- Nginx,
- HTTPS,
- automatyczne odnawianie certyfikatu,
- GitHub Actions CI,
- automatyczne testy.

## **Licencja**

Projekt jest udostępniany na licencji MIT.

Pełna treść licencji znajduje się w pliku:

```text
LICENSE
```