# Python Template Project

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8 Status](./reports/flake8/badge.svg)](./reports/flake8/index.html)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Coverage Status](./reports/coverage/badge.svg)](./reports/coverage/badge.svg)

[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Build Status](https://github.com/kylekap/RelativePlacement/workflows/pre-commit/badge.svg)](https://github.com/kylekap/RelativePlacement/actions)
[![Build Status](https://travis-ci.com/kylekap/RelativePlacement.svg?branch=main)](https://travis-ci.com/kylekap/RelativePlacement)

[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Python](https://img.shields.io/pypi/pyversions/cookiecutter-hypermodern-python-instance)](https://www.python.org/downloads/release/python-3100/)

[![GitHub Issues](https://img.shields.io/github/issues/kylekap/RelativePlacement.svg)](https://github.com/kylekap/RelativePlacement/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylekap/RelativePlacement.svg)](https://github.com/kylekap/RelativePlacement/pulls)

## About
Output the relative placement scores of each competitior

This project is intended to meet the requirements of PEP-518 and PEP-621, removing the setup.py file and having only minor use of setup.cfg (intended at this time only for flake8 support)

## Contents
- [Python Template Project](#python-template-project)
  - [About](#about)
  - [Contents](#contents)


## Relative Placements

1. Determine Majority
  - Find at what number the majority of each contestants rankings are <=. This determines the first round of relative placements - lower the # the better the rank. This serves as the primary differentiator.

2. Sum Total
  - If the majority determination results in competitors sharing a number, find the sum of the rankings that resulted in that majority.
  - This is a tiebreaker mechanic.

3. Next lowest
  - If Sum Total produces the same results, the next level tiebreaker is to determine the next lowest ranking a competitor has. The lowest # will be ranked better.
  - This is a tiebreaker mechanic.

4. Equal Scores
  - If Majority, Sum Total, and Next Lowest all produce equal results for 2 or more competitors, evaluate those competitors as if they were a contest. This means, for each judge, re-number the rankings against each other.
  - This is a tiebreaker mechnic.

5. Ties
  - If the scores end up as such that 1-4 fail to differentiate, it is encouraged to leave the competitors as a tie.
  - Alternatively, a "tiebreaker" can be determined by designating one judge as a head judge, whose ranking will serve to differentiate the contestants.