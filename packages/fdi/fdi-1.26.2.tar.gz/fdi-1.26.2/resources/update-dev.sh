!/bin/bash
if [ $# -lt 1 ]; then echo version missing; exit -1; echo versiom=$1; fi
echo 'deleting pod...'; echo ./del-dev.sh &&\
YFILE=svompool-dev_$1.yml &&\
echo generating $YFILE...; sed -e "s/DKVERSION/$1/" svompool-dev.template > $YFILE &&\
echo applying...; kubectl -n svom apply -f $YFILE

kubectl -n svom get pod | grep pool
~