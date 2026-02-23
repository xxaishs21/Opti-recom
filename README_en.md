# Project: Optimizing Friend Recommendation on a Social Network

## Presentation

Social networks now play a central role in our lives and influence our interactions and access to information. I became interested in the actual role of recommendation systems and in their possible contribution to the formation of closed, poorly diversified groups within networks.

In a social network modeled as a graph, links represent connections between users. When these links form many cycles, information and interactions remain confined. The challenge is therefore to understand how to create links that make it possible to connect people and promote circulation within the network.

**This project is individual work.**

## Selected Research Question

How, from the graph of a social network, can one define recommendation strategies that allow a user to expand their network beyond their immediate neighborhood through the addition of relevant contacts?

## Objectives

I aim to:

- implement different friend recommendation strategies on artificial social graphs;
- analyze their influence on the network structure using metrics such as modularity, the clustering coefficient, and the number of cycles;
- compare strategies based on friendship links and on similarity of interests;
- study phenomena of network opening or closure;
- introduce probabilistic approaches in order to make the modeling closer to behaviors observed in reality.

## Annotated Bibliography

Modeling social networks as graphs makes it possible to represent interactions between individuals in a simple way. In this framework, users are modeled as vertices and relationships as edges. The book by M. E. J. Newman helps understand the structure of complex networks: in particular, it explains how measures such as the clustering coefficient make it possible to evaluate a network’s tendency to form triangles, and how the global structure influences the circulation of information. These notions provide the general framework within which the study of social networks and their evolution is situated [1].

In this continuity, it is essential to analyze communities in order to understand how a network can fragment into strongly connected groups. S. Fortunato’s article presents the main community detection algorithms, in particular those based on modularity optimization. The principle of these methods is to search for a partition of the graph such that connections are denser within groups than between different groups. This work helps explain why some networks naturally tend to close in on themselves and form relational bubbles [2].

The creation of new links in a social network is studied through work on link prediction. The article by L. Lü and T. Zhou provides a survey of algorithms used to estimate the probability that a link will appear between two vertices. Among the methods presented are simple algorithms based on the number of mutual friends, similarity measures between vertices, and probabilistic approaches. The common principle of these methods is to assign a score to each pair of users, which is then interpreted as a probability of connection. This reference constitutes the theoretical foundation of the recommendation algorithms studied in this project [3].

INSEE resources on graph partitioning and graph analysis provide a methodological complement to this work. They describe the general principles of graph partitioning and the interpretation of results obtained using global indicators such as modularity. These tools make it possible to connect algorithmic choices to observable properties of the network structure [4].

The practical implementation of these algorithms requires appropriate tools. The NetworkX library makes it possible to generate artificial graphs, automatically compute metrics such as clustering or modularity, and simulate the addition of links according to different recommendation strategies. It therefore provides an experimental framework for observing the evolution of a network under the effect of given algorithmic rules [5].

In addition, recommendation systems are studied in applied contexts. Yiyang Pan’s article analyzes how recommendation algorithms used on digital platforms work, especially those based on user similarity and collaborative filtering. It shows that these algorithms rely on estimations rather than certain decisions, which naturally leads to introducing probabilities into the recommendation process [6].

Finally, Arvind Narayanan’s essay offers a broader analysis of how recommendation algorithms operate on social networks. It highlights the fact that, even when algorithmic rules are simple, the effects observed at the network scale are complex and difficult to predict. This idea justifies the use of probabilistic methods and Monte Carlo simulations, which consist of repeating a random experiment several times in order to study its average behavior [7].

- [1] **M. E. J. NEWMAN**: *Networks: An Introduction* : https://doi.org/10.1093/acprof:oso/9780199206650.001.0001
- [2] **S. FORTUNATO**: *Community detection in graphs* : https://doi.org/10.48550/arXiv.0906.0612
- [3] **L. LÜ, T. ZHOU**: *Link prediction in complex networks: A survey* : https://doi.org/10.1016/j.physa.2010.11.027
- [4] **INSEE**: *Partitionnement et analyse de graphes* : https://www.insee.fr/fr/statistiques/fichier/3635442/imet131-q-chapitre-13.pdf
- [5] **NETWORKX**: *Official documentation* : https://networkx.org/documentation/stable/
- [6] **YIYANG PAN**: *The role of recommendation algorithms in driving the development of ecommerce platforms* : https://www.researchgate.net/publication/384790760_The_role_of_recommendation_algorithms_in_driving_the_development_of_ecommerce_platforms
- [7] **ARVIND NARAYANAN**: *Understanding Social Media Recommendation Algorithms* : https://academiccommons.columbia.edu/doi/10.7916/khdk-m460
