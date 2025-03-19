/*
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
*/
package main

import "fmt"

func main() {
	var l1, l2, l3 float64

	fmt.Scanln(&l1, &l2, &l3)

	// Ensure l1 is the largest side
	if l1 < l2 {
		l1, l2 = l2, l1
	}
	if l2 < l3 {
		l2, l3 = l3, l2
	}

	// First check if it's a valid triangle
	if l1 >= l2+l3 {
		fmt.Println("NAO FORMA TRIANGULO")
		return
	}

	// Check the type of triangle
	// Check for right triangle (Pythagorean theorem)
	if (l1 * l1) == (l2*l2)+(l3*l3) {
		fmt.Println("TRIANGULO RETANGULO")
	}

	// Check for obtuse triangle
	if (l1 * l1) > (l2*l2)+(l3*l3) {
		fmt.Println("TRIANGULO OBTUSANGULO")
	}

	// Check for acute triangle
	if (l1 * l1) < (l2*l2)+(l3*l3) {
		fmt.Println("TRIANGULO ACUTANGULO")
	}

	// Check for equilateral triangle (all sides equal)
	if l1 == l2 && l2 == l3 {
		fmt.Println("TRIANGULO EQUILATERO")
	}

	// Check for isosceles triangle (two sides equal)
	if l1 == l2 || l2 == l3 || l3 == l1 {
		fmt.Println("TRIANGULO ISOSCELES")
	}
}
