"""
Main evaluation CLI

"""
from click import command, option
from microcosm.loaders import load_from_dict
from microcosm.object_graph import ObjectGraph

from microcosm_sagemaker.app_hooks import create_evaluate_app
from microcosm_sagemaker.commands.options import input_artifact_option, input_data_option
from microcosm_sagemaker.input_data import InputData


@command()
@input_data_option()
@input_artifact_option()
@option(
    "--testing/--no-testing",
    default=False,
    help="Whether the training is for testing purposes"
)
def main(input_data, input_artifact, testing):
    graph = create_evaluate_app(
        extra_loader=load_from_dict(
            root_input_artifact_path=input_artifact.path,
            testing=testing,
        ),
    )

    run_evaluate(
        graph=graph,
        input_data=input_data,
    )


def run_evaluate(
    graph: ObjectGraph,
    input_data: InputData,
) -> None:

    graph.experiment_metrics.init()

    graph.active_evaluation(graph.active_bundle, input_data)


def run_evaluate_on_test(
    graph: ObjectGraph,
    input_data: InputData,
) -> None:

    graph.experiment_metrics.init()

    results = graph.test_evaluation(graph.active_bundle, input_data)

    return results
