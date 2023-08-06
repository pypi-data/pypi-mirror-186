"""Tests the BotBoy Module"""

import unittest, os

from botboy.core import BotBoy, Sequencer


class BotBoyTests(unittest.TestCase):
    TASKS = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]

    def test_init(self):
        task = self.TASKS[0]
        bot = BotBoy(name="InitBot", task=task, verbose=True, params=[1, 2])
        self.assertIsInstance(bot, BotBoy)
        self.assertIsInstance(bot.task(), object)
        self.assertIsInstance(bot._verbose, bool)
        self.assertIsInstance(bot.name(), str)
        self.assertEqual(bot.name(), "InitBot")
        self.assertEqual(bot._verbose, True)
        self.assertEqual(bot.result(), None)
        self.assertEqual(bot.task(), task)
        self.assertEqual(bot.params(), [1, 2])

        # Test getters and setter
        bot.setup(name="InitBot2", task=self.TASKS[1], params=[3, 4])
        self.assertEqual(bot.name(), "InitBot2")
        self.assertEqual(bot.task(), self.TASKS[1])
        self.assertEqual(bot.result(), None)
        self.assertEqual(bot.params(), [3, 4])

        print(f"Testing __str__: \n{bot}")

    def test_wrapper(self):
        task = self.TASKS[0]
        name = "WrapperBot"
        bot = BotBoy(name, task, True, [1, 2])
        bot._wrapper()
        self.assertEqual(bot.result(), 3)

    def test_client(self):
        bot = BotBoy(name="ClientBot", verbose=True)

        # Test log state
        bot.silent()
        self.assertEqual(bot._verbose, False)

        bot.verbose()
        self.assertEqual(bot._verbose, True)

        # Test execute
        results = []

        task = self.TASKS[0]
        bot.setup(task=task, params=[1, 2])
        results.append(bot.execute())

        task = self.TASKS[1]
        bot.setup(task=task, params=[1, 2])
        results.append(bot.execute(wait=False))

        task = self.TASKS[2]
        bot.setup(task=task, params=[1, 2])
        results.append(bot.execute(is_process=True))

        self.assertEqual(results[0], 3)
        self.assertEqual(results[1], -1)
        self.assertEqual(results[2], 2)

        # Test save
        bot.save("result.txt")
        path = os.getcwd() + "/result.txt"
        self.assertEqual(os.path.exists(path), True)

    def test_sequencer(self):
        params = [[1, 2], [3, 4], [5, 6]]
        bots = Sequencer.pack(tasks=self.TASKS, params=params, verbose=True)
        seq = Sequencer(bots)
        results = seq()
        expected = [3, -1, 30]

        for i in range(len(results)):
            self.assertEqual(results[i], expected[i])
