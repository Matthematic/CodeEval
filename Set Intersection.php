<?php

function intersect($a, $b) {
    $result = array();
    $array_to_use = (sizeof($a) > sizeof($b) ? $a : $b);
    
    foreach ($array_to_use as $array1) {
        if (in_array($array1, ($array_to_use == $a ? $b : $a))) {
            array_push($result, $array1);
        }
    }
    
    return $result;
}

function output_csv($arr) {
    for ($i = 0;$i < sizeof($arr)-1;$i++) { //output values
        echo $arr[$i].",";
    }
        echo end($arr);
        echo "\n";
}



$file = fopen($argv[1], "r");

while (!feof($file)) {
    $test = fgets($file); //get line
    $test = trim($test); //strip whitespace
    
    if ($test != "") {
        $array = explode(";", $test); //break by ; delimiter
        $first = explode(",", $array[0]); //break the two pieces into their values
        $second = explode(",", $array[1]);
        
        $result = intersect($first, $second); //return the values that intersect
        
        if (empty($result)) {echo "\n";} //if no intersection, print newline
        else {
            output_csv($result);
        }
        
    }
    
    
}

?>
