

#spark-submit --packages org.apache.hadoop:hadoop-aws:2.7.1 SimpleApp.py
#spark-submit --packages org.apache.hadoop:hadoop-aws:2.7.1 --master spark://x SimpleApp.py



from pyspark import SparkContext
import json

#dataFile = "/Users/salagappa/Projects/sree/spark/Ratings-Counter.py"  # Should be some file on your system

dataFile = ("")


sc = SparkContext("local", "Simple App")
logData = sc.textFile(dataFile).cache()
#count = logData.map(lambda : line.split(' '))
#print count.collect()



logs_json = logData.map(lambda x: json.loads(x))
logs_json.take(3)


#numAs = logData.filter(lambda s: 'a' in s).count()
#numBs = logData.filter(lambda s: 'b' in s).count()

#print "Lines with a: %i, lines with b: %i" % (numAs, numBs)



# load the events json and count

#val dfs = sqlContext.read.json("2016-07-01+00-06-49.txt")
#dfs.groupBy("imageids").count().show()
