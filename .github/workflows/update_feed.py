from feedgen.feed import FeedGenerator
from datetime import datetime
import random

# Updated trivia dataset with images
trivia_pool = [
    {
        "title": "Birthday: Robin Williams",
        "description": "Born July 21, 1951 — beloved comedian and actor known for 'Mrs. Doubtfire' and 'Good Will Hunting'.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Robin_Williams_2011a_%28cropped%29.jpg/440px-Robin_Williams_2011a_%28cropped%29.jpg"
    },
    {
        "title": "Who holds the most Olympic gold medals?",
        "description": "Michael Phelps holds the record with 23 Olympic gold medals.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Michael_Phelps_Rio_2016c.jpg/440px-Michael_Phelps_Rio_2016c.jpg"
    },
    {
        "title": "What year did the Berlin Wall fall?",
        "description": "The Berlin Wall fell in 1989, symbolizing the end of the Cold War.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Berlin_Wall_1989.jpg/440px-Berlin_Wall_1989.jpg"
    },
    {
        "title": "Birthday: Alex Trebek",
        "description": "Born July 22, 1940 — Legendary 'Jeopardy!' host who became a pop culture icon.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Alex_Trebek_2010.jpg/440px-Alex_Trebek_2010.jpg"
    },
    {
        "title": "Who won the first Super Bowl?",
        "description": "The Green Bay Packers won the first Super Bowl in 1967, defeating the Kansas City Chiefs.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Super_Bowl_I_Ticket.jpg/440px-Super_Bowl_I_Ticket.jpg"
    },
    {
        "title": "Birthday: Serena Williams",
        "description": "Born September 26, 1981 — one of the greatest tennis players of all time.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Serena_Williams_2013_US_Open.jpg/440px-Serena_Williams_2013_US_Open.jpg"
    },
    {
        "title": "Who was the youngest U.S. president?",
        "description": "Theodore Roosevelt became president at age 42 after the assassination of William McKinley.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Theodore_Roosevelt_circa_1904.jpg/440px-Theodore_Roosevelt_circa_1904.jpg"
    },
    {
        "title": "Birthday: Kobe Bryant",
        "description": "Born August 23, 1978 — legendary NBA player and five-time champion with the Lakers.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kobe_Bryant_2014.jpg/440px-Kobe_Bryant_2014.jpg"
    },
    {
        "title": "What historic event happened on July 20, 1969?",
        "description": "Neil Armstrong became the first human to walk on the moon.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Aldrin_Apollo_11.jpg/440px-Aldrin_Apollo_11.jpg"
    },
    {
        "title": "Who scored the 'Hand of God' goal?",
        "description": "Diego Maradona scored the infamous 'Hand of God' goal in the 1986 FIFA World Cup.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Maradona_goal_of_the_century_2.jpg/440px-Maradona_goal_of_the_century_2.jpg"
    }
]

# Generate RSS feed
fg = FeedGenerator()
fg.title("TPTN Daily Trivia Feed")
fg.link(href="https://cjburke42.github.io/TPTN-trivia-feed/")
fg.description("2 new trivia questions or facts daily — history, sports, and birthdays.")
fg.language("en")

today = datetime.now().strftime('%a, %d %b %Y 05:00:00 -0400')
entries = random.sample(trivia_pool, 2)

for entry in entries:
    fe = fg.add_entry()
    fe.title(entry["title"])
    fe.description(f'<p>{entry["description"]}</p><img src="{entry["image"]}" width="400"/>')
    fe.pubDate(today)

fg.rss_file("feed.xml")
