""" Volley Implementation"""

class Volleyball(_Sport):
    """ Volleyball Implementation"""

    def __init__(self):
        super().__init__()

class MatchVolleyball(_Match):
    """ Volleyball Match Implementation"""

    def __init__(self, team_1, coach_1, team_2, coach_2, country_1, country_2, set_1, set_2) -> None:
        super().__init__(team_1, team_2)
        self.coach_1 = coach_1
        self.coach_2 = coach_2
        self.country_1 = country_1
        self.country_2 = country_2
        self.set_1 = set_1
        self.set_2 = set_2
    
    def __str__(self):
        return f"Match: {self.team_1} vs {self.team_2}\n" \
    
    def __repr__(self):
        return f"MatchVolleyball(team_1='{self.team_1}', coach_1='{self.coach_1}', team_2='{self.team_2}', coach_2='{self.coach_2}', country_1='{self.country_1}', country_2='{self.country_2}', set_1={self.set_1}, set_2={self.set_2})" 
    
    def __eq__(self, other):
        if not isinstance(other, MatchVolleyball):
            return NotImplemented
        return (self.team_1 == other.team_1 and self.coach_1 == other.coach_1 and
                self.team_2 == other.team_2 and self.coach_2 == other.coach_2 and
                self.country_1 == other.country_1 and self.country_2 == other.country_2 and
                self.set_1 == other.set_1 and self.set_2 == other.set_2)
    
    def __hash__(self):
        return hash((self.team_1, self.coach_1, self.team_2, self.coach_2, self.country_1, self.country_2, self.set_1, self.set_2))
        
    def get_result(self):
        return f"Result: {self.team_1} {self.set_1} - {self.set_2} {self.team_2}"
    
    def get_coaches(self):
        return f"Coaches: {self.coach_1} (Team 1), {self.coach_2} (Team 2)"
    
    def get_countries(self):
        return f"Countries: {self.country_1} (Team 1), {self.country_2} (Team 2)"

    def get_winning_team(self):
        if self.set_1 > self.set_2:
            return f"{self.team_1} wins."
        elif self.set_2 > self.set_1:
            return f"{self.team_2} wins."
        else:
            return "It's a tie."
    
    def get_loosing_team(self):
        if self.set_1 < self.set_2:
            return f"{self.team_1} loses."
        elif self.set_2 < self.set_1:
            return f"{self.team_2} loses."
        else:
            return "It's a tie."
        
        
               
    


