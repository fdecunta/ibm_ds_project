import graphviz

dot = graphviz.Digraph('models')

dot.node('logreg', 'Logistic Regression')
dot.node('svm', 'Support Vector Machine')
dot.node('tree', 'Classification Tree')
dot.node('knn', 'K-nearest neighbors')
dot.node('gs', 'Search optimal parameters with GridSearch')
dot.node('best-model', 'Select Best model')
dot.node('evaluate', 'Evaluate model')

dot.edge('logreg', 'gs')
dot.edge('svm', 'gs')
dot.edge('tree', 'gs')
dot.edge('knn', 'gs')
dot.edge('gs', 'best-model')
dot.edge('best-model', 'evaluate')

dot.render('diagrams/models', format='png',  cleanup=True)

