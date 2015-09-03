import simplegui
import random
#@Anne Marie Hoskins
#PONG game

#Set Canvas Height
canvas_width = 900
canvas_height = 600

#Define width of paddle and paddle center
paddle_width = 20
paddle_height = 80
paddle_center_pink = [paddle_width/2, canvas_height/2]
paddle_center_blue = [paddle_width/2, canvas_height/2]
paddle_velocity_pink = 0
paddle_velocity_blue = 0

#Define ball stuff
radius = 20 
ball_pos = [canvas_width/2,canvas_height/2]
accX = 3
accY = 3
vel = [1, .5]
vel[0] = random.choice([-1,1])
vel[1] = random.choice([-.5,-.25,.5,.25,.1])

#blue Score Stuff
score_blue = "0"
xblue = ((canvas_width*3)/4- paddle_width*2)
yblue = 50

#pink score stuff
score_pink = "0"
xpink = (canvas_width/4 - paddle_width*2)
ypink = 50

def key_down_handler(key):
    global vel_down, paddle_velocity_pink, paddle_velocity_blue
    vel_down = 5
    if key == simplegui.KEY_MAP['v']:
        paddle_velocity_pink = paddle_velocity_pink + vel_down
    if key == simplegui.KEY_MAP['f']:
        paddle_velocity_pink = paddle_velocity_pink - vel_down
    if key == simplegui.KEY_MAP['down']:
        paddle_velocity_blue = paddle_velocity_blue + vel_down
    if key == simplegui.KEY_MAP['up']:
        paddle_velocity_blue = paddle_velocity_blue - vel_down
        
def key_up_handler(key):
    global paddle_velocity_pink, paddle_velocity_blue
    if key == simplegui.KEY_MAP['v']:
        paddle_velocity_pink = 0
    if key == simplegui.KEY_MAP['f']:
        paddle_velocity_pink = 0
    if key == simplegui.KEY_MAP['down']:
        paddle_velocity_blue = 0
    if key == simplegui.KEY_MAP['up']:
        paddle_velocity_blue = 0
def spawn_ball():
    global accX, accY, ball_pos, vel
    #resets ball to the center, chooses a direction, resets velocity
    accX = 3
    accY = 3
    vel = [1, 0]
    vel[0] = random.choice([-1,1])
    vel[1] = random.choice([-.5,-.25,.5,.25,.1])
    ball_pos = [canvas_width/2,canvas_height/2]
    ball_pos[0] += accX*vel[0]
    ball_pos[1] += accY*vel[1]
    

def draw_handler(canvas):
    global accX, accY, score_blue, score_pink, vel
    #Draws the paddles
    paddle_center_pink[1] = paddle_center_pink[1] + paddle_velocity_pink
    paddle_center_blue[1] = paddle_center_blue[1] + paddle_velocity_blue
    canvas.draw_line((paddle_center_pink[0], paddle_center_pink[1]-40),(paddle_center_pink[0], paddle_center_pink[1]+40) , paddle_width, 'deeppink')
    canvas.draw_line((canvas_width-paddle_width/2, paddle_center_blue[1]-40),(canvas_width-paddle_width/2, paddle_center_blue[1]+40) , paddle_width, 'deepskyblue')
    
    #draws the gutter lines
    canvas.draw_line((paddle_width,0), (paddle_width, 900), 1, 'deeppink')
    canvas.draw_line((canvas_width-paddle_width,0), (canvas_width-paddle_width, 900), 1, 'deepskyblue')
    
    #draw center line
    canvas.draw_line((canvas_width/2,0), (canvas_width/2,canvas_height), 2, 'white')
    
    #draw Ball
    canvas.draw_circle(ball_pos, radius, 2, 'darkorange', 'darkorange')
    
    #draws score for each color by dividing the screen to make it centered
    canvas.draw_text(score_blue, [xblue+69,yblue] , 20, 'deepskyblue',"monospace")
    canvas.draw_text("SCORE", [xblue,yblue] , 20, 'deepskyblue', "monospace")
    canvas.draw_text(score_pink, [xpink+69,ypink] , 20, 'deeppink',"monospace")
    canvas.draw_text("SCORE", [xpink,ypink] , 20, 'deeppink', "monospace")
    
    # updates the ball position based on the velocity and acceleration 
    ball_pos[0] += accX*vel[0]
    ball_pos[1] += accY*vel[1]
    
    #prevents ball from moving too fast in both 
    if accX >= 25:
        accX = 25
    if accX <= -25:
        accX = -25
    if accY >= 25:
        accY = 25
    if accY <= -25:
        accY = -25
    
    #bounce off paddle?
    #left
    if ball_pos[0] - radius <= paddle_width:   
        if ball_pos[1] <= paddle_center_pink[1] + paddle_height/2 and ball_pos[1] >= paddle_center_pink[1]-paddle_height/2:
            accX = accX * -1.08
            ball_pos[0] = radius + paddle_width
         
        else:
            score_blue = int(score_blue) + 1
            score_blue = str(score_blue)
            spawn_ball()
    #right      
    if ball_pos[0] >= canvas_width - (radius + paddle_width):
        if ball_pos[1] <= paddle_center_blue[1] + paddle_height/2 and ball_pos[1] >= paddle_center_blue[1]-paddle_height/2:
            accX = accX * -1.08
            ball_pos[0] = canvas_width - (radius+paddle_width)
        else:
            score_pink = int(score_pink) + 1
            score_pink = str(score_pink)
            spawn_ball()
    
    #  bottom
    if ball_pos[1] >  canvas_height - radius:
        accY = accY * -1
        ball_pos[1] = canvas_height - radius
    #  top
    if ball_pos[1] < radius:
        accY = accY * -1
        ball_pos[1] = radius

frame = simplegui.create_frame('PONG', canvas_width, canvas_height)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_down_handler)
frame.set_keyup_handler(key_up_handler)
frame.start()


