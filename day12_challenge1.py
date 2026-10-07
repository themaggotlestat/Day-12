careers = [
    {"career": "Software Engineer", "salary": 30, "remote": True},
    {"career": "Cybersecurity", "salary": 25, "remote": True},
    {"career": "Web Developer", "salary": 20, "remote": True},
    {"career": "IT Support", "salary": 18, "remote": False}
]

def show_remote_jobs():

    for career in careers:

        if career["remote"]:

            print(career["career"])

show_remote_jobs()