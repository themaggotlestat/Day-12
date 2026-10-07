remote_jobs = [
    "Software Engineer",
    "Cybersecurity",
    "Web Developer"
]

local_jobs = [
    "Warehouse Worker",
    "IT Support",
    "Mechanic"
]

def show_jobs(job_list):
    for job in job_list:
            print(job)

show_jobs(remote_jobs)

print("Local Jobs:")

show_jobs(local_jobs)