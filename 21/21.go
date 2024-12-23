package main

import (
	"advent_of_code/utils/grid"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

const FILE_NAME = "example.txt"

type Node struct {
	Location grid.Point
	Steps    int
	Path []int
}

var NumericKeypad = [4][3]int{
	{7, 8, 9},
	{4, 5, 6},
	{1, 2, 3},
	{-1, 0, 0x0A},
}

var DirectionalKeypad = [2][3]int{
	{-1, grid.DIR_UP, 0x0A},
	{grid.DIR_LEFT, grid.DIR_DOWN, grid.DIR_RIGHT},
}

var Codes [][]int

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}

func bfs(start grid.Point, target int, keypad [][]int) []grid.Point {
	stack := []Node{{Location: start, Steps: 0}}

	for len(stack) > 0 {
		n := stack[0]
		stack = stack[1:]

		unvisited := 
	}
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
		var code []int
		for _, c := range line {
			v, _ := strconv.ParseInt(string(c), 16, 0)
			code = append(code, int(v))
		}
		Codes = append(Codes, code)
	}

	defer timeTrack(time.Now())

	run()
}
