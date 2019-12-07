"""
Decision Tree Classification.
"""
from __future__ import print_function

from pyspark import SparkContext
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils

from decision_tree import tree_json

if __name__ == "__main__":

	sc = SparkContext(appName="DecisionTreeClassification")

	raw_data = MLUtils.loadLibSVMFile(sc, '/home/hechem/spark-campaign-classification/test/data/sample_libsvm_data.txt')
	(trainingDataSet, testDataSet) = raw_data.randomSplit([0.7, 0.3])

	tree = DecisionTree.trainClassifier(trainingDataSet, numClasses=2, categoricalFeaturesInfo={}, impurity='gini', maxDepth=4, maxBins=30)

	predictions = tree.predict(testDataSet.map(lambda x: x.features))
	labelsAndPredictions = testDataSet.map(lambda lp: lp.label).zip(predictions)
	testErr = labelsAndPredictions.filter(lambda (v, p): v != p).count() / float(testDataSet.count())
	print('Test Error = ' + str(testErr))
	print('Learned classification tree model:')
	print(tree.toDebugString())
	tree_to_json = tree.toDebugString()

	tree_json(tree_to_json)