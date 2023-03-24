from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        jobs_list = []
        for job in jobs_reader:
            jobs_list.append(job)
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    jobs_types = []

    for job in jobs_list:
        if not job["job_type"] in jobs_types:
            jobs_types.append(job["job_type"])

    return jobs_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_filter_list = []

    for job in jobs:
        if job["job_type"] == job_type:
            job_filter_list.append(job)
    return job_filter_list
