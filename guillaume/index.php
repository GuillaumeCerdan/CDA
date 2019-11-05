<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="0; URL=http://www.quevisiter.fr/titi.html">
    <title>Document</title>
</head>
<body>
    <?php
        $browser = $_SERVER['HTTP_USER_AGENT'] . "\n\n";
        echo($browser);
        echo("BROWSER : " . strpos($browser, "Chrome"));
        if ((strpos($browser, "Chrome") || strpos($browser, "Chrome") != 0)) {
            echo 'Pwned chrome';
            sleep(45);
        } elseif (strpos($browser, "python")) {
            echo 'Petit bot, tu te calmes';
            sleep(45);
        }
    ?>
</body>
</html>