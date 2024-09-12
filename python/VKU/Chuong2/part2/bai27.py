class Shaper:
    def __init__(self, sides):
        self.sides = sides
    def identify_Shape(self):
        Shaper ={
            3: "Hình tam giác",
            4: "Hình từ giác",
            5: "Hình ngũ giác",
            6: "Hình lục giác",
            7: "Hình thất giác",
            8: "Hình bát giác",
            9: "Hình cửu giác",
            10: "Hình thập giác"
        }
        if (self.sides in Shaper):
            return f"Số cạnh {self.sides} là {Shaper[self.sides]}."
        else:
            return "Số cạnh không phù hợp "
if __name__ == "__main__":
    try:
        sides = int(input("Nhập số cạnh: "))
        shaper = Shaper(sides)
        result = shaper.identify_Shape()
        print(result)
    except ValueError:
        print("Vui long nhập số cạnh hợp lệ")