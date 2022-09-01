# Standard library
import math


class Competition:
    def __init__(self, filepath):
        self.competitors, self.placings = {}, {}
        self._generate_competitors(self.import_data(filepath))
        self._generate_placings()

    def import_data(self, filepath):
        with open(filepath) as fp:
            contents = fp.read()
            data = contents.splitlines()
            return data

    def _generate_placings(self):
        for ea in range(1, len(self.competitors)):
            self.placings[ea] = None

    def _generate_competitors(self, data):
        data
        for ea in data:
            line = ea.split(",")
            self.competitors[line[0]] = Competitor(line[0], line[1:])

    def equal_scores(comp_1, comp_2):
        gt = 0
        for i in range(len(comp_1)):
            if comp_1[i] > comp_2[i]:
                gt += 1
            elif comp_1[i] < comp_2[i]:
                gt -= 1
        if gt > 1:
            return 1
        elif gt < 1:
            return 2
        else:
            return None


class Competitor:
    def __init__(self, name, placements=[]):
        self.name = name
        self.placements = self.str_to_int(placements)
        self.sorted_placements = sorted(self.placements)
        self._majority_at()
        return None

    def str_to_int(self, li):
        x = []
        for ea in li:
            x.append(int(ea))
        return x

    def _majority_at(self):
        for ea in range(1, max(self.placements)):
            a = [i for i in self.placements if i <= ea]
            if len(a) > len(self.placements) / 2:
                self.majority = ea
                self.majority_ct = len(a)
                self.majority_sum = sum(a)
                self.majority_next = self.sorted_placements[math.ceil(len(self.placements) / 2) :]
                break


def main():
    # Main function

    try:
        bluesmuse = Competition("Tests/test.csv")
        for ea, values in bluesmuse.competitors.items():
            print(ea, values.placements, values.majority, values.majority_ct, values.majority_sum, values.majority_next)

    except Exception as E:
        print(type(E).__name__, __file__, E.__traceback__.tb_lineno, "\n", E)


if __name__ == "__main__":
    """[summary]"""
    main()
