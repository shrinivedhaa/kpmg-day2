class Concert:
    def __init__(self, band, artists, venue, venue_capacity, ticket_types):
        self.band = band 
        self.artists = artists  
        self.venue = venue  
        self.venue_capacity = venue_capacity  
        self.ticket_types = ticket_types  

    def display_concert_info(self):
        """Displays the details of the concert."""
        info = f"Concert Details:\n" \
               f"Band: {self.band}\n" \
               f"Artists: {', '.join(self.artists)}\n" \
               f"Venue: {self.venue}\n" \
               f"Capacity: {self.venue_capacity}\n" \
               f"Tickets:\n"
        for ticket_type, price in self.ticket_types.items():
            info += f"  - {ticket_type}: ${price}\n"
        return info

    def update_ticket_price(self, ticket_type, new_price):
        """Updates the price of a specific ticket type."""
        if ticket_type in self.ticket_types:
            self.ticket_types[ticket_type] = new_price
            return f"Price updated for {ticket_type}: ${new_price}"
        else:
            return f"Ticket type '{ticket_type}' not found."

    def add_artist(self, artist_name):
        """Adds a new artist to the concert lineup."""
        if artist_name not in self.artists:
            self.artists.append(artist_name)
            return f"Artist {artist_name} added to the lineup."
        else:
            return f"Artist {artist_name} is already in the lineup."

    def is_sold_out(self, tickets_sold):
        """Checks if the concert is sold out based on tickets sold."""
        return tickets_sold >= self.venue_capacity


concert = Concert(
    band="Coldplay",
    artists=["Chris Martin", "Jonny Buckland"],
    venue="Madison Square Garden",
    venue_capacity=20000,
    ticket_types={"VIP": 500, "General": 100, "Balcony": 250}
)


print(concert.display_concert_info())


print(concert.update_ticket_price("VIP", 600))


print(concert.add_artist("Will Champion"))


print(concert.is_sold_out(20000)) 


