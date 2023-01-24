from pages.base_page import BasePage


class Dashboard(BasePage):
    my_team_field = "//input[@name='myTeam']"
    enemy_team_field = "//input[@name='enemyTeam']"
    my_team_score = "// input[ @ name = 'myTeamScore']"
    enemy_team_score = "// input[ @ name = 'enemyTeamScore']"
    date_field = "// input[ @ name = 'date']"
    match_at_home_radio_btn = "// label[ @ type = 'radio'][1]"
    match_out_home_radio_btn = "(// input[@class ='jss281'])[1]"
    submit_btn = "//button[@type='submit']"
    league_field = "// input[ @ name = 'league']"
    time_played_field = "// input[ @ name = 'timePlayed']"

    pass