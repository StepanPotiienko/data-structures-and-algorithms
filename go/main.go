package main

import "fmt"

// O(N)
func linearSearch(list []any, target any) int {
	for i := 0; i < len(list); i++ {
		if list[i] == target {
			return i
		}
	}

	return -1
}

// That's the basic example of O(N).
// As N goes up, O also goes up. That's called Linear Difficulty.
// By the way, if we have O(2N), we would usually drop constants.
func sum(list []float64) float64 {
	sum := 0.0

	for i := 0; i < len(list); i++ {
		sum += list[i]
	}

	return sum
}

// But what if we have 2D array?
// Well, then we will get O(N^2).
func SumOf2DArray(array [][]float64) float64 {
	sum := 0.0

	for i := 0; i < len(array); i++ {
		for j := 0; j < len(array[i]); j++ {
			sum += array[i][j]
		}
	}

	return sum
}

func main() {
	a := [...]any{1, 2, 3, 4, 5}
	testing_array := [][]float64{{0, 1, 1}, {0, 1, 0}}

	fmt.Println(a)
	fmt.Println("Entry found at position", linearSearch(a[:], 2))

	fmt.Println(testing_array)
	fmt.Println("The sum of testing_array: ", SumOf2DArray(testing_array))
}
