#  Copyright 2020 Rikai Authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os

from typing import Optional
from pyspark.sql import SparkSession

from liga.logging import logger
from liga.spark import _liga_assembly_jar

from ligavision.__version__ import version


def liga_init_spark(
        conf: Optional[dict] = None,
        app_name: str = "Liga",
        scala_version: str = "2.12",
        num_cores: int = 2,
) -> SparkSession:
    import sys

    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    # Avoid reused session polluting configs
    active_session = SparkSession.getActiveSession()
    if active_session and conf:
        for k, v in conf.items():
            if str(active_session.conf.get(k)) != str(v):
                print(
                    f"active session: want {v} for {k}"
                    f" but got {active_session.conf.get(k)},"
                    f" will restart session"
                )
                active_session.stop()
                break

    builder = (
        SparkSession.builder.appName(app_name)
        .config(
            "spark.sql.extensions",
            "ai.eto.rikai.sql.spark.RikaiSparkSessionExtensions",
        )
        .config(
            "spark.driver.extraJavaOptions",
            "-Dio.netty.tryReflectionSetAccessible=true",
        )
        .config(
            "spark.executor.extraJavaOptions",
            "-Dio.netty.tryReflectionSetAccessible=true",
        )
    )
    conf = conf or {}
    for k, v in conf.items():
        if k == "spark.jars":
            logger.info(v)
        builder = builder.config(k, v)
    session = builder.master(f"local[{num_cores}]").getOrCreate()
    return session


def _liga_vision_jar(vision_type: str, jar_type: str, scala_version: str) -> str:
    name = f"liga-{vision_type}-assembly_{scala_version}"
    url = "https://github.com/liga-ai/liga-vision/releases/download"
    github_jar = f"{url}/v{version}/{name}-{version}.jar"
    if jar_type == "github":
        if "dev" in version:
            logger.warning(
                "Jar type `github` is for stable release, "
                "it may fail when version contains dev"
            )
        return github_jar
    elif jar_type == "local":
        project_path = os.environ.get("ROOTDIR")
        if project_path:
            local_jar_path = f"{project_path}/out/{vision_type}/{scala_version}/assembly.dest/out.jar"
            if os.path.exists(local_jar_path):
                return local_jar_path
            else:
                raise ValueError("Please run `sbt clean assembly` first")
        else:
            logger.warning(
                "Jar type `local` is for developing purpose, fallback to Jar"
                " type `github` because no project root is specified"
            )
            return github_jar
    else:
        raise ValueError(f"Invalid jar_type ({jar_type})!")


def init_session(jar_type="github", scala_version: str = "2.12"):
    liga_uri = _liga_assembly_jar("github", scala_version)
    liga_image_uri = _liga_vision_jar("image", jar_type, scala_version)
    conf = dict(
        [
            (
                "spark.jars",
                ",".join([liga_uri,liga_image_uri])
            )
        ]
    )
    return liga_init_spark(conf=conf)
