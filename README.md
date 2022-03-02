# Scrapper-en-python
Scrapper des données signifie récuperer des données pour les traiter ou les analyser. En python, il y'a 2 grands moyens de scrapper, tout d'abord en utilisant la librairie selenium, qui va simuler un navigateur, ou en utilisant request pour récuperer le code source et BeautifulSoup4 pour le traiter. Dans ce tuto, nous verrons uniquement la première méthode, pourquoi ? Car nous allons nous connecter à un compte et qu'il est bien plus simple de le faire avec selenium en envoyant des touches de clavier dans les input que d'envoyer des requêtes HTTP. (néanmoins les requêtes sont beaucoup plus fiable car elles se basent sur l'API du site, qui ne sera jamais amené à changer, alors que selenium se base sur le site en lui même qui peut amener à changer (changement de design, refonte) ce qui a pour effet de ne plus faire fonctionner notre code)

## Utiliser selenium :

Pour uriliser selenium, nous allons tout d'abord l'installer avec ```pip install Selenium```, puis nous allons avoir besoin de "WebDriver", c'est une petit programme qui est crée par le navigateur et qui permet de le controler. Dans notre tuto nous allons utiliser firefox, donc il nous faudra les "geckodriver", vous pouvez l'installer en ligne a partir de ce lien : https://github.com/mozilla/geckodriver/releases (il vous faudra bien évidemment Firefox installé).

## Le code et les explications :

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
Nous pouvons maintenant aller sur notre site, pour ma part, je vais prendre ecoledirecte, qui est un site qui répértorie les notes, devoirs, et agenda des élèves (ce site est mis en place par les établissements scolaires), mon objectif va être de calculer ma moyenne générale, car celle-ci n'est pas affiché sur le site. Néanmoins nous avons les notes de chaque matière, (voir image ci-dessous)
![alt text](https://github.com/Lun4rIum/Scrapper-en-python/blob/main/images/Capture%20d’écran%202021-12-05%20151419.png?raw=true)

## phase pratique :

Tout d'abord, il faut analyser le site, pour acceder à cette fameuse page contenant les notes (https://www.ecoledirecte.com/Eleves/0001/Notes), il faut passer une page de connexion qui demande un nom d'utilisateur et un mot de passe, ensuite, il faut récuperer les moyennes dans le code source, créer une variable nbrMoyenne contenant le nombre de moyenne, les additioner puis divisier le tout par nbrMoyenne. Ok, challenge accepted.

nous allons indiquer à selenium sur quelle page il doit se rendre (en l'occurence https://www.ecoledirecte.com/Eleves/0001/Notes) :
```
driver.get("https://www.ecoledirecte.com/Eleves/0001/Notes")
```
ensuite, nous allons chercher le xpath des éléments input qui nous intéressent (langage d'interrogation simple d'emploi, selon wikipédia).

Pour faire simple, le XPATH est un chemin qui permet de sélectionner un élément de la page web à partir des balyses. Par exemple, si on a un site web :
```
<html>
  <body>
    <div>
      <h1>Titre1</h1>
    </div>
    <div>
      <img src="symfunc.fr">
    </div>
  <body>
</html>
```
Le XPATH de l'élément **Titre1** correspond à : 
```
/html/body/div/h1
```
Et celui de l'**image** est :
```
/html/body/div[2]/img
```

Pour récuperer ce fameux xpath, il suffit d'aller sur le site qui nous intéresse, faire clique droit inspecter l'élément sur l'input qui nous intéresse, et dans le code source, clique droit -> copy -> full xpath (sinon voir image en dessous).

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
Et voila, selenium sait ou sont les éléments que nous avons demandé, maintenant, il s'agirait de les remplir avec nos informations de connexion non ? 
pour cela rien de plus simple :

```
username.send_keys("VOTRE NOM D'UTILISATEUR")
password.send_keys("VOTRE MOT DE PASSE")
```
Ensuite pour nous connecter, nous pouvons soit utiliser la touche entrée du clavier, soit trouver le bouton de connexion et cliquer dessus, personnelement j'ai opté pour la seconde option car cela nous permet de voir l'intéraction avec les éléments :

```
login = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/button').click()
```
Et oui, pour cliquer on doit juste rajouter le .click() à la fin de notre variable, fastoche non ?

Dans notre exemple, vu que nous avons demandé la page "https://www.ecoledirecte.com/Eleves/0001/Notes", le site va nous rediriger automatiquement sur l'onglet note, sinon vous pouvez utiliser le .click() et le xpath pour trouver la page dans un menu.
Nous sommes maintenant sur la fameuse page de notes. C'est maintenant que ça devient intéressant. En analysant le code source, nous pouvons voir que les moyennes sont contenus dans des balises <span>, sous forme de texte. Voilà le code source
  
![alt text]( https://github.com/Lun4rIum/Scrapper-en-python/blob/main/images/Capture%20d’écran%202021-12-05%20153723.png?raw=true)
 
Comme nous pouvons le voir, la balise <span> n'a pas d'ID ou de classe. Mais la balise <td> a la classe "relevemoyenne", parfait, pourquoi ? Car toutes les autres ont aussi la balise, ce qui va nous permettre de tout récupérer d'un coup en utilisant la commande
```
moyennes = driver.find_elements_by_class_name("relevemoyenne")
```
Comme vous le voyez, elements prend un S, cela dit à selenium de lister tous les éléments possédant la même classe, mais si vous faites ``` print(moyennes)``` vous verrez que cela n'affiche que du texte incompréhensible. C'est normal, selenium à récuperer les éléments mais pas le texte, pour récuperer celui-ci, nous allons faire :
```
for elem in moyennes:
    print(elem.text)
```
Soit pour tous les éléments dans moyennes, écrire : le texte contenu dans ces éléments. Et là si vous faites un print(), magie ! Ca fonctionne. Mais ne criez pas victoire trop vite ce n'est pas fini. Nous voulons calculer la moyenne général. Et pour cela, nous allons supprimer l'élément 0 de notre liste de moyennes, pourquoi ? Car il avait aussi la classe "relevemoyenne" mais c'est le texte Moyenne au dessus des vrais moyennes. Voila comment nous allons faire :
  
```
ls = []
for elem in moyennes:
  ls.append(elem.text.replace(",","."))
```
Là, je remplace les , de mes moyennes par des . sinon python ne comprend pas que ce sont des nombres, puis je les ajoutes à la liste ls[] que j'ai crée juste avant
```
del ls[0]
del ls[-1]
```
Je supprime l'élément 0 qui est "MOYENNES" et l'élément -1 (dernier élément de la liste) qui est vide car je suis dispensé de sport et je n'ai donc aucune moyenne
```
ls = [ float(x) for x in ls ]
``` 
je convertis mes valeurs en "float" (nombre décimaux)
  
```
nbrMoyenne = len(ls)
ls = sum(ls)
ls = ls / nbrMoyenne
print(ls)
driver.quit()
```
- Je définis le nombre de moyennes dans ma liste avec nbrMoyenne
- J'additionne tous les éléments de ma liste
- Je divise la somme de l'adition par le nombre de moyennes
- J'écris le résultat dans ma console
- Et enfin, je quitte Firefox.
  
 Et voilà ! j'ai ma moyenne général. Alors oui, il y'a un inconvéniant à cette méthode, c'est le temps. En effet, vu que Selenium simule un navigateur, il prend énormement de temps à charger les pages, c'est pour ça que parfois vous aurez l'erreur "Unable to locate element:". Pour y remédier importer le module time et faites des pauses entre chaque page que vous charger, ce qui donnerait ça :
  
```
import time
  
//PAGE
time.sleep(2)
//AUTRE PAGE
time.sleep(2)
```
  
Voilà ! J'espère que ce cours vous aura été utile. (Et voilà le code final que vous pouvez retrouver aussi dans main.py)
  
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path ="VOTRE PATH GECKODRIVER"

driver = webdriver.Firefox(executable_path=path)

driver.get('https://www.ecoledirecte.com/Eleves/0001/Notes')

username = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[1]')
password = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[2]')

username.send_keys("VOTRE USERNAME")
password.send_keys("VOTRE MOT DE PASSE")

login = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/button').click()
time.sleep(5)
  
#j'ai mis ça en commentaire car cela me permettai d'avoir les notes du premier trimestres, plus complètes que celles du second
#trimestre = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/eleve-note/div/div/ul/li[1]/a').click()
#time.sleep(5)

moyennes = driver.find_elements_by_class_name("relevemoyenne")
ls = []
for elem in moyennes:
  ls.append(elem.text.replace(",","."))
del ls[0]
del ls[-1]
ls = [ float(x) for x in ls ]
nbrMoyenne = len(ls)
ls = sum(ls)
ls = ls / nbrMoyenne
print(ls)
driver.quit()
```
Merci à BiMathAx pour l'ajout d'informations !
