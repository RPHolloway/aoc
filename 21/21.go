package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

const FILE_NAME = "example.txt"

var Codes [][]rune

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}

func run() {

}

func main() {
	// Read input
	data, _ := os.ReadFile(FILE_NAME)
	input := string(data)

	// Parse input
	lines := strings.Split(input, "\r\n")
	for _, line := range lines {
		Codes = append(Codes, []rune(line))
	}

	defer timeTrack(time.Now())

	run()
}
