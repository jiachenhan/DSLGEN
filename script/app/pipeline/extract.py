from pathlib import Path

import utils.config
from interface.java.run_java_api import java_extract_pattern
from utils.config import PipelineConfig


def do_extract(dataset_path: Path):
    java_extract_pattern(5,
                         dataset_path,
                         PipelineConfig.pattern_ori_path,
                         PipelineConfig.pattern_info_path,
                         PipelineConfig.jar_path
                         )

def open_main():
    _config = utils.config.set_config("ppinfra")
    jar_path = _config.get("jar_path")

    dataset_name = "codeql_sampled_v1"
    checker = "Random_used_only_once"
    group = "1"
    case = "2"

    dataset_path = Path("") / dataset_name / checker / group / case

    pattern_ori_path = utils.config.get_pattern_base_path() / dataset_name / "ori" / checker / group / f"{case}.ser"
    pattern_info_path = utils.config.get_pattern_info_base_path() / dataset_name / "input" /  checker / group / f"{case}.json"
    java_extract_pattern(10, dataset_path, pattern_ori_path, pattern_info_path, jar_path)


if __name__ == '__main__':
    open_main()