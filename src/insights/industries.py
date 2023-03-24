from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    jobs_industries = []

    for job in jobs_list:
        if not job["industry"] in jobs_industries and job["industry"]:
            jobs_industries.append(job["industry"])

    return jobs_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_filter_list = []

    for job in jobs:
        if job["industry"] == industry:
            industry_filter_list.append(job)
    return industry_filter_list
