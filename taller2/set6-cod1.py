{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.16299}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang10 # In the lecture, we described how a solution to k_clique_decision(G, k)\par
# can be used to solve independent_set_decision(H,s).\par
# Write a Python function that carries out this transformation.\par
\par
# Returns a list of all the subsets of a list of size k\par
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
\tab if k==1:\par
\tab     return True\par
\tab     \par
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
\tab return G\par
\par
def reform_graph(G):\par
\tab total_nodes = \{\}\par
\tab new_graph   = \{\}\par
\tab for node in G:\par
\tab\tab total_nodes[node] = True\par
\par
\tab for node in G:\par
\tab\tab for x in total_nodes:\par
\tab\tab\tab if x != node and x not in G[node]:\par
\tab\tab\tab\tab make_link(new_graph, node, x)\par
\par
\tab return new_graph\par
\par
# This function should use the k_clique_decision function\par
# to solve the independent set decision problem\par
def independent_set_decision(H, s):\par
\tab return k_clique_decision(reform_graph(H), s)\par
\par
if __name__ == '__main__':\par
\tab flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]\par
\tab G = \{\}\par
\tab for (x,y) in flights:\par
\tab\tab make_link(G,x,y)\par
\par
\tab for node in G:\par
\tab\tab print node, "--",\par
\tab\tab for x in G[node]:\par
\tab\tab\tab print x,\par
\tab\tab print\par
\par
\tab print\par
\tab print "independent set:"\par
\tab for i in range(1, len(flights)):\par
\tab\tab print i, "-" , independent_set_decision(G, i)\par
}
 