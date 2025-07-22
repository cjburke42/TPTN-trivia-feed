from feedgen.feed import FeedGenerator
from datetime import datetime
import random

# Sample trivia data (you can expand this later)
trivia_pool = [
    ("Who invented the telephone?", "Alexander Graham Bell invented it in 1876."),
    ("Birthday: Serena Williams", "Born September 26, 1981 — one of the greatest tennis players ever."),
    ("What year did the Berlin Wall fall?", "1989 — marking the symbolic end of the Cold War."),
    ("Who holds the record for most Olympic gold medals?", "Michael Phelps with 23 gold medals."),
    ("Birthday: Robin Williams", "Born July 21, 1951 — beloved comedian and actor."),
    ("Who won the 1999 FIFA Women’s World Cup?", "The USA, in a dramatic penalty shootout."),
]

# Generate the feed
fg = FeedGenerator()
fg.title("TPTN Daily Trivia Feed")
fg.link(href="https://cjburke42.github.io/TPTN-trivia-feed/")
fg.description("2 new trivia questions or facts daily — history, sports, and birthdays.")
fg.language("en")

# Pick 2 random trivia items
today = datetime.now().strftime('%a, %d %b %Y 05:00:00 -0400')
entries = random.sample(trivia_pool, 2)

for title, description in entries:
    fe = fg.add_entry()
    fe.title(title)
    fe.description(description)
    fe.pubDate(today)

# Output the XML
fg.rss_file("feed.xml")
