import os

l = ["ALB", "BET", "DOL", "LAG", "OTHER", "SHARK", "YFT"]

for word in l:
    print ("convert -fill black -background white -bordercolor white -border 4 -font Helvetica -pointsize 18 label:\"%s\" \"%s.png\""%(word, word))
    os.system("convert -fill black -background white -bordercolor white -border 4 -font Helvetica -pointsize 18 label:\"%s\" \"%s.png\""%(word, word))
