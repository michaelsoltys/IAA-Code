package euclids

// Alg returns the gcd of two numbers a and b
// folloing euclids algorithm
func Alg(a, b int) int {
	m, n, r := a, b, a%b

	for r > 0 {
		m, n, r = n, r, m%n
	}

	return n
}
