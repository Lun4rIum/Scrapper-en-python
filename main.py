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
