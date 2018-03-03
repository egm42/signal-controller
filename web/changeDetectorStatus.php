<?php
$detector = htmlspecialchars($_GET["det"]);
$toggle = htmlspecialchars($_GET["toggle"]);
$my_file = file("../controller/detectorStatus");
$my_file[$detector - 1] = $toggle . "\n";
$data = implode($my_file);

$handle = fopen("../controller/detectorStatus", "w") or die("Cannot open detector file!");
fwrite($handle, $data);
fclose($handle);
; ?>