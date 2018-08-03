Given an array and a value Y, count and print the number of array values greater than Y.

var y= 0;
var arr = []; 
function valy ()  {
	for (var i = 0; i < arr.length; i ++); {
		if (arr[i] > var y) {
			y = arr[i];
		}
		console.log arr [i] 
	}
}



2. Given an array, print the max, min and average values for that array.


function maxMinAvg(arr) {
    var max = arr[0];
    var min = arr[0];
    var sum = arr [0];
    
    for (var i = 1; i < arr.length; i ++){
        if (arr[i] > max) {
            max = arr [i];
        }
        if (arr [i] < min) {
            min = arr [i];
        }
        sum = sum + arr [i];
    }
    var avg = sum / arr.length;
    var arrnew = [ max, min, avg];
    return arrnew; 
}



3. Given an array of numbers, create a function that returns a new array 
where negative values were replaced with the string ‘Dojo’.   
For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].

function Dojo() {
	for (var i= 0; i< arr.length; i ++){
		if (arr[i] < 0){
			arr[i] = "Dojo";
			}

		}
	console.log(arr)
	} 


4. Given array, and indices start and end, remove vals in that index range,
working in-place (hence shortening the array).  For example,
removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].


function end(){ 
for (var i = 0; i < arr.length; i ++);{

	console.log arr[0];
	console.log arr [1];
	console.log [arr.length-1];
}


}





