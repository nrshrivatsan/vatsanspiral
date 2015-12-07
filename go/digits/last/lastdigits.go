package main

import (
	"./primes"
)
func main() {

  println(primes.GetPrimes())
	// for i, v := range primes.GetPrimes() {
	// 	print(v % 10)
	// 	if i+1 >= 40 {
	// 			break
	// 	} else {
	// 		print(",")
	// 	}
	// }
}
