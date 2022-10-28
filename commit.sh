#!/bin/bash

SCRIPT=$(readlink -f $0);
cd $SCRIPT
git pull
git add .
git commit -m "upload"
git push
