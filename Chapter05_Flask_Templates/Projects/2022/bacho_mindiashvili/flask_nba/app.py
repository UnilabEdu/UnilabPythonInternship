from flask import Flask, render_template, url_for

app = Flask(__name__)

teams = [
    {
        "id": '1',
        "name": 'lakers',
        "logoUrl": 'https://westsidetoday-enki-v2.s3.amazonaws.com/wp-content/uploads/2014/10/lakers-logo.jpg',
        "description": "The Los Angeles Lakers are an American professional basketball team based in Los Angeles. The Lakers compete in the National Basketball Association (NBA) as a member of the league's Western Conference Pacific Division. The Lakers play their home games at Crypto.com Arena, an arena shared with the NBA's Los Angeles Clippers, the Los Angeles Sparks of the Women's National Basketball Association, and the Los Angeles Kings of the National Hockey League.",
        "wiki": "https://en.wikipedia.org/wiki/Los_Angeles_Lakers"
    },
    {
        "id": '2',
        "name": 'golden',
        "logoUrl": 'https://images.squarespace-cdn.com/content/v1/560b7296e4b03420b41c2110/1594077232294-JXRL4HIO0YXOXCAWWTI7/Blog-800x500_golden.png',
        "description": """The Golden State Warriors are an American professional basketball team based in San Francisco. The Warriors compete in the National Basketball
                                        Association (NBA), as a member of the league's Western Conference Pacific Division. Founded in 1946 in Philadelphia, the Warriors moved to the
                                        San Francisco Bay Area in 1962 and took the city's name, before changing its
                                         geographic moniker to Golden State in 1971.The club plays its home games at the Chase Center
                                         .""",
        "wiki": "https://en.wikipedia.org/wiki/Golden_State_Warriors"
    },
    {
        "id": '3',
        "name": 'boston',
        "logoUrl": 'https://c4.wallpaperflare.com/wallpaper/674/559/755/basketball-boston-celtics-logo-nba-hd-wallpaper-preview.jpg ',
        "description": 'The Boston Celtics  are an American professional basketball team based in Boston. The Celtics compete in the National Basketball Association (NBA) as a member of the leagues Eastern Conference Atlantic Division. Founded in 1946 as one of the leagues original eight teams, the Celtics play their home games at TD Garden,which they share with the National Hockey Leagues Boston Bruins. The Celtics are one of the most successful basketball teams in NBA history.',
        "wiki": "https://en.wikipedia.org/wiki/Boston_Celtics"
    },
    {
        "id": '4',
        "name": 'bucks',
        "logoUrl": 'https://newscdn2.weigelbroadcasting.com/DCnXk-1650515406-224314-blog-Bucks-Logo_Web.jpg',
        "description": "The Milwaukee Bucks are an American professional basketball team based in Milwaukee. The Bucks compete in the National Basketball Association (NBA) as a member of the league's Eastern Conference Central Division. The team was founded in 1968 as an expansion team, and play at Fiserv Forum. Former U.S. Senator Herb Kohl was the long-time owner of the team, but on April 16, 2014, a group led by billionaire hedge fund managers Wes Edens and Marc Lasry agreed to purchase a majority interest in the team from Kohl.",
        "wiki": "https://en.wikipedia.org/wiki/Milwaukee_Bucks"
    }
]


players = [
    {
        "id": "1",
        "name": "lebron",
        "team_id": "1",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png',
        "site": "https://www.nba.com/player/2544/lebron-james",
        "date": "1984 (37 age)",
        "point": "37,062",
        "ring": "4",
        "logoUrl": 'https://pbs.twimg.com/profile_images/1467008403717324801/vDVwcwkM_400x400.jpg',

    },
    {
        "id": "2",
        "name": "davis",
        "team_id": "1",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/203076.png',
        "site": "https://www.nba.com/player/203076/anthony-davis",
        "date": "1993 (29 age)",
        "point": "14390",
        "ring": "1",
        "logoUrl": 'https://pbs.twimg.com/profile_images/1467008403717324801/vDVwcwkM_400x400.jpg',

    },
    {
        "id": "3",
        "name": "Stephen Carry",
        "team_id": "2",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/201939.png',
        "site": "https://www.nba.com/player/201939/stephen-curry",
        "date": "1988 (34 age)",
        "point": "20064	",
        "ring": "4",
        "logoUrl": 'https://images.squarespace-cdn.com/content/v1/560b7296e4b03420b41c2110/1594077232294-JXRL4HIO0YXOXCAWWTI7/Blog-800x500_golden.png'

    },
    {
        "id": "4",
        "name": "Klay Thompson",
        "team_id": "2",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/202691.png',
        "site": "https://www.nba.com/player/202691/klay-thompson",
        "date": "1990 (32 age)",
        "point": "12647",
        "ring": "4",
        "logoUrl": 'https://images.squarespace-cdn.com/content/v1/560b7296e4b03420b41c2110/1594077232294-JXRL4HIO0YXOXCAWWTI7/Blog-800x500_golden.png'

    },
    {
        "id": "5",
        "name": " Jayson Tatum",
        "team_id": "3",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/1628369.png',
        "site": "https://www.nba.com/player/1628369/jayson-tatum",
        "date": "1998 (24 age)",
        "point": "7640",
        "ring": "0",
        "logoUrl": 'https://c4.wallpaperflare.com/wallpaper/674/559/755/basketball-boston-celtics-logo-nba-hd-wallpaper-preview.jpg'

    }, {
        "id": "6",
        "name": "Jaylen Brown",
        "team_id": "3",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/1627759.png',
        "site": "https://www.nba.com/player/1627759/jaylen-brown",
        "date": "1996 (25age)",
        "point": "6644",
        "ring": "0",
        "logoUrl": 'https://c4.wallpaperflare.com/wallpaper/674/559/755/basketball-boston-celtics-logo-nba-hd-wallpaper-preview.jpg '

    },

{
        "id": "7",
        "name": "Giannis Antetokounmpo",
        "team_id": "4",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/203507.png',
        "site": "https://www.nba.com/player/203507/giannis-antetokounmpo",
        "date": "1994 (27age)",
        "point": "14321",
        "ring": "1",
        "logoUrl": 'https://newscdn2.weigelbroadcasting.com/DCnXk-1650515406-224314-blog-Bucks-Logo_Web.jpg'

},
{
        "id": "8",
        "name": "Sandro Mamukelashvili",
        "team_id": "4",
        "p_url": 'https://cdn.nba.com/headshots/nba/latest/1040x760/1630572.png',
        "site": "https://www.nba.com/player/1630572/sandro-mamukelashvili",
        "date": "1999 (23age)",
        "point": "154",
        "ring": "0",
        "logoUrl": 'https://newscdn2.weigelbroadcasting.com/DCnXk-1650515406-224314-blog-Bucks-Logo_Web.jpg'

}


];

@app.route('/')
def home():  # put application's code here
    return render_template("team.html", teams = teams)

@app.route('/team/<id>')
def team(id):
    team = {}
    pla1 = []
    for current_team in teams:
        if current_team['id'] == id:
            team = current_team

            pla1 = [p for p in players if p['team_id'] == id]

    return render_template("players.html", team=team, players=pla1)

@app.route('/player/<id>')
def nba_player(id):
    n_player = {}
    for play in players:
        if play['id'] == id:
            n_player = play

    return render_template("home.html", player = n_player)


@app.route('/contact')
def form():  # put application's code here
    return render_template("form.html")



if __name__ == '__main__':
    app.run(port = 8081)
