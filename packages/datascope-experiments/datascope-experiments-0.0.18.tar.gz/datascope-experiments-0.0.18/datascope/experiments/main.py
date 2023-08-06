import argparse
import os

from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set

from .base import run, run_scenario, report
from .datasets import preload_datasets
from .scenarios import (
    Scenario,
    Report,
    Backend,
    DEFAULT_RESULTS_PATH,
    DEFAULT_RESULTS_SCENARIOS_PATH,
    DEFAULT_STUDY_PATH,
    DEFAULT_BACKEND,
    DEFAULT_SLURM_JOBTIME,
    DEFAULT_SLURM_JOBMEMORY,
)


def make_type_parser(target: Optional[type]) -> Callable[[str], Any]:
    def parser(source: str) -> Any:
        if target is None:
            return source
        result: Any = source
        if issubclass(target, bool):
            result = result in ["True", "true", "T", "t", "Yes", "yes", "y"]
        elif issubclass(target, int):
            result = int(result)
        elif issubclass(target, float):
            result = float(result)
        elif issubclass(target, Enum):
            result = target(result)
        return result

    return parser


def add_dynamic_arguments(
    parser: argparse.ArgumentParser,
    attribute_domains: Dict[str, Set],
    attribute_types: Dict[str, Optional[type]],
    attribute_defaults: Dict[str, Optional[Any]],
    attribute_helpstrings: Dict[str, Optional[str]],
    attribute_isiterable: Dict[str, bool],
    single_instance: bool = False,
) -> None:
    for name in attribute_domains:
        default = attribute_defaults[name]
        domain: Optional[List] = [x.value if isinstance(x, Enum) else x for x in attribute_domains[name]]
        if domain == [None]:
            domain = None
        helpstring = attribute_helpstrings[name] or ("Scenario " + name + ".")
        if default is None:
            helpstring += " Default: [all]" if not single_instance else ""
        else:
            helpstring += " Default: %s" % str(default)
        parser.add_argument(
            "--%s" % name.replace("_", "-"),
            help=helpstring,
            type=make_type_parser(attribute_types[name]),
            choices=domain,
            nargs=(1 if single_instance else "+") if attribute_isiterable[name] else None,  # type: ignore
        )


