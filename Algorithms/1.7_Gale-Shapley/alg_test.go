package stablemarriage

import (
	"testing"
)

func TestAlg00(t *testing.T) {
	people, err := LoadPeopleFromFile("testdata/set00.json")
	if err != nil {
		t.Fatal(err)
	}
	males, females := SortPeopleByGender(people)
	Alg(males, females)

	if SinglesExist(males) || SinglesExist(females) {
		t.Fail()
	}
	// for _, person := range males {
	// 	t.Log(person)
	// }
}

func TestAlg01(t *testing.T) {
	people, err := LoadPeopleFromFile("testdata/set01.json")
	if err != nil {
		t.Fatal(err)
	}
	males, females := SortPeopleByGender(people)
	Alg(males, females)

	if SinglesExist(males) || SinglesExist(females) {
		t.Fail()
	}
	// for _, person := range males {
	// 	t.Log(person)
	// }
}

func TestAlg02(t *testing.T) {
	people, err := LoadPeopleFromFile("testdata/set02.json")
	if err != nil {
		t.Fatal(err)
	}
	males, females := SortPeopleByGender(people)

	for _, person := range append(males, females...) {
		t.Log(person)
	}

	Alg(males, females)

	if SinglesExist(males) || SinglesExist(females) {
		t.Fail()
	}
	for _, person := range males {
		t.Log(person)
	}
}

func TestLoadPeopleFromFile(t *testing.T) {
	if _, err := LoadPeopleFromFile("testdata/badData.json"); err == nil {
		t.Error("testdata/badData.json should err")
	}
	if _, err := LoadPeopleFromFile("testdata/badData00.json"); err == nil {
		t.Error("testdata/badData00.json should err")
	}
	if _, err := LoadPeopleFromFile("testdata/badData01.json"); err == nil {
		t.Error("testdata/badData01.json should err")
	}
	if _, err := LoadPeopleFromFile("testdata/badData02.json"); err == nil {
		t.Error("testdata/badData02.json should err")
	}
}
