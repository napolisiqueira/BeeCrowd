package main

import "fmt"

func main() {
	var num int = 1
	var N int

	fmt.Scanln(&N)

	for i := 0; i <= N; i++ {
		fmt.Printf("%d ", num)
		num += 1
		fmt.Printf("%d ", num)
		num += 1
		fmt.Printf("%d PUM\n", num)
		num += 2
	}
}
