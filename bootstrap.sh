#!/usr/bin/env bash
pkg=dos2unix
status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"
if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
  apt-get update;
  apt-get upgrade;
  apt-get install $pkg;
fi
