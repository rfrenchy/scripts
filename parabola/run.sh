# python3 parabola.py --pow 1 -o ballp1.gif                      
python3 cli.py --pow 2 -o ballp2.gif                      
python3 cli.py --pow 3 -o ballp3.gif                      
python3 cli.py --pow 4 -o ballp4.gif                      
python3 cli.py --pow 5 -o ballp5.gif                      



# python3 ../montage/montage.py --glob "*.gif" -r 2 -c 2 -o ball.gif

# doesn't work, image magick doesn't work as intended with gifs
# montage -geometry +0+0 -tile 2x2 ballp2.gif ballp3.gif ballp4.gif ballp5.gif ball.gif

# find . -maxdepth 1 -name "ball*.gif" |
#    xargs -n1 xdg-open 

# python3 parabola.py --pow 2 -o ball-p2.png
# python3 parabola.py --pow 3 -o ball-p3.png
# python3 parabola.py --pow 4 -o ball-p4.png
# python3 parabola.py --pow 5 -o ball-p5.png
# 
# find . -maxdepth 1 -name "ball*" |
#     xargs -n1 xdg-open 

