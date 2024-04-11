<?php
session_start();
session_destroy();
$redirect = "../index.html";
header("Location:$redirect");
exit();
?>