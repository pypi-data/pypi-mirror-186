from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING, Dict

from aws_cdk import (
    aws_ecs as _ecs,
    aws_ec2 as _ec2,
    aws_route53 as _route53,
    aws_cloudwatch as _cloudwatch,
    aws_elasticloadbalancingv2 as _elb,
    Duration
)
from constructs import Construct
from aws_cdk_constructs.load_balancer import Alb

if TYPE_CHECKING:
    from .microservice import ECSMicroservice


class ECSCluster(Construct):
    """
        A CDK construct that creates an AWS ECS Cluster.
        This cluster is the placeholder where ECSMicroservices will be deployed to

    Args:
            scope (Construct): Parent construct

            id (str): the logical id of the newly created resource

            environment (str): The environment the cluster is being created in. This is used to determine the VPC to use

            environments_parameters (dict): The dictionary containing the references to CSI AWS environments. This will simplify the environment promotions and enable a parametric development of the infrastructures.

            domain_name (str): every cluster has associated a route53 hosted zone, where entries will be created to

            hosted_zone (aws_route53.IHostedZone): Route53 hosted zone where the cluster will create entries for the microservices

            app_name (str): The name of the application that will be deployed in the cluster,

            create_alb (Optional - bool): Whether to create the alb or not. Default is true
    """

    def __init__(
            self,
            scope: Construct,
            id: str,
            environments_parameters: Dict,
            app_name: str,
            environment: str,
            domain_name: str = "example.com",
            hosted_zone: Optional[_route53.IHostedZone] = None,
            create_alb:  Optional[bool] = True,
            create_alb_dns: Optional[bool] = False,
            track: Optional[bool] = False,
    ) -> None:
        self.id = id
        self.scope = scope
        self.environments_parameters = environments_parameters
        self.microservices: List[ECSMicroservice] = []
        self.hosted_zone = hosted_zone
        self.domain_name = domain_name
        self.app_name = app_name
        self.aws_account = self.environments_parameters["accounts"][environment.lower()]
        self.vpc = self._get_vpc()
        self.target_priority = 1
        self.environment = environment
        ssl_certificate_arn = self.aws_account.get('ssl_certificate_star_fao_org_arn')
        self.create_alb = create_alb

        super().__init__(scope, id)

        create_alb_dns = "True" if create_alb_dns else "False"

        if track:
            self.dashboard = self._get_dashboard()

        self._create_cluster()
        if(create_alb):
            self.alb = Alb(
                scope=self.scope,
                id=f"{self.app_name}-alb",
                app_name=self.app_name,
                environment=environment,
                environments_parameters=self.environments_parameters,
                ssl_certificate_arn=ssl_certificate_arn,
                vpc=self.vpc,
                access_log_bucket_name='fao-elb-logs',
                will_create_tg=False,
                traffic_port="443",
                create_dns=create_alb_dns
            )
        else:
            self.alb = None

    def _get_vpc(self) -> _ec2.IVpc:
        return _ec2.Vpc.from_lookup(
            self.scope, self.id + "VPC", vpc_id=self.aws_account.get("vpc")
        )

    def _create_cluster(self) -> None:
        self.cluster = _ecs.Cluster(scope=self.scope, id=self.id+"_ecs", vpc=self.vpc, container_insights=True)

    def register_ms(self, microservice: ECSMicroservice) -> None:
        """Adds a ECSMicroservice instance to the list of hosted services in the cluster"""
        self.microservices.append(microservice)

    def _get_dashboard(self) -> _cloudwatch.Dashboard:
        return self.scope.node.try_find_child(f"{self.app_name}-dashboard") or self._create_dashboard()

    def _create_dashboard(self) -> _cloudwatch.Dashboard:
        path = '_'.join(self.node.path.split('/')[:-1])
        return _cloudwatch.Dashboard(
            self.scope,
            f"{self.app_name}-{path}-dashboard",
            dashboard_name=f"{self.app_name}-{path}",
            end="end",
            period_override=_cloudwatch.PeriodOverride.AUTO,
            start="start",
        )

    def render_widgets(self) -> None:
        path = '_'.join(self.node.path.split('/')[:-1])
        self.dashboard = self._get_dashboard()

        self.dashboard.add_widgets(
            _cloudwatch.TextWidget(markdown=f"# {self.app_name} {path}", width=24)
        )

        http_codes_200 = []
        http_codes_300 = []
        http_codes_400 = []
        http_codes_500 = []
        alb_response_time = []
        cpu = []
        memory = []
        task_count = []
        for ms in self.microservices:
            alb_response_time.append(
                ms.target_group.metric_target_response_time(label=ms.id)
            )
            http_codes_200.append(
                ms.target_group.metric_http_code_target(
                    code=_elb.HttpCodeTarget.TARGET_2XX_COUNT, statistic="Avg",
                    period=Duration.minutes(1), label=f"2xx {ms.id}"
                )
            )
            http_codes_300.append(
                ms.target_group.metric_http_code_target(
                    code=_elb.HttpCodeTarget.TARGET_3XX_COUNT, statistic="Avg",
                    period=Duration.minutes(1), label=f"{ms.id}"
                )
            )
            http_codes_400.append(
                ms.target_group.metric_http_code_target(
                    code=_elb.HttpCodeTarget.TARGET_4XX_COUNT, statistic="Avg",
                    period=Duration.minutes(1), label=f"{ms.id}"
                )
            )
            http_codes_500.append(
                ms.target_group.metric_http_code_target(
                    code=_elb.HttpCodeTarget.TARGET_5XX_COUNT, statistic="Avg",
                    period=Duration.minutes(1), label=f"{ms.id}"
                )
            )
            task_count.append(
                _cloudwatch.Metric(
                    metric_name="RunningTaskCount",
                    namespace="ECS/ContainerInsights",
                    dimensions_map={
                        "ClusterName": self.cluster.cluster_name,
                        "ServiceName": ms.service.service_name,
                    },
                    period=Duration.minutes(1),
                    statistic="Average",
                    label=ms.id
                )
            )
            ms_id_normalized = str(ms.id).replace('-', '')
            cpu.append(_cloudwatch.MathExpression(
                label=ms.id,
                expression=f"100*(used_{ms_id_normalized}/reserved_{ms_id_normalized})",
                using_metrics={
                    f"used_{ms_id_normalized}": _cloudwatch.Metric(
                        metric_name="CpuUtilized",
                        namespace="ECS/ContainerInsights",
                        dimensions_map={
                            "ClusterName": self.cluster.cluster_name,
                            "ServiceName": ms.service.service_name
                        },
                        period=Duration.minutes(5),
                        statistic="Average",
                        label=f"{ms.id} used"
                    ),
                    f"reserved_{ms_id_normalized}": _cloudwatch.Metric(
                        metric_name="CpuReserved",
                        namespace="ECS/ContainerInsights",
                        dimensions_map={
                            "ClusterName": self.cluster.cluster_name,
                            "ServiceName": ms.service.service_name
                        },
                        period=Duration.minutes(5),
                        statistic="Average",
                        label=f"{ms.id} reserved"
                    )
                }
            )
            )

            memory.append(
                _cloudwatch.MathExpression(
                    label=ms.id,
                    expression=f"100*(used_{ms_id_normalized}/reserved_{ms_id_normalized})",
                    using_metrics={
                        f"used_{ms_id_normalized}": _cloudwatch.Metric(
                            metric_name="MemoryUtilized",
                            namespace="ECS/ContainerInsights",
                            dimensions_map={
                                "ClusterName": self.cluster.cluster_name,
                                "ServiceName": ms.service.service_name
                            },
                            period=Duration.minutes(5),
                            statistic="Average",
                            label=f"{ms.id} used"
                        ),
                        f"reserved_{ms_id_normalized}": _cloudwatch.Metric(
                            metric_name="MemoryReserved",
                            namespace="ECS/ContainerInsights",
                            dimensions_map={
                                "ClusterName": self.cluster.cluster_name,
                                "ServiceName": ms.service.service_name
                            },
                            period=Duration.minutes(5),
                            statistic="Average",
                            label=f"{ms.id} reserved"
                        )
                    }
                )
            )

        self.dashboard.add_widgets(
            _cloudwatch.GraphWidget(
                title="ALB response times",
                left=alb_response_time,
                width=24
            )
        )

        self.dashboard.add_widgets(
            _cloudwatch.GraphWidget(
                title="2xx count",
                left=http_codes_200,
                width=12
            ),
            _cloudwatch.GraphWidget(
                title="3xx count",
                left=http_codes_300,
                width=12
            ),
            _cloudwatch.GraphWidget(
                title="4xx count",
                left=http_codes_400,
                width=12
            ),
            _cloudwatch.GraphWidget(
                title="5xx count",
                left=http_codes_500,
                width=12
            ),
            _cloudwatch.GraphWidget(
                title="Task running count",
                left=task_count,
                width=24
            ),
            _cloudwatch.GraphWidget(
                title="CPU used/reserved %",
                left=cpu,
                width=24
            ),
            _cloudwatch.GraphWidget(
                title="Memory used/reserved %",
                left=memory,
                width=24
            )
        )