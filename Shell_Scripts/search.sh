#!/bin/bash

#Enter the name of the file which you want to search for in the present directory

directory="$(pwd)"
find $directory -name  "$1"
