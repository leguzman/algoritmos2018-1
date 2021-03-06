{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.16299}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang10 #\par
# Write a function, `bipartite` that\par
# takes as input a graph, `G` and tries\par
# to divide G into two sets where\par
# there are no edges between elements of the\par
# the same set - only between elements in\par
# different sets.\par
# If two sets exists, return one of them\par
# or `None` otherwise\par
# Assume G is connected\par
#\par
\par
def bipartite(G):\par
\tab checked = \{\}\par
\par
\tab def _iter_check(node, side):\par
\tab\tab if node in checked:\par
\tab\tab\tab return\par
\tab\tab checked[node] = side\par
\tab\tab for neighbor in G[node]:\par
\tab\tab\tab _iter_check(neighbor, not side)\par
\par
\tab for node in G:\par
\tab\tab _iter_check(node, True)\par
\par
\tab def _valid(subset):\par
\tab\tab for node in subset:\par
\tab\tab\tab for neighbor in G[node]:\par
\tab\tab\tab\tab if neighbor in subset:\par
\tab\tab\tab\tab\tab return False\par
\tab\tab return True\par
\par
\tab left_set  = set(filter(lambda x: checked[x], checked))\par
\tab right_set = set(G.keys()) - left_set\par
\par
\tab if _valid(left_set) and _valid(right_set):\par
\tab\tab return left_set\par
\par
########\par
#\par
# Test\par
\par
def make_link(G, node1, node2, weight=1):\par
\tab if node1 not in G:\par
\tab\tab G[node1] = \{\}\par
\tab (G[node1])[node2] = weight\par
\tab if node2 not in G:\par
\tab\tab G[node2] = \{\}\par
\tab (G[node2])[node1] = weight\par
\tab return G\par
\par
def test():\par
\tab edges = [(1, 2), (2, 3), (1, 4), (2, 5),\par
\tab\tab\tab  (3, 8), (5, 6)]\par
\tab G = \{\}\par
\tab for n1, n2 in edges:\par
\tab\tab make_link(G, n1, n2)\par
\tab g1 = bipartite(G)\par
\tab assert (g1 == set([1, 3, 5]) or\par
\tab\tab\tab g1 == set([2, 4, 6, 8]))\par
\tab edges = [(1, 2), (1, 3), (2, 3)]\par
\tab G = \{\}\par
\tab for n1, n2 in edges:\par
\tab\tab make_link(G, n1, n2)\par
\tab g1 = bipartite(G)\par
\tab assert g1 == None\par
\par
if __name__ == '__main__':\par
\tab test()\par
\tab print "Test passes"\par
}
 