# Courtesy of http://stackoverflow.com/a/10551190 with env-var retrieval fixed
class EnvDefault(argparse.Action):
    """An argparse action class that auto-sets missing default values from env
    vars. Defaults to requiring the argument."""

    def __init__(self, envvar: Optional[str], required: bool = True, default: Optional[Any] = None, **kwargs):
        if default is not None and envvar is not None:
            if envvar in os.environ:
                default = os.environ[envvar]
        if required and default is not None:
            required = False
        super(EnvDefault, self).__init__(default=default, required=required, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


def env_default(envvar: Optional[str]):
    def wrapper(**kwargs):
        return EnvDefault(envvar, **kwargs)

    return wrapper


def main():

    parser = argparse.ArgumentParser(
        prog="experiments", description="This command allows interaction with datascope experiments."
    )
    subparsers = parser.add_subparsers(title="commands", help="Available commands.", dest="command")

    parser_run = subparsers.add_parser("run")

    parser_run.add_argument(
        "-o",
        "--output-path",
        type=str,
        action=env_default("EXPERIMENTS_RESULTS_PATH"),
        default=DEFAULT_RESULTS_PATH,
        help="Path where the data is stored. Default: '%s'" % DEFAULT_RESULTS_PATH,
    )

    parser_run.add_argument(
        "-b",
        "--backend",
        type=Backend,
        choices=[x.value for x in list(Backend)],
        action=env_default("EXPERIMENTS_BACKEND"),
        default=DEFAULT_BACKEND,
        help="The backend to run against. Default: '%s'" % str(DEFAULT_BACKEND.value),
    )

    parser_run.add_argument(
        "--no-save",
        action="store_true",
        help="Prevent saving the study.",
    )

    parser_run.add_argument(
        "--ray-address",
        type=str,
        action=env_default("EXPERIMENTS_RAY_ADDRESS"),
        required=False,
        default=None,
        help="Address of the ray server. If omitted, a new server ad-hoc will be created.",
    )

    parser_run.add_argument(
        "--ray-numprocs",
        type=int,
        action=env_default("EXPERIMENTS_RAY_NUMPROCS"),
        required=False,
        default=None,
        help="Number of ray processes to start if running in parallel. Defaults to the number of cores.",
    )

    parser_run.add_argument(
        "--slurm-jobtime",
        type=str,
        action=env_default("EXPERIMENTS_SLURM_JOBTIME"),
        default=DEFAULT_SLURM_JOBTIME,
        help="Runtime requirement for each slurm job (if slurm is used as backend).",
    )

    parser_run.add_argument(
        "--slurm-jobmemory",
        type=str,
        action=env_default("EXPERIMENTS_SLURM_JOBMEMORY"),
        default=DEFAULT_SLURM_JOBMEMORY,
        help="Memory requirements for each slurm job (if slurm is used as backend).",
    )

    parser_run.add_argument(
        "--slurm-constraint",
        type=str,
        action=env_default("EXPERIMENTS_SLURM_CONSTRAINT"),
        required=False,
        default=None,
        help="Constraint to be specified for selecting slurm cluster nodes (if slurm is used as backend).",
    )

    parser_run.add_argument(
        "--slurm-maxjobs",
        type=int,
        action=env_default("EXPERIMENTS_SLURM_MAXJOBS"),
        required=False,
        default=None,
        help="Maimum number of slurm jobs that will be running at any given time (if slurm is used as backend).",
    )

    parser_run.add_argument(
        "--eventstream-host-ip",
        type=str,
        action=env_default("EVENTSTREAM_HOST_IP"),
        required=False,
        default=None,
        help="The IP address to use for receiving events from distributed jobs (if slurm is used as backend).",
    )

    parser_run.add_argument(
        "--eventstream-host-port",
        type=int,
        action=env_default("EVENTSTREAM_HOST_PORT"),
        required=False,
        default=None,
        help="The port to use for receiving events from distributed jobs (if slurm is used as backend).",
    )

    # Build arguments from scenario attributes.
    add_dynamic_arguments(
        parser=parser_run,
        attribute_domains=Scenario.attribute_domains,
        attribute_types=Scenario.attribute_types,
        attribute_defaults=Scenario.attribute_defaults,
        attribute_helpstrings=Scenario.attribute_helpstrings,
        attribute_isiterable=Scenario.attribute_isiterable,
        single_instance=False,
    )

    parser_run_scenario = subparsers.add_parser("run-scenario")

    parser_run_scenario.add_argument(
        "-o",
        "--output-path",
        type=str,
        default=DEFAULT_RESULTS_SCENARIOS_PATH,
        help="Path where the data is stored. Default: '%s'" % DEFAULT_RESULTS_SCENARIOS_PATH,
    )

    parser_run_scenario.add_argument(
        "--no-save",
        action="store_true",
        help="Prevent saving the scenario.",
    )

    parser_run_scenario.add_argument(
        "-e",
        "--event-server",
        type=str,
        default=None,
        help="Address of the event server. If specified, logging and progress events will be streamed to it.",
    )

    add_dynamic_arguments(
        parser=parser_run_scenario,
        attribute_domains=Scenario.attribute_domains,
        attribute_types=Scenario.attribute_types,
        attribute_defaults=Scenario.attribute_defaults,
        attribute_helpstrings=Scenario.attribute_helpstrings,
        attribute_isiterable=Scenario.attribute_isiterable,
        single_instance=True,
    )

    parser_report = subparsers.add_parser("report")

    parser_report.add_argument(
        "-s",
        "--study-path",
        type=str,
        default=DEFAULT_STUDY_PATH,
        help="Path where the target study is stored. Default: '%s'" % DEFAULT_STUDY_PATH,
    )

    parser_report.add_argument(
        "-o",
        "--output-path",
        type=str,
        help="Path where the reports are stored. Default: same as study path",
    )

    parser_report.add_argument(
        "-g",
        "--groupby",
        type=str,
        nargs="+",
        help="List of columns used to group results.",
    )

    parser_report.add_argument(
        "--saveonly",
        type=str,
        nargs="+",
        help="List of result attributes to save.",
    )

    parser_report.add_argument(
        "--use-subdirs",
        action="store_true",
        help="Store report artifacts in a hierarchy of subdirectories based on groupby keys.",
    )

    parser_report.add_argument(
        "--no-multiprocessing",
        action="store_true",
        help="Do not use multiprocessing for generating reports. Run in single threaded mode.",
    )

    # Build arguments from report attributes.
    add_dynamic_arguments(
        parser=parser_report,
        attribute_domains=Report.attribute_domains,
        attribute_types=Report.attribute_types,
        attribute_defaults=Report.attribute_defaults,
        attribute_helpstrings=Report.attribute_helpstrings,
        attribute_isiterable=Report.attribute_isiterable,
        single_instance=False,
    )

    # print(Report.attribute_domains)

    subparsers.add_parser("dataload")

    args = parser.parse_args()
    kwargs = vars(args)

    if args.command == "run":
        run(**kwargs)
    elif args.command == "run-scenario":
        run_scenario(**kwargs)
    elif args.command == "report":
        report(**kwargs)
    elif args.command == "dataload":
        preload_datasets(**kwargs)
    else:
        parser.print_help()
