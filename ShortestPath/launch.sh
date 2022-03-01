#!/bin/bash

mergeOutputParts() {
  cat /home/hadoop/shortestPath_output/part-* > /home/hadoop/shortestPath_output/all.txt
}
merge() {
  cat /home/hadoop/shortestPath_output/output/part-* > /home/hadoop/shortestPath_output/all.txt
}
startHadoop() {
  hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.4.jar -file /home/hadoop/shortestPath/mapper.py -mapper /home/hadoop/shortestPath/mapper.py -file /home/hadoop/shortestPath/reducer.py -reducer /home/hadoop/shortestPath/reducer.py -input shortestPath/data/$inputFile -output shortestPath$i/output
  
  if [ $i -eq 1 ]
  then
      hdfs dfs -copyToLocal shortestPath$i/output /home/hadoop/shortestPath_output
      mergeOutputParts
  else
     hdfs dfs -copyToLocal shortestPath$i/output /home/hadoop/shortestPath_output
     merge
     rm -rf /home/hadoop/shortestPath_output/output/part-*
     rm -rf /home/hadoop/shortestPath_output/output/_SUCCESS
  fi
  mv "/home/hadoop/shortestPath_output/all.txt" "/home/hadoop/shortestPath_output/sp_small_output$i.txt"
  inputFile="sp_small_output$i.txt"
  hdfs dfs -copyFromLocal /home/hadoop/shortestPath_output/$inputFile shortestPath/data
  echo "END$i"
}
main(){
  for i in $(seq 1 $iterationCount);
  do
     startHadoop $i
  done
}


if [ $# -eq 0 ]
then
  echo "No argument supplied"
  inputFile="mapper_input.txt"
  iterationCount=5
else
  inputFile=$1
  iterationCount=$2
fi

main