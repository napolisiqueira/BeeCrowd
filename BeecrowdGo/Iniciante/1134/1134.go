package main

import "fmt"

/*
(codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário
informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código
(até que seja válido). O programa será encerrado quando o código informado for o número 4.
*/
func main() {

	var alcool int
	var gasolina int
	var diesel int

	for {
		var resp string
		fmt.Scanln(&resp)

		switch resp {
		case "1":
			alcool += 1
		case "2":
			gasolina += 1
		case "3":
			diesel += 1
		case "4":
			fmt.Println("MUITO OBRIGADO")
			fmt.Printf("Alcool: %d\n", alcool)
			fmt.Printf("Gasolina: %d\n", gasolina)
			fmt.Printf("Diesel: %d\n", diesel)
			return
		default:
			continue
		}
	}
}
