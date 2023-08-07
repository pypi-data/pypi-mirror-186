def product_description(competency, names):
    """return scenario description and example query for a specified product"""
    description = ""
    example_queries = ""
    if competency == "get_transactions":
        description = f"User inquires about {names[-1]} account transactions."
        example_queries = f"What are the transactions on my {names[-1]} account?"
    elif competency == "faq_open_account":
        description = f"User requests to open about a {names[-1]} account."
        example_queries = f"Can I open a {names[-1]} account?"
    else:
        account_type = names[0].split("_")
        if account_type[-1] in ["rates", "fees"]:
            description = f"User inquires about {names[-1]} account {account_type[-1]}."
            example_queries = f"What are the {names[-1]} account {account_type[-1]}?"
        else:
            description = f"User inquires about {names[-1]} accounts."
            example_queries = f"Tell me about {names[-1]} accounts."
    return (description, example_queries)


def build_describe_accounts_cases(names):
    return [
        {"name": "subtype", "values": [f"{names[0]}"]},
        {"name": "type_of_account", "values": [f"{names[1]}"]},
    ]


def build_get_transaction_cases(names):
    return [
        {"name": "trxn_spnd_hist_filter", "values": [f"{names[0]}"]},
    ]


def build_faq_open_account_cases(names):
    return [{"name": "type_of_account", "values": [f"{names[0]}"]}]


def get_special_products_competencies(product):
    return [
        {
            "competency": "faq_describe_accounts",
            "cases": {
                "subtype": "faq_describe_accounts",
                "type_of_account": product,
            },
        },
        {
            "competency": "faq_describe_accounts",
            "cases": {
                "subtype": "faq_product_rates",
                "type_of_account": product,
            },
        },
        {
            "competency": "faq_describe_accounts",
            "cases": {
                "subtype": "faq_product_fees",
                "type_of_account": product,
            },
        },
        {
            "competency": "faq_open_account",
            "cases": {"type_of_account": product},
        },
        {
            "competency": "get_transactions",
            "cases": {"trxn_spnd_hist_filter": product},
        },
    ]


def build_cases(competency, names: list):
    if competency == "faq_describe_accounts":
        return build_describe_accounts_cases(names)
    if competency == "get_transactions":
        return build_get_transaction_cases(names)
    if competency == "faq_open_account":
        return build_faq_open_account_cases(names)


def get_product_scenario(competency, description, example_queries, names):
    return {
        "name": ": ".join(names),
        "description": description,
        "example_queries": [example_queries],
        "disabled": True,
        "tags": ["new_scenario"],
        "cases": build_cases(competency, names),
        "response_elements": [
            {
                "type": "paragraph",
                "speakable_fallback_behavior": "default",
                "values": [
                    {
                        "value": f"Thanks for asking! We offer a variety of {names[-1]} accounts to fit your needs. Click below to learn more.",
                        "display": "",
                        "speakable": "",
                    }
                ],
            },
            {
                "type": "url",
                "speakable_fallback_behavior": "default",
                "values": [
                    {
                        "value": f'https://example.com/{names[-1].lower().replace(" ", "-")}',
                        "display": f"{names[-1]}",
                        "speakable": "",
                    }
                ],
            },
        ],
    }
