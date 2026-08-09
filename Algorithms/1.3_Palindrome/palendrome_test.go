package palendrome_test

import (
	"testing"

	palendrome "github.com/crhntr/IAA-Code/Algorithms/1.3_Palindrome"
)

func TestIsPalendromeRacecar(t *testing.T) {
	if !palendrome.Alg("racecar") {
		t.Fail()
	}
}

func TestIsPalendromeAsdffdsa(t *testing.T) {
	if !palendrome.Alg("asdffdsa") {
		t.Fail()
	}
}

func TestIsPalendromeQwertyterwq(t *testing.T) {
	if palendrome.Alg("qwertyterwq") {
		t.Fail()
	}
}
