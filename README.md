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

#phase pratique :

Tout d'abord, il faut analyser le site, pour acceder à cette fameuse page contenant les notes (https://www.ecoledirecte.com/Eleves/0001/Notes), il faut passer une page de connexion qui demande un nom d'utilisateur et un mot de passe, ensuite, il faut récuperer les moyennes dans le code source, créer une variable nbrMoyenne contenant le nombre de moyenne, les additioner puis divisier le tout par nbrMoyenne. Ok, challenge accepted.

nous allons indiquer à selenium sur quelle page il doit se rendre (en l'occurence https://www.ecoledirecte.com/Eleves/0001/Notes) :
```
driver.get("https://www.ecoledirecte.com/Eleves/0001/CahierDeTexte")
```
ensuite, nous allons chercher le xpath des éléments input qui nous intéressent ( langage d'interrogation simple d'emploi, selon wikipédia)
pour récuperer ce fameux xpath, il suffit d'aller sur le site qui nous intéresse, faire clique droit inspecter l'élément sur l'input qui nous intéresse, et dans le code source, clique droit -> copy -> full xpath (sinon voir image en dessous).

![alt text](https://github.com/Lun4rIum/Scrapper-en-python/blob/main/images/2021-12-05%2015-20-47.gif?raw=true)

Bon, que faire de ce xpath ? nous allons le mettre dans une variable qui s'appelera username,

```
username = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[1]')
```
Comme vous le voyez, on utilise driver, qui est notre variable de navigateur, puis nous lui demandons de trouver l'élément grâce au xpath.
Nous allons répeter l'opération pour le mot de passe :
```
password = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[2]')
```
et voila, selenium sait ou sont les éléments que nous avons demandé, maintenant, il s'agirait de les remplir avec nos informations de connexion non ? 
pour cela rien de plus simple :

```
username.send_keys("VOTRE NOM D'UTILISATEUR")
password.send_keys("VOTRE MOT DE PASSE")
```
ensuite pour nous connecter, nous pouvons soit utiliser la touche entrée du clavier, soit trouver le bouton de connexion et cliquer dessus, personnelement j'ai opté pour la seconde option car cela nous permet de voir l'intéraction avec les éléments :

```
login = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/button').click()
```
et oui, pour cliquer on doit juste rajouter le .click() à la fin de notre variable, fastoche non ?
Dans notre exemple, vu que nous avons demandé la page "https://www.ecoledirecte.com/Eleves/0001/Notes", le site va nous rediriger automatiquement sur l'onglet note, sinon vous pouvez utiliser le .click() et le xpath pour trouver la page dans un menu.
Nous sommes maintenant sur la fameuse page de notes. C'est maintenant que ça devient intéressant. En analysant le code source, nous pouvons voir que les moyennes sont contenus dans des balises <span>, sous forme de texte. Voilà le code source
  
![alt text]( https://github.com/Lun4rIum/Scrapper-en-python/blob/main/images/Capture%20d’écran%202021-12-05%20153723.png?raw=true)
 
comme nous pouvons le voir, la balise <span> n'a pas d'ID ou de classe. Mais la balise <td> a la classe "relevemoyenne", parfait, pourquoi ? Car toutes les autres ont aussi la balise, ce qui va nous permettre de tout récupérer d'un coup en utilisant la commande
```
moyennes = driver.find_elements_by_class_name("relevemoyenne").text
```
comme vous le voyez, elements prend un S, cela dit à selenium de lister tous les éléments possédant la même classe, et le .text nous permet de relever tout le texte qui se trouve dans la balise <td> qui contient la classe "relevemoyenne".


