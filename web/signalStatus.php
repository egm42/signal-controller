<?php
$signal = htmlspecialchars($_GET["arg"]);
$status = file("../controller/signalStatus") or
die("Error reading current signal status!");
echo $status[$signal - 1];

if (strpos($status[$signal - 1], "Green") !== false) {
	echo '<style type="text/css"> #signal' . $signal . ' {color:green; font-weight: bold;}</style>';
}
else {
	echo '<style type="text/css"> #signal' . $signal . ' {color:red; font-weight: bold;}</style>';
}
; ?>