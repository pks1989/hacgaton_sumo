#!/bin/sh
# This is a comment!
echo "<additionals>
    <tlLogic id=\"center\" type=\"static\" programID=\"1\" offset=\"0\">
        <phase duration=\"$1\" state=\"GgrrGG\"/>
        <phase duration=\"$2\" state=\"yyrryy\"/>
        <phase duration=\"$3\" state=\"rrGGGr\"/>
        <phase duration=\"$4\" state=\"rryyyr\"/>
    </tlLogic>
</additionals>" > ./simple_road.tls.xml
