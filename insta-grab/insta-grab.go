package main

import (
	"fmt"
	"log"
	"os"

	"github.com/chromedp/chromedp"
	"github.com/urfave/cli/v2"
)

func main() {
	app := &cli.App{
		Name:  "insta-grab",
		Usage: "use to download images from a given instagram url",
		Action: func(ctx *cli.Context) error {

			ctxx, cancel := chromedp.NewContext(ctx.Context)
			defer cancel()

			var html string
			err := chromedp.Run(ctxx,
				// todo make param gained from input
				//	chromedp.Navigate("https://www.instagram.com/p/C04EDoCIahN/"),
				chromedp.Navigate("www.google.com"),
				chromedp.OuterHTML("#splash-screen", &html, chromedp.ByQuery),
			)

			if err != nil {
				return err
			}

			fmt.Println(html)

			return err

			// login to instagram

			// e.g input: a instagram url e.g. https://www.instagram.com/p/DBTa9CtI6lj/?img_index=1

			// pull down all images from url
		},
	}

	if err := app.Run(os.Args); err != nil {
		log.Fatal(err)
	}
}
