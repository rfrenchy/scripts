package main

import (
	"image"
	"log"
	"os"

	"github.com/urfave/cli/v2"
	"gopkg.in/gographics/imagick.v2/imagick"
)

func main() {
	app := &cli.App{
		Name:     "insta-resize",
		HelpName: "",
		Usage:    "resize images to instagram ratios",
		Commands: []*cli.Command{},
		Flags:    []cli.Flag{},
		Action: func(ctx *cli.Context) error {
			// get image path from arguments
			//			img_path := ctx.Args().Get(0)

			imagick.Initialize()
			defer imagick.Terminate()

			//imagick.Initialize()
			//defer imagick.Terminate()

			//			_ = imagick.NewMagickWand()

			return nil
		},
	}
	if err := app.Run(os.Args); err != nil {
		log.Fatal(err)
	}
}

// 1:1
func square(_ *image.Image) error {

	return nil
}
