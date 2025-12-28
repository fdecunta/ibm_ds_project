import graphviz

dot = graphviz.Digraph('collection')

dot.node('API', 'SpaceX API')
dot.node('wiki', 'Wikipedia: SpaceX launches')
dot.node('w', 'Data wrangling step')

dot.edge('API', 'w')
dot.edge('wiki', 'w')

dot.render('diagrams/data_collection', format='png',  cleanup=True)
