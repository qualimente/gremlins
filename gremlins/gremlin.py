#!/usr/bin/env python
#
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import time
from gremlins import faults
from gremlins.profiles import hbase
import signal
import logging
import sys

logging.basicConfig(level=logging.INFO)

def run_profile(profile):
  for trigger in profile:
    trigger.start()

  logging.info("Started profile")

  for trigger in profile:
    trigger.stop()
    trigger.join()


def main(argv):
  run_profile(hbase.profile)

if __name__ == "__main__":
  main(sys.argv)


