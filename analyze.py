from pathlib import Path
import json

# print matchups
for i in range(5,6):

    with open(Path(__file__).parent / f"output/week_{i}_matchup.json") as f:
        data = json.load(f)
        print(f"Week {i} recap:")
        for j in range(6):
            summary = ""
            for t in range(2):
                team_name = data[j]["matchup"]["teams"][t]["team"]["name"] 
                proj = data[j]["matchup"]["teams"][t]["team"]["team_projected_points"]["total"]
                actual = data[j]["matchup"]["teams"][t]["team"]["team_points"]["total"]

                summary += f"{team_name} scored {actual} points (projected {proj}) vs. "
            
            summary = summary[:-5]
            print(summary)
        print("\n")

# print standings
with open(Path(__file__).parent / f"output/week_4_standings.json") as f:
    data = json.load(f)
    for i in range(12):
        name = data["teams"][i]["team"]["name"]
        wins = data["teams"][i]["team"]["team_standings"]["outcome_totals"]["wins"]
        losses = data["teams"][i]["team"]["team_standings"]["outcome_totals"]["losses"]
        pf = data["teams"][i]["team"]["team_standings"]["points_for"]
        print(f"{i+1}: {name}: {wins}-{losses} ({pf})")


