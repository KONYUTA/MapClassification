#!/bin/zsh
for d in $(find $1 -type d);do
	echo dirname:$d
	ls -l $d |wc -l
	echo
done
