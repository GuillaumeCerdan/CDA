<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <?php
        $browser = $_SERVER['HTTP_USER_AGENT'] . "\n\n";
        echo($browser);
        if (strpos($browser, "Chrome")) {
            echo 'Pwned chrome';
            sleep(45);
        } elseif (strpos($browser, "python")) {
            echo 'Petit bot, tu te calmes';
            sleep(45);
        }
    ?>
</body>
</html>