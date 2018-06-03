# Modelling

This data in about airport and fligths between American and European airports, the question which I want to solve is discover the most immportant airport and if the traffic could be divided in two categories. For this reason, modelling the problem as a graph will help to answer these questions.

The idea is calculate the frecuencies of flights which are beetween each airport, this information will be used to weight the edges of the directed graph. When the graph is constructed to find the most important airport I will use centrality meauseres as Degree and Page Rank. In order to discover communities Girvan-Newman algorithm will be used. 

All the code was developed in Python with the library Network X.
