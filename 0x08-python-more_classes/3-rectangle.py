class Rectangle:
    """
    Defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle
        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value (int): width of the rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle
        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args:
            value (int): height of the rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
