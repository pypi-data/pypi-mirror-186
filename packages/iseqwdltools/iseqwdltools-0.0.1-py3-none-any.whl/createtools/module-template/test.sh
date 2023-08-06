#!/bin/bash

VERSION='1.0.0'

function version() {
  script_name=`basename "$0"`
  printf "$script_name $VERSION\n"
}

INDEX=-1

while [[ $# -gt 0 ]]
do
  key="$1"
  case $key in
    -v|--version)
    version
    exit 0;;
    -i|--index)
    export INDEX=$2
    shift # past argument
    shift # past value
    ;;
    *)
    echo "Invalid argument"
    exit 1;
  esac
done

SOURCE="${BASH_SOURCE[0]}"
export ROOTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd | grep -oh '.*/workflows/' )"
wdltest -t $( dirname "$SOURCE" )/test.json -i $INDEX
EXITCODE=$?
echo exitcode $EXITCODE
if [ "$EXITCODE" -eq "0" ]; then
   echo "TEST SUCCEEDED";
else
   echo "TEST FAILED";
fi
exit $EXITCODE
