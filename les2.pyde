g_x = 0
g_y = 300


def setup():
    size(800,600)
    
def draw():
    global g_x
    global g_y
    noStroke() 
    fill(random(255),random(255),255)
    g_x +=5
    if(g_x> width):
        g_x = 0
        
    ellipse(g_x,g_y,100,100) 
