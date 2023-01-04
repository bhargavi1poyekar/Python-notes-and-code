package main

// package from go standard library 
// fmt- formatting strings and printing to console
import "fmt"

// only 1 main function in the application
func main() {

	age:=45

	// fmt.Println(age<=50)
	// fmt.Println(age>=50)
	// fmt.Println(age==45)
	// fmt.Println(age!=50)

	if age<30{
		fmt.Println("Hello")
	}else if age <40{
		fmt.Println("Hii")
	}else{
		fmt.Println("Yoo")
	}


	// if else inside loop

	names:= []string{"B","X","D","R","Y"}
	
	for index, value :=range names {

		if index==1{
			fmt.Println(index)
			continue
			// continues to next iteration, without executing further statements in the loop
		}

		fmt.Println(value)
	}
}