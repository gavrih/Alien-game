class Settings():
    """A class to store all settings for Alien Invasion."""
    screen_width: int

    def __init__(self):
        # Screen settings
        self.screen_width = 1200  # רוחב_מסך
        self.screen_height = 800  # אורך_מסך
        self.bg_color = (230, 230, 230)  # צבע_מסך
        self.ship_limit = 3  # כמות הפסילות המוצגות במסך

        # Bullet settings
        self.bullet_width = 3  # רוחב הכדור
        self.bullet_height = 15  # אורך הכדור
        self.bullet_color = 60, 60, 60  # צבע הכדור
        self.bullets_allowed = 3  # כמות הכדורים בלוח

        # Alien settings
        self.fleet_drop_speed = 10  # כמות השורות שהחייזר יורד

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1  # מהירות החייזר

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5  # מהירות תזוזת הספינה
        self.bullet_speed_factor = 1  # מהירות הכדורים של הספינה
        self.alien_speed_factor = 0.5  # קצב תזוזת החייזר

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1  # כיון צי החייזרים

        # Scoring
        self.alien_points = 50  # ניקוד פר חייזר

    def increase_speed(self):  # שלבים מתקדמים
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
