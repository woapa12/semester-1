# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated
        if isinstance(pounds, int) and isinstance(pence, int):
            if pounds > 0 and pence > 0 and pence < 0:
                self.pounds: int = pounds
                self.pence: int = pence
            else:
                raise ValueError
        else:
            raise TypeError


    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return(f"{self.pounds}.{self.pence:02d}")

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """


        # Add code here to check that parameter 'other' is a Money object,
        if not isinstance(other, Money):
            raise TypeError
        else:
            pence = self.pence + other.pence
            pounds = self.pounds + other.pounds
            overflow = pence // 100
            if overflow:
                pounds += overflow
                pence -= overflow * 100
            newAmount = Money(pounds, pence)
            return newAmount

        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
