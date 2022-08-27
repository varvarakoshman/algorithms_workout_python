HOME_TEAM_WON = 1


def tournament_winner(competitions, results):
    curr_best_team = ""
    teams_scores = {curr_best_team: 0}
    for idx, competition in enumerate(competitions):
        home_team, away_team = competition
        winning_team = home_team if results[idx] == HOME_TEAM_WON else away_team
        update_scores(winning_team, 3, teams_scores)
        if teams_scores[winning_team] > teams_scores[curr_best_team]:
            curr_best_team = winning_team
    return curr_best_team


def update_scores(winning_team, score, teams_scores):
    if winning_team not in teams_scores.keys():
        teams_scores[winning_team] = 0
    teams_scores[winning_team] += score

    # complexity: O(n), n - # of competitions
    # space complexity: O(k), k - # of teams


if __name__ == '__main__':
    assert tournament_winner([["HTML", "C#"],
                              ["C#", "Python"],
                              ["Python", "HTML"]], [0, 0, 1]) == "Python"
    assert tournament_winner([["Java", "C#"],
                              ["JS", "Python"],
                              ["Python", "JS"],
                              ["Python", "Java"]], [1, 0, 0, 0]) == "Java"
    assert tournament_winner([["Java", "Python"],
                              ["Java", "Python"],
                              ["Python", "Java"],
                              ["Python", "Java"]], [1, 1, 0, 0]) == "Java"
    assert tournament_winner([["Java", "Python"],
                              ["Java", "Python"],
                              ["Python", "Java"],
                              ["Python", "Java"]], [0, 0, 1, 1]) == "Python"
    assert tournament_winner([["Java", "Python"]], [0]) == "Python"
    assert tournament_winner([["Java", "Python"],
                              ["Java", "Python"],
                              ["Java", "Python"],
                              ["Python", "Java"]], [1, 1, 1, 1]) == "Java"
    assert tournament_winner([["Java", "Python"],
                              ["Java", "Python"],
                              ["Java", "Python"],
                              ["Python", "Java"]], [0, 0, 0, 0]) == "Python"
