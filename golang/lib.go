package main

// package from go standard library
// fmt- formatting strings and printing to console
import (
	"fmt"
	"sort"
	"strings"
)

// only 1 main function in the application
func main() {

	// String Package
	greeting := "Hola! friends, ola"

	fmt.Println(strings.Contains(greeting, "Hola"))
	fmt.Println(strings.Contains(greeting, "hola"))
	// Prints true of false, if string contains the given word.
	// It is case sensitive

	fmt.Println(strings.ReplaceAll(greeting, "Hola","Hi"))
	// doesn't replace the original string, just returns a new string

	fmt.Println(strings.ToUpper(greeting))

	fmt.Println(strings.Index(greeting, "ola"))
	// returns first occurence starting index of given string 

	fmt.Println(strings.Split(greeting, " "))
	// Splits as empty space


	// Sort Package

	ages:= []int{40,50,1,2,30,70,20,34}
	sort.Ints(ages)
	// changes the original slice
	fmt.Println(ages)


	index := sort.SearchInts(ages,30)
	// Gives the index of given int in the slice, doesnt sort the slice.
	// if try to search an integer not present in the slice, returns the last index+1 (len of slice)
	fmt.Println(index)

	names:= []string{"B","X","D","R","Y"}

	sort.Strings(names)
	fmt.Println(names)

	index2 := sort.SearchStrings(names,"D")

	fmt.Println(index2)


}