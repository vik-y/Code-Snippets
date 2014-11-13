#!/bin/bash

#Enter the name of the file which you want to search for in the present directory
read filename
directory="$pwd"
find $directory -name  "$filename"
