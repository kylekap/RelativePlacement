# Standard library
import math
import pandas as pd


class Competition:
    def __init__(self, filepath):
        self.competitors, self.placings = {}, {}
        self.df = pd.read_csv(filepath)
        self.data = self.import_data(filepath).split(",")
        self._generate_competitors(self.data)
        # self._generate_placings()

    def import_data(self, filepath):
        with open(filepath) as fp:
            contents = fp.read()
            data = contents.splitlines()[1:]
            return data

    def _still_to_place(self):
        temp = {}
        for k, i in self.competitors.items():
            if k not in self.placings:
                temp[k] = i
        return temp

    def _maj_dict(self, x):
        a = {}
        for k, i in x.items():
            a[k] = i.majority
        return a

    def _generate_competitors(self, data):
        data
        for ea in data:
            line = ea.split(",")
            self.competitors[line[0]] = Competitor(line[0], line[1:])

    def _equal_scores(comp_1, comp_2):
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
        self.all_sum = sum(self.placements)
        self._majority_at()
        return None

    def str_to_int(self, li):
        x = []
        for ea in li:
            if type(ea) == int:
                x.append(ea)
            elif type(ea) == str:
                try:
                    x.append(int(ea))
                except Exception as E:
                    print(E)
        return x

    def _majority_at(self):
        for ea in range(1, max(self.placements)):
            a = [i for i in self.placements if i <= ea]
            if len(a) > len(self.placements) / 2:
                self.majority = ea
                self.majority_ct = len(a)
                self.majority_sum = sum(a)
                self.majority_next = self.sorted_placements[math.ceil(len(self.placements) / 2) :][0]
                break


if __name__ == "__main__":
    """[summary]"""
    try:
        bluesmuse = Competition("Tests/test.csv")
        for ea, values in bluesmuse.competitors.items():
            print(ea, values.placements, "Majority:", values.majority, "CT", values.majority_ct, "Sum", values.majority_sum, "Next", values.majority_next, "Total", values.all_sum)

    except Exception as E:
        print(type(E).__name__, __file__, E.__traceback__.tb_lineno, "\n", E)
