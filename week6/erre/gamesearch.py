import requests

# import json # implicitly imported by requests

BASE_URL = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com"


class Game:
    def __init__(
        self,
        home_score: int,
        away_score: int,
        date: str = "",
        time: str = "",
        home_team: str = "",
        away_team: str = "",
    ):
        self.date = date
        self.time = time
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score

    def __eq__(self, other):  # IMPORTANT: Checks the SCORES
        return (
            self.home_score == other.home_score and self.away_score == other.away_score
        )

    def __str__(self):
        return (
            f"[{self.home_team}-{self.away_team}] {self.home_score}-{self.away_score}"
        )
        # return f"[{self.date} {self.time}] [{self.home_team}-{self.away_team}] {self.home_score}-{self.away_score}"

    def total_score(self) -> int:
        return self.home_score + self.away_score


def get_seasons() -> list[str]:
    try:
        res = requests.get(f"{BASE_URL}/api")
        seasons = res.json()["seasons"]
    except requests.HTTPError as http_exception:
        print(f"Http error: {http_exception}")
    except requests.exceptions.JSONDecodeError:
        print("Malformed JSON")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        return seasons


def get_season_dates(season: str):
    try:
        res_season = requests.get(f"{BASE_URL}/api/{season}")
        game_dates = res_season.json()["gamedays"]
    except requests.HTTPError as http_exception:
        print(f"Http error: {http_exception}")
    except requests.exceptions.JSONDecodeError:
        print("Malformed JSON")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        return game_dates


def iso_from_year_date(year: str, date: str):
    month, day = date.split("/")
    return f"{year}-{month}-{day}"


def prompt_number_safe(prompt: str) -> int:
    while True:
        input_data = input(prompt)
        try:
            ret = int(input_data)
        except ValueError:
            print("Invalid number")
            continue
        return ret


def get_date(season: str, date: str) -> list[Game]:
    games = []
    try:
        res = requests.get(f"{BASE_URL}/api/{season}/{date}")
        res_json = res.json()
        date = res_json["date"]  # From the API docs
        for game in res_json["games"]:
            time = game["clock"]
            home_team = game["score"]["home"]["team"]
            home_score = game["score"]["home"]["goals"]
            away_team = game["score"]["away"]["team"]
            away_score = game["score"]["away"]["goals"]
            games.append(
                Game(
                    date=date,
                    time=time,
                    home_team=home_team,
                    home_score=home_score,
                    away_team=away_team,
                    away_score=away_score,
                )
            )
    except requests.HTTPError as http_exception:
        print(f"Http error: {http_exception}")
    except requests.exceptions.JSONDecodeError:
        print("Malformed JSON")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        return games


def get_games(season: str, dates: list[str]) -> dict[list[Game]]:
    games = {}
    total_games = 0

    for date in dates:
        date_string = iso_from_year_date(season, date)
        games[date_string] = get_date(season, date)  # No check should be necessary
        total_games += len(games[date_string])

    return games, total_games


def prompt_season(seasons: list[str]) -> str:
    user_season = str(prompt_number_safe("Enter season year: "))

    while not user_season in seasons:
        print("Invalid season")
        user_season = str(prompt_number_safe("Enter season year: "))

    return user_season


def print_ui(year: int):
    print(
        f"""
Search games for season {year}, choose an option
    1 - Query exact standing
    2 - Query total goal count
    3 - Query maximum amount of goals
    4 - Exit program
    """
    )


def user_query(games: dict[list[Game]], total_games: int, season: int):

    print_ui(season)
    user_choice = prompt_number_safe("Enter your choice (1-4): ")

    while user_choice != 4:
        matched_games = 0
        if user_choice == 1:  # Query exact game
            home_score = prompt_number_safe("Enter home score: ")
            away_score = prompt_number_safe("Enter away score: ")
            matcher_game = Game(home_score=home_score, away_score=away_score)
            for date, date_games in games.items():
                matched = False
                for date_game in date_games:
                    if (
                        date_game == matcher_game
                    ):  # Check implementation, looks only at scores
                        if not matched:
                            print(date)
                            matched = True
                        print(date_game)
                        matched_games += 1
                if matched:
                    print()
        elif user_choice == 2:
            target_score = prompt_number_safe("Enter the total score: ")
            for date, date_games in games.items():
                matched = False
                for date_game in date_games:
                    if date_game.total_score() == target_score:
                        if not matched:
                            print(date)
                            matched = True
                        print(date_game)
                        matched_games += 1
                if matched:
                    print()

        elif user_choice == 3:
            target_score = prompt_number_safe("Enter the upper bound: ")
            for date, date_games in games.items():
                matched = False
                for date_game in date_games:
                    if date_game.total_score() < target_score:
                        if not matched:
                            print(date)
                            matched = True
                        print(date_game)
                        matched_games += 1
                if matched:
                    print()
        else:
            print("Invalid option")

        percentage = round(100 * (matched_games / total_games), 1)
        print(f"{matched_games} matched out of {total_games} ({percentage}%)")

        print_ui(season)
        user_choice = prompt_number_safe("Enter your choice (1-4): ")


def main():
    seasons = get_seasons()
    user_season = prompt_season(seasons)
    print("Loading...", end="", flush=True)
    dates = get_season_dates(user_season)
    games, total_games = get_games(user_season, dates)
    print("done")

    user_query(games, total_games, user_season)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit(0)
