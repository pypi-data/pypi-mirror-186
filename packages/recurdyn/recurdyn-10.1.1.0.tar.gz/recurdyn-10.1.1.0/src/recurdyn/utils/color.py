from enum import IntEnum

_COLOR_TABLE_RGR = {
    'ALICEBLUE' : 0xF0F8FF
    ,'ANTIQUEWHITE' : 0xFAEBD7
    ,'AQUA' : 0x00FFFF
    ,'AQUAMARINE' : 0x7FFFD4
    ,'AZURE' : 0xF0FFFF
    ,'BEIGE' : 0xF5F5DC
    ,'BISQUE' : 0xFFE4C4
    ,'BLACK' : 0x000000
    ,'BLANCHEDALMOND' : 0xFFEBCD
    ,'BLUE' : 0x0000FF
    ,'BLUEVIOLET' : 0x8A2BE2
    ,'BROWN' : 0xA52A2A
    ,'BURLYWOOD' : 0xDEB887
    ,'CADETBLUE' : 0x5F9EA0
    ,'CHARTREUSE' : 0x7FFF00
    ,'CHOCOLATE' : 0xD2691E
    ,'CORAL' : 0xFF7F50
    ,'CORNFLOWERBLUE' : 0x6495ED
    ,'CORNSILK' : 0xFFF8DC
    ,'CRIMSON' : 0xDC143C
    ,'CYAN' : 0x00FFFF
    ,'DARKBLUE' : 0x00008B
    ,'DARKCYAN' : 0x008B8B
    ,'DARKGOLDENROD' : 0xB8860B
    ,'DARKGRAY' : 0xA9A9A9
    ,'DARKGREEN' : 0x006400
    ,'DARKKHAKI' : 0xBDB76B
    ,'DARKMAGENTA' : 0x8B008B
    ,'DARKOLIVEGREEN' : 0x556B2F
    ,'DARKORANGE' : 0xFF8C00
    ,'DARKORCHID' : 0x9932CC
    ,'DARKRED' : 0x8B0000
    ,'DARKSALMON' : 0xE9967A
    ,'DARKSEAGREEN' : 0x8FBC8B
    ,'DARKSLATEBLUE' : 0x483D8B
    ,'DARKSLATEGRAY' : 0x2F4F4F
    ,'DARKTURQUOISE' : 0x00CED1
    ,'DARKVIOLET' : 0x9400D3
    ,'DEEPPINK' : 0xFF1493
    ,'DEEPSKYBLUE' : 0x00BFFF
    ,'DIMGRAY' : 0x696969
    ,'DODGERBLUE' : 0x1E90FF
    ,'FIREBRICK' : 0xB22222
    ,'FLORALWHITE' : 0xFFFAF0
    ,'FORESTGREEN' : 0x228B22
    ,'FUCHSIA' : 0xFF00FF
    ,'GAINSBORO' : 0xDCDCDC
    ,'GHOSTWHITE' : 0xF8F8FF
    ,'GOLD' : 0xFFD700
    ,'GOLDENROD' : 0xDAA520
    ,'GRAY' : 0x808080
    ,'GREEN' : 0x008000
    ,'GREENYELLOW' : 0xADFF2F
    ,'HONEYDEW' : 0xF0FFF0
    ,'HOTPINK' : 0xFF69B4
    ,'INDIANRED' : 0xCD5C5C
    ,'INDIGO' : 0x4B0082
    ,'IVORY' : 0xFFFFF0
    ,'KHAKI' : 0xF0E68C
    ,'LAVENDER' : 0xE6E6FA
    ,'LAVENDERBLUSH' : 0xFFF0F5
    ,'LAWNGREEN' : 0x7CFC00
    ,'LEMONCHIFFON' : 0xFFFACD
    ,'LIGHTBLUE' : 0xADD8E6
    ,'LIGHTCORAL' : 0xF08080
    ,'LIGHTCYAN' : 0xE0FFFF
    ,'LIGHTGOLDENRODYELLOW' : 0xFAFAD2
    ,'LIGHTGRAY' : 0xD3D3D3
    ,'LIGHTGREEN' : 0x90EE90
    ,'LIGHTPINK' : 0xFFB6C1
    ,'LIGHTSALMON' : 0xFFA07A
    ,'LIGHTSEAGREEN' : 0x20B2AA
    ,'LIGHTSKYBLUE' : 0x87CEFA
    ,'LIGHTSLATEGRAY' : 0x778899
    ,'LIGHTSTEELBLUE' : 0xB0C4DE
    ,'LIGHTYELLOW' : 0xFFFFE0
    ,'LIME' : 0x00FF00
    ,'LIMEGREEN' : 0x32CD32
    ,'LINEN' : 0xFAF0E6
    ,'MAGENTA' : 0xFF00FF
    ,'MAROON' : 0x800000
    ,'MEDIUMAQUAMARINE' : 0x66CDAA
    ,'MEDIUMBLUE' : 0x0000CD
    ,'MEDIUMORCHID' : 0xBA55D3
    ,'MEDIUMPURPLE' : 0x9370DB
    ,'MEDIUMSEAGREEN' : 0x3CB371
    ,'MEDIUMSLATEBLUE' : 0x7B68EE
    ,'MEDIUMSPRINGGREEN' : 0x00FA9A
    ,'MEDIUMTURQUOISE' : 0x48D1CC
    ,'MEDIUMVIOLETRED' : 0xC71585
    ,'MIDNIGHTBLUE' : 0x191970
    ,'MINTCREAM' : 0xF5FFFA
    ,'MISTYROSE' : 0xFFE4E1
    ,'MOCCASIN' : 0xFFE4B5
    ,'NAVAJOWHITE' : 0xFFDEAD
    ,'NAVY' : 0x000080
    ,'OLDLACE' : 0xFDF5E6
    ,'OLIVE' : 0x808000
    ,'OLIVEDRAB' : 0x6B8E23
    ,'ORANGE' : 0xFFA500
    ,'ORANGERED' : 0xFF4500
    ,'ORCHID' : 0xDA70D6
    ,'PALEGOLDENROD' : 0xEEE8AA
    ,'PALEGREEN' : 0x98FB98
    ,'PALETURQUOISE' : 0xAFEEEE
    ,'PALEVIOLETRED' : 0xDB7093
    ,'PAPAYAWHIP' : 0xFFEFD5
    ,'PEACHPUFF' : 0xFFDAB9
    ,'PERU' : 0xCD853F
    ,'PINK' : 0xFFC0CB
    ,'PLUM' : 0xDDA0DD
    ,'POWDERBLUE' : 0xB0E0E6
    ,'PURPLE' : 0x800080
    ,'RED' : 0xFF0000
    ,'ROSYBROWN' : 0xBC8F8F
    ,'ROYALBLUE' : 0x4169E1
    ,'SADDLEBROWN' : 0x8B4513
    ,'SALMON' : 0xFA8072
    ,'SANDYBROWN' : 0xF4A460
    ,'SEAGREEN' : 0x2E8B57
    ,'SEASHELL' : 0xFFF5EE
    ,'SIENNA' : 0xA0522D
    ,'SILVER' : 0xC0C0C0
    ,'SKYBLUE' : 0x87CEEB
    ,'SLATEBLUE' : 0x6A5ACD
    ,'SLATEGRAY' : 0x708090
    ,'SNOW' : 0xFFFAFA
    ,'SPRINGGREEN' : 0x00FF7F
    ,'STEELBLUE' : 0x4682B4
    ,'TAN' : 0xD2B48C
    ,'TEAL' : 0x008080
    ,'THISTLE' : 0xD8BFD8
    ,'TOMATO' : 0xFF6347
    ,'TURQUOISE' : 0x40E0D0
    ,'VIOLET' : 0xEE82EE
    ,'WHEAT' : 0xF5DEB3
    ,'WHITE' : 0xFFFFFF
    ,'WHITESMOKE' : 0xF5F5F5
    ,'YELLOW' : 0xFFFF00
    ,'YELLOWGREEN' : 0x9ACD32
}

