import json
import os

from scribe_updater.changelog import ChangeLog
from scribe_updater.utils import (
    get_competencies,
    get_product_names,
    get_scenarios,
    process_competency,
    process_variable_rows,
)


class Updater:
    def __init__(
        self, ground, target, variables, output_file_path, ground_to_target_map
    ):
        self.ground = ground
        self.target = target
        self.variables = variables
        self.target_scenarios = {}
        self.ground_scenarios = {}
        self.target_competencies = {}
        self.ground_competencies = {}
        self.products = {}
        self.output = {}
        self.output_file_path = output_file_path
        self.ground_to_target_map = ground_to_target_map

    def set_ground_scenarios(self):
        """
        Set scenarios from the ground truth
        """
        self.ground_scenarios = get_scenarios(self.ground)

    def set_target_scenarios(self):
        """
        Set scenarios from the input ground truth (ex. Landmark Ground Truth)
        """
        self.target_scenarios = get_scenarios(self.target)

    def set_ground_competencies(self):
        """
        Set competencies from the ground truth
        """
        self.ground_competencies = get_competencies(self.ground)

    def set_target_competencies(self):
        """
        Set competencies from the input ground truth (ex. Landmark Ground Truth)
        """
        self.target_competencies = get_competencies(self.target)

    def set_product(self):
        """
        Set the institution products for the individual fi
        """
        if not self.variables:
            return

        v = process_variable_rows(self.variables)
        products = get_product_names(v)
        self.products = products

    def init(self):
        """
        Initialize all the data from the ground truths both input and master
        """
        self.set_ground_competencies()
        self.set_ground_scenarios()
        self.set_target_competencies()
        self.set_target_scenarios()
        self.set_product()

    def prep_output_pba(self):
        """
        preparation function for pba output
        """
        self.output = {
            "auth": "pre",
            "competencies": [],
            "disabled_response": self.target["disabled_response"],
            "outofscope_response": self.target["outofscope_response"],
        }

    def prep_output_vba(self):
        """
        preparation function for vba output
        """
        self.output = {"auth": "post", "competencies": []}

    def update(self):
        """
        Main logic is performed here to create an output file.
        The newly generated output file can be used as the new
        master ground truth
        """
        self.init()
        self.output["competencies"] = [
            process_competency(
                competency,
                self.target_competencies,
                self.ground_competencies,
                self.products,
                self.ground_scenarios,
                self.target_scenarios,
                self.ground_to_target_map,
            )
            for competency in self.ground_competencies.keys()
        ]

    def output_to_json(self):
        """
        Takes the output formed from the update functions and prints the results as json
        """
        if not os.path.isdir("results"):
            os.mkdir("results")

        with open("results/" + self.output_file_path, "w") as f:
            f.write(json.dumps(self.output, indent=4))

    def get_change_log(self):
        """
        Creates a change log that can be views in the terminal
        """
        change_log = ChangeLog(
            self.ground_scenarios,
            self.target_scenarios,
            self.ground_competencies,
            self.target_competencies,
            self.output,
            self.ground_to_target_map,
        )
        log = change_log.create_change_log()
        change_log.write_change_log_to_file()
        change_log.display_change_log()
        return log
