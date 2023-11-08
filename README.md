# poec-tp-docker
##Create poec-tp-docker repository in GITHUB
- # On Pycharm: 
. Create a python script src/calc.py 
. create main.py, dans ce fichier on crée la fonction qui print les valeurs 
- Create Docker file 
- Create requirements.txt
- Test_calc.py c'est dans ce fichier où se fait le calcul, 
- Create in calc.py, the fonctions. 
. This fonction applicate % of TVA with 
. % of TVA must be between 0 and 100. 
- If % of TVA not between 0 and 100.
- If % of TVA, is not a number.
- Fonction exception.
- Price must be a positif number

- pour faire tourner main.py dans docker, taper :
  docker build -t tp-docker .
  ensuite:
  docker run -it tp-docker python src/main.py 100 20
- 

  
  
