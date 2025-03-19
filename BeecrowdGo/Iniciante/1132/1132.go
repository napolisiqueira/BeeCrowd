package main

import "fmt"

func main() {
	var num1, num2 int
	var soma int
	fmt.Scanln(&num1)
	fmt.Scanln(&num2)

	if num1 > num2 {
		num2, num1 = num1, num2
	}

	for i := num1; i <= num2; i++ {
		if (i % 13) == 0 {
			continue
		} else {
			soma += i
		}
	}
	fmt.Println(soma)
}
