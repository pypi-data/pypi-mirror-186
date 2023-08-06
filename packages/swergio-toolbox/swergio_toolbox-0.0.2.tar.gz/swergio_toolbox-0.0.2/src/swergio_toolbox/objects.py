class MutableObject:
    """
    A class representing a mutable object with a value.

    :param value: The value of the object.
    :type value: Any

    :ivar value: The value of the object.
    :vartype value: Any
    """
    def __init__(self, value=None):
        self.value = value
        
    def __str__(self):
        """
        Return the string representation of the object's value.
        """
        return str(self.value)
   
    def __set__(self, value):
        """
        Set the value of the object.

        :param value: The new value of the object.
        :type value: Any
        """
        self.value = value
    
    def set(self, value):
        """
        Set the value of the object.

        :param value: The new value of the object.
        :type value: Any
        """
        self.value = value
        
    def __eq__(self, other):
        """
        Return True if the value of this object is equal to the value of the other object, False otherwise.

        :param other: The other object to compare with.
        :type other: Any

        :return: True if the values are equal, False otherwise.
        :rtype: bool
        """
        return self.value == other
    
    def __ne__(self, other):
        """
        Return True if the value of this object is not equal to the value of the other object, False otherwise.

        :param other: The other object to compare with.
        :type other: Any

        :return: True if the values are not equal, False otherwise.
        :rtype: bool
        """
        return self.value != other

        
class MutableBool(MutableObject):
    """
    A class representing a mutable boolean value.
    
    :param value: The initial value of the boolean.
    :type value: bool
    """
    def __init__(self, value=False):
        super().__init__(value) 
 

class MutableNumber(MutableObject):
    """
    A class representing a mutable number value.
    
    :param value: The initial value of the number.
    :type value: int or float
    """
    def __init__(self, value=0):
        super().__init__(value)
    
    def __add__(self, other):
        """
        Add the other value to this object's value and return the object.

        :param other: The value to add.
        :type other: int or float

        :return: The object with the updated value.
        :rtype: MutableNumber
        """
        self.value += other
        return self
        
    def __sub__(self, other):
        """
        Subtract the other value from this object's value and return the object.

        :param other: The value to subtract.
        :type other: int or float

        :return: The object with the updated value.
        :rtype: MutableNumber
        """
        self.value -= other
        return self
    
    def __mul__(self,other):
        """
        Multiply this object's value by the other value and return the object.

        :param other: The value to multiply by.
        :type other: int or float

        :return: The object with the updated value.
        :rtype: MutableNumber
        """
        self.value = self.value*other
        return self
    
    def __truediv__(self, other):
        """
        Divide this object's value by the other value and return the object.

        :param other: The value to divide by.
        :type other: int or float

        :return: The object with the updated value.
        :rtype: MutableNumber
        """
        self.value = self.value/other
        return self
    
    def __lt__(self, other):
        """
        Return True if this object's value is less than the other value, False otherwise.

        :param other: The value to compare with.
        :type other: int or float

        :return: True if this object's value is less than the other value, False otherwise.
        :rtype: bool
        """
        return self.value < other
        
    def __gt__(self, other):
        """
        Return True if this object's value is greater than the other value, False otherwise.

        :param other: The value to compare with.
        :type other: int or float

        :return: True if this object's value is greater than the other value, False otherwise.
        :rtype: bool
        """
        return self.value > other
        
    def __ge__(self, other):
        """
        Return True if this object's value is greater than or equal to the other value, False otherwise.

        :param other: The value to compare with.
        :type other: int or float

        :return: True if this object's value is greater than or equal to the other value, False otherwise.
        :rtype: bool
        """
        return self.value >= other
        
    def __le__(self, other):
        """
        Return True if this object's value is less than or equal to the other value, False otherwise.

        :param other: The value to compare with.
        :type other: int or float

        :return: True if this object's value is less than or equal to the other value, False otherwise.
        :rtype: bool
        """
        return self.value <= other
