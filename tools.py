import math
def rgb_to_hex(rgb):
    def digit_to_letter(num):
        translator = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        if num >= 10:
            return translator[num]
        else:
            return str(num)


    red, green, blue = rgb

    red = [digit_to_letter(num) for num in (math.floor(red / 16), red % 16)]
    green = [digit_to_letter(num) for num in (math.floor(green / 16), green % 16)]
    blue = [digit_to_letter(num) for num in (math.floor(blue / 16), blue % 16)]

    return f"#{''.join(red)}{''.join(green)}{''.join(blue)}"