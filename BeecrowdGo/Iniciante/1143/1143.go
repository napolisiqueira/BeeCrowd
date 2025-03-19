package main

import "fmt"

func main() {
	var N int

	fmt.Scanln(&N)

	for i := 1; i <= N; i++ {
		var num1 int = i * i
		var num2 int = i * num1
		fmt.Printf("%d %d %d\n", i, num1, num2)
	}
}
