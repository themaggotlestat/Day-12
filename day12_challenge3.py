careers = [
    {"career": "Software Engineer", "salary": 30, "remote": True},
    {"career": "Cybersecurity", "salary": 25, "remote": True},
    {"career": "Web Developer", "salary": 20, "remote": True},
    {"career": "IT Support", "salary": 18, "remote": False}
]

minimum_salary = int(input("What is your minimum salary?"))

def show_jobs_by_salary(job_list, minimum_salary):
    for job in job_list:
        if job["salary"] >= minimum_salary:
            print(job["career"])



show_jobs_by_salary(careers, minimum_salary)
