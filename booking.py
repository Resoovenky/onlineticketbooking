import mysql.connector
import random
import string
def generate_pnr():
  pnr = ""
  for i in range(6):
    pnr += random.choice(string.ascii_uppercase)
  return pnr
def book_ticket(name, source, destination, date):
  # Connect to the database
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ticket_booking"
  )
  # Create a cursor
  cursor = connection.cursor()
  # Generate a PNR
  pnr = generate_pnr()
  # Insert the booking details into the database
  cursor.execute("INSERT INTO bookings (pnr, name, source, destination, date) VALUES (%s, %s, %s, %s, %s)", (pnr, name, source, destination, date))
  # Commit the changes
  connection.commit()
  # Close the cursor and connection
  cursor.close()
  connection.close()
  # Return the PNR
  return pnr
def main():
  # Get the user input
  name = input("Enter your name: ")
  source = input("Enter the source station: ")
  destination = input("Enter the destination station: ")
  date = input("Enter the date of travel: ")
  # Book the ticket
  pnr = book_ticket(name, source, destination, date)
  # Print the PNR
  print("Your PNR is:", pnr)
if __name__ == "__main__":
  main()