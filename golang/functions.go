package main

// package from go standard library 
// fmt- formatting strings and printing to console
import (
	"fmt"
	"math"
	"strings"
)

func sayGreet(name string){
	fmt.Printf("Good morning %v\n",name)
}

func sayBye(name string){
	fmt.Printf("Good bye %v\n",name)
}

// function with multiple parameters
func cycleNames(n []string, f func(string)){
	for _,v:=range n{
		f(v)
	}
}

// funtion returning float64 value
func circle(r float64) float64{
	return math.Pi*r*r
}

// function returning multiple values
func getInitials(n string)(string,string){
	s:=strings.ToUpper(n)
	names:=strings.Split(s," ")
	var initials []string
	for _,v :=range names{
		initials=append(initials,v[:1])
	} 

	if len(initials)>1{
		return initials[0],initials[1]
	}
	return initials[0],"_"
}

// func main() {

// 	// sayGreet("Bhargavi")
// 	// sayBye("Bhargavi")

// 	// cycleNames([]string{"Nam","Bhbh","shuhu"},sayGreet)

// 	// fmt.Printf("%0.2f",circle(10.5))

// 	fmt.Println(getInitials("Bhargavi Poyekar"))
// 	fmt.Println(getInitials("Bhargavi poyekar"))
// 	fmt.Println(getInitials("bhargavi poyekar"))
// 	fmt.Println(getInitials("Bhargavi"))

// 	fn,sn:=getInitials("Bhargavi poyekar")
// 	fmt.Println(fn,sn)

// }