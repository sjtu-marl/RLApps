import argparse
import logging
import os

import rlapps
from rlapps.algos.p2sro.p2sro_manager import P2SROManagerWithServer, P2SROManager
from rlapps.apps.psro.general_psro_eval import launch_evals
from rlapps.apps.scenarios.catalog import scenario_catalog
from rlapps.apps.scenarios.psro_scenario import PSROScenario
from rlapps.apps.scenarios.ray_setup import init_ray_for_scenario
from rlapps.apps import GRL_SEED
from rlapps.apps.psro.exploitability_psro_logger import ExploitabilityP2SROManagerLogger
from rlapps.utils.common import datetime_str, ensure_dir
from rlapps.utils.port_listings import establish_new_server_port_for_service
from rlapps.apps.psro.approx_exploitability_psro_logger import (
    ApproxExploitabilityP2SROManagerLogger,
)


def launch_manager(
    scenario: PSROScenario,
    psro_port: int,
    eval_port: int,
    block: bool = True,
    include_evals: bool = True,
) -> P2SROManagerWithServer:
    if not isinstance(scenario, PSROScenario):
        raise TypeError(
            f"Only instances of {PSROScenario} can be used here. {scenario.name} is a {type(scenario)}."
        )

    ray_head_address = init_ray_for_scenario(
        scenario=scenario, head_address=None, logging_level=logging.INFO
    )

    log_dir = os.path.join(
        os.path.dirname(rlapps.__file__),
        "data",
        scenario.name,
        f"manager_{datetime_str()}",
    )

    name_file_path = os.path.join(log_dir, "scenario.name.txt")
    ensure_dir(name_file_path)
    with open(name_file_path, "w+") as name_file:
        name_file.write(scenario.name)

    if scenario.calc_exploitability_for_openspiel_env:

        def get_manager_logger(_manager: P2SROManager):
            return ExploitabilityP2SROManagerLogger(
                p2sro_manger=_manager, log_dir=_manager.log_dir, scenario=scenario
            )

    else:

        def get_manager_logger(_manager: P2SROManager):
            return ApproxExploitabilityP2SROManagerLogger(
                p2sro_manger=_manager, log_dir=_manager.log_dir, scenario=scenario
            )

    manager = P2SROManagerWithServer(
        port=psro_port,
        eval_dispatcher_port=eval_port,
        n_players=2,
        is_two_player_symmetric_zero_sum=scenario.single_agent_symmetric_game,
        do_external_payoff_evals_for_new_fixed_policies=True,
        games_per_external_payoff_eval=scenario.games_per_payoff_eval,
        payoff_table_exponential_average_coeff=scenario.p2sro_payoff_table_exponential_avg_coeff,
        log_dir=log_dir,
        manager_metadata={"ray_head_address": ray_head_address},
        get_manager_logger=get_manager_logger,
    )
    print(
        "Launched P2SRO Manager with server. ray_head_address={}".format(
            ray_head_address
        )
    )

    if include_evals:
        launch_evals(
            scenario_name=scenario.name,
            block=False,
            ray_head_address=ray_head_address,
            eval_dispatcher_port=eval_port,
            eval_dispatcher_host="localhost",
        )
        print(f"Launched evals")

    if block:
        manager.wait_for_server_termination()

    return manager


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", type=str)
    parser.add_argument("--psro_port", type=int, required=False, default=None)
    parser.add_argument("--eval_port", type=int, required=False, default=None)
    commandline_args = parser.parse_args()

    scenario_name = commandline_args.scenario
    scenario: PSROScenario = scenario_catalog.get(scenario_name=scenario_name)

    psro_port = commandline_args.psro_port
    if psro_port is None:
        psro_port = establish_new_server_port_for_service(
            service_name=f"seed_{GRL_SEED}_{scenario.name}"
        )

    eval_port = commandline_args.eval_port
    if eval_port is None:
        eval_port = establish_new_server_port_for_service(
            service_name=f"seed_{GRL_SEED}_{scenario.name}_evals"
        )

    launch_manager(scenario=scenario, psro_port=psro_port, eval_port=eval_port)
