package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	"github.com/chromedp/chromedp"
	"github.com/urfave/cli/v2"
)

func main() {
	app := &cli.App{
		Name:  "insta-grab",
		Usage: "download images from instagram",
		Action: func(ctx *cli.Context) error {

			// HAVE TO SETUP LOGIN THE FIRST TIME THIS IS RAN
			opts := append(chromedp.DefaultExecAllocatorOptions[:],
				chromedp.Flag("profile-directory", "Scraper"),
				chromedp.UserDataDir("/home/ryan/.config/google-chrome/Scraper"),
				chromedp.Flag("disable-sync", false),
				//chromedp.Flag("headless", false),
			)

			e_ctx, cancel := chromedp.NewExecAllocator(ctx.Context, opts...)
			defer cancel()

			ctxx, cancel := chromedp.NewContext(e_ctx, chromedp.WithLogf(log.Printf))
			defer cancel()

			// Find image url
			var url string
			var sx bool
			err := chromedp.Run(ctxx,
				chromedp.Navigate("https://www.instagram.com/p/C04EDoCIahN/"), // go to url
				chromedp.AttributeValue("img[src*=scontent]", "src", &url, &sx, chromedp.ByQuery),
			)

			if err != nil {
				return err
			}

			fmt.Println(url)

			// save image from url
			resp, err := http.Get(url)
			if err != nil {
				return err
			}
			defer resp.Body.Close()

			file, err := os.Create("./12312312.png")
			if err != nil {
				return err
			}
			defer file.Close()

			_, err = io.Copy(file, resp.Body)
			if err != nil {
				return err
			}

			return err
		},
	}

	if err := app.Run(os.Args); err != nil {
		log.Fatal(err)
	}
}
