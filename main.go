package main

import (
	"os"

	"github.com/JUNAID-KT/dummybeat/cmd"

	_ "github.com/JUNAID-KT/dummybeat/include"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}
