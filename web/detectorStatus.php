<?php
$detector = htmlspecialchars($_GET["arg"]);
$status = file("../controller/detectorStatus") or
die("Error reading current detector status!");
echo $status[$detector - 1];
; ?>