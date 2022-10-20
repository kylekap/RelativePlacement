import pandas as pd
import math


class Competition:
    def __init__(self, filepath):
        self.competitors, self.placings = {}, {}
        self.df = pd.read_csv(filepath)
        self.df.set_index("Competitor", inplace=True)
        self.df.apply(pd.to_numeric)
        self.judges = self.df.columns
        self.majority_number = self._majority()
        self._majority_col()
        self._sum_majority()
        self.df.sort_values(by=['majority_col', 'majority_tot'], ascending=[True, True], inplace=True)

    def _majority(self):
        for i in range(1, len(self.df.index) + 1):
            self.df[f"{str(i)}"] = (self.df[self.judges] <= i).sum(1)
        for i in range(1, len(self.df.index) + 1):
            self.df[f"{str(i)}_sum"] = self.df[self.df[self.judges] <= i].sum(1)
        return math.ceil(len(self.judges) / 2)

    def _majority_col(self):
        self.df["majority_col"] = ""
        for i in range(1, len(self.df.index) + 1):
            self.df.loc[(self.df[f"{str(i)}"] >= self.majority_number) & (self.df["majority_col"] == ""), "majority_col"] = i

    def _sum_majority(self):
        for index, row in self.df.iterrows():
            self.df.loc[(self.df.index == index), "majority_tot"] = row[row[-1] + len(self.judges) + len(self.df.index) - 1]
        self.df = self.df.loc[:, ~self.df.columns.str.contains('sum')]

    def import_data(self, filepath):
        with open(filepath) as fp:
            contents = fp.read()
            data = contents.splitlines()[1:]
            return data

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


if __name__ == "__main__":
    """[summary]"""
    try:
        bluesmuse = Competition("Tests/test.csv")
        for ea, values in bluesmuse.competitors.items():
            print(
                ea,
                values.placements,
                "Majority:",
                values.majority,
                "CT",
                values.majority_ct,
                "Sum",
                values.majority_sum,
                "Next",
                values.majority_next,
                "Total",
                values.all_sum,
            )

    except Exception as E:
        print(type(E).__name__, __file__, E.__traceback__.tb_lineno, "\n", E)
