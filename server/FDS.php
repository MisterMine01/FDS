<?php
function properties($enter) {
	return json_decode(file_get_contents("properties.json"), true)[$enter];
}

function all_version() {
	$version = array();

	if ($handle = opendir(properties("fdv_folder"))) {
		while (false !== ($entry = readdir($handle))) {
			if ($entry != "." && $entry != "..") {
				$version[] = pathinfo($entry)['filename'];
			}
		}
		closedir($handle);
	}
	return json_encode($version);
}

function get_version() {
	$folder = properties("fdv_folder");
	return file_get_contents("{$folder}/{$_POST["version"]}.fdv");
}

function download_fdf() {
	$folder = properties("fdf_folder");
	$filename = "{$_POST["id"]}.{$_POST["name"]}.{$_POST["version"]}.fdf";
	$path = "{$folder}/{$filename}";
	$type = "application/octet-stream";
	if (file_exists($path)) {
		header($_SERVER["SERVER_PROTOCOL"] . " 200 OK");
		header("Cache-Control: public"); // needed for internet explorer
		header("Content-Type: {$type}");
		header("Content-Transfer-Encoding: Binary");
		header("Content-Length:".filesize($path));
		header("Content-Disposition: attachment; filename={$filename}");
		readfile($path);
		die();
	} else {
		die("Error: File not found.");
	}
}

?>