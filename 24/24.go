package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Gate struct {
	In1 string
	In2 string
	Out string
	Op  string
}

const FILE_NAME = "input.txt"

var Wires map[string]int
var Gates []Gate

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}

func run() {
	result := 0

	for len(Gates) > 0 {
		gate := Gates[0]
		Gates = Gates[1:]

		in1, in1Available := Wires[gate.In1]
		in2, in2Available := Wires[gate.In2]

		if !in1Available || !in2Available {
			Gates = append(Gates, gate)
			continue
		}

		switch gate.Op {
		case "AND":
			Wires[gate.Out] = in1 & in2
		case "OR":
			Wires[gate.Out] = in1 | in2
		case "XOR":
			Wires[gate.Out] = in1 ^ in2
		}

		if gate.Out[0] == 'z' {
			i, _ := strconv.Atoi(gate.Out[1:])
			v := Wires[gate.Out]
			result |= v << i
		}
	}

	fmt.Println(result)
}

func main() {
	// Read input
	data, _ := os.ReadFile(FILE_NAME)
	input := string(data)

	// Parse input
	sections := strings.Split(input, "\r\n\r\n")

	Wires = make(map[string]int)
	lines := strings.Split(sections[0], "\r\n")
	for _, line := range lines {
		x := strings.Split(line, ": ")
		v, _ := strconv.Atoi(x[1])
		Wires[x[0]] = v
	}

	lines = strings.Split(sections[1], "\r\n")
	for _, line := range lines {
		fields := strings.Fields(line)
		Gates = append(Gates, Gate{
			In1: fields[0],
			Op:  fields[1],
			In2: fields[2],
			Out: fields[4],
		})
	}

	defer timeTrack(time.Now())

	run()
}
