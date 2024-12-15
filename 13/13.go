package main

import (
	"advent_of_code/utils/grid"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"time"
)

const BUTTON_A_COST int = 3
const BUTTON_B_COST int = 1

var re = regexp.MustCompile(`X[+=](\d+), Y[+=](\d+)`)

type Button struct {
	Action grid.Point
	XCost  float32
	YCost  float32
}

type Machine struct {
	ButtonA Button
	ButtonB Button
	Prize   grid.Point
	Cost    int
}

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}

func check_result(delta grid.Point, machine Machine) bool {
	return ((delta.X%machine.ButtonA.Action.X == 0) && (delta.Y%machine.ButtonA.Action.Y == 0)) ||
		((delta.X%machine.ButtonB.Action.X == 0) && (delta.Y%machine.ButtonB.Action.Y == 0))
}

func run(machines []Machine) {
	var delta grid.Point
	total := 0

	for _, machine := range machines {
		fmt.Println(machine.Prize)
		delta = machine.Prize
		for b := 1; b <= 100; b++ {
			delta = delta.Sub(machine.ButtonB.Action)

			if check_result(delta, machine) {
				a := 0
				a = delta.X / machine.ButtonA.Action.X
				cost := a*BUTTON_A_COST + b*BUTTON_B_COST
				if machine.Cost == 0 || machine.Cost > cost {
					fmt.Println(cost)
					machine.Cost = cost
				}
			}

			if delta.X < 0 || delta.Y < 0 {
				break
			}
		}

		for a := 1; a <= 100; a++ {
			delta = delta.Sub(machine.ButtonA.Action)

			if check_result(delta, machine) {
				b := 0
				b = delta.X / machine.ButtonB.Action.X
				cost := a*BUTTON_A_COST + b*BUTTON_B_COST
				if machine.Cost == 0 || machine.Cost > cost {
					fmt.Println(cost)
					machine.Cost = cost
				}
			}

			if delta.X < 0 || delta.Y < 0 {
				break
			}
		}

		total += machine.Cost
		fmt.Println(machine.Cost)
	}

	fmt.Printf("Total: %d\r\n", total)
}

func main() {
	// Read input
	//data, _ := os.ReadFile("example.txt")
	data, _ := os.ReadFile("input.txt")
	input := string(data)

	// Parse input
	var machines []Machine
	var machine Machine
	lines := strings.Split(input, "\r\n")
	for _, line := range lines {
		matches := re.FindStringSubmatch(line)
		if matches != nil {
			x, _ := strconv.Atoi(matches[1])
			y, _ := strconv.Atoi(matches[2])

			switch {
			case strings.Contains(line, "Button A:"):
				machine.ButtonA.Action = grid.Point{X: x, Y: y}
				machine.ButtonA.XCost = float32(x) / 3.0
				machine.ButtonA.YCost = float32(y) / 3.0
			case strings.Contains(line, "Button B:"):
				machine.ButtonB.Action = grid.Point{X: x, Y: y}
				machine.ButtonB.XCost = float32(x) / 1.0
				machine.ButtonB.YCost = float32(y) / 1.0
			case strings.Contains(line, "Prize:"):
				machine.Prize = grid.Point{X: x, Y: y}
			}
		} else {
			machines = append(machines, machine)
		}
	}

	defer timeTrack(time.Now())

	run(machines)
}
