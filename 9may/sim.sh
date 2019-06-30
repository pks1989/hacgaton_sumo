#!/bin/sh
# This is a comment!
#sumo -c may.sumocfg -b 0 -e 100 --no-step-log --summary-output stdout
sumo -n may.net.xml -r may.rou.xml -a may.tls.xml -b 0 -e 900 --no-step-log --summary-output stdout
