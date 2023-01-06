package main

// package from go standard library 
// fmt- formatting strings and printing to console
import "fmt"

// only 1 main function in the application
func main() {
	// Hello world
	fmt.Println("Hello World")

	// Strings and variables

	var nameOne string = "abc" 
	// cannot use single quotes and once a type is assigned cannot change it
 
	var nameTwo = "Automatically identifies type as String"

	// declaring a string, doesnt need to be assigned
	var nameThree string
	// prints empty string for nameThree-> Default is empty string if not assigned

	// nameOne="Can change the string value"

	fmt.Println(nameOne, nameTwo, nameThree)

	// Another way to declare variables
	nameFour := "Name"
	// this method of declaring cannot be used outside of a function

	fmt.Println(nameFour)

	// Int
	var ageOne int = 20
	var ageTwo = 10
	ageThree := 40

	fmt.Println(ageOne, ageTwo, ageThree)

	// bits and memory- int8, int16, int32, int64 to decide how much memory to assign

	var numOne int8= 25

	var numTwo = -128

	// var numThree int8 =-129  not allowed, doesnt fit into the range

	var numThree uint = 25
	// in uint, we cannot assign negative numbers

	fmt.Println(numOne, numTwo, numThree)

	// float- have to declare bit size 32/64

	var scoreOne float32=2.18
	// mostly use float 64

	scoreThree := 1.5 
	// default is float64

	fmt.Println(scoreOne, scoreThree)


	// Printing and formatting

	fmt.Print("Hello ")
	fmt.Print("World ")
	// doesnt add new line at the end, while Println does

	// prints new line now
	fmt.Print("Hello \n")
	fmt.Print("World ")


	// printing string with variables

	fmt.Println("\nAge One is:", ageOne, "and name One is:",nameOne )

	// Formatted strings- %v(variables), %d(int) ,%q(strings), %f(floats), %T(Type)

	fmt.Printf("Age One is: %v , and name One is: %v \n", ageOne,nameOne)
	
	fmt.Printf("Age One is: %d , and name One is: %q \n", ageOne,nameOne)

	fmt.Printf("Float %0.1f", 255.55)

	var str = fmt.Sprintf("\nAge One is: %v , and name One is: %v \n", ageOne,nameOne)
	fmt.Println(str)

	sayGreet("Bhargavi")
	// can use functions, variables (defined outside main function) from other file here, as they both belong to same package, but while running, we need to run both the files

}



