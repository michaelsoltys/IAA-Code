package euclids

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
