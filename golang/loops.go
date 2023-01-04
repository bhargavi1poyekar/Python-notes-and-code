package main

// package from go standard library 
// fmt- formatting strings and printing to console
import "fmt"

// only 1 main function in the application
func main() {

	// While 
	// x:=0

	// for x<5{
	// 	fmt.Println(x)
	// 	x++
	// }

	// for

	// for i:=0; i<5; i++{
	// 	fmt.Println(i)
	// }

	names:= []string{"B","X","D","R","Y"}

	// for i:=0; i<len(names);i++{
	// 	fmt.Println(i,names[i])
	// }

	// for index, value :=range names {
	// 	fmt.Println(index,value)
	// }

	for _, value :=range names {
		fmt.Println(value)
		// value="new"
		// this wont update original values in names
	}
	// if dont want value of index, replace it with _




}