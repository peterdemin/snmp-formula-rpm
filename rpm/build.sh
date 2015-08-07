#!/bin/bash

set -ex

for dir in RPMS BUILD
do
 [[ -d $dir ]] && rm -Rf $dir
  mkdir $dir
done

rpmbuild --define '_topdir '`pwd` --define '_tmppath '`pwd`/BUILD -bb snmp_formula.spec
