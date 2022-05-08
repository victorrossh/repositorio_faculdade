import turtle

turtle.hideturtle()
turtle.setup(1000, 700)
turtle.speed(2)
turtle.title("Mulher Maravilha")

ouro1 = [(0,0), (-30,40), (0,80), (30,40), (0,0)]

ouro2 = [(0,90), (-34,45), (-64,85), (-20,140), (-35, 150), (-20,160), (10,160), (64,85), (34,45), (0,90)]

ouro3 = [(-4,-4), (-128,160), (-400,160), (-370,120), (-153,120),(-31,-41), (-4,-4)]

ouro4 = [(4,-4), (128,160), (400,160), (370,120), (153,120), (31,-41), (4,-4)]

ouro5 = [(-366,115), (-156,115), (-69,0), (-96,-37), (-181,75), (-336,75), (-366,115)]

ouro6 = [(366,115), (156,115), (69,0), (96,-37), (181,75), (336,75), (366,115)]

ouro7 = [(-35,-45), (-66,-4), (-96,-45), (-184,70), (-332,70), (-302,30), (-206,30), (-94,-120), (-35,-45)]

ouro8 = [(35,-45), (66,-4), (96,-45), (184,70), (332,70), (302,30), (206,30), (94,-120), (35,-45)]

posicao1 = (0, 0)

posicao2 = (0, 90)

posicao3 = (-4, -4)

posicao4 = (4, -4)

posicao5 = (-366, 115)

posicao6 = (366, 115)

posicao7 = (-35, -45)

posicao8 = (35, -45)

def mulher_parte(part, posicaoGoto, fillColor):
    turtle.up()
    turtle.goto(posicaoGoto)
    turtle.down()
    turtle.color(fillColor)
    turtle.begin_fill()

    for x in range(len(part)):
        turtle.goto(part[x])
    
    turtle.end_fill()


mulher_parte(part = ouro1, posicaoGoto = posicao1, fillColor = '#B69312')

mulher_parte(part = ouro2, posicaoGoto = posicao2, fillColor = '#B69312')

mulher_parte(part = ouro3, posicaoGoto = posicao3 , fillColor ='#B69312')

mulher_parte(part = ouro4, posicaoGoto = posicao4, fillColor ='#B69312')

mulher_parte(part = ouro5, posicaoGoto = posicao5, fillColor ='#B69312')

mulher_parte(part = ouro6, posicaoGoto = posicao6, fillColor ='#B69312')

mulher_parte(part = ouro7, posicaoGoto = posicao7, fillColor ='#B69312')

mulher_parte(part = ouro8, posicaoGoto = posicao8, fillColor ='#B69312')


turtle.hideturtle()
turtle.done()