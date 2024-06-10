def PosToString(x: int, y: int):
    return (str(x) + "," + str(y))


def IntSign(x: int):
    return (x > 0) - (x < 0)


class Knot:

    def __init__(self, name):
        self.Position = [0, 0]
        self.name = name
        pass

    def ComparePos(self, Other: 'Knot'):

        Delta = [(Other.Position[0] - self.Position[0]), (Other.Position[1] - self.Position[1])]

        Temp = self.Position

        while (abs(Delta[0]) + abs(Delta[1]) > 2):
            # handle Diagonal
            self.Position[0] += IntSign(Delta[0])
            self.Position[1] += IntSign(Delta[1])
            Delta = [(Other.Position[0] - self.Position[0]), (Other.Position[1] - self.Position[1])]
        # move Horizontally
        if abs(Delta[0]) == 2:
            self.Position[0] += int(Delta[0] / 2)
        # move Vertically
        elif abs(Delta[1]) == 2:
            self.Position[1] += int(Delta[1] / 2)


def main():
    Line = 1
    Input = open("text.txt")
    Text = Input.readlines()

    Positions = {PosToString(0, 0)}

    Knots = [Knot(i) for i in range(0, 10)]

    for Movement in Text:
        Movement = Movement.strip()
        Dir = Movement[0]
        Count = int(Movement[2:])

        for i in range(Count):

            match Dir:
                case "U":
                    Knots[0].Position[1] += 1
                case "D":
                    Knots[0].Position[1] -= 1
                case "L":
                    Knots[0].Position[0] -= 1
                case "R":
                    Knots[0].Position[0] += 1
            if (Line == 42):
                pass
            for j in range(1, len(Knots)):
                Knots[j].ComparePos(Knots[j - 1])
                if j == (len(Knots) - 1):
                    Positions.add(PosToString(Knots[j].Position[0], Knots[j].Position[1]))
        Line += 1

    print("output 2: ", len(Positions))


if __name__ == "__main__":
    main()