class Game:
    def __init__(self, title):
        self._title = None
        self.title = title   # uses the setter

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # title must be an immutable string → do NOT allow reset after initialization
        if self._title is None:
            if isinstance(value, str) and len(value) > 0:
                self._title = value
            else:
                pass  # tests expect you to silently ignore invalid assignment
        else:
            pass  # ignore attempts to change title

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        scores = [r.score for r in self.results() if r.player is player]
        if scores:
            return sum(scores) / len(scores)
        return None


class Player:
    def __init__(self, username):
        self._username = None
        self.username = username  # use setter

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        else:
            pass  # ignore invalid update

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([r for r in self.results() if r.game is game])


class Result:

    all = []

    def __init__(self, player, game, score):
        self._score = None
        self.player = player
        self.game = game
        self.score = score  # use setter

        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        # score must be immutable → only set if _score not set yet
        if self._score is None:
            if isinstance(value, int) and 1 <= value <= 5000:
                self._score = value
            else:
                pass
        else:
            pass  # ignore reassignment
