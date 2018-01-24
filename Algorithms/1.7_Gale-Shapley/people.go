package galeshapley

import (
	"encoding/json"
	"fmt"
	"os"
)

func LoadPeopleFromFile(filename string) ([]Person, error) {
	file := struct {
		People []Person `json:"people"`
	}{}

	f, err := os.Open(filename)
	if err != nil {
		return file.People, err
	}

	err = json.NewDecoder(f).Decode(&file)
	if err != nil {
		return file.People, err
	}

	for personIndex, person := range file.People {
	nextPreference:
		for preferenceIndex, preference := range person.Preferences {
			if person.Name == preference {
				return file.People, fmt.Errorf("person %s cannot prefer themeselves (preferences: %d)", person.Name, preferenceIndex)
			}

			for i, p := range file.People {
				if i != personIndex && p.Name == preference {
					continue nextPreference
				}
			}
			return file.People, fmt.Errorf("%s has an unknown person named %s in their preference list", person.Name, preference)
		}
	}

	return file.People, nil
}

func SortPeopleByGender(people []Person) (males, females []Person) {
	for _, person := range people {
		if person.Male {
			males = append(males, person)
		} else {
			females = append(females, person)
		}
	}
	return
}
