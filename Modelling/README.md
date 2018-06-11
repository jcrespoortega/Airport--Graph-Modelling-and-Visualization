# Modelling

This dataset is about airports and fligths between American and European airports, the questions which I want to solve are discover the most important airport and if the traffic could be splited in two categories. For this reason, modelling the problem as a graph will help to answer these questions.

The idea is use the frecuencies  beetween  airports in order to weight the edges of the directed graph. When the graph is constructed, to find the most important airport I will use centrality measures as Degree Centrality and Page Rank. For discovering communities Girvan-Newman algorithm will be used. 

All the code was developed in Python with the library Network X.
