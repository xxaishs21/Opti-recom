Read this document in [english](README_en.md)

# Projet : Optimisation de recommandation d'amis sur un réseau social

## Présentation 
Les réseaux sociaux occupent aujourd’hui une place centrale dans nos vies et influencent nos interactions et notre accès à l’information. Je me suis interrogée sur le rôle réel des systèmes de recommandation et sur leur possible contribution à la formation de groupes fermés et peu diversifiés au sein des réseaux.

Dans un réseau social modélisé par un graphe, les liens représentent les connexions entre utilisateurs. Lorsque ces liens forment de nombreux cycles, l’information et les interactions restent confinées. L’enjeu est alors de comprendre comment créer des liens permettant de connecter les personnes et de favoriser la circulation dans le réseau.


**Ce projet fait l'object d'un travail individuel**

## Problématique retenue

Comment, à partir du graphe d’un réseau social, définir des stratégies de recommandation permettant à un utilisateur d’étendre son réseau au-delà de son voisinage immédiat par des ajouts de contacts pertinents ?


## Objectifs 

Je me propose :
- d’implémenter différentes stratégies de recommandation d’amis sur des graphes sociaux
artificiels ;
- d’analyser leur influence sur la structure du réseau à l’aide de métriques telles que la
modularité, le coefficient de clustering et le nombre de cycles ;
- de comparer des stratégies fondées sur les liens d’amitié et sur la similarité d’intérêts ;
- d’étudier les phénomènes d’ouverture ou de fermeture du réseau social ;
- d’introduire des approches probabilistes afin de rendre la modélisation plus proche des
comportements observés dans la réalité.


## Bibliographie commentée

La modélisation des réseaux sociaux sous forme de graphes permet de représenter simplement les interactions entre individus. Dans ce cadre, les utilisateurs sont modélisés par des sommets et les relations par des arêtes. L’ouvrage de M. E. J. Newman permet de comprendre la structure des réseaux complexes : il décrit notamment comment des mesures comme le coefficient de clustering permettent d’évaluer la tendance d’un réseau à former des triangles, et comment la structure globale influence la circulation de l’information. Ces notions fournissent le cadre général dans lequel s’inscrit l’étude des réseaux sociaux et de leur évolution **[1]**.

Dans cette continuité, il est essentiel d’analyser des communautés pour comprendre comment un réseau peut se fragmenter en groupes fortement connectés. L’article de S. Fortunato présente les principaux algorithmes de détection de communautés, en particulier ceux fondés sur l’optimisation de la modularité. Le principe de ces méthodes est de chercher une partition du graphe telle que les connexions soient plus denses à l’intérieur des groupes qu’entre groupes différents. Ces travaux permettent d’expliquer pourquoi certains réseaux tendent naturellement à se fermer sur eux-mêmes et à former des bulles relationnelles **[2]**.

On étudie la création de nouveaux liens dans un réseau social à travers les travaux sur la prédiction de liens.
L’article de L. Lü et T. Zhou propose une synthèse des algorithmes qui permet d’estimer la probabilité d’apparition d’un lien entre deux sommets. Parmi les méthodes présentées figurent des algorithmes simples basés sur le nombre d’amis communs, des mesures de similarité entre sommets, ainsi que des approches probabilistes. Le principe commun à ces méthodes est d’attribuer un score à chaque paire d’utilisateurs, ce score étant ensuite interprété comme une probabilité de connexion. Cette référence constitue le fondement théorique des algorithmes de recommandation étudiés dans ce projet **[3]**.

Les ressources de l’INSEE sur le partitionnement et l’analyse de graphes apportent un complément méthodologique à ces travaux. Elles décrivent les principes généraux du partitionnement des graphes et l’interprétation des résultats obtenus à l’aide d’indicateurs globaux comme la modularité. Ces outils permettent de relier les choix algorithmiques à des propriétés observables de la structure du réseau **[4]**.

La mise en œuvre concrète de ces algorithmes nécessite des outils adaptés. La bibliothèque NetworkX permet de générer des graphes artificiels, de calculer automatiquement des métriquestelles que le clustering ou la modularité, et de simuler l’ajout de liens selon différentes stratégies de recommandation. Elle fournit ainsi un cadre expérimental pour observer l’évolution d’un réseau sous l’effet de règles algorithmiques données **[5]**.

De plus, les systèmes de recommandation sont étudiés dans des contextes applicatifs. L’article de Y. Pan analyse le fonctionnement des algorithmes de recommandation utilisés sur les plateformes numériques, en particulier ceux fondés sur la similarité entre utilisateurs et le filtrage collaboratif. Il montre que ces algorithmes reposent sur des estimations et non sur des décisions certaines, ce qui conduit naturellement à introduire des probabilités dans le processus de recommandation **[6]**.

Enfin, l’essai d’Arvind Narayanan propose une analyse plus globale du fonctionnement des algorithmes de recommandation sur les réseaux sociaux. Il met en évidence le fait que, même lorsque les règles algorithmiques sont simples, les effets observés à l’échelle du réseau sont complexes et difficiles à prévoir. Cette idée justifie l’utilisation de méthodes probabilistes et de simulations de type Monte Carlo, qui consistent à répéter plusieurs fois une expérience aléatoire afin d’en étudier le comportement moyen [7].


- **[1]** M. E. J. NEWMAN : Networks: An Introduction : https://doi.org/10.1093/acprof:oso/9780199206650.001.0001
- **[2]** S. FORTUNATO : Community detection in graphs : https://doi.org/10.48550/arXiv.0906.0612
- **[3]** L. LÜ, T. ZHOU : Link prediction in complex networks: A survey : https://doi.org/10.1016/j.physa.2010.11.027
- **[4]** INSEE : Partitionnement et analyse de graphes : https://www.insee.fr/fr/statistiques/fichier/3635442/imet131-q-chapitre-13.pdf
- **[5]** NETWORKX : Dcumentation officielle : https://networkx.org/documentation/stable/
- **[6]** YIYANG PAN : The role of recommendation algorithms in driving the development of ecommerce platforms : https://www.researchgate.net/publication/384790760_The_role_of_recommendation_algorithms_in_driving_the_development_of_ecommerce_platforms
- **[7]** ARVIND NARAYANAN : Understanding Social Media Recommendation Algorithms : https://academiccommons.columbia.edu/doi/10.7916/khdk-m460

