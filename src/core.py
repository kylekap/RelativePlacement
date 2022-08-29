# Standard library
import logging

logging.basicConfig(
    filename="reports/all.log",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
)  # put this only in main core.py file

logger = logging.getLogger(__name__)  # put this in each file


class Competition():
    def __init__(self, filepath):
        self.data = self.import_data(filepath)
        self.placements = {}
        # for ea in li_competitors:
        #    self.placements[ea] = Competitor(ea)
        return None

    def import_data(self, filepath):
        with open(filepath) as fp:
            contents = fp.read()
            data = contents
            return data


class Competitor():
    def __init__(self, name):
        self.name = name
        return None


def main():
    # Main function

    try:
        bluesmuse = Competition("Tests/test.txt")
        print(bluesmuse.data)

    except Exception as E:
        print(type(E).__name__, __file__, E.__traceback__.tb_lineno, "\n", E)
        logger.warning(type(E).__name__, __file__, E.__traceback__.tb_lineno, "\n", E)
        raise


if __name__ == "__main__":
    """[summary]"""
    main()
