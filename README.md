# Simple Flask App [![Build Status](https://travis-ci.org/akubicz/se_hello_printer_app.svg?branch=master)](https://travis-ci.org/akubicz/se_hello_printer_app)

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

  # Status aplikacji
Aplikacja monitorowana z wykorzystaniem StatusCake
  [![App Status](https://app.statuscake.com/button/index.php?Track=5902157&Days=1&Design=2)](https://app.statuscake.com/UptimeStatus.php?tid=5902157)

- W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowisko dla aplikacji:

  # == TWORZENIE WIRTUALNEGO SRODOWISKA ==
  ```
  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  $ python3 -m venv .venv

  # aktywowanie hermetycznego środowiska
  $ source .venv/bin/activate

  # instalacja requirements
  $ make deps

  # $ pip install -r requirements.txt
  # $ pip install -r test_requirements.txt

  # zobacz
  $ pip list
  ```

  Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) oraz [biblioteki flask](http://flask.pocoo.org).


  # == URUCHAMIANIE APLIKACJI==

- Uruchamianie applikacji:
  $ make run

  ```
  # jako zwykły program
  # $ python main.py
  # albo:
  # $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):
  $ make test
  ```
  # $ PYTHONPATH=. py.test
  # $ PYTHONPATH=. py.test --verbose -s
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:
m
  ```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja
  $ source .venv/bin/activate
  ```

  # == INTEGRACJA Z TRAVIS CI==

- Integracja z TravisCI:

  ```
  # dodaj do repozytorium plik .travis.yml
  #language: python
python:
- "3.6"
install:
- make deps
script:
- make test
  ```

# Pomocnicze

## Ubuntu

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Centos

- Instalacja docker-a:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```
