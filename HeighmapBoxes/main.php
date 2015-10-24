<?php
//1) Determine where squares begin and end
//2) Determine if square is within another square
//Need a structure that stores when we have discovered a square side and what level it is
// Can determine a current squares level based on how many squares on previous lines we have determined
// True statement: Squares cannot intersect
//Go line by line when we find a square side store this
//Use number of square lines above us (caclucate) to determine how to draw blank space
//When we find a matching square side remove it from storage
//Input file needs newline at end!!
$filename = $argv[1];
$handle = fopen($filename,"r");
//Determines the level of the next square
//$currentLevel = -1;
//Holds info about incompleted squares
$captures = array();
if($handle) {
    $buffer = fgets($handle, 4096);
    //read in row and columns lengths 
    $rowsColumns = explode(" ", trim($buffer));
    $numberRows = $rowsColumns[0];
    $numberColumns = $rowsColumns[1];
    echo "Number of Rows: $numberRows \nNumber of Columns: $numberColumns\n";
    //while(($buffer = fgets($handle, 4096)) !== false) {
    for($rowIndex = 0; $rowIndex < $numberRows; $rowIndex += 1) {
        $buffer = fgets($handle, 4096);
        //print_r(str_split($buffer));
        $currentLevel = -1;
        processLine(str_split($buffer), $currentLevel, $captures, $numberColumns, $rowIndex, $numberRows);
        echo "\n";
    }
    // echo "\n";
    // print_r($captures);
    fclose($handle);
} else {
    echo "$filename could not be opened!\n";
}
//Read each character in line from left to right:
//If a + is encountered store this in array 

//every time we encounter a | we need to check if this ends or begins a square and adjust level accordingly
//how to know if | is end or beginning? check if it's related + (closest one above it)
function processLine($line, &$currentLevel, &$captures, $numColumns, $currentRow, $numberRows) {
    $cornerExists = false;
    $lastSideLength = 0;
    $container = array();
    $sideContainer = array();
    $lastMatchLeftSide = false;
    $lastMatchRightSide = false;
    for($colIndex = 0; $colIndex < $numColumns; $colIndex += 1) {
        if($line[$colIndex] == " ") {
            echo fillSpace($currentLevel);
            //echo $line[$colIndex];
        } else if($line[$colIndex] == "+") {
            echo $line[$colIndex];
            $container = determineSquareCapture($captures, $colIndex, $currentRow, $cornerExists, $lastSideLength);
            $lastSideLength = $container[0];
            $cornerExists = $container[1];
        } else if($line[$colIndex] == "-") {
            echo $line[$colIndex];
            $lastSideLength += 1;
        } else if($line[$colIndex] == "|") {
            echo $line[$colIndex];
            $lastMatchRow = $numberRows + 1;
            foreach($captures as $corner) {
                $leftSide = $corner["left_column"] == $colIndex;
                $rightSide = $corner["right_column"] == $colIndex;
                if($leftSide || $rightSide) {
                    if($lastMatchRow > $currentRow - $corner["row"]) {
                        $lastMatchRightSide = $rightSide;
                        $lastMatchLeftSide = $leftSide;
                    }
                }
            }

            if($lastMatchLeftSide) {
                $currentLevel += 1;
            } else if($lastMatchRightSide) {
                $currentLevel -= 1; 
            }
            //store the | and determine the column of the nearest + above it 
            //foreach | in this array determine if they are opposite ends of the same
            //square by seeing if their related + are the same row if so then subtract one from
            //the level, otherwise add one to the level

        }
        else {
            echo $line[$colIndex];
        }
    }
}

 

function determineSquareCapture(&$captures, $currentCol, $currentRow, $cornerExists, $lastSideLength) {
    // if there is no other + in the array...
    if($cornerExists) {
        $cornerExists = false;
        array_push($captures, array(
            "length" => $lastSideLength,
            "right_column" => $currentCol,
            "left_column" => $currentCol - $lastSideLength - 1,
            "row" => $currentRow
        ));
        $lastSideLength = 0;
    } else {
        $cornerExists = true;
    }

    return array(
        $lastSideLength,
        $cornerExists,
    );
}

function fillSpace($currentLevel) {
    if($currentLevel == 0) {
        return "#";
    } else if($currentLevel == 1) {
        return "=";
    } else if($currentLevel == 2) {
        return "-";
    } else if($currentLevel == 3) {
        return ".";
    } else {
        return " ";
    }
}

?>