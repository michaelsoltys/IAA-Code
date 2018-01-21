package euclids_test

import (
	"testing"

	"github.com/crhntr/alg/euclids"
)

func TestAlg(t *testing.T) {
	if gcd := euclids.Alg(40, 12); gcd != 4 {
		t.Fail()
	}
}

// TestExtended only ensures the Extended algorithm completes
// and returns a valid gcd, not all return values are validated.
func TestExtended(t *testing.T) {
	if _, _, gcd, _, _ := euclids.Extended(40, 12); gcd != 4 {
		t.Fail()
	}
}
