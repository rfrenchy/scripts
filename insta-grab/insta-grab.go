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

			var ix string
			//			username := os.Getenv("INSTAGRAM_USERNAME")
			//	password := os.Getenv("INSTAGRAM_PASSWORD")

			//			fmt.Println(username)

			// TODO, setup a profile directory to avoid logging in out
			// https://stackoverflow.com/questions/59287313/load-up-existing-chrome-user-profile-data-with-chromedp

			opts := append(chromedp.DefaultExecAllocatorOptions[:],
				chromedp.Flag("profile-directory", "Profile 1"),
				chromedp.UserDataDir("/home/ryan/.config/google-chrome/Profile 1"),
				chromedp.Flag("disable-sync", false),
				chromedp.Flag("headless", false),
			)

			e_ctx, cancel := chromedp.NewExecAllocator(ctx.Context, opts...)
			defer cancel()

			ctxx, cancel := chromedp.NewContext(e_ctx, chromedp.WithLogf(log.Printf))
			defer cancel()

			// login
			err := chromedp.Run(ctxx,
				chromedp.Navigate("https://www.instagram.com/p/C04EDoCIahN/"), // go to url
				chromedp.OuterHTML("img[src*=scontent]", &ix, chromedp.ByQuery),
			//	chromedp.Click("._a9--", chromedp.ByQuery),                              // click allow all cookies
			//	chromedp.SendKeys("[aria-label~=username]", username, chromedp.ByQuery), // enter username
			//	chromedp.SendKeys("[aria-label=Password]", password, chromedp.ByQuery),  // enter password
			//	chromedp.OuterHTML("button._acan", &ix, chromedp.ByQuery),               // click login
			//chromedp.OuterHTML("[aria-label=Password]", &ix, chromedp.ByQuery),      // click login
			//chromedp.OuterHTML("*", &ix, chromedp.ByQuery),
			)

			if err != nil {
				return err
			}

			fmt.Println(ix)

			return err

			// login to instagram

			// pull down all images from url
		},
	}

	if err := app.Run(os.Args); err != nil {
		log.Fatal(err)
	}
}
