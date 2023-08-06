from __future__ import annotations

import os
from typing import TYPE_CHECKING, Mapping, Optional, Tuple, Union

from great_expectations.util import get_context

if TYPE_CHECKING:
    from great_expectations.alias_types import PathStr

from great_expectations.data_context.data_context.abstract_data_context import (
    AbstractDataContext,
)
from great_expectations.data_context.types.base import DataContextConfig, GXCloudConfig


def BaseDataContext(
    project_config: Union[DataContextConfig, Mapping],
    context_root_dir: Optional[PathStr] = None,
    runtime_environment: Optional[dict] = None,
    cloud_mode: bool = False,
    cloud_config: Optional[GXCloudConfig] = None,
    # Deprecated as of 0.15.37
    ge_cloud_mode: bool = False,
    ge_cloud_config: Optional[GXCloudConfig] = None,
) -> AbstractDataContext:
    """
        This class implements most of the functionality of DataContext, with a few exceptions.

        1. BaseDataContext does not attempt to keep its project_config in sync with a file on disc.
        2. BaseDataContext doesn't attempt to "guess" paths or objects types. Instead, that logic is pushed
            into DataContext class.

        Together, these changes make BaseDataContext class more testable.

    --ge-feature-maturity-info--

        id: os_linux
        title: OS - Linux
        icon:
        short_description:
        description:
        how_to_guide_url:
        maturity: Production
        maturity_details:
            api_stability: N/A
            implementation_completeness: N/A
            unit_test_coverage: Complete
            integration_infrastructure_test_coverage: Complete
            documentation_completeness: Complete
            bug_risk: Low

        id: os_macos
        title: OS - MacOS
        icon:
        short_description:
        description:
        how_to_guide_url:
        maturity: Production
        maturity_details:
            api_stability: N/A
            implementation_completeness: N/A
            unit_test_coverage: Complete (local only)
            integration_infrastructure_test_coverage: Complete (local only)
            documentation_completeness: Complete
            bug_risk: Low

        id: os_windows
        title: OS - Windows
        icon:
        short_description:
        description:
        how_to_guide_url:
        maturity: Beta
        maturity_details:
            api_stability: N/A
            implementation_completeness: N/A
            unit_test_coverage: Minimal
            integration_infrastructure_test_coverage: Minimal
            documentation_completeness: Complete
            bug_risk: Moderate
    ------------------------------------------------------------
        id: workflow_create_edit_expectations_cli_scaffold
        title: Create and Edit Expectations - suite scaffold
        icon:
        short_description: Creating a new Expectation Suite using suite scaffold
        description: Creating Expectation Suites through an interactive development loop using suite scaffold
        how_to_guide_url: https://docs.greatexpectations.io/en/latest/how_to_guides/creating_and_editing_expectations/how_to_automatically_create_a_new_expectation_suite.html
        maturity: Experimental (expect exciting changes to Profiler capability)
        maturity_details:
            api_stability: N/A
            implementation_completeness: N/A
            unit_test_coverage: N/A
            integration_infrastructure_test_coverage: Partial
            documentation_completeness: Complete
            bug_risk: Low

        id: workflow_create_edit_expectations_cli_edit
        title: Create and Edit Expectations - CLI
        icon:
        short_description: Creating a new Expectation Suite using the CLI
        description: Creating a Expectation Suite great_expectations suite new command
        how_to_guide_url: https://docs.greatexpectations.io/en/latest/how_to_guides/creating_and_editing_expectations/how_to_create_a_new_expectation_suite_using_the_cli.html
        maturity: Experimental (expect exciting changes to Profiler and Suite Renderer capability)
        maturity_details:
            api_stability: N/A
            implementation_completeness: N/A
            unit_test_coverage: N/A
            integration_infrastructure_test_coverage: Partial
            documentation_completeness: Complete
            bug_risk: Low

        id: workflow_create_edit_expectations_json_schema
        title: Create and Edit Expectations - Json schema
        icon:
        short_description: Creating a new Expectation Suite from a json schema file
        description: Creating a new Expectation Suite using JsonSchemaProfiler function and json schema file
        how_to_guide_url: https://docs.greatexpectations.io/en/latest/how_to_guides/creating_and_editing_expectations/how_to_create_a_suite_from_a_json_schema_file.html
        maturity: Experimental (expect exciting changes to Profiler capability)
        maturity_details:
            api_stability: N/A
            implementation_completeness: N/A
            unit_test_coverage: N/A
            integration_infrastructure_test_coverage: Partial
            documentation_completeness: Complete
            bug_risk: Low

    --ge-feature-maturity-info--
    """
    # Chetan - 20221208 - not formally deprecating these values until a future date
    cloud_mode, cloud_config = _resolve_cloud_args(
        cloud_mode=cloud_mode,
        cloud_config=cloud_config,
        ge_cloud_mode=ge_cloud_mode,
        ge_cloud_config=ge_cloud_config,
    )

    project_data_context_config: DataContextConfig = (
        AbstractDataContext.get_or_create_data_context_config(project_config)
    )

    if context_root_dir is not None:
        context_root_dir = os.path.abspath(context_root_dir)
    # initialize runtime_environment as empty dict if None
    runtime_environment = runtime_environment or {}

    cloud_base_url: Optional[str] = None
    cloud_access_token: Optional[str] = None
    cloud_organization_id: Optional[str] = None
    if cloud_config:
        cloud_base_url = cloud_config.base_url
        cloud_access_token = cloud_config.access_token
        cloud_organization_id = cloud_config.organization_id

    return get_context(
        project_config=project_data_context_config,
        context_root_dir=context_root_dir,
        runtime_environment=runtime_environment,
        cloud_base_url=cloud_base_url,
        cloud_access_token=cloud_access_token,
        cloud_organization_id=cloud_organization_id,
        cloud_mode=cloud_mode,
    )


def _resolve_cloud_args(
    cloud_mode: bool = False,
    cloud_config: Optional[GXCloudConfig] = None,
    # <GX_RENAME> Deprecated as of 0.15.37
    ge_cloud_mode: bool = False,
    ge_cloud_config: Optional[GXCloudConfig] = None,
) -> Tuple[bool, Optional[GXCloudConfig]]:
    cloud_mode = True if cloud_mode or ge_cloud_mode else False
    cloud_config = cloud_config if cloud_config is not None else ge_cloud_config
    return cloud_mode, cloud_config
