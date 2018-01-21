package division

import "testing"

func TestDivisionVerbose(t *testing.T) {
	DivisionVerbose(13, 3)
}

func TestDivision3_6(t *testing.T) {
	if q, r := Division(6, 3); q != 2 && r != 0 {
		t.Fail()
	}
}

func TestDivision7_2(t *testing.T) {
	if q, r := Division(7, 2); q != 3 && r != 1 {
		t.Fail()
	}
}

func BenchmarkDivision72(b *testing.B) {
	benchmarkDiv(7, 2, b)
}

func BenchmarkDivision702(b *testing.B) {
	benchmarkDiv(70, 2, b)
}

func BenchmarkDivision7002(b *testing.B) {
	benchmarkDiv(700, 2, b)
}

func benchmarkDiv(x, y int, b *testing.B) {
	for n := 0; n < b.N; n++ {
		Division(x, y)
	}
}
