Read this document in [english](README_en.md) -> il faut le faire 

# Projet : Optimisation de recommandation 

## Présentation 
Les réseaux sociaux sont omniprésents dans notre quotidien. Leur modélisation sous forme de graphes permet d’analyser des phénomènes complexes, parfois problématiques, tels que la formation de communautés fermées ou la diffusion biaisée de l’information.
Ce projet explore la manière dont une stratégie de recommandation peut influencer la structure du réseau : soit en favorisant des cycles fermés, créant ainsi des chambres d’écho, soit au contraire en élargissant les connexions en privilégiant les liens vers l’extérieur. L’objectif est d’implémenter, de comparer et d'analyser différentes stratégies sur un graphe social artificiel.

**Ce projet fait l'object d'un travail individuel**

## Problématique retenue

Comment concevoir, sur le graphe d’un réseau social, une stratégie de recommandation qui étend le réseau d’un utilisateur au-delà de son voisinage immédiat ?

## Objectifs 

Je me propose :
  - D’implémenter plusieurs algorithmes de recommandation d’amis sur des graphes sociaux artificiels ;
  - D’analyser leur impact sur la structure du réseau à l’aide de métriques telles que la modularité, le coefficient de clustering et le nombre de composantes connexes ;
  - De comparer les effets des stratégies fondées sur les liens d’amitié à celles basées sur la similarité d’intérêts (et une autre si j'en trouve);
  - D’interpréter les résultats obtenus pour mettre en évidence les phénomènes de fermeture ou d’ouverture du réseau social ;
  - De proposer des pistes d’amélioration pour diversifier les recommandations et limiter les effets de bulles relationnelles.


## Bibliographie commentée

Ce projet s’appuie sur des résultats à la fois théorique, issue d'implémentation et d'analyse de graphes, qui permettent une étude approfondie du sujet.
Les notions fondamentales telles que les cycles, les composantes connexes ou les fonctions de parcours de graphes ont été abordées dans le cadre des cours d’informatique du programme officielde MP2I/MPI [1]. Ces bases théoriques ont permis de poser les fondements nécessaires à l’analyse d’un graphe social.
Le calcul du coefficient de clustering, qui essentiel pour quantifier la densité locale dans un réseau, ainsi que la recherche des différentes métriques pouvant être utilisées pour l’analyse du graphe, s’appuient sur les explications détaillées proposées par GeeksForGeeks [2] et l’Insee [3], qui combinent une approche conceptuelle et une mise en œuvre algorithmique.
Pour la partie implémentation, la documentation officielle de networkx [4] a été utilisée pour générer, manipuler et afficher les graphes, explorer les communautés, mesurer la modularité et coder les stratégies de recommandation.
Une chaîne YouTube [5] a permis de mieux appréhender certains concepts d’informatique théorique, en apportant un appui pédagogique grâce à des visualisations clairesdurant les phases exploratoires du projet.

  [1] Programme officiel d’informatique de MP2I/MPI : https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/64/6/spe777_annexe_1373646.pdf
  [2] GeeksForGeeks, *Clustering Coefficient in Graph Theory* : https://www.geeksforgeeks.org/clustering-coefficient-graph-theory/
  [3] GeeksForGeeks, *Partitionnement et analyse de graphes* : https://www.insee.fr/fr/statistiques/fichier/3635442/imet131-q-chapitre-13.pdf
  [4] NetworkX, *Documentation officielle* : https://networkx.org/documentation/stable/
  [5] Chaine YouTube *Informatique Théorique* : http://www.youtube.com/@informatiquetheorique9146

