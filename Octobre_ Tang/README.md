
## Automne 2021 - Atelier # 2 - 14 octobre 2021

*(English version will follow)*

# Titre : TorchDrug: A powerful and flexible machine learning platform for drug discovery

# Invités : *Jian Tang* HEC, MILA


## Résumé 
Pour cette présentation, nous allons introduire un outil open-source utilisant l'apprentissage machine appliqué à la découverte de médicaments. Cette application, nommée TorchDrug, a été développée par notre groupe dans le but rendre disponibles gratuitement des outils logiciels d'intelligence artificielle pour la découverte de médicaments.

## Instructions
Afin de préparer l’atelier Code@Santé auquel vous allez participer et de profiter un maximum de la session de programmation en direct, voici quelques instructions qui vous seront utiles :
 
 
### Setup
#### *Option 1: ordinateur personnel*
Assurez-vous d’avoir 
* une version de python >= 3.7 (https://www.python.org/downloads/) 
* une version de PyTorch >= 1.4.0. 
* Une version récente de jupyter-notebook si vous voulez saisir une à une les lignes de code proposées dans cet atelier (https://jupyter.org/). 

#### *Option 2: notebook de type « Google Colab »*
Cette option sera utilisée pendant l'atelier. 

Il vous faudra une adresse gmail active. Vous pouvez alors simplement vous identifier (https://colab.research.google.com/notebooks/intro.ipynb). Notez que la version gratuite de Google Colab ne vous permet pas de conserver vos environnements actifs plus de 20h. Cela signifie que dès que vous fermez votre notebook ou que votre session est interrompue, vous perdez les installations qui y sont associées. Vous devrez donc procéder à une nouvelle installation de Torchdrug lors de votre reconnexion.   

### Contenu de l'Atelier
Nous aborderons deux composantes de TorchDrug qui correspondent à deux notebooks. Dans chacun d’entre eux, quelques lignes de commandes sont volontairement manquantes et seront complétées pendant la session de code. 

1)	Les représentations moléculaires pré-entrainées :  
Contexte : TorchDrug-Website_Pretrain_molecular_representations: https://torchdrug.ai/docs/tutorials/pretrain

Notebook Colab : Google-Colab_Pretrain_molecular_representations: https://colab.research.google.com/drive/1jCCQYGq5ladDgysN3fGFmNMr_9-hEb_L

2)	Conception de molécules de novo et recherche en faisceau:
Contexte : TorchDrug-Website_De_novo_design: https://torchdrug.ai/docs/tutorials/generation.html

Notebook Colab : Google-Colab_De_novo_molecule_design: https://colab.research.google.com/drive/1g0fjyZ8g3JAtMuv83DV9jjqxOd0IY5s4

### Informations Supplémentaires
Quelques sources utiles pour comprendre pourquoi et comment TorchDrug a été développé dans un contexte de découverte de médicaments : 

* Site TorchDrug avec tutoriels : https://torchdrug.ai/
* Présentation de Jian Tang sur l’utilisation des « graph neural networks » (GNNs) dans un contexte de découverte de médicaments : https://drive.google.com/file/d/19e0scMh4Fxzsbq6a8Z9idsYcsnLAgYAx/view
* Vidéo explicative très complète sur les graph neural networks  par Miltos Allamanis : https://www.youtube.com/watch?v=zCEYiCxrL_0&ab_channel=MicrosoftResearch
* L’utilisation des GNNs en chimie par Andrew Smith : https://dmol.pub/dl/gnn.html

-------------------------------------------------------------------------------

## Fall 2021 - Workshop # 2 - October 14, 2021


# Title: Title of the workshop: TorchDrug: A powerful and flexible machine learning platform for drug discovery

# Guests :  *Jian Tang* HEC, MILA


## Summary
In this presentation, we are going to introduce an open-source machine learning framework for drug discovery developed at my group, TorchDrug, aiming at making AI drug discovery software and libraries freely available to the research community.

## Instructions
To prepare for the Code@Santé workshop and participate in the live coding session, please follow these instructions. 

### Setup
#### *Option 1: personnal computer*
It is recommended that you have :  
* a version of Python >= 3.7 (https://www.python.org/downloads/). 
* a version of PyTorch >= 1.4.0 
* a recent installation of Jupyter Notebook to follow the workshop line by line (https://jupyter.org/)

#### *Option 2: notebook of type « Google Colab »*
This option will be used during the workshop.

First, you have to create a gmail address if you don’t have one.  Then, you have to login (https://colab.research.google.com/notebooks/intro.ipynb). Please keep in mind that your session is active for 20 hours. If you log out, you will have to start from scratch. 
 
 
### Live Coding
Please be aware that some some lines are missing. This is intentional and will be filled by the participants during the presentation. The hand-on part of this tutorial includes two Colab notebooks.

1) Pretrain molecular representations
Background : TorchDrug-Website_Pretrain_molecular_representations: https://torchdrug.ai/docs/tutorials/pretrain

Colab notebook : Google-Colab_Pretrain_molecular_representations: https://colab.research.google.com/drive/1jCCQYGq5ladDgysN3fGFmNMr_9-hEb_L

2) De novo molecule design & beam search:
Background : TorchDrug-Website_De_novo_design: https://torchdrug.ai/docs/tutorials/generation.html

Colab notebook: Google-Colab_De_novo_molecule_design: https://colab.research.google.com/drive/1g0fjyZ8g3JAtMuv83DV9jjqxOd0IY5s4

### Supplemental Information
Some useful resources to better understand why and how TorchDrug was developed in the context of drug design  : 
* TorchDrug website with tutorials : https://torchdrug.ai/
* Jian Tang’s presentation about « graph neural networks » (GNNs) : https://drive.google.com/file/d/19e0scMh4Fxzsbq6a8Z9idsYcsnLAgYAx/view
* An overview of  GNNs by Miltos Allamanis : https://www.youtube.com/watch?v=zCEYiCxrL_0&ab_channel=MicrosoftResearch
* GNNs in chemistery by Andrew Smith : https://dmol.pub/dl/gnn.html
