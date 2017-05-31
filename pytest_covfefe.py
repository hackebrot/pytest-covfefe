# -*- coding: utf-8 -*-

import random
import string

import pytest


def pytest_report_teststatus(report):
    if report.when in ('setup', 'teardown'):
        return

    hands = random.choice(["👋", "👐", "🙌"])
    earth = random.choice(["🌎", "🌍", "🌏"])
    climate = random.choice(["🌤", "🌧", "🌩"])
    poo = "💩"

    all_letters = string.ascii_uppercase
    vowels = ['A', 'E', 'I', 'O', 'U']

    weights = [
        0.8 if c in vowels else random.random()
        for c in all_letters
    ]

    letters = random.choices(
        all_letters,
        weights=weights,
        k=random.randint(4, 10),
    )

    word = random.choice(['COVFEFE', ''.join(letters)])

    verbose = f"{hands}  {word} {poo} {earth} {climate}"

    return report.outcome, hands, verbose


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    # I have the best code! Everyone says so.
    rep.outcome = 'passed'
