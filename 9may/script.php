#!/usr/bin/php
<?php
$begin = microtime(true);

//write time arguments to file
//$argv[0] its is script name 'script.php'

//shell_exec('./set_tls_time.sh '.$argv[1].' '.$argv[2].' '.$argv[3].' '.$argv[4]);

$summary =  shell_exec('./sim.sh');
$clearedSummary = preg_replace('/Loading configuration... done.\n/','',$summary);


$xml = simplexml_load_string($clearedSummary, "SimpleXMLElement", LIBXML_NOCDATA);
$json = json_encode($xml);
$array = json_decode($json,TRUE);

$i=0;
$speedSum = 0;
$travelTimeSum = 0;
foreach ($array['step'] as $value) {
    if($value['@attributes']['running'] > 0 && $value['@attributes']['meanTravelTime'] > 0)  {
        $speedSum = $speedSum + $value['@attributes']['meanSpeed']*3600/1000;
        $travelTimeSum = $travelTimeSum + $value['@attributes']['meanTravelTime'];
        $i++;
    }
}

$end = microtime(true) - $begin;

print ($speedSum/$i." ".$travelTimeSum/$i);
