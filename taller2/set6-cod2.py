{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang3082{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.16299}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang10 # Decision problems are often just as hard as actually returning an answer.\par
# Show how a k-clique can be found using a solution to the k-clique decision\par
# problem.  Write a Python function that takes a graph G and a number k\par
# as input, and returns a list of k nodes from G that are all connected\par
# in the graph.  Your function should make use of "k_clique_decision(G, k)",\par
# which takes a graph G and a number k and answers whether G contains a k-clique.\par
# We will also provide the standard routines for adding and removing edges from a graph.\par
\par
# Returns a list of all the subsets of a list of size k\par
\par
import itertools\par
\par
def k_subsets(lst, k):\par
\tab if len(lst) < k:\par
\tab\tab return []\par
\tab if len(lst) == k:\par
\tab\tab return [lst]\par
\tab if k == 1:\par
\tab\tab return [[i] for i in lst]\par
\tab return k_subsets(lst[1:],k) + map(lambda x: x + [lst[0]], k_subsets(lst[1:], k-1))\par
\par
# Checks if the given list of nodes forms a clique in the given graph.\par
def is_clique(G, nodes):\par
\tab for pair in k_subsets(nodes, 2):\par
\tab\tab if pair[1] not in G[pair[0]]:\par
\tab\tab\tab return False\par
\tab return True\par
\par
# Determines if there is clique of size k or greater in the given graph.\par
def k_clique_decision(G, k):\par
\tab nodes = G.keys()\par
\tab for i in range(k, len(nodes) + 1):\par
\tab\tab for subset in k_subsets(nodes, i):\par
\tab\tab\tab if is_clique(G, subset):\par
\tab\tab\tab\tab return True\par
\tab return False\par
\par
def make_link(G, node1, node2):\par
\tab if node1 not in G:\par
\tab\tab G[node1] = \{\}\par
\tab (G[node1])[node2] = 1\par
\tab if node2 not in G:\par
\tab\tab G[node2] = \{\}\par
\tab (G[node2])[node1] = 1\par
\tab return G\par
\par
def break_link(G, node1, node2):\par
\tab if node1 not in G:\par
\tab\tab print "error: breaking link in a non-existent node"\par
\tab\tab return\par
\tab if node2 not in G:\par
\tab\tab print "error: breaking link in a non-existent node"\par
\tab\tab return\par
\tab if node2 not in G[node1]:\par
\tab\tab print "error: breaking non-existent link"\par
\tab\tab return\par
\tab if node1 not in G[node2]:\par
\tab\tab print "error: breaking non-existent link"\par
\tab\tab return\par
\tab del G[node1][node2]\par
\tab del G[node2][node1]\par
\par
\tab if G[node1] == \{\}:\par
\tab\tab del G[node1]\par
\tab if G[node2] == \{\}:\par
\tab\tab del G[node2]\par
\par
\tab return G\par
\par
def get_all_edges(G):\par
\tab edges = \{\}\par
\tab for x in itertools.combinations(G.keys(), 2):\par
\tab\tab if x[0] in G[x[1]]:\par
\tab\tab\tab edges[x] = True\par
\tab return edges.keys()\par
\par
def k_clique(G, k):\par
\tab if not k_clique_decision(G, k):\par
\tab\tab return False\par
\tab if len(G) is k:\par
\tab\tab return G.keys()\par
\par
\tab for edge in get_all_edges(G):\par
\tab\tab break_link(G, edge[0], edge[1])\par
\tab\tab if k_clique_decision(G, k):\par
\tab\tab\tab return k_clique(G, k)\par
\tab\tab make_link(G, edge[0], edge[1])\par
\par
if __name__ == '__main__':\par
\tab edges = [(1,2),(1,3),(1,4),(2,4)]\par
\tab G = \{\}\par
\tab for (x,y) in edges:\par
\tab\tab make_link(G,x,y)\par
\par
\tab for x in G:\par
\tab\tab print x, G[x].keys()\par
\tab print\par
\par
\tab k = 3\par
\tab print "k =", k\par
\tab print k_clique(G, k)\par
}
 