package main

import "fmt"

func main() {
	var num1, num2 int
	fmt.Scanln(&num1)
	fmt.Scanln(&num2)

	if num1 > num2 {
		num1, num2 = num2, num1
	}

	for i := num1 + 1; i < num2; i++ {
		if i%5 == 2 || i%5 == 3 {
			fmt.Println(i)
		}
	}

}
