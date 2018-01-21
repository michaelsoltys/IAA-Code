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

// Extended based on Pseudocode from
// wikipedia:
// https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
// Returned ingeter names used to express the semantics each of the
// returned integers.
func Extended(a, b int) (BézoutCoefficientsX, BézoutCoefficientsY, gcd, quotientsByGCDa, quotientsByGCDb int) {
	s, sPrevious := 0, 1
	t, tPrevious := 1, 0
	r, rPrevious := b, a

	for r > 0 {
		quotient := rPrevious / r
		rPrevious, r = r, rPrevious-quotient*r
		sPrevious, s = s, sPrevious-quotient*s
		tPrevious, t = t, tPrevious-quotient*t
	}

	return sPrevious, tPrevious, rPrevious, t, s
}
