package division

import "fmt"

// Alg returns quotient (q) and remainder (r)
// for a given dividend (x) and divisor (y)
func Alg(x, y int) (int, int) {
	q, r := 0, x

	for y <= r {
		r, q = r-y, q+1
	}

	return q, r
}

func Verbose(x, y int) (int, int) {
	q, r := 0, x
	fmt.Printf("Precondition: x≥0 AND y≥0: %t\n", x >= 0 && y >= 0)

	for y <= r {
		fmt.Printf("x: %-3d y: %-3d r: %-3d q: %-3d   ", x, y, r, q)
		fmt.Printf("Loop Invariant: x = (q*y) + r ⋏ r ≥ 0: %t\n", x == (q*y)+r && r >= 0)
		r, q = r-y, q+1
	}

	fmt.Printf("Postcondition: x=(q*y)+r ⋏ 0 ≤ r < y: %t\n", x == (q*y)+r && 0 <= r && r < y)

	return q, r
}
