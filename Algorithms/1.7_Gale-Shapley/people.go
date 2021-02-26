package galeshapley

import (
	"encoding/json"
	"fmt"
	"os"
)

func LoadPeopleFromFile(filename string) ([]Person, []Person, error) {
	file := struct {
		People []Person `json:"people"`
	}{}

	var (
		males, females []Person
	)

	f, err := os.Open(filename)
	if err != nil {
		return males, females, err
	}

	err = json.NewDecoder(f).Decode(&file)
	if err != nil {
		return males, females, err
	}

	for personIndex, person := range file.People {
	nextPreference:
		for preferenceIndex, preference := range person.Preferences {
			if person.Name == preference {
				return males, females, fmt.Errorf("person %s cannot prefer themeselves (preferences: %d)", person.Name, preferenceIndex)
			}

			for i, p := range file.People {
				if i != personIndex && p.Name == preference {
					continue nextPreference
				}
			}
			return males, females, fmt.Errorf("%s has an unknown person named %s in their preference list", person.Name, preference)
		}
	}

	for _, person := range file.People {
		if person.Male {
			males = append(males, person)
		} else {
			females = append(females, person)
		}
	}
	return males, females, nil
}
