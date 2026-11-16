def register_team(teams, name):
    cleaned = name.strip()

    # 1. Validate first
    if not (2 <= len(cleaned) <= 30):
        raise ValueError("Name must be 2-30 characters.")

    if not (len(teams) <= 8):
        raise ValueError("Team limit is full")
    team.append(name)

    for team in teams:
        if team["name"].casefold() == cleaned.casefold():
            raise ValueError("That name is already taken.")

    # 2. Only change data after everything passed
    new_id = f"TM{len(teams) + 1:03d}"
    team = {"id": new_id, "name": cleaned}
    teams.append(team)
    return team

def list_teams(teams):
    return list(teams)

try:
    register_team(teams, " red comets ")
except ValueError as error:
    print("Rejected:", error)

try:
    register_team(teams, "X")
except ValueError as error:
    print("Rejected:", error)

print(list_teams(teams))

if __name__ == "__main__":
    teams = []
    print(register_team(teams, "Red Comets"))    # TM001
    print(register_team(teams, "Blue Sharks"))   # TM002
    # ...the rest of your demo, indented under this line