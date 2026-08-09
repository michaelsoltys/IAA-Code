package galeshapley

import (
	"strings"
)

type Person struct {
	Name        string   `json:"name"`
	Male        bool     `json:"male"`
	Preferences []string `json:"preferences"`

	Match *Person
}

func Alg(males, females []Person) {
	// by having a nil EngagedTo, a person is free... inital state all
	// people are free

	// while (∃ free man m who still has a woman w to propose to)
	for SinglesExist(males) {
		for mi := range males {
			if !males[mi].IsSingle() {
				continue
			}

			fi := males[mi].GetPreferedMatch(females)
			if females[fi].IsSingle() {
				match(&males[mi], &females[fi])
				continue
			}

			if females[fi].CompareToExistingMatch(&males[mi]) {
				females[fi].BreakUp()
				match(&males[mi], &females[fi])
				continue
			}
		}
	}
}

func (person Person) String() string {
	str := strings.Title(person.Name)
	if person.Match == nil {
		str += " (single)"
		return str
	}
	str += " is engaged to "
	str += strings.Title(person.Match.Name)
	return str
}

func (person Person) IsSingle() bool {
	return person.Match == nil
}

func (person *Person) BreakUp() {
	person.Match.Match = nil
	person.Match = nil
}

// Perfers returns
//  n > 1 if person1 a is prefered
//  n = 0 if there is no preference
//  n < 1 if person2 a is prefered
func (person Person) CompareToExistingMatch(otherPerson *Person) bool {
	otherPersonIndex := len(person.Preferences)
	engagedToIndex := len(person.Preferences)

	for i, prefName := range person.Preferences {
		if prefName == otherPerson.Name {
			otherPersonIndex = i
		}
		if prefName == person.Match.Name {
			engagedToIndex = i
		}
	}

	return engagedToIndex > otherPersonIndex
}

func (person *Person) GetPreferedMatch(people []Person) int {
	preferenceIndex := 0

	for preferenceIndex = range people {
		if people[preferenceIndex].Name == person.Preferences[0] {
			break
		}
	}

	if len(person.Preferences) > 1 {
		person.Preferences = person.Preferences[1:] // shortens preference list
	}
	return preferenceIndex
}

func SinglesExist(people []Person) bool {
	for i := range people {
		if people[i].Match == nil {
			return true
		}
	}
	return false
}

func match(person1, person2 *Person) {
	person1.Match, person2.Match = person2, person1
}
