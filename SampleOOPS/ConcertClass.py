class Concert:
    def __init__(self, band, venue, artist,venueCapacity, ticketCategory):
        self.band=band
        self.venue=venue
        self.artist=artist
        self.venueCapacity=venueCapacity
        self.ticketCategory=ticketCategory

    def __repr__(self):
        return f"Band: {self.band}, Venue: {self.venue}, Artist: {self.artist}, Venue Capacity: {self.venueCapacity}, Ticket Category: {self.ticketCategory}"
    

concert1=Concert("Band1", "Venue1", ["Artist1", "Artist2","Artist3"], 24000, {"Silver":1000, "Gold":5000, "Platinum":10000})
print(concert1)