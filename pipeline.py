#!/usr/bin/python
import time,datetime,string,re,os,ConfigParser

## https://www.percona.com/blog/2015/10/07/using-apache-spark-mysql-data-analysis/
from datetime import timedelta, date
from optparse import OptionParser

parser = OptionParser()
parser.add_option( "--pipe",
                  action="store_true", dest="pipe", default=False,
                  help="run in pipe mode", metavar = "BOOL")

(options, args) = parser.parse_args()
#############################################################
#############################################################
if (options.pipe):
  from pyspark import SparkContext
  # sc is an existing SparkContext.
  sc=SparkContext()
  makerdd= sc.parallelize( ["hi","hello","how","are","you"] )
                            
  # http://blog.madhukaraphatak.com/pipe-in-spark/
  outputframe = makerdd.pipe("/rsrch2/ip/dtfuentes/github/SparkPipeExample/echo.sh").collect()
  
  ## pipe() returns strings
  #
  for (num) in outputframe :
      print "%s" % (num)

  sc.stop()
else:
  parser.print_help()
  print options

