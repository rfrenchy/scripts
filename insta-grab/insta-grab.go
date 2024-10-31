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

			// fmt.Println("hello world")

			var ix string
			username := os.Getenv("INSTAGRAM_USERNAME")
			password := os.Getenv("INSTAGRAM_PASSWORD")

			fmt.Println(username)

			// TODO, setup a profile directory to avoid logging in out
			// https://stackoverflow.com/questions/59287313/load-up-existing-chrome-user-profile-data-with-chromedp
			chromedp.Flag("profile-directory", "Profile 1")
			chromedp.UserDataDir("/home/user/.config/chromium/Profile 1")
			chromedp.Flag("disable-sync", false)

			// login
			err := chromedp.Run(ctxx,
				chromedp.Navigate("https://www.instagram.com/p/C04EDoCIahN/"),           // go to url
				chromedp.Click("._a9--", chromedp.ByQuery),                              // click allow all cookies
				chromedp.SendKeys("[aria-label~=username]", username, chromedp.ByQuery), // enter username
				chromedp.SendKeys("[aria-label=Password]", password, chromedp.ByQuery),  // enter password
				chromedp.OuterHTML("button._acan", &ix, chromedp.ByQuery),               // click login
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
