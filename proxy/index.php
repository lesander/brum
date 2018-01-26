<?php

header("Access-Control-Allow-Origin: *");
$path = $_SERVER["REQUEST_URI"];
$context = stream_context_create([
	'http' => [
		'method' => 'POST',
		'header' => 'Content-Type: application/x-www-form-urlencoded',
		'content' => http_build_query([])
	]
]);
file_put_contents("path.txt", $path);
if ($path == '/status') {
	echo file_get_contents("status.txt");
}

else if (substr( $path, 0, 10 ) === "/setstatus") {
	echo "SETSTATUS to " . $_GET["s"];
	var_dump($_GET);
	file_put_contents("status.txt", $_GET["s"]);
}

echo file_get_contents("http://github.brum.ultrahook.com$path", false, $context);
