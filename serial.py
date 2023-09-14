class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize the SerialGenerator with a start number."""
        self.start = start
        self.next_serial = start

    def generate(self):
        """Return the next sequential serial number."""
        serial_number = self.next_serial
        self.next_serial += 1
        return serial_number

    def reset(self):
        """Reset the serial number back to the original start number."""
        self.next_serial = self.start

    def __repr__(self):
        """Return a string representation of the SerialGenerator instance."""
        return f"<SerialGenerator start={self.start} next={self.next_serial}>"
