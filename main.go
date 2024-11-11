package main

import "fmt"

func linearSearch(list []any, target any) int {
	for i := 0; i < len(list); i++ {
		if list[i] == target {
			return i
		}
	}

	return -1
}

func main() {
	a := [...]any{1, 2, 3, 4, 5}

	fmt.Println(a)
	fmt.Println("Entry found at position", linearSearch(a[:], 2))
}
