package palendrome

// Alg returns whether a given string word
// is a palendrome.
func Alg(word string) bool {
	n := len(word) - 1
	for i := 0; i <= len(word)/2; i++ {
		if word[i] != word[n-i] {
			return false
		}
	}
	return true
}
