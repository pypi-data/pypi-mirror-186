# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Common test asserts
"""

from typing import Iterable

import allure
from adcm_client.objects import BaseAPIObject

from adcm_pytest_plugin.exceptions.bundles import BundleError
from adcm_pytest_plugin.exceptions.infrastructure import InfrastructureProblem


def assert_state(obj: BaseAPIObject, state):
    """
    Asserts object state to be equal to 'state' argument

    >>> some_obj = lambda: None
    >>> some_obj.reread = lambda: None
    >>> some_obj.state = "installed"
    >>> assert_state(some_obj, "installed") is None
    True
    >>> assert_state(some_obj, "started") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    AssertionError:
    """
    obj.reread()
    name = _get_name(obj)
    with allure.step(f"Assert state of {obj.__class__.__name__} '{name}' to be equal to '{state}'"):
        assert obj.state == state, f"Object '{name}' have unexpected state - '{obj.state}'. " f"Expected - '{state}'"


@allure.step("Assert action result to be equal to {status}")
def assert_action_result(result: str, status: str, name="", additional_message=""):
    """
    Asserts action result to be equal to 'status' argument

    >>> assert_action_result("200", "200") is None
    True
    >>> assert_action_result("200", "400")
    Traceback (most recent call last):
    ...
    AssertionError: Action  finished execution with unexpected result - '200'. Expected - '400'
    >>> assert_action_result("200", "400", "some_action")
    Traceback (most recent call last):
    ...
    AssertionError: Action some_action finished execution with unexpected result - '200'. Expected - '400'
    >>> assert_action_result("200", "500", additional_message="My custom message")
    Traceback (most recent call last):
    ...
    AssertionError: Action  finished execution with unexpected result - '200'. Expected - '500'
    My custom message
    """
    message = f"Action {name} finished execution with unexpected result - '{result}'. " f"Expected - '{status}'"
    if additional_message:
        message += f"\n{additional_message}"
        InfrastructureProblem.raise_if_suitable(message)
        BundleError.raise_if_suitable(message)
    assert result == status, message


def assert_multi_state(obj: BaseAPIObject, multi_state: Iterable[str]) -> None:
    """
    Asserts object's multi-state to be equal to `multi_state` argument,
    both are converted to `set`.

    >>> some_obj = lambda: None
    >>> some_obj.reread = lambda: None
    >>> some_obj.multi_state = ["prepared", "initialized"]
    >>> assert_multi_state(some_obj, ["prepared", "initialized"]) is None
    True
    >>> assert_multi_state(some_obj, ["started"]) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    AssertionError:
    >>> assert_multi_state(some_obj, ["prepared", "initialized", "started"]) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    AssertionError:
    """
    obj.reread()
    expected_state = set(multi_state)
    name = _get_name(obj)
    with allure.step(f"Assert multi-state of {obj.__class__.__name__} '{name}' to be equal to '{expected_state}'"):
        actual_state = set(obj.multi_state)
        assert (
            actual_state == expected_state
        ), f"Object has incorrect multi-state.\nExpected: {expected_state}\nActual: {actual_state}"


def _get_name(obj: BaseAPIObject) -> str:
    if hasattr(obj, "name"):
        return obj.name
    if hasattr(obj, "fqdn"):
        return obj.fqdn
    return repr(obj)
