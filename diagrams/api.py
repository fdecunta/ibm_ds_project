import graphviz

dot = graphviz.Digraph('api')

dot.node('api', 'Call SpaceX API')
dot.node('df', 'Parse JSON to data frame')
dot.node('clean', 'Clean data')
dot.node('store', 'Store data as CSV')

dot.edge('api', 'df')
dot.edge('df', 'clean')
dot.edge('clean', 'store')

dot.render('diagrams/api_call', format='png',  cleanup=True)

