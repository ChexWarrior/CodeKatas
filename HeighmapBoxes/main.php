<?php

    //1) Determine where squares begin and end
    //2) Determine if square is within another square
    //The position of corners is cruical to this...

    $filename = $argv[1];
    $handle = @fopen($filename,"r");

    if($handle) {
        $buffer = fgets($handle, 4096);
        //read in row and columns lengths 
        $rowsColumns = explode(" ", trim($buffer));
        echo "Number of Rows: $rowsColumns[0] \nNumber of Columns: $rowsColumns[1]\n";
        // while(($buffer =  !== false) {
        //     echo $buffer;
        // }

        // if(!feof($handle)) {
        //     echo "Unexpected Error!\n";
        // }

        // fclose($handle);
    } else {
        echo "$filename could not be opened!\n";
    }

    function processLine($line) {
        $newline = $line;
    }
?>