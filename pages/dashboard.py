from pages.base_page import BasePage

class Dashboard(BasePage):
    scouts_panel_title = "//*[@id='__next']/div[1]/header/div/h6"
    main_page_btn = "(//div[@role='button'])[1]"
    players_btn = "(//div[@role='button'])[2]"
    language_btn = "(// div[@ role='button'])[3]"
    sign_out_btn = "(// div[@ role='button'])[4]"
    dev_team_contact = "// a[ @ href = 'https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6']"
    add_player_btn = "//button[@type='button']//span[text()='Add player']"
    players_count = "//div //div[text()='Players count']"
    last_upd_match = "//h6[text()='Last updated match']"
    last_created_match = "// h6[text() = 'Last created match']"
    activity_title = "// h2[text() = 'Activity']"
    last_created_player = "// h6[text() = 'Last created player']"

    pass