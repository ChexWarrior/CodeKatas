<?php
//1) Determine where squares begin and end
//2) Determine if square is within another square
//Need a structure that stores when we have discovered a square side and what level it is
// Can determine a current squares level based on how many squares on previous lines we have determined
// True statement: Squares cannot intersect
//Go line by line when we find a square side store this
//Use number of square lines above us (caclucate) to determine how to draw blank space
//When we find a matching square side remove it from storage
$filename = $argv[1];
$handle = fopen($filename,"r");
//Determines the level of the next square
$currentLevel = 0;
//Holds info about incompleted squares
$captures = array();
if($handle) {
    $buffer = fgets($handle, 4096);
    //read in row and columns lengths 
    $rowsColumns = explode(" ", trim($buffer));
    $numberRows = $rowsColumns[0];
    $numColumns = $rowsColumns[1];
    echo "Number of Rows: $numberRows \nNumber of Columns: $numColumns\n";
    //while(($buffer = fgets($handle, 4096)) !== false) {
    for($rowIndex = 0; $rowIndex < $numberRows; $rowIndex += 1) {
        $buffer = fgets($handle, 4096);
        processLine(str_split($buffer), $currentLevel, $captures, $numColumns, $numberRows);
    }
    fclose($handle);
} else {
    echo "$filename could not be opened!\n";
}
//Read each character in line from left to right:
//If a + is encountered store this in array 
function processLine($line, $currentLevel, $captures, $numColumns, $numberRows) {
    $newLine = $line;
    foreach($line as $character) {
        //processCharacter($character, $currentLevel, $captures);
        echo $character;
    }
}

function processCharacter($character, $currentLevel, $captures) {
    if($character == " ") {
        echo fillSpace($currentLevel);
    } else if($character == "+") {

    }
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