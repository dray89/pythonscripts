# -*- coding: utf-8 -*-
"""
This is a program to calculate attributes belonging to insurance plans.
"""

class InsurancePlans:
    """
    This is a class for insurance plans.
    Attributes:
        list price (float): The price at which the service is offered.
        intercept (float): The intercept of the demand function.
    """
    def __init__(self, list_price, intercept=100.00, uninsured_perc = 1.00):
        self.list_price = list_price
        self.intercept = intercept
        self.uninsured_perc = self.uninsured_perc
        self.uninsured_price = self.uninsured_perc*self.list_price
        self.uninsured_qty = self.intercept - self.uninsured_price

    def benefit(self):
        pass

    def premium(self):
        pass

class Full(InsurancePlans):
    """
    This is a class for full insurance plans.
    """

    def __init__(self, list_price, uninsured_qty, uninsured_price, intercept=100):
        InsurancePlans.__init__(self, list_price, uninsured_qty, self.uninsured_price, intercept)

    def quantity(self):
        """
        This method calculates the quantity demanded of full insurance plans
        """
        return self.intercept - self.self_pay*self.list_price

    def social_loss(self):
        """
        This method calculates the social loss from the uninsured state.
        """
        return .5*self.list_price**2*(self.uninsured_price - self.self_pay)**2

    def unfair_premium(self):
        pass

    def fair_premium(self):
        pass

class Coinsure(InsurancePlans):
    """
    This is a class for coinsurance plans.
    """
    def __init__(self, list_price, uninsured_qty, uninsured_price, intercept=100, perc_cover=.5):
        InsurancePlans.__init__(self, list_price, uninsured_qty, uninsured_price, intercept)
        self.perc_cover = perc_cover

    def quantity(self):
        """
        This method calculates the quantity demanded of coinsurance insurance policies.
        """
        return self.intercept - self.self_pay*self.list_price

    def social_loss(self):
        """
        This method calculates the social loss from the uninsured state.
        """
        return .5*(self.list_price*(1-self.self_pay))**2
    
    def unfair_premium(InsurancePlans):
        pass
    
    def fair_premium(InsurancePlans):
        pass
    
class Copay(InsurancePlans):
    """
    This is a class for copay plans.
    """
    def __init__(self, list_price, uninsured_qty, uninsured_price, intercept=100, copay=25):
        InsurancePlans.__init__(self, list_price, uninsured_qty, uninsured_price, intercept)
        self.copay = copay

    def quantity(self):
        """
        This method calculates the quantity demanded of copay insurance policies.
        """
        return self.intercept - self.copay

    def social_loss(self):
        """
        This method calculates the social loss from the uninsured state.
        """
        return .5*(self.list_price-self.copay)**2

    def unfair_premium(InsurancePlans):
        pass
    
    def fair_premium(InsurancePlans):
        pass