class Printable:
    # Returns a printable representation of the given object
    def __repr__(self):
        return str(self.__dict__)
