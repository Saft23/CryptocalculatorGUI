import pyglet
class Square():
    def __init__(self,startx, starty, dx, dy, r,g,b):
        self.startx = startx
        self.starty = starty
        self.dx = dx
        self.dy = dy
        self.r = r
        self.g = g
        self.b = b
        self.width = startx-dx
        self.height = starty-dy
        self.color = [r,g,b]
        self.cords = (startx,starty,dx,dy)
        self.averageX = int(((dx-startx)//2)+startx)
        self.averageY = int(((dy-starty)//2)+starty)
        
    def draw(self):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS, [0,2,1,3,1,2,3,0], 
            ('v2i', (self.startx, 
                self.starty, self.startx+self.dx, 
                self.starty, self.startx+self.dx,self.starty+self.dy,self.startx,self.startx+self.dy)),
            ('c3B',(self.r,self.g,self.b,self.r,self.g,self.b,self.r,self.g,self.b,self.r,self.g,self.b)))

    def within(self,x,y):
        if(x >= self.startx and x <= self.dx):
            if(y >= self.starty and y <= self.dy):
                return 1
        else:
            return 0
class Label():
    def __init__(self,text,font,size,x,y,anchorX,anchorY):
        self.text = text
        self.font = font
        self.size = size
        self.x = x
        self.y = y
        self.anchorX = anchorX
        self.anchorY = anchorY
        label = pyglet.text.Label(self.text,
        font_name=self.font,
        font_size=self.size,
        x=self.x,y=self.y,
        anchor_x=self.anchorX, anchor_y=self.anchorY)


    def draw(self):
        label = pyglet.text.Label(self.text,
        font_name=self.font,
        x = self.x, y = self.y,
        font_size=self.size,
        anchor_x=self.anchorX, anchor_y=self.anchorY)
        label.draw()

