import graphviz

dot = graphviz.Digraph('web-scrapping')

dot.node('request', 'Request wiki URL')
dot.node('soup', 'Parse with BeautifulSoup')
dot.node('table', 'Find table with launch records')
dot.node('rows', 'Iterate over rows to extract data')
dot.node('pandas', 'Create data frame and save as csv')

dot.edge('request', 'soup')
dot.edge('soup', 'table')
dot.edge('table', 'rows')
dot.edge('rows', 'pandas')

dot.render('diagrams/web_scrapping', format='png',  cleanup=True)


