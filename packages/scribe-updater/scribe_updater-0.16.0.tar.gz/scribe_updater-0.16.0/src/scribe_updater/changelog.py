import json
import os


class ChangeLog:
    def __init__(
        self,
        ground_scenarios,
        target_scenarios,
        ground_competencies,
        target_competencies,
        output,
        ground_to_target_map,
    ):
        self.ground_scenarios = ground_scenarios
        self.ground_competencies = ground_competencies
        self.target_competencies = target_competencies
        self.target_scenarios = target_scenarios
        self.output = output
        self.change_log = {"added": [], "removed": [], "changed": []}
        self.ground_to_target_map = ground_to_target_map

    def log_competency_added(self, competency, num_scenarios):
        self.change_log["added"].append(
            "{} was added with {} new scenarios".format(competency, num_scenarios)
        )

    def log_scenario_added(self, competency, scenario):
        self.change_log["added"].append(
            "In {} the scenario {} was added".format(competency, scenario)
        )

    def log_competency_removed(self, competency, num_scenarios):
        self.change_log["removed"].append(
            "{} was removed along with {} scenarios".format(competency, num_scenarios)
        )

    def log_scenario_removed(self, competency, scenario):
        self.change_log["removed"].append(
            "In {} the scenario {} was removed".format(competency, scenario)
        )

    def log_competency_changed(self, competency, field):
        self.change_log["changed"].append(
            "In the {} competency changes were made to the {} field".format(
                competency, field
            )
        )

    def log_scenario_changed(self, competency, scenario, field):
        if field == "mapped":
            old_competency = self.ground_to_target_map[
                competency + "-*-" + scenario
            ].split("-*-")[0]
            old_scenario = self.ground_to_target_map[
                competency + "-*-" + scenario
            ].split("-*-")[1]
            self.change_log["changed"].append(
                "The {} scenario in the {} competency from the last version was moved to the {} scenario in the {} competency in the new version.".format(
                    old_scenario, old_competency, scenario, competency
                )
            )
        else:
            self.change_log["changed"].append(
                "In the {} competency: changes were made in the {} scenario to the {} field".format(
                    competency, scenario, field
                )
            )

    def log_template_change(self):
        self.change_log["changed"].append("A change was made to the template field")

    def check_for_removed_competencies_scenarios(self):
        for competency in self.target_scenarios:
            base_mapped = [
                value
                for value in [
                    self.ground_to_target_map[key]
                    for key in self.ground_to_target_map
                    if competency in key
                ]
                if "base" in value
            ]
            if (
                competency not in self.ground_scenarios
                and not base_mapped
                and competency not in ["disabled", "out_of_scope"]
            ):
                self.log_competency_removed(
                    competency, len(self.target_scenarios[competency])
                )
            else:
                for scenario in self.target_scenarios[competency]:
                    target_mapped = [
                        value
                        for value in self.ground_to_target_map.values()
                        if competency in value and scenario in value
                    ]
                    if (
                        scenario not in self.ground_scenarios.get(competency, [])
                        and not target_mapped
                        and competency not in ["disabled", "out_of_scope"]
                    ):
                        self.log_scenario_removed(competency, scenario)

    def check_for_added_competencies_scenarios(self):
        for competency in self.ground_scenarios:
            if competency not in self.target_scenarios:
                self.log_competency_added(
                    competency, len(self.ground_scenarios[competency])
                )
            else:
                for scenario in self.ground_scenarios[competency]:
                    output_key = competency + "-*-" + scenario
                    if (
                        scenario not in self.target_scenarios[competency]
                        and output_key not in self.ground_to_target_map.keys()
                    ):
                        self.log_scenario_added(competency, scenario)

    def check_for_changed_competencies_scenarios(self):
        # old_competencies = [
        #     key.split("-*-")[0]
        #     for key in self.ground_to_target_map.values()
        #     if "base" in key
        # ]
        for competency in self.output["competencies"]:
            if competency["name"] in self.target_scenarios:
                self.check_competency(
                    competency, self.target_competencies[competency["name"]]
                )
                if not competency["scenarios"]:
                    return
                for scenario in competency["scenarios"]:
                    output_key = competency["name"] + "-*-" + scenario["name"]
                    competency_scenario = self.ground_to_target_map.get(
                        output_key, ""
                    ).split("-*-")
                    target_mapped = (
                        len(competency_scenario) == 2
                        and competency_scenario[0] in self.target_scenarios
                        and competency_scenario[1]
                        in self.target_scenarios[competency_scenario[0]]
                    )
                    if self.target_scenarios.get(
                        competency["name"]
                    ) and self.target_scenarios[competency["name"]].get(
                        scenario["name"]
                    ):
                        self.check_scenario(
                            competency["name"],
                            scenario,
                            self.target_scenarios[competency["name"]][scenario["name"]],
                        )
                    elif target_mapped:
                        self.log_scenario_changed(
                            competency["name"], scenario["name"], "mapped"
                        )
            elif [
                value
                for value in [
                    self.ground_to_target_map[key]
                    for key in self.ground_to_target_map
                    if competency["name"] in key
                ]
                if "base" in value
            ]:
                for scenario in competency["scenarios"]:
                    output_key = competency["name"] + "-*-" + scenario["name"]
                    competency_scenario = self.ground_to_target_map.get(
                        output_key, ""
                    ).split("-*-")
                    target_mapped = (
                        len(competency_scenario) == 2
                        and competency_scenario[0] in self.target_scenarios
                        and competency_scenario[1]
                        in self.target_scenarios[competency_scenario[0]]
                    )
                    if target_mapped:
                        self.log_scenario_changed(
                            competency["name"], scenario["name"], "mapped"
                        )

    def check_competency(self, competency, target_competency):
        field_names = ["disabled"]
        # field_names = [
        # "type",
        # "disabled",
        # "templates"
        # ]
        for i in field_names:
            if competency[i] != target_competency[i]:
                self.log_competency_changed(competency["name"], i)

    def check_scenario(self, competency_name, output_scenario, target_scenario):
        field_names = ["disabled", "response_elements"]
        # field_names = [
        #   "description",
        #   "example_queries",
        #   "disabled",
        #   "tags",
        #   "cases",
        #   "response_elements"
        # ]
        for i in field_names:
            if output_scenario[i] != target_scenario[i]:
                self.log_scenario_changed(competency_name, output_scenario["name"], i)

    def check_for_removed_added_competencies_scenarios(self):
        self.check_for_removed_competencies_scenarios()
        self.check_for_added_competencies_scenarios()
        self.check_for_changed_competencies_scenarios()

    def create_change_log(self):
        self.check_for_removed_added_competencies_scenarios()
        return self.change_log

    def display_change_log(self):
        for i in self.change_log.keys():
            print("-- {} -- ".format(i.upper()))
            for vals in self.change_log[i]:
                print("-- {}".format(vals))

    def write_change_log_to_file(self):
        if not os.path.isdir("results"):
            os.mkdir("results")

        with open("results/diff_log.json", "w") as f:
            f.write(json.dumps(self.change_log, indent=4))
