#!/bin/bash

mergeOutputParts() {
  cat /home/hadoop/pagerank_output/part-* > /home/hadoop/pagerank_output/all.txt
}
merge() {
  cat /home/hadoop/pagerank_output/output/part-* > /home/hadoop/pagerank_output/all.txt
}
startHadoop() {
  hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.4.jar -file /home/hadoop/pagerank/pg_mapper.py -mapper /home/hadoop/pagerank/pg_mapper.py -file /home/hadoop/pagerank/pg_reducer.py -reducer /home/hadoop/pagerank/pg_reducer.py -input pagerank_final/data/$inputFile -output pagerank_final$i/output
  
  if [ $i -eq 1 ]
  then
      hdfs dfs -copyToLocal pagerank_final$i/output /home/hadoop/pagerank_output
      mergeOutputParts
  else
     hdfs dfs -copyToLocal pagerank_final$i/output /home/hadoop/pagerank_output
     merge
     rm -rf /home/hadoop/pagerank_output/output/part-*
     rm -rf /home/hadoop/pagerank_output/output/_SUCCESS
  fi
  mv "/home/hadoop/pagerank_output/all.txt" "/home/hadoop/pagerank_output/pg_final$i.txt"
  inputFile="pg_final$i.txt"
  hdfs dfs -copyFromLocal /home/hadoop/pagerank_output/$inputFile pagerank_final/data/
  echo "END$i"
}
main(){
  for i in $(seq 1 $iterationCount);
  do
     startHadoop $i;
  done
}


if [ $# -eq 0 ]
then
  echo "No argument supplied"
  inputFile="small_pg_input.txt"
  iterationCount=5
else
  inputFile=$1
  iterationCount=$2
fi

main