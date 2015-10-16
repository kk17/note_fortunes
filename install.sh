#! /bin/bash

python note2data.py
strfile data/*
base_dir=`pwd`
# echo $base_dir
bin_path=`which fortune`
link_path=`readlink $bin_path`
# echo $bin_path
cd `dirname $bin_path`
cd `dirname $link_path`
real_path=`pwd`/../share/games/fortunes
# echo $real_path
cd $base_dir
# python ./note2data.py
cp data/* $real_path
fortune 100% refactor_your_wetware
