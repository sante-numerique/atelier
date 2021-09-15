
## Automne 2021 - Atelier # 1 - 16 septembre 2021

*(English version will follow)*

Invités : *Tariq Daouda* CEO Bluwr, *Albert Feghaly* IRIC

Titre de l'atelier : **PyGeno, le module python pour manipuler les données omiques (génomique, transcriptomique et protéomique)**

## Instructions :
Afin de préparer l’atelier Code@Santé auquel vous allez participer et de profiter un maximum de la session de live coding, voici quelques instructions qui pourront vous seront utiles.
 
1. Si vous utilisez votre propre ordinateur: <br/>  
      Assurez-vous d’avoir une version de python >= 3.0 (https://www.python.org/downloads/). <br/>  
      Une version récente de jupyter-notebook vous sera également utile si vous voulez saisir les lignes de code proposées dans cet atelier (https://jupyter.org/) une à une.

2. Si vous voulez utiliser un notebook google colab comme nous le feront pendant l’atelier, il vous faudra une adresse gmail active. Vous pouvez alors simplement vous identifier (https://colab.research.google.com/notebooks/intro.ipynb). <br/>  
      *Notez que la version gratuite de google colab ne vous permet pas de conserver vos environnements actifs plus de 20h. Cela signifie que dès que vous fermez votre notebook ou que votre session est interrompue, vous perdez les installations qui y sont associées. Vous devrez donc procéder à une nouvelle installation de PyGeno lors de votre reconnexion.*
 
Que vous ayez adopté une solution locale ou en ligne, l’utilisation de PyGeno nécessite de télécharger un génome (ici le génome humain) et les annotations qui y sont associées. Ce processus prend habituellement 20 mn et occupe un espace disque de quelques GigaBases.
 
L’atelier débutant par une présentation de 30mn, vous aurez le temps de faire l’installation de PyGeno pendant cette introduction.
 
Pour cela, vous devrez d’abord procéder à l’installation du package :
 
                pip install pygeno
 
Il existe des alternatives à pip (voir https://github.com/tariqdaouda/pyGeno)
 
Puis installer les bases de données de la dernière version du génome humain :
 
from pyGeno.Genome import *
import pyGeno.bootstrap as B
B.importRemoteGenome('GRCh38.98')
 
Il se peut que l’installation échoue. Dans ce cas, il suffit de relancer la ligne de commande.
 
Le code qui sera analysé en détail est disponible dans github: 
https://github.com/sante-numerique/code_at_sante/blob/master/Septembre_Daouda_Feghaly/km_target_generator.py
 
-------------------------------------------------------------------------------

## Fall 2021 - Workshop # 1 - September 16, 2021

Guests :  *Tariq Daouda* CEO Bluwr, *Albert Feghaly* IRIC

Title of the workshop: **PyGeno, the python module for handling omics data (genomics, transcriptomics and proteomics)**

## Instructions :
To be sure that you take full advantage of the workshop, please follow these instructions:

1. If you use your personal computer: <br/>  
   Python >= 3.0 should be installed (https://www.python.org/downloads/). <br/>  
   We advise you to install a version of jupyter notebook (https://jupyter.org/)

2. An alternative is to use google colab, an online notebook which allows you to execute a python3 script line by line. <br/>  
   *First, you have to create a gmail address. Then, you have to login (https://colab.research.google.com/notebooks/intro.ipynb). Please keep in mind that your session is active for 20 hours. If you log out, you will have to start from scratch.*
 
In both cases, you have to download a human genome and associated annotations (> 3Gb of disk space needed). This process takes ~ 20 mn.
 
As the workshop will start with an overview of PyGeno, you can install the package and the genome database In the meantine.
 
To install PyGeno :
 
            pip install pygeno
 
Note that alternatives to pip exists (voir https://github.com/tariqdaouda/pyGeno)
 
Then install the last version of the human genome database :
 
from pyGeno.Genome import *
import pyGeno.bootstrap as B
B.importRemoteGenome('GRCh38.98')
 
     This step may fail. If this happens, simply rerun this part of the code.

The shared code is available on github: 
https://github.com/sante-numerique/code_at_sante/blob/master/Septembre_Daouda_Feghaly/km_target_generator.py
