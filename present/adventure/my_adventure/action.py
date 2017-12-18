class Action():
    def __init__(self, method, name, hotkey):
        """Creates a new action

        :param method: the function object to execute
        :param name: the name of the action
        :param hotkey: The keyboard key the player should use to initiate this action
        """
        self.method = method
        self.hotkey = hotkey
        self.name = name

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)
