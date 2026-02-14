from PIL import Image
import os

BASE = os.path.join(os.path.dirname(__file__), '..', 'giveaways', 'static', 'giveaways')
IN = os.path.join(BASE, 'giveawayF.png')
OUT = os.path.join(BASE, 'giveawayF_transparent.png')

im = Image.open(IN).convert('RGBA')
px = im.load()
width, height = im.size

# sample corner pixels to detect background color
corners = [px[0,0], px[width-1,0], px[0,height-1], px[width-1,height-1]]
# take the most common color among corners
from collections import Counter
col_counts = Counter(corners)
bg_color = col_counts.most_common(1)[0][0]
print('Detected background color (RGBA):', bg_color)

# tolerance for color similarity
tol = 30

def similar(c1, c2, tol=tol):
    return all(abs(c1[i]-c2[i])<=tol for i in range(3))

for y in range(height):
    for x in range(width):
        r,g,b,a = px[x,y]
        if similar((r,g,b), bg_color[:3], tol):
            px[x,y] = (r,g,b,0)

im.save(OUT)
print('Saved transparent image to', OUT)
