from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    max_salary = 0

    for job in jobs_list:
        salary = job["max_salary"]
        if salary and salary.isdigit():
            salary = int(salary)
            if salary > max_salary:
                max_salary = salary

    return max_salary


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    min_salary = float('inf')

    for job in jobs_list:
        salary = job["min_salary"]
        if salary and salary.isdigit():
            salary = int(salary)
            if salary < min_salary:
                min_salary = salary

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(salary) not in [int, str]
        or not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
        or not int(job["max_salary"]) > int(job["min_salary"])
    ):
        raise ValueError("Invalid number")

    min_salary = int(job["min_salary"])
    max_salary = int(job["max_salary"])
    salary = int(salary)

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filter_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_jobs.append(job)
        except ValueError:
            ("Invalid number")

    return filter_jobs
