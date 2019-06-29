#!/usr/bin/php
<?php
$summary =  shell_exec('./sim.sh');
$clearedSummary = preg_replace('/Loading configuration... done.\n/','',$summary);

$xml = simplexml_load_string($clearedSummary, "SimpleXMLElement", LIBXML_NOCDATA);
$json = json_encode($xml);
$array = json_decode($json,TRUE);

$i=0;
$speedSumm = 0;
foreach ($array['step'] as $value) {
    if($value['@attributes']['running'] > 0) {
        $speedSumm = $speedSumm + $value['@attributes']['meanSpeed'];
        $i++;
    }
}

print_r ($speedSumm/$i);
