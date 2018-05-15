import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights")
    for flight in flights:
        print(
            f"{flight.origin} to {flight.destination} takes {flight.duration} minutes")


def insert():
    f = open("fights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUE (:origin, :destination, :duration)",
                   {"origin": origin, "destination": destination, "duration": duration})
        print(
            f"Added flight from {origin} to {destination} lasting {duration} minutes.")
        db.commit()

if __name__ == "__main__":
    main()
    insert()
