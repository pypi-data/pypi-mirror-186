import traceback
from typing import Union
import argparse
import pathlib
import balder
from junit_xml import TestCase, TestSuite, to_xml_report_string
from balder.exceptions import BalderException
from _balder.testresult import ResultState
from _balder.balder_session import BalderSession
from _balder.executor.executor_tree import ExecutorTree
from _balder.executor.testcase_executor import TestcaseExecutor


class JunitPlugin(balder.BalderPlugin):

    def __init__(self, session: BalderSession):
        super().__init__(session=session)

    def addoption(self, argument_parser: argparse.ArgumentParser):
        argument_parser.add_argument('--junit-file', help="creates a junit result file at given path", default=None)

    def create_test_case(self, cur_test_case_executor: TestcaseExecutor) -> TestCase:
        class_name = cur_test_case_executor.parent_executor.parent_executor.parent_executor.\
            base_setup_class.__class__.__name__
        test_case = TestCase(cur_test_case_executor.base_testcase_callable.__qualname__, classname=class_name,
                             elapsed_sec=cur_test_case_executor.execution_time_sec)
        exception = cur_test_case_executor.construct_result.exception
        exception = exception if exception is not None \
            else cur_test_case_executor.body_result.exception
        exception = exception if exception is not None \
            else cur_test_case_executor.teardown_result.exception

        if cur_test_case_executor.executor_result in [ResultState.ERROR, ResultState.FAILURE]:
            if isinstance(exception, BalderException):
                test_case.add_error_info(
                    str(exception), ''.join(traceback.format_exception(exception)),
                    error_type=exception.__class__.__name__)
            else:
                test_case.add_failure_info(
                    str(exception), ''.join(traceback.format_exception(exception)),
                    failure_type=exception.__class__.__name__)

        elif cur_test_case_executor.executor_result == ResultState.SUCCESS:
            # do nothing
            pass
        else:
            test_case.add_skipped_info(f'test was skipped (executor result: {cur_test_case_executor.executor_result})')
        return test_case

    def session_finished(self, executor_tree: Union[ExecutorTree, None]):
        filepath = pathlib.Path(self.balder_session.parsed_args.junit_file)
        if executor_tree is not None and filepath is not None:
            all_test_suites = []
            for cur_setup_executor in executor_tree.setup_executors:
                for cur_scenario_executor in cur_setup_executor.scenario_executors:
                    for cur_variation_executor in cur_scenario_executor.variation_executors:
                        all_testcases = []
                        for cur_test_case_executor in cur_variation_executor.testcase_executors:
                            test_case = self.create_test_case(cur_test_case_executor)
                            all_testcases.append(test_case)

                        mapping_str = "|".join(
                            [f"{cur_scenario_dev.__name__}:{cur_setup_dev.__name__}"
                             for cur_scenario_dev, cur_setup_dev in cur_variation_executor.base_device_mapping.items()])
                        suite_name = f"{cur_scenario_executor.base_scenario_class.__class__.__qualname__}:" \
                                     f"{cur_setup_executor.base_setup_class.__class__.__qualname__}<{mapping_str}>"
                        properties = {
                            'scenario': cur_scenario_executor.base_scenario_class.__class__.__qualname__,
                            'setup': cur_setup_executor.base_setup_class.__class__.__qualname__,
                            'devices': {cur_scenario_dev.__name__: cur_setup_dev.__name__
                                        for cur_scenario_dev, cur_setup_dev in
                                        cur_variation_executor.base_device_mapping.items()}
                        }
                        all_test_suites.append(TestSuite(suite_name, test_cases=all_testcases, properties=properties))

            with open(filepath, 'w') as f:
                f.write(to_xml_report_string(all_test_suites))
