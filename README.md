# Scrapper-en-python
Scrapper des données signifie récuperer des données pour les traiter où les analyser. En python, il y'a 2 grands moyens de scrapper, tout d'abord en utilisant la librairie selenium, qui va simuler un navigateur, ou en utilisant request pour récuperer le code source et BeautifulSoup4 pour la traiter. Dans ce tuto, nous verrons uniquement la première méthode, pourquoi ? Car nous allons nous connecter à un compte et qu'il est bien plus simple de le faire avec selenium en evnoyant des touches de clavier dans les input que d'envoyer des requêtes HTTP.

#Utiliser selenium :

Pour uriliser selenium, nous allons tout d'abord l'installer avec ```pip install Selenium```, puis nous allons avoir besoin de "WebDriver", c'est une petit programme qui est crée par le navigateur pour être utilisé par une machine. Dans notre tuto nous allons utiliser firefox, donc il nous faudra les "geckodriver", vous pouvez l'installer en ligne a partir de ce lien : https://github.com/mozilla/geckodriver/releases (il vous faudra bien évidemment Firefox installé).

#Le code et les explications :

tout d'abord, nous allons importer le webdriver selenium et le module Key qui nous permettra de simuler des touches de clavier, pour cela nous allons rédiger comme cela :

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```
nous allons maintenant définir le chemin d'accès au geckodriver pour que notre programme puisse l'utiliser, 
``` 
path= "CHEMIN D'ACCES DE VOTRE GECKODRIVER"
``` 
nous allons maintenant définir la variable driver, qui nous permettra de démarrer notre navigateur et d'intéragir avec le site :
```
driver = webdriver.Firefox(executable_path=path)
```
la variable "executable_path" indique à selenium que notre geckodriver se trouve à la variable "path", qui souvenez vous, contient notre chemin d'accès.
Nous pouvons maintenant aller sur notre site, pour ma part, je vais prendre ecoledirecte, qui est un site qui répértorie les notes, devoirs, et agenda des élèves (ce site est mis en place par les établissement scolaire), mon objectif va être de calculer ma moyenne, car celle-ci n'est pas affiché sur le site. néanmoins nous avons les notes de chaque matière, (voir image ci-dessous)
![alt text](https://github.com/Lun4rIum/Scrapper-en-python/blob/main/images/Capture%20d’écran%202021-12-05%20151419.png?raw=true)
