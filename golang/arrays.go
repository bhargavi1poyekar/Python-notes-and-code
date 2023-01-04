package main

// package from go standard library 
// fmt- formatting strings and printing to console
import "fmt"

// only 1 main function in the application
func main() {

	// var ages [3]int=[3]int{20,35,40}
	// array of 3 items of type int

	var ages =[3]int{20,35,40}

	names := [4]string{"A","B","C","D"}

	fmt.Println(ages, len(ages))
	fmt.Println(names, len(names))

	names[1]="X"
	fmt.Println(names, len(names))
	// Slices (Uses array under the hood)

	var scores=[]int{100,20,30} 
	// Creates slice, with unfixed length

	fmt.Println(scores, len(scores))


	scores=append(scores,85)
	// append returns new slice
	fmt.Println(scores, len(scores))

	// slice ranges
	rangeOne:=names[1:3]
	rangeTwo:=names[2:]
	rangeThree:=names[:3]

	fmt.Println(rangeOne, rangeTwo, rangeThree)

}