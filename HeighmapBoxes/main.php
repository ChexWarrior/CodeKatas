<?php
    //echo "Hello Console!\n";
    $handle = @fopen("input1.txt","r");

    if($handle) {
        while(($buffer = fgets($handle, 4096)) !== false) {
            echo $buffer;
        }

        if(!feof($handle)) {
            echo "Unexpected Error!\n";
        }

        fclose($handle);
    }
?>