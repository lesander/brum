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

echo file_get_contents("http://github.brum.ultrahook.com$path", false, $context);
