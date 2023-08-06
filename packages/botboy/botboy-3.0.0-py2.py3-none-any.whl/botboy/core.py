"""Multithreading & processing worker and Sequencer"""

import threading
import multiprocessing


class BotBoy:
    def __init__(
        self,
        name: str = None,
        task: object = None,
        params: list = [],
        verbose: bool = False,
    ):
        self.setup(name, task, params)
        self._verbose = verbose

    def __str__(self):
        return f"Name: {self._name}\nTask: {self._task.__name__}\nParameters: {self._params}\nResult: {self._result}"

    def _log(self, msg: str, end: str = None):
        """Logs a message to output

        Args:
            msg (str): Message to output
            end (str): String appended after the last value. Default a newline.
        """
        if self._verbose:
            print(msg, end=end)

    def _wrapper(self):
        """Task wrapping, adds logging and error handling

        Raises:
            Exception: any
        """
        try:
            self._log(
                f"{self._name} is executing task: {self._task.__name__}", end=", "
            )
            self._result = self._task(*self._params)
        except Exception as e:
            print(
                f"_wrapper failed to execute {self._task} with params {self._params}: {e}"
            )
            raise
        else:
            self._log("done.")

    # ---------------------------------- Getters --------------------------------- #

    def name(self):
        """Returns the name of the BotBoy instance

        Returns:
            Str: Name
        """
        return self._name

    def task(self):
        """Returns the task assigned to BotBoy instance

        Returns:
            Object: Task
        """
        return self._task

    def result(self):
        """Returns the result of task when executed

        Returns:
            Any: Result
        """
        return self._result

    def params(self):
        """Returns task arguments

        Returns:
            List: Task arguments
        """
        return self._params

    # ---------------------------------- Setter ---------------------------------- #

    def setup(self, name: str = None, task: object = None, params: list = []):
        """Set name and task

        Args:
            name (str): Name of instance (used to name thread and process)
            task (object): Method to execute on separate process or thread
            params (list): Task arguments
        """
        if name:
            self._name = name
        if task:
            self._task = task
        if params:
            self._params = params
        # Reset result since new task was given
        self._result = None

    # ------------------------------ Client Methods ------------------------------ #

    def execute(self, wait: bool = True, is_process: bool = False):
        """Runs the assigned task

        Args:
            wait (bool): Pause execution until task is finished running. Default is True.
            is_process (bool): Run task on a separate process instead of thread. Default is False.

        Returns:
            Any: Result from executed task method
        """
        try:
            if is_process:
                process = multiprocessing.Process(target=self._wrapper, name=self._name)

                self._log(f"Running on process: {process}", end=", ")
                process.run()
            else:
                thread = threading.Thread(target=self._wrapper, name=self._name)

                self._log(f"Running on thread: {thread}", end=", ")
                if wait:
                    self._log(f"Waiting for {self._task.__name__} to finish", end=", ")
                    thread.run()
                else:
                    thread.start()
        except Exception as e:
            print(f"Execute failed to run {self._task.__name__}: {e}")
            raise

        return self._result

    def save(self, filename: str):
        """Save the result in a file

        Args:
            filename (str): The name of the file or the path to store the result in

        Raises:
            Exception: Failed to save result in file
        """
        self._log(f"Storing result {self._result} at {filename}", end=", ")

        try:
            with open(filename, "w") as f:
                f.write(f"{self._result}")
        except Exception as e:
            print(f"Failed to save result {self._result} in file {filename}: {e}")
            raise
        else:
            self._log("done.")

    def verbose(self):
        """Turn on logging"""
        self._verbose = True

    def silent(self):
        """Turn off logging"""
        self._verbose = False


class Sequencer:
    def __init__(self, bots: list):
        self._bots = bots

    def __call__(self):
        results = []
        for bot in self._bots:
            results.append(bot.execute(wait=True))
        return results

    @classmethod
    def pack(self, tasks: list, params: list, verbose: bool = False):
        """Create a list of bots ready to be sequenced

        Args:
            tasks (list): Tasks for each bot
            params (list): Params for each task
            verbose (bool, optional): Turn on logging. Defaults to False.

        Returns:
            List: List of BotBoys ready to be sequenced
        """
        bots = []
        for i in range(len(tasks)):
            bots.append(
                BotBoy(name=f"Bot{i}", task=tasks[i], verbose=verbose, params=params[i])
            )
        return bots
