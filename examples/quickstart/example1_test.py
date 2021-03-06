# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""Example Checkers test run that checks 1 + 1 = 2."""

from checkers.python import checkers
from checkers.python.integrations.hamcrest import AssertThat
from checkers.python.integrations.hamcrest import EqualTo
from checkers.python.integrations.hamcrest import Is
from checkers.python.integrations.pyunit import pyunit


@checkers.Test
def TestOnePlusOneEqualsTwo():
  print '1 + 1 = 2'
  AssertThat(1 + 1, Is(EqualTo(2)))


def CreateTestRun():
  """Test run that will execute the defined test."""
  test_run = checkers.TestRun()
  test_run.LoadTestCase(TestOnePlusOneEqualsTwo)
  return test_run


if __name__ == '__main__':
  pyunit.main(CreateTestRun())
