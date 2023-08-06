# Circé modification du pipeline

Branche créée à partir du dépôt : https://git.unicaen.fr/fnso/i-fair-ir/xsl-tei-circe/-/tree/md/circe-transfo


Voir documentation rédigée par Jean-François sur le wiki du redmine : https://redmine.unicaen.fr/Etablissement/projects/fnso-i-fair-ir/wiki/Documentation_usage


- venv : dépendance installée au niveau du virtual env (et non au niveau de la machine)
  - création des dépendances via la commande `python3 -m venv venv` puis de l'activer `. ./venv/bin/activate`
- nom du module : `doc2tei`
- la fonction est définie dans le fichier `doc2tei/init.py`



- transformation `doc2tei` (l.152)

  - dossier de travail
  - logger
  - dictionnaire (tableau clé/valeur) 

  > attention, les espaces sont signifiants dans la syntaxe



En détails

- l. 51 `_process_doc`
- l. 59 lancement de la commande libre office
- l. 69 définition de la sortie standard (`stdout`), l. 70 sortie erreur (`stderr`)
  - pour l'instant, si pas d'erreur, on prend la sortie standard



Là on veut lancer la transformation depuis les sources, deux solutions : 

- `python setup.py install` (prend le dossier doc2tei et va le copier à l'endroit où sont les librairies python)
- ou alors on peut lancer le module en précisant dans les infos de circé : `CIRCE_TRANSFORMATIONS_MODULE=doc2tei circe run`



On relance l'environnement.



Journal d'événements : système clé/valeur ;

- `logger.info` (niveau info) exemple l. 107
  - message
  - date

vs logger.stderr



Attraper les erreurs de validation (information) et de transformation saxon (erreur) 

retourne booleen et chaîne 



fonction appelable directement sans interface : `from doc2tei import _process_doc`

