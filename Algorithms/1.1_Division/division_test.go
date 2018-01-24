package division_test

import (
	"testing"

	division "github.com/crhntr/IAA-Code/Algorithms/1.1_Division"
)

func TestAlg3_6(t *testing.T) {
	if q, r := division.Alg(6, 3); q != 2 && r != 0 {
		t.Fail()
	}
}

func TestAlg7_2(t *testing.T) {
	if q, r := division.Alg(7, 2); q != 3 && r != 1 {
		t.Fail()
	}
}

func BenchmarkAlg72(b *testing.B) {
	benchmarkDiv(7, 2, b)
}

func BenchmarkAlg702(b *testing.B) {
	benchmarkDiv(70, 2, b)
}

func BenchmarkAlg7002(b *testing.B) {
	benchmarkDiv(700, 2, b)
}

func benchmarkDiv(x, y int, b *testing.B) {
	for n := 0; n < b.N; n++ {
		division.Alg(x, y)
	}
}

func ExampleAlg() {
	division.Verbose(13, 3)

	// Output: Precondition: x≥0 AND y≥0: true
	// x: 13  y: 3   r: 13  q: 0     Loop Invariant: x = (q*y) + r ⋏ r ≥ 0: true
	// x: 13  y: 3   r: 10  q: 1     Loop Invariant: x = (q*y) + r ⋏ r ≥ 0: true
	// x: 13  y: 3   r: 7   q: 2     Loop Invariant: x = (q*y) + r ⋏ r ≥ 0: true
	// x: 13  y: 3   r: 4   q: 3     Loop Invariant: x = (q*y) + r ⋏ r ≥ 0: true
	// Postcondition: x=(q*y)+r ⋏ 0 ≤ r < y: true
}
