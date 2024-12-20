from django.shortcuts import render

# Create your views here.
def sports(request):
    return render(request, 'sports.html')
def News(request,data):
    if(data=='cricket'):
        htmldata={
            'name':'Cricket',
            'information':" Originating in England, cricket is a bat-and-ball game that has become immensely popular in countries like India, Australia, and England. Played between two teams of 11 players, it features various formats, including Test matches, One Day Internationals (ODIs), and T20s. The game emphasizes strategy, skill, and sportsmanship, with iconic tournaments like the ICC Cricket World Cup and the Indian Premier League (IPL) drawing massive audiences. Cricket has a rich history, with legendary players like Sachin Tendulkar, Sir Donald Bradman, and Viv Richards leaving an indelible mark on the sport. The game fosters a sense of community and national pride, especially during international competitions",
            'imsrc':'IMAGES/cricket.png'
        }
    elif(data=='chess'):
        htmldata={
            'name':"Chess",
            'information':'A two-player strategy board game with roots in India, chess is played on an 8x8 grid with 16 pieces per player, including pawns, knights, bishops, rooks, a queen, and a king. The objective is to checkmate the opponents king, leading to a win. Chess is renowned for its deep strategic elements and has a rich history, with global tournaments like the World Chess Championship and the Chess Olympiad showcasing top talent. The game has evolved with technology, leading to online platforms where players can compete globally. Chess has also gained popularity in schools, promoting critical thinking and problem-solving skills among students',
            'imsrc':'IMAGES/chess.png'
        }
    elif(data=='kabbadi'):
        htmldata={
            'name':"Kabbadi",
            'information':'A traditional Indian contact sport, kabaddi involves two teams taking turns to send a "raider" into the opponents half to tag players and return without being tackled. The game emphasizes strength, agility, and strategy, gaining popularity through leagues like the Pro Kabaddi League, which has brought the sport to a wider audience. Kabaddi is not only a test of physical prowess but also mental acuity, as players must strategize their moves while holding their breath. The sport has cultural significance in many regions of India and is celebrated for its vibrant atmosphere during matches',
            'imsrc':'IMAGES/kabbadi.png'
        }
    elif(data=='volleyball'):
        htmldata={
            'name':"Volley Ball",
            'information':'A team sport played on a rectangular court divided by a net, volleyball features two teams of six players. The objective is to score points by hitting the ball over the net and into the opponents court. It can be played indoors or on beaches, with major events like the Olympics and FIVB World Championships showcasing its global appeal and athleticism. Volleyball promotes teamwork and communication, as players must work together to set up plays and defend against opponents. The sport has a strong following in countries like Brazil, the USA, and Italy, with professional leagues and clubs contributing to its growth',
            'imsrc':'IMAGES/volleyball.png'
        }
    elif(data=='football'):
        htmldata={
            'name':"Foot Ball",
            'information':'Known as soccer in some regions, football is the worlds most popular sport, played between two teams of 11 players. The objective is to score goals by getting the ball into the opponents net. Major tournaments include the FIFA World Cup, UEFA Champions League, and continental championships, drawing millions of fans worldwide and fostering a rich culture of club and national pride. Football legends like Pelé, Diego Maradona, and Lionel Messi have become global icons, inspiring generations. The sport promotes inclusivity and community, with grassroots programs encouraging participation at all levels.',
            'imsrc':'IMAGES/football.png'
        }
    elif(data=='hockey'):
        htmldata={
            'name':"Hockey",
            'information':'A fast-paced team sport played on ice or field, hockey involves two teams aiming to score goals by hitting a puck (ice) or ball (field) into the opponents net. Field hockey is especially popular in countries like India, Pakistan, and the Netherlands, while ice hockey has a strong following in North America and Europe, with leagues like the NHL showcasing top talent and thrilling gameplay. Hockey emphasizes speed, skill, and teamwork, with players often displaying incredible athleticism. The sport has a passionate fan base, and major tournaments like the Hockey World Cup and the Stanley Cup Finals attract significant viewership and support',
            'imsrc':'IMAGES/hockey.png'
        }    
    htmldata['category']='Sports '                     
    return render(request,'news.html',htmldata)    