class Color(IntEnum):
    '''
    The color of each pixel is represented as a 24-bit number: 8 bits each for red, green, and blue (RGB).
    Each of the four components is a number from 0 through 255, with 0 representing no intensity and 255 representing full intensity.
    To determine the red, green, or blue component of a color, use the R, G, or B property, respectively.
    '''
	
    @classmethod
    def rgb(cls, r, g, b):
        '''
        Represents an RGB(red, green, blue) color

        :param r: red component value
        :param g: green component value
        :param b: blue component value
        :type r: int
        :type g: int
        :type b: int
        :return: RGB(red, green, blue) color
        :rtype: int
        '''
        _rgb = [r, g, b]
        for i in range(3):
            if 255 < _rgb[i]:
                _rgb[i] = 255
            elif _rgb[i] < 0:
                _rgb[i] = 0
            _rgb[i] = hex(_rgb[i])[2:].zfill(2)

        hex_value_string = '{}{}{}'.format(_rgb[0], _rgb[1], _rgb[2])
        return int(hex_value_string, 16)

    @classmethod
    def _change_color_bits_position(cls, val):
        if 0xffffff < val:
            val = 0xffffff
        elif val < 0:
            val = 0
        hex_value = str(hex(val)[2:].zfill(6))
        r = hex_value[:2]
        g = hex_value[2:4]
        b = hex_value[4:]
        hex_value = '{}{}{}'.format(b, g, r)
        return int(hex_value, 16)

    @classmethod
    def sawp_rb(cls, val):
        '''
        Convert red to blue or blue to red

        :param val: BGR or RGB color
        :type val: int
        :return: RGB or BGR color
        :rtype: int
        '''
        return cls._change_color_bits_position(val)

    @classmethod
    def rgb_to_bgr(cls, val):
        '''
        Convert RGB value to BGR value

        :param val: RGB(red, green, blue) color
        :type val: int
        :return: BGR(blue, green, red) color
        :rtype: int
        '''
        return cls._change_color_bits_position(val)

    @classmethod
    def bgr_to_rgb(cls, val):
        '''
        Convert BGR value to RGB value

        :param val: BGR(blue, green, red) color
        :type val: int
        :return: RGB(red, green, blue) color
        :rtype: int
        '''
        return cls._change_color_bits_position(val)

    @classmethod
    def from_name(cls, name):
        '''
        Get a Color from the specified name of a predefined color.

        :rtype: int
        '''
        if type(name) == type(''):
            return _COLOR_TABLE_RGR.get(name.upper())
        else:
            return None

    AliceBlue = 0xF0F8FF
    '''Gets a system-defined color that has an RGB value of 0xF0F8FF'''
    AntiqueWhite = 0xFAEBD7
    '''Gets a system-defined color that has an RGB value of 0xFAEBD7'''
    Aqua = 0x00FFFF
    '''Gets a system-defined color that has an RGB value of 0x00FFFF'''
    Aquamarine = 0x7FFFD4
    '''Gets a system-defined color that has an RGB value of 0x7FFFD4'''
    Azure = 0xF0FFFF
    '''Gets a system-defined color that has an RGB value of 0xF0FFFF'''
    Beige = 0xF5F5DC
    '''Gets a system-defined color that has an RGB value of 0xF5F5DC'''
    Bisque = 0xFFE4C4
    '''Gets a system-defined color that has an RGB value of 0xFFE4C4'''
    Black = 0x000000
    '''Gets a system-defined color that has an RGB value of 0x000000'''
    BlanchedAlmond = 0xFFEBCD
    '''Gets a system-defined color that has an RGB value of 0xFFEBCD'''
    Blue = 0x0000FF
    '''Gets a system-defined color that has an RGB value of 0x0000FF'''
    BlueViolet = 0x8A2BE2
    '''Gets a system-defined color that has an RGB value of 0x8A2BE2'''
    Brown = 0xA52A2A
    '''Gets a system-defined color that has an RGB value of 0xA52A2A'''
    BurlyWood = 0xDEB887
    '''Gets a system-defined color that has an RGB value of 0xDEB887'''
    CadetBlue = 0x5F9EA0
    '''Gets a system-defined color that has an RGB value of 0x5F9EA0'''
    Chartreuse = 0x7FFF00
    '''Gets a system-defined color that has an RGB value of 0x7FFF00'''
    Chocolate = 0xD2691E
    '''Gets a system-defined color that has an RGB value of 0xD2691E'''
    Coral = 0xFF7F50
    '''Gets a system-defined color that has an RGB value of 0xFF7F50'''
    CornflowerBlue = 0x6495ED
    '''Gets a system-defined color that has an RGB value of 0x6495ED'''
    Cornsilk = 0xFFF8DC
    '''Gets a system-defined color that has an RGB value of 0xFFF8DC'''
    Crimson = 0xDC143C
    '''Gets a system-defined color that has an RGB value of 0xDC143C'''
    Cyan = 0x00FFFF
    '''Gets a system-defined color that has an RGB value of 0x00FFFF'''
    DarkBlue = 0x00008B
    '''Gets a system-defined color that has an RGB value of 0x00008B'''
    DarkCyan = 0x008B8B
    '''Gets a system-defined color that has an RGB value of 0x008B8B'''
    DarkGoldenrod = 0xB8860B
    '''Gets a system-defined color that has an RGB value of 0xB8860B'''
    DarkGray = 0xA9A9A9
    '''Gets a system-defined color that has an RGB value of 0xA9A9A9'''
    DarkGreen = 0x006400
    '''Gets a system-defined color that has an RGB value of 0x006400'''
    DarkKhaki = 0xBDB76B
    '''Gets a system-defined color that has an RGB value of 0xBDB76B'''
    DarkMagenta = 0x8B008B
    '''Gets a system-defined color that has an RGB value of 0x8B008B'''
    DarkOliveGreen = 0x556B2F
    '''Gets a system-defined color that has an RGB value of 0x556B2F'''
    DarkOrange = 0xFF8C00
    '''Gets a system-defined color that has an RGB value of 0xFF8C00'''
    DarkOrchid = 0x9932CC
    '''Gets a system-defined color that has an RGB value of 0x9932CC'''
    DarkRed = 0x8B0000
    '''Gets a system-defined color that has an RGB value of 0x8B0000'''
    DarkSalmon = 0xE9967A
    '''Gets a system-defined color that has an RGB value of 0xE9967A'''
    DarkSeaGreen = 0x8FBC8B
    '''Gets a system-defined color that has an RGB value of 0x8FBC8B'''
    DarkSlateBlue = 0x483D8B
    '''Gets a system-defined color that has an RGB value of 0x483D8B'''
    DarkSlateGray = 0x2F4F4F
    '''Gets a system-defined color that has an RGB value of 0x2F4F4F'''
    DarkTurquoise = 0x00CED1
    '''Gets a system-defined color that has an RGB value of 0x00CED1'''
    DarkViolet = 0x9400D3
    '''Gets a system-defined color that has an RGB value of 0x9400D3'''
    DeepPink = 0xFF1493
    '''Gets a system-defined color that has an RGB value of 0xFF1493'''
    DeepSkyBlue = 0x00BFFF
    '''Gets a system-defined color that has an RGB value of 0x00BFFF'''
    DimGray = 0x696969
    '''Gets a system-defined color that has an RGB value of 0x696969'''
    DodgerBlue = 0x1E90FF
    '''Gets a system-defined color that has an RGB value of 0x1E90FF'''
    Firebrick = 0xB22222
    '''Gets a system-defined color that has an RGB value of 0xB22222'''
    FloralWhite = 0xFFFAF0
    '''Gets a system-defined color that has an RGB value of 0xFFFAF0'''
    ForestGreen = 0x228B22
    '''Gets a system-defined color that has an RGB value of 0x228B22'''
    Fuchsia = 0xFF00FF
    '''Gets a system-defined color that has an RGB value of 0xFF00FF'''
    Gainsboro = 0xDCDCDC
    '''Gets a system-defined color that has an RGB value of 0xDCDCDC'''
    GhostWhite = 0xF8F8FF
    '''Gets a system-defined color that has an RGB value of 0xF8F8FF'''
    Gold = 0xFFD700
    '''Gets a system-defined color that has an RGB value of 0xFFD700'''
    Goldenrod = 0xDAA520
    '''Gets a system-defined color that has an RGB value of 0xDAA520'''
    Gray = 0x808080
    '''Gets a system-defined color that has an RGB value of 0x808080'''
    Green = 0x008000
    '''Gets a system-defined color that has an RGB value of 0x008000'''
    GreenYellow = 0xADFF2F
    '''Gets a system-defined color that has an RGB value of 0xADFF2F'''
    Honeydew = 0xF0FFF0
    '''Gets a system-defined color that has an RGB value of 0xF0FFF0'''
    HotPink = 0xFF69B4
    '''Gets a system-defined color that has an RGB value of 0xFF69B4'''
    IndianRed = 0xCD5C5C
    '''Gets a system-defined color that has an RGB value of 0xCD5C5C'''
    Indigo = 0x4B0082
    '''Gets a system-defined color that has an RGB value of 0x4B0082'''
    Ivory = 0xFFFFF0
    '''Gets a system-defined color that has an RGB value of 0xFFFFF0'''
    Khaki = 0xF0E68C
    '''Gets a system-defined color that has an RGB value of 0xF0E68C'''
    Lavender = 0xE6E6FA
    '''Gets a system-defined color that has an RGB value of 0xE6E6FA'''
    LavenderBlush = 0xFFF0F5
    '''Gets a system-defined color that has an RGB value of 0xFFF0F5'''
    LawnGreen = 0x7CFC00
    '''Gets a system-defined color that has an RGB value of 0x7CFC00'''
    LemonChiffon = 0xFFFACD
    '''Gets a system-defined color that has an RGB value of 0xFFFACD'''
    LightBlue = 0xADD8E6
    '''Gets a system-defined color that has an RGB value of 0xADD8E6'''
    LightCoral = 0xF08080
    '''Gets a system-defined color that has an RGB value of 0xF08080'''
    LightCyan = 0xE0FFFF
    '''Gets a system-defined color that has an RGB value of 0xE0FFFF'''
    LightGoldenrodYellow = 0xFAFAD2
    '''Gets a system-defined color that has an RGB value of 0xFAFAD2'''
    LightGray = 0xD3D3D3
    '''Gets a system-defined color that has an RGB value of 0xD3D3D3'''
    LightGreen = 0x90EE90
    '''Gets a system-defined color that has an RGB value of 0x90EE90'''
    LightPink = 0xFFB6C1
    '''Gets a system-defined color that has an RGB value of 0xFFB6C1'''
    LightSalmon = 0xFFA07A
    '''Gets a system-defined color that has an RGB value of 0xFFA07A'''
    LightSeaGreen = 0x20B2AA
    '''Gets a system-defined color that has an RGB value of 0x20B2AA'''
    LightSkyBlue = 0x87CEFA
    '''Gets a system-defined color that has an RGB value of 0x87CEFA'''
    LightSlateGray = 0x778899
    '''Gets a system-defined color that has an RGB value of 0x778899'''
    LightSteelBlue = 0xB0C4DE
    '''Gets a system-defined color that has an RGB value of 0xB0C4DE'''
    LightYellow = 0xFFFFE0
    '''Gets a system-defined color that has an RGB value of 0xFFFFE0'''
    Lime = 0x00FF00
    '''Gets a system-defined color that has an RGB value of 0x00FF00'''
    LimeGreen = 0x32CD32
    '''Gets a system-defined color that has an RGB value of 0x32CD32'''
    Linen = 0xFAF0E6
    '''Gets a system-defined color that has an RGB value of 0xFAF0E6'''
    Magenta = 0xFF00FF
    '''Gets a system-defined color that has an RGB value of 0xFF00FF'''
    Maroon = 0x800000
    '''Gets a system-defined color that has an RGB value of 0x800000'''
    MediumAquamarine = 0x66CDAA
    '''Gets a system-defined color that has an RGB value of 0x66CDAA'''
    MediumBlue = 0x0000CD
    '''Gets a system-defined color that has an RGB value of 0x0000CD'''
    MediumOrchid = 0xBA55D3
    '''Gets a system-defined color that has an RGB value of 0xBA55D3'''
    MediumPurple = 0x9370DB
    '''Gets a system-defined color that has an RGB value of 0x9370DB'''
    MediumSeaGreen = 0x3CB371
    '''Gets a system-defined color that has an RGB value of 0x3CB371'''
    MediumSlateBlue = 0x7B68EE
    '''Gets a system-defined color that has an RGB value of 0x7B68EE'''
    MediumSpringGreen = 0x00FA9A
    '''Gets a system-defined color that has an RGB value of 0x00FA9A'''
    MediumTurquoise = 0x48D1CC
    '''Gets a system-defined color that has an RGB value of 0x48D1CC'''
    MediumVioletRed = 0xC71585
    '''Gets a system-defined color that has an RGB value of 0xC71585'''
    MidnightBlue = 0x191970
    '''Gets a system-defined color that has an RGB value of 0x191970'''
    MintCream = 0xF5FFFA
    '''Gets a system-defined color that has an RGB value of 0xF5FFFA'''
    MistyRose = 0xFFE4E1
    '''Gets a system-defined color that has an RGB value of 0xFFE4E1'''
    Moccasin = 0xFFE4B5
    '''Gets a system-defined color that has an RGB value of 0xFFE4B5'''
    NavajoWhite = 0xFFDEAD
    '''Gets a system-defined color that has an RGB value of 0xFFDEAD'''
    Navy = 0x000080
    '''Gets a system-defined color that has an RGB value of 0x000080'''
    OldLace = 0xFDF5E6
    '''Gets a system-defined color that has an RGB value of 0xFDF5E6'''
    Olive = 0x808000
    '''Gets a system-defined color that has an RGB value of 0x808000'''
    OliveDrab = 0x6B8E23
    '''Gets a system-defined color that has an RGB value of 0x6B8E23'''
    Orange = 0xFFA500
    '''Gets a system-defined color that has an RGB value of 0xFFA500'''
    OrangeRed = 0xFF4500
    '''Gets a system-defined color that has an RGB value of 0xFF4500'''
    Orchid = 0xDA70D6
    '''Gets a system-defined color that has an RGB value of 0xDA70D6'''
    PaleGoldenrod = 0xEEE8AA
    '''Gets a system-defined color that has an RGB value of 0xEEE8AA'''
    PaleGreen = 0x98FB98
    '''Gets a system-defined color that has an RGB value of 0x98FB98'''
    PaleTurquoise = 0xAFEEEE
    '''Gets a system-defined color that has an RGB value of 0xAFEEEE'''
    PaleVioletRed = 0xDB7093
    '''Gets a system-defined color that has an RGB value of 0xDB7093'''
    PapayaWhip = 0xFFEFD5
    '''Gets a system-defined color that has an RGB value of 0xFFEFD5'''
    PeachPuff = 0xFFDAB9
    '''Gets a system-defined color that has an RGB value of 0xFFDAB9'''
    Peru = 0xCD853F
    '''Gets a system-defined color that has an RGB value of 0xCD853F'''
    Pink = 0xFFC0CB
    '''Gets a system-defined color that has an RGB value of 0xFFC0CB'''
    Plum = 0xDDA0DD
    '''Gets a system-defined color that has an RGB value of 0xDDA0DD'''
    PowderBlue = 0xB0E0E6
    '''Gets a system-defined color that has an RGB value of 0xB0E0E6'''
    Purple = 0x800080
    '''Gets a system-defined color that has an RGB value of 0x800080'''
    Red = 0xFF0000
    '''Gets a system-defined color that has an RGB value of 0xFF0000'''
    RosyBrown = 0xBC8F8F
    '''Gets a system-defined color that has an RGB value of 0xBC8F8F'''
    RoyalBlue = 0x4169E1
    '''Gets a system-defined color that has an RGB value of 0x4169E1'''
    SaddleBrown = 0x8B4513
    '''Gets a system-defined color that has an RGB value of 0x8B4513'''
    Salmon = 0xFA8072
    '''Gets a system-defined color that has an RGB value of 0xFA8072'''
    SandyBrown = 0xF4A460
    '''Gets a system-defined color that has an RGB value of 0xF4A460'''
    SeaGreen = 0x2E8B57
    '''Gets a system-defined color that has an RGB value of 0x2E8B57'''
    SeaShell = 0xFFF5EE
    '''Gets a system-defined color that has an RGB value of 0xFFF5EE'''
    Sienna = 0xA0522D
    '''Gets a system-defined color that has an RGB value of 0xA0522D'''
    Silver = 0xC0C0C0
    '''Gets a system-defined color that has an RGB value of 0xC0C0C0'''
    SkyBlue = 0x87CEEB
    '''Gets a system-defined color that has an RGB value of 0x87CEEB'''
    SlateBlue = 0x6A5ACD
    '''Gets a system-defined color that has an RGB value of 0x6A5ACD'''
    SlateGray = 0x708090
    '''Gets a system-defined color that has an RGB value of 0x708090'''
    Snow = 0xFFFAFA
    '''Gets a system-defined color that has an RGB value of 0xFFFAFA'''
    SpringGreen = 0x00FF7F
    '''Gets a system-defined color that has an RGB value of 0x00FF7F'''
    SteelBlue = 0x4682B4
    '''Gets a system-defined color that has an RGB value of 0x4682B4'''
    Tan = 0xD2B48C
    '''Gets a system-defined color that has an RGB value of 0xD2B48C'''
    Teal = 0x008080
    '''Gets a system-defined color that has an RGB value of 0x008080'''
    Thistle = 0xD8BFD8
    '''Gets a system-defined color that has an RGB value of 0xD8BFD8'''
    Tomato = 0xFF6347
    '''Gets a system-defined color that has an RGB value of 0xFF6347'''
    Turquoise = 0x40E0D0
    '''Gets a system-defined color that has an RGB value of 0x40E0D0'''
    Violet = 0xEE82EE
    '''Gets a system-defined color that has an RGB value of 0xEE82EE'''
    Wheat = 0xF5DEB3
    '''Gets a system-defined color that has an RGB value of 0xF5DEB3'''
    White = 0xFFFFFF
    '''Gets a system-defined color that has an RGB value of 0xFFFFFF'''
    WhiteSmoke = 0xF5F5F5
    '''Gets a system-defined color that has an RGB value of 0xF5F5F5'''
    Yellow = 0xFFFF00
    '''Gets a system-defined color that has an RGB value of 0xFFFF00'''
    YellowGreen = 0x9ACD32
    '''Gets a system-defined color that has an RGB value of 0x9ACD32'''
