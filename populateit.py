from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Items for Soccer
category1 = Category(title="Soccer")

session.add(category1)
session.commit()

Item1 = MenuItem(title="Soccer cleats", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category1)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Shinguards", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category1)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Soccer Jersey", description="Just do it and win.",
                 course="Entree", category=category1)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Goalkeeper gloves", description="Don't let them score a single goal!",
                 category=category1)

session.add(Item4)
session.commit()

# Items for Baseball

category2 = Category(title="Baseball")

session.add(category2)
session.commit()

Item1 = MenuItem(title="Baseball cleats", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category2)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Shinguards", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category2)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Baseball Jersey", description="Just do it and win.",
                 category=category2)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Baseball glove", description="Don't let them score and catch that ball!",
                 category=category2)

session.add(Item4)
session.commit()

# Items for Basketball

category3 = Category(title="Basketball")

session.add(category3)
session.commit()

Item1 = MenuItem(title="Basketball shoes", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category3)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Basketball", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category3)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Basketball Jersey", description="Just do it and win.",
                 category=category3)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Basketball socks", description="Don't let them score! Fly high!",
                 category=category3)

session.add(Item4)
session.commit()

# Itmes for Cycling

category4 = Category(title="Cycling")

session.add(category4)
session.commit()

Item1 = MenuItem(title="Cycling shoes", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Ride Explosive.",
                 category=category4)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Cycling shorts", description="Always Be Prepared For The Season With our Cycling shorts.",
                 category=category4)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Cycling Jersey", description="Just do it and win.",
                 category=category4)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Cycling gloves", description="Don't let them win, be a winner!",
                 category=category4)

session.add(Item4)
session.commit()

# Items for Hockey

category5 = Category(title="Hockey")

session.add(category5)
session.commit()

Item1 = MenuItem(title="Hockey skates", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category5)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Hockey Shinguards", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category5)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Hockey Jersey", description="Just do it and win.",
                 category=category5)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Hockey gloves", description="Don't let them score and catch that thing!",
                 category=category5)

session.add(Item4)
session.commit()

# Items for Boxing

category6 = Category(title="Boxing")

session.add(category6)
session.commit()

Item1 = MenuItem(title="Boxing gloves", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Hit Explosive.",
                 category=category6)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Cup protector", description="Always Be Prepared For The biggest fight of your life with our Sporting Goods.",
                 category=category6)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Boxing shorts", description="Just do it and win.",
                 category=category6)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Boxing rope", description="Walk into the ring like a winner!",
                 category=category6)

session.add(Item4)
session.commit()

# Items for Running

category7 = Category(title="Running")

session.add(category7)
session.commit()

Item1 = MenuItem(title="Running shoes", description="Unleash The Speed In The Exclusive Initiator Pack. Run Fast. Run Explosive.",
                 category=category7)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Running shorts", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category7)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Running shirt", description="Just do it and win.",
                 category=category7)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Running socks", description="Don't stop running!",
                 category=category7)

session.add(Item4)
session.commit()

# Items for Swimming

category8 = Category(title="Swimming")

session.add(category8)
session.commit()

Item1 = MenuItem(title="Swimming shorts", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Swim Explosive.",
                 category=category8)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Swimming cap", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category8)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Swimming goggles", description="Just do it and swim.",
                 category=category8)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Swimming rope", description="Swim to win!",
                 category=category8)

session.add(Item4)
session.commit()

# Items for Rock Climbing

category9 = Category(title="Rock Climbing")

session.add(category9)
session.commit()

Item1 = MenuItem(title="Climbing cleats", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Climb Explosive.",
                 category=category9)

session.add(Item1)
session.commit()


Item2 = MenuItem(title="Climbing chalk", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category9)

session.add(Item2)
session.commit()

Item3 = MenuItem(title="Climbing Jersey", description="Just do it and Climb to the top.",
                 category=category9)

session.add(Item3)
session.commit()

Item4 = MenuItem(title="Climbing rope", description="Don't let go, use the best ropes!",
                 category=category9)

session.add(Item4)
session.commit()

print "Items added!"

