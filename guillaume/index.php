<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <?php
        $browser = $_SERVER['HTTP_USER_AGENT'] . "\n\n";
        echo($browser);
        var_dump(strpos($browser, "Chrome"));
        /*if ((strpos($browser, "Chrome") || strpos($browser, "Chrome") != 0)) {
            echo 'Pwned chrome';
            sleep(45);
        } elseif (strpos($browser, "python")) {
            echo 'Petit bot, tu te calmes';
            sleep(45);
        }*/
    ?>

    <script type="text/javascript">
        <!--
            
    </script>

</body>
</html>
