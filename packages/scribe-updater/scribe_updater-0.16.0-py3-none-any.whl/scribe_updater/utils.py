import csv
import json

from scribe_updater.product import (
    get_product_scenario,
    get_special_products_competencies,
    product_description,
)


def read_csv(filename: str):
    """
    Reads csv specified at filename
    """
    with open(filename, "r") as csvreader:
        return list(csv.DictReader(csvreader))


def load_json(file):
    """
    Reads json file and stores into a dict
    """
    if not file:
        return {}

    with open(file, "r") as f:
        f = json.loads(f.read())

    return f


def get_scenarios(info):
    """
    creates a dictionary of scenarios
    """
    ids = {}

    if "competencies" not in info:
        return ids

    for i in info["competencies"]:
        s = {}
        if not i["scenarios"]:
            ids[i["name"]] = []
        else:
            for scenario in i["scenarios"]:
                s["{}".format(scenario["name"])] = scenario
            ids[i["name"]] = s
    return ids


def get_competencies(info):
    """
    Creates a dictionary of competencies
    """
    competencies = {}

    if "competencies" not in info:
        return competencies

    for i in info["competencies"]:
        comp = {
            "name": i["name"],
            "type": i["type"],
            "disabled": i["disabled"],
            "templates": i["templates"],
        }
        competencies[i["name"]] = comp
    return competencies


def merge_scenarios(
    scenario_name, ground_scenarios, target_scenarios, target_scenario_name
):
    """Used to merge two scenarios"""
    scenario = {}
    fields = [
        "name",
        "description",
        "example_queries",
        "disabled",
        "tags",
        "cases",
        "response_elements",
    ]
    for field in fields:
        scenario[field] = (
            target_scenarios[target_scenario_name][field]
            if (field == "disabled" or field == "response_elements")
            and (
                target_scenarios.get(target_scenario_name)
                and target_scenarios[target_scenario_name].get(field)
            )
            else ground_scenarios[scenario_name][field]
        )
    return scenario


def create_scenario(
    c, scenario_name, ground_scenarios, all_target_scenarios, finie_to_fi_map
):
    """
    Creates a new scenario
    """
    scenario = {}

    fields = [
        "name",
        "description",
        "example_queries",
        "disabled",
        "tags",
        "cases",
        "response_elements",
    ]
    for field in fields:
        if f"{c}-*-{scenario_name}" in finie_to_fi_map.keys():
            fi_competency_name = finie_to_fi_map[f"{c}-*-{scenario_name}"].split("-*-")[
                0
            ]
            fi_scenario_name = finie_to_fi_map[f"{c}-*-{scenario_name}"].split("-*-")[1]
            return merge_scenarios(
                scenario_name,
                ground_scenarios,
                all_target_scenarios[fi_competency_name],
                fi_scenario_name,
            )
        else:
            if field == "tags":
                scenario[field] = ground_scenarios[scenario_name][field] + [
                    "new_scenario"
                ]
            elif field == "disabled":
                scenario[field] = True
            else:
                scenario[field] = ground_scenarios[scenario_name][field]
    return scenario


def parse_product_name(name: str):
    names = name.split(": ")
    return [name.strip() for name in names]


def build_product_scenario(competency, names: list):
    (description, example_queries) = product_description(competency, names)
    return get_product_scenario(competency, description, example_queries, names)


def create_product_scenario(c, scenario_name, target_scenarios, is_new):
    """
    Creates a new product scenario
    """
    if is_new:
        names = parse_product_name(scenario_name)
        scenario = build_product_scenario(c, names)
        return scenario

    scenario = {}

    fields = [
        "name",
        "description",
        "example_queries",
        "disabled",
        "tags",
        "cases",
        "response_elements",
    ]
    for field in fields:
        scenario[field] = target_scenarios[scenario_name][field]
    return scenario


def process_scenario_list(
    competency, ground_scenarios, target_scenarios, products, finie_to_fi_map
):
    """
    Wrapper for handling the scenarios
    """
    product_list = [
        "faq_describe_accounts",
        "faq_open_account",
        "get_transactions",
    ]
    scenarios = []

    if not ground_scenarios[competency]:
        return scenarios

    for scenario in ground_scenarios[competency].keys():

        if "straight bussin" in scenario:
            return scenarios

        if (
            not target_scenarios.get(competency)
            or scenario not in target_scenarios[competency].keys()
        ):
            scenarios.append(
                create_scenario(
                    competency,
                    scenario,
                    ground_scenarios[competency],
                    target_scenarios,
                    finie_to_fi_map,
                )
            )
        else:
            scenarios.append(
                merge_scenarios(
                    scenario,
                    ground_scenarios[competency],
                    target_scenarios[competency],
                    scenario,
                )
            )

    if not products:
        return scenarios

    if competency in product_list:
        products_lower = [p.lower() for p in products[competency]]
        for scenario in target_scenarios[competency].keys():
            if scenario.lower().strip() in products_lower:
                scenarios.append(
                    create_product_scenario(
                        competency,
                        scenario,
                        target_scenarios[competency],
                        False,
                    )
                )
                # removes scenario, anything that remains should
                # have a new special product created
                products[competency].remove(scenario)

        # loop through and add remaining products as new scenarios
        for remaining_scenario in products[competency]:
            scenarios.append(
                create_product_scenario(competency, remaining_scenario, {}, True)
            )

    scenarios[1:] = sorted(scenarios[1:], key=lambda s: s["name"])
    return scenarios


def process_competency(
    competency_name,
    target_competencies,
    ground_competencies,
    products,
    ground_scenarios,
    target_scenarios,
    finie_to_fi_map,
):
    """
    Process a competency
    """
    competency = {}
    competency["name"] = competency_name
    competency["type"] = ground_competencies[competency_name]["type"]
    competency["disabled"] = (
        target_competencies[competency_name]["disabled"]
        if competency_name in target_competencies
        else True
    )
    competency["scenarios"] = process_scenario_list(
        competency_name,
        ground_scenarios,
        target_scenarios,
        products,
        finie_to_fi_map,
    )
    competency["templates"] = ground_competencies[competency_name]["templates"]
    return competency


def make_lower(data: dict):
    if not data:
        return {}

    for competency in data["competencies"]:
        for scenario in competency["scenarios"]:
            scenario["name"] = scenario["name"].lower()

    return data


def process_variable_rows(variables):
    """
    Processes the rows of the CSV for the Variables sheet into a list of variables
    """
    v = []
    for row in variables:

        value: str = row["Value"]

        if value in ["TRUE", "FALSE"]:
            value = value.lower()

        v.append(
            {
                "name": row["Name"],
                "value": value,
            }
        )

    return {"variables": v}


def get_institution_products(variables: dict):
    v = variables.get("variables", [])
    for variable in v:
        if variable.get("name", "") == "institution_products":
            return variable.get("value", "")

    return ""


def create_product_names(products: list):
    product_names = {
        "faq_describe_accounts": [],
        "faq_open_account": [],
        "get_transactions": [],
    }
    for product in products:
        target = get_special_products_competencies(product)

        for i in target:
            case_names = []
            cases: dict = i["cases"]
            for _, v in cases.items():
                case_names.append(v.strip().lower())

            product_names[i["competency"]].append(": ".join(case_names))

    return product_names


def get_product_names(variables):
    institution_products = get_institution_products(variables)
    institution_products = institution_products.split(",")
    product_names = create_product_names(institution_products)
    return product_names
