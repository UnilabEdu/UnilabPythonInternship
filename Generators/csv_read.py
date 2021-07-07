# $ pip install memory_profiler
import memory_profiler as mem_profile
from timer import Timer

with Timer():
    print(f"Memory Usage before the operation is {mem_profile.memory_usage()} Mb")

    lines = (line for line in open('founding.csv'))

    list_lines = (s.rstrip().split(",") for s in lines)

    columns = next(list_lines)  # first line of the list

    print(columns)

    dict_of_companies = (dict(zip(columns, row)) for row in list_lines)

    funded_on_c_round = (
        int(company_dict.get("raisedAmt"))
        for company_dict in dict_of_companies
        if company_dict.get('round') == "c"
    )

    total_raised_in_c = sum(funded_on_c_round)

    print(f"Total amount of money raised during the C round is: {total_raised_in_c}")

    print(f"Memory Usage before the operation is {mem_profile.memory_usage()} Mb")