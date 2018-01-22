package ulam

// Alg pre-condition: a > 0
func Alg(a int) {
	x := a

	lastValues := make([]int, 3)

	for lastValues[0] != 4 || lastValues[1] != 2 || lastValues[2] != 1 {
		// println(x)

		if x%2 == 0 {
			x = x / 2
		} else {
			x = 3*x + 1
		}

		lastValues = append(lastValues[1:], x) // reuses underlying array
	}
}
