#!/bin/bash
for i in *
do  echo \"$i\"\:; nlines=`wc -l $i | awk '{print $1}'`
       	awk -v n=$nlines 'NR==1{print "[[",$1,",", $2,"]"}NR>1&&NR<n{print ", [",$1,",", $2,"]"}NR==n{print ", [",$1,",", $2,"]]"}' $i
done
