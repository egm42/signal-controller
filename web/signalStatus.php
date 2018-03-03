<?php
$signal = htmlspecialchars($_GET["arg"]);
$status = file("../controller/signalStatus") or
die("Error reading current signal status!");
echo $status[$signal - 1];
; ?>