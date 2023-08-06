'''
# Amazon Textract IDP CDK Constructs

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

# Context

This CDK Construct can be used as Step Function task and call Textract in Asynchonous mode for DetectText and AnalyzeDocument APIs.

For samples on usage, look at [Amazon Textact IDP CDK Stack Samples](https://github.com/aws-samples/amazon-textract-idp-cdk-stack-samples)

## Input

Expects a Manifest JSON at 'Payload'.
Manifest description: https://pypi.org/project/schadem-tidp-manifest/

Example call in Python

```python
        textract_async_task = t_async.TextractGenericAsyncSfnTask(
            self,
            "textract-async-task",
            s3_output_bucket=s3_output_bucket,
            s3_temp_output_prefix=s3_temp_output_prefix,
            integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
            lambda_log_level="DEBUG",
            timeout=Duration.hours(24),
            input=sfn.TaskInput.from_object({
                "Token":
                sfn.JsonPath.task_token,
                "ExecutionId":
                sfn.JsonPath.string_at('$$.Execution.Id'),
                "Payload":
                sfn.JsonPath.entire_payload,
            }),
            result_path="$.textract_result")
```

## Output

Adds the "TextractTempOutputJsonPath" to the Step Function ResultPath. At this location the Textract output is stored as individual JSON files. Use the CDK Construct schadem-cdk-construct-sfn-textract-output-config-to-json to combine them to one single JSON file.

example with ResultPath = textract_result (like configured above):

```
"textract_result": {
    "TextractTempOutputJsonPath": "s3://schademcdkstackpaystuban-schademcdkidpstackpaystu-bt0j5wq0zftu/textract-temp-output/c6e141e8f4e93f68321c17dcbc6bf7291d0c8cdaeb4869758604c387ce91a480"
  }
```

## Spacy Classification

Expect a Spacy textcat model at the root of the directory. Call the script <TO_INSERT) to copy a public one which classifies Paystub and W2.

aws s3 cp s3://amazon-textract-public-content/constructs/en_textcat_demo-0.0.0.tar.gz .
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_ec2
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.aws_rds
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import aws_cdk.aws_stepfunctions
import aws_cdk.aws_stepfunctions_tasks
import constructs


class CSVToAuroraTask(
    aws_cdk.aws_stepfunctions.TaskStateBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.CSVToAuroraTask",
):
    '''CSVToAuroraTask is a demo construct to show import into a serverless Aurora DB.

    At the moment it also creates the Aurora Serverless RDS DB, initializes a table structure the matches the output of the GenerateCSV construct.
    The Step Functions flow expect a pointer to a CSV at "csv_output_location"."TextractOutputCSVPath" and uses that to execute a batch insert statement command.

    Example::

       csv_to_aurora_task = tcdk.CSVToAuroraTask(
         self,
         "CsvToAurora",
         vpc=vpc,
         integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
         lambda_log_level="DEBUG",
         timeout=Duration.hours(24),
         input=sfn.TaskInput.from_object({
           "Token":
           sfn.JsonPath.task_token,
           "ExecutionId":
           sfn.JsonPath.string_at('$$.Execution.Id'),
           "Payload":
           sfn.JsonPath.entire_payload
         }),
         result_path="$.textract_result")

    Input: "csv_output_location"."TextractOutputCSVPath"
    Output: CSV in Aurora Serverless DB, table name 'textractcsvimport"
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        aurora_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        csv_to_aurora_backoff_rate: typing.Optional[jsii.Number] = None,
        csv_to_aurora_interval: typing.Optional[jsii.Number] = None,
        csv_to_aurora_max_retries: typing.Optional[jsii.Number] = None,
        db_cluster: typing.Optional[aws_cdk.aws_rds.IServerlessCluster] = None,
        enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory: typing.Optional[jsii.Number] = None,
        lambda_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param aurora_security_group: auroraSecurity Group for Cluster.
        :param csv_to_aurora_backoff_rate: default is 1.1.
        :param csv_to_aurora_interval: default is 1.
        :param csv_to_aurora_max_retries: 
        :param db_cluster: DBCluster to import into.
        :param enable_cloud_watch_metrics_and_dashboard: enable CloudWatch Metrics and Dashboard. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param lambda_memory: Memory allocated to Lambda function, default 512.
        :param lambda_security_group: lambdaSecurity Group for Cluster.
        :param lambda_timeout: Lambda Function Timeout in seconds, default 300.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param textract_state_machine_timeout_minutes: 
        :param vpc: VPC to install the database into, optional if dbCluster is passed in.
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                aurora_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                csv_to_aurora_backoff_rate: typing.Optional[jsii.Number] = None,
                csv_to_aurora_interval: typing.Optional[jsii.Number] = None,
                csv_to_aurora_max_retries: typing.Optional[jsii.Number] = None,
                db_cluster: typing.Optional[aws_cdk.aws_rds.IServerlessCluster] = None,
                enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory: typing.Optional[jsii.Number] = None,
                lambda_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CSVToAuroraTaskProps(
            associate_with_parent=associate_with_parent,
            aurora_security_group=aurora_security_group,
            csv_to_aurora_backoff_rate=csv_to_aurora_backoff_rate,
            csv_to_aurora_interval=csv_to_aurora_interval,
            csv_to_aurora_max_retries=csv_to_aurora_max_retries,
            db_cluster=db_cluster,
            enable_cloud_watch_metrics_and_dashboard=enable_cloud_watch_metrics_and_dashboard,
            input=input,
            lambda_log_level=lambda_log_level,
            lambda_memory=lambda_memory,
            lambda_security_group=lambda_security_group,
            lambda_timeout=lambda_timeout,
            name=name,
            textract_state_machine_timeout_minutes=textract_state_machine_timeout_minutes,
            vpc=vpc,
            comment=comment,
            heartbeat=heartbeat,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig]:
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], jsii.get(self, "taskPolicies"))

    @builtins.property
    @jsii.member(jsii_name="auroraSecurityGroup")
    def aurora_security_group(self) -> aws_cdk.aws_ec2.ISecurityGroup:
        return typing.cast(aws_cdk.aws_ec2.ISecurityGroup, jsii.get(self, "auroraSecurityGroup"))

    @aurora_security_group.setter
    def aurora_security_group(self, value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auroraSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="csvToAuroraFunction")
    def csv_to_aurora_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "csvToAuroraFunction"))

    @csv_to_aurora_function.setter
    def csv_to_aurora_function(self, value: aws_cdk.aws_lambda.IFunction) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvToAuroraFunction", value)

    @builtins.property
    @jsii.member(jsii_name="csvToAuroraLambdaLogGroup")
    def csv_to_aurora_lambda_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "csvToAuroraLambdaLogGroup"))

    @csv_to_aurora_lambda_log_group.setter
    def csv_to_aurora_lambda_log_group(self, value: aws_cdk.aws_logs.ILogGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_logs.ILogGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvToAuroraLambdaLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="dbCluster")
    def db_cluster(self) -> aws_cdk.aws_rds.IServerlessCluster:
        return typing.cast(aws_cdk.aws_rds.IServerlessCluster, jsii.get(self, "dbCluster"))

    @db_cluster.setter
    def db_cluster(self, value: aws_cdk.aws_rds.IServerlessCluster) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_rds.IServerlessCluster) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbCluster", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaSecurityGroup")
    def lambda_security_group(self) -> aws_cdk.aws_ec2.ISecurityGroup:
        return typing.cast(aws_cdk.aws_ec2.ISecurityGroup, jsii.get(self, "lambdaSecurityGroup"))

    @lambda_security_group.setter
    def lambda_security_group(self, value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.IStateMachine, jsii.get(self, "stateMachine"))

    @state_machine.setter
    def state_machine(self, value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachine", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="csvToAuroraNumberRowsInsertedMetric")
    def csv_to_aurora_number_rows_inserted_metric(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "csvToAuroraNumberRowsInsertedMetric"))

    @csv_to_aurora_number_rows_inserted_metric.setter
    def csv_to_aurora_number_rows_inserted_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvToAuroraNumberRowsInsertedMetric", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.CSVToAuroraTaskProps",
    jsii_struct_bases=[aws_cdk.aws_stepfunctions.TaskStateBaseProps],
    name_mapping={
        "comment": "comment",
        "heartbeat": "heartbeat",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "timeout": "timeout",
        "associate_with_parent": "associateWithParent",
        "aurora_security_group": "auroraSecurityGroup",
        "csv_to_aurora_backoff_rate": "csvToAuroraBackoffRate",
        "csv_to_aurora_interval": "csvToAuroraInterval",
        "csv_to_aurora_max_retries": "csvToAuroraMaxRetries",
        "db_cluster": "dbCluster",
        "enable_cloud_watch_metrics_and_dashboard": "enableCloudWatchMetricsAndDashboard",
        "input": "input",
        "lambda_log_level": "lambdaLogLevel",
        "lambda_memory": "lambdaMemory",
        "lambda_security_group": "lambdaSecurityGroup",
        "lambda_timeout": "lambdaTimeout",
        "name": "name",
        "textract_state_machine_timeout_minutes": "textractStateMachineTimeoutMinutes",
        "vpc": "vpc",
    },
)
class CSVToAuroraTaskProps(aws_cdk.aws_stepfunctions.TaskStateBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        aurora_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        csv_to_aurora_backoff_rate: typing.Optional[jsii.Number] = None,
        csv_to_aurora_interval: typing.Optional[jsii.Number] = None,
        csv_to_aurora_max_retries: typing.Optional[jsii.Number] = None,
        db_cluster: typing.Optional[aws_cdk.aws_rds.IServerlessCluster] = None,
        enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory: typing.Optional[jsii.Number] = None,
        lambda_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param aurora_security_group: auroraSecurity Group for Cluster.
        :param csv_to_aurora_backoff_rate: default is 1.1.
        :param csv_to_aurora_interval: default is 1.
        :param csv_to_aurora_max_retries: 
        :param db_cluster: DBCluster to import into.
        :param enable_cloud_watch_metrics_and_dashboard: enable CloudWatch Metrics and Dashboard. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param lambda_memory: Memory allocated to Lambda function, default 512.
        :param lambda_security_group: lambdaSecurity Group for Cluster.
        :param lambda_timeout: Lambda Function Timeout in seconds, default 300.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param textract_state_machine_timeout_minutes: 
        :param vpc: VPC to install the database into, optional if dbCluster is passed in.
        '''
        if __debug__:
            def stub(
                *,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                aurora_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                csv_to_aurora_backoff_rate: typing.Optional[jsii.Number] = None,
                csv_to_aurora_interval: typing.Optional[jsii.Number] = None,
                csv_to_aurora_max_retries: typing.Optional[jsii.Number] = None,
                db_cluster: typing.Optional[aws_cdk.aws_rds.IServerlessCluster] = None,
                enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory: typing.Optional[jsii.Number] = None,
                lambda_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument associate_with_parent", value=associate_with_parent, expected_type=type_hints["associate_with_parent"])
            check_type(argname="argument aurora_security_group", value=aurora_security_group, expected_type=type_hints["aurora_security_group"])
            check_type(argname="argument csv_to_aurora_backoff_rate", value=csv_to_aurora_backoff_rate, expected_type=type_hints["csv_to_aurora_backoff_rate"])
            check_type(argname="argument csv_to_aurora_interval", value=csv_to_aurora_interval, expected_type=type_hints["csv_to_aurora_interval"])
            check_type(argname="argument csv_to_aurora_max_retries", value=csv_to_aurora_max_retries, expected_type=type_hints["csv_to_aurora_max_retries"])
            check_type(argname="argument db_cluster", value=db_cluster, expected_type=type_hints["db_cluster"])
            check_type(argname="argument enable_cloud_watch_metrics_and_dashboard", value=enable_cloud_watch_metrics_and_dashboard, expected_type=type_hints["enable_cloud_watch_metrics_and_dashboard"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument lambda_memory", value=lambda_memory, expected_type=type_hints["lambda_memory"])
            check_type(argname="argument lambda_security_group", value=lambda_security_group, expected_type=type_hints["lambda_security_group"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument textract_state_machine_timeout_minutes", value=textract_state_machine_timeout_minutes, expected_type=type_hints["textract_state_machine_timeout_minutes"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if timeout is not None:
            self._values["timeout"] = timeout
        if associate_with_parent is not None:
            self._values["associate_with_parent"] = associate_with_parent
        if aurora_security_group is not None:
            self._values["aurora_security_group"] = aurora_security_group
        if csv_to_aurora_backoff_rate is not None:
            self._values["csv_to_aurora_backoff_rate"] = csv_to_aurora_backoff_rate
        if csv_to_aurora_interval is not None:
            self._values["csv_to_aurora_interval"] = csv_to_aurora_interval
        if csv_to_aurora_max_retries is not None:
            self._values["csv_to_aurora_max_retries"] = csv_to_aurora_max_retries
        if db_cluster is not None:
            self._values["db_cluster"] = db_cluster
        if enable_cloud_watch_metrics_and_dashboard is not None:
            self._values["enable_cloud_watch_metrics_and_dashboard"] = enable_cloud_watch_metrics_and_dashboard
        if input is not None:
            self._values["input"] = input
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if lambda_memory is not None:
            self._values["lambda_memory"] = lambda_memory
        if lambda_security_group is not None:
            self._values["lambda_security_group"] = lambda_security_group
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout
        if name is not None:
            self._values["name"] = name
        if textract_state_machine_timeout_minutes is not None:
            self._values["textract_state_machine_timeout_minutes"] = textract_state_machine_timeout_minutes
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the heartbeat.

        :default: - None
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns

        :default: IntegrationPattern.REQUEST_RESPONSE

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the state machine.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def associate_with_parent(self) -> typing.Optional[builtins.bool]:
        '''Pass the execution ID from the context object to the execution input.

        This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines.

        If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely.

        :default: - false

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html#nested-execution-startid
        '''
        result = self._values.get("associate_with_parent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def aurora_security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''auroraSecurity Group for Cluster.'''
        result = self._values.get("aurora_security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def csv_to_aurora_backoff_rate(self) -> typing.Optional[jsii.Number]:
        '''default is 1.1.'''
        result = self._values.get("csv_to_aurora_backoff_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def csv_to_aurora_interval(self) -> typing.Optional[jsii.Number]:
        '''default is 1.'''
        result = self._values.get("csv_to_aurora_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def csv_to_aurora_max_retries(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("csv_to_aurora_max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def db_cluster(self) -> typing.Optional[aws_cdk.aws_rds.IServerlessCluster]:
        '''DBCluster to import into.'''
        result = self._values.get("db_cluster")
        return typing.cast(typing.Optional[aws_cdk.aws_rds.IServerlessCluster], result)

    @builtins.property
    def enable_cloud_watch_metrics_and_dashboard(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''enable CloudWatch Metrics and Dashboard.

        :default: - false
        '''
        result = self._values.get("enable_cloud_watch_metrics_and_dashboard")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskInput]:
        '''The JSON input for the execution, same as that of StartExecution.

        :default: - The state input (JSON path '$')

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskInput], result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_memory(self) -> typing.Optional[jsii.Number]:
        '''Memory allocated to Lambda function, default 512.'''
        result = self._values.get("lambda_memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''lambdaSecurity Group for Cluster.'''
        result = self._values.get("lambda_security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        '''Lambda Function Timeout in seconds, default 300.'''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the execution, same as that of StartExecution.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def textract_state_machine_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("textract_state_machine_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''VPC to install the database into, optional if dbCluster is passed in.'''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CSVToAuroraTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendGenericSyncSfnTask(
    aws_cdk.aws_stepfunctions.TaskStateBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.ComprehendGenericSyncSfnTask",
):
    '''Calls a Comprehend Classification endpoint and parses the result, filters on > 50 % confidence and sets the highest confidence score classification.

    Input: "textract_result"."txt_output_location"
    Output:  { "documentType": "AWS_PAYSTUBS" } (example will be at "classification"."documentType")

    Example (Python::

         comprehend_sync_task = tcdk.ComprehendGenericSyncSfnTask(
             self,
             "Classification",
             comprehend_classifier_arn=
             '<your comprehend classifier arn>',
             integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
             lambda_log_level="DEBUG",
             timeout=Duration.hours(24),
             input=sfn.TaskInput.from_object({
                 "Token":
                 sfn.JsonPath.task_token,
                 "ExecutionId":
                 sfn.JsonPath.string_at('$$.Execution.Id'),
                 "Payload":
                 sfn.JsonPath.entire_payload,
             }),
             result_path="$.classification")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        comprehend_classifier_arn: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param comprehend_classifier_arn: 
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param lambda_memory: Memory allocated to Lambda function, default 512.
        :param lambda_timeout: Lambda Function Timeout in seconds, default 300.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param textract_state_machine_timeout_minutes: how long can we wait for the process (default is 48 hours (60*48=2880)).
        :param workflow_tracing_enabled: 
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                comprehend_classifier_arn: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ComprehendGenericSyncSfnTaskProps(
            comprehend_classifier_arn=comprehend_classifier_arn,
            associate_with_parent=associate_with_parent,
            input=input,
            lambda_log_level=lambda_log_level,
            lambda_memory=lambda_memory,
            lambda_timeout=lambda_timeout,
            name=name,
            textract_state_machine_timeout_minutes=textract_state_machine_timeout_minutes,
            workflow_tracing_enabled=workflow_tracing_enabled,
            comment=comment,
            heartbeat=heartbeat,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig]:
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], jsii.get(self, "taskPolicies"))

    @builtins.property
    @jsii.member(jsii_name="comprehendSyncCallFunction")
    def comprehend_sync_call_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "comprehendSyncCallFunction"))

    @comprehend_sync_call_function.setter
    def comprehend_sync_call_function(
        self,
        value: aws_cdk.aws_lambda.IFunction,
    ) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comprehendSyncCallFunction", value)

    @builtins.property
    @jsii.member(jsii_name="comprehendSyncLambdaLogGroup")
    def comprehend_sync_lambda_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "comprehendSyncLambdaLogGroup"))

    @comprehend_sync_lambda_log_group.setter
    def comprehend_sync_lambda_log_group(
        self,
        value: aws_cdk.aws_logs.ILogGroup,
    ) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_logs.ILogGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comprehendSyncLambdaLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="comprehendSyncSQS")
    def comprehend_sync_sqs(self) -> aws_cdk.aws_sqs.IQueue:
        return typing.cast(aws_cdk.aws_sqs.IQueue, jsii.get(self, "comprehendSyncSQS"))

    @comprehend_sync_sqs.setter
    def comprehend_sync_sqs(self, value: aws_cdk.aws_sqs.IQueue) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_sqs.IQueue) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comprehendSyncSQS", value)

    @builtins.property
    @jsii.member(jsii_name="putOnSQSLambdaLogGroup")
    def put_on_sqs_lambda_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "putOnSQSLambdaLogGroup"))

    @put_on_sqs_lambda_log_group.setter
    def put_on_sqs_lambda_log_group(self, value: aws_cdk.aws_logs.ILogGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_logs.ILogGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "putOnSQSLambdaLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.IStateMachine, jsii.get(self, "stateMachine"))

    @state_machine.setter
    def state_machine(self, value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachine", value)

    @builtins.property
    @jsii.member(jsii_name="textractPutOnSQSFunction")
    def textract_put_on_sqs_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "textractPutOnSQSFunction"))

    @textract_put_on_sqs_function.setter
    def textract_put_on_sqs_function(self, value: aws_cdk.aws_lambda.IFunction) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textractPutOnSQSFunction", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.ComprehendGenericSyncSfnTaskProps",
    jsii_struct_bases=[aws_cdk.aws_stepfunctions.TaskStateBaseProps],
    name_mapping={
        "comment": "comment",
        "heartbeat": "heartbeat",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "timeout": "timeout",
        "comprehend_classifier_arn": "comprehendClassifierArn",
        "associate_with_parent": "associateWithParent",
        "input": "input",
        "lambda_log_level": "lambdaLogLevel",
        "lambda_memory": "lambdaMemory",
        "lambda_timeout": "lambdaTimeout",
        "name": "name",
        "textract_state_machine_timeout_minutes": "textractStateMachineTimeoutMinutes",
        "workflow_tracing_enabled": "workflowTracingEnabled",
    },
)
class ComprehendGenericSyncSfnTaskProps(aws_cdk.aws_stepfunctions.TaskStateBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        comprehend_classifier_arn: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        :param comprehend_classifier_arn: 
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param lambda_memory: Memory allocated to Lambda function, default 512.
        :param lambda_timeout: Lambda Function Timeout in seconds, default 300.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param textract_state_machine_timeout_minutes: how long can we wait for the process (default is 48 hours (60*48=2880)).
        :param workflow_tracing_enabled: 
        '''
        if __debug__:
            def stub(
                *,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                comprehend_classifier_arn: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument comprehend_classifier_arn", value=comprehend_classifier_arn, expected_type=type_hints["comprehend_classifier_arn"])
            check_type(argname="argument associate_with_parent", value=associate_with_parent, expected_type=type_hints["associate_with_parent"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument lambda_memory", value=lambda_memory, expected_type=type_hints["lambda_memory"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument textract_state_machine_timeout_minutes", value=textract_state_machine_timeout_minutes, expected_type=type_hints["textract_state_machine_timeout_minutes"])
            check_type(argname="argument workflow_tracing_enabled", value=workflow_tracing_enabled, expected_type=type_hints["workflow_tracing_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "comprehend_classifier_arn": comprehend_classifier_arn,
        }
        if comment is not None:
            self._values["comment"] = comment
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if timeout is not None:
            self._values["timeout"] = timeout
        if associate_with_parent is not None:
            self._values["associate_with_parent"] = associate_with_parent
        if input is not None:
            self._values["input"] = input
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if lambda_memory is not None:
            self._values["lambda_memory"] = lambda_memory
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout
        if name is not None:
            self._values["name"] = name
        if textract_state_machine_timeout_minutes is not None:
            self._values["textract_state_machine_timeout_minutes"] = textract_state_machine_timeout_minutes
        if workflow_tracing_enabled is not None:
            self._values["workflow_tracing_enabled"] = workflow_tracing_enabled

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the heartbeat.

        :default: - None
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns

        :default: IntegrationPattern.REQUEST_RESPONSE

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the state machine.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def comprehend_classifier_arn(self) -> builtins.str:
        result = self._values.get("comprehend_classifier_arn")
        assert result is not None, "Required property 'comprehend_classifier_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_with_parent(self) -> typing.Optional[builtins.bool]:
        '''Pass the execution ID from the context object to the execution input.

        This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines.

        If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely.

        :default: - false

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html#nested-execution-startid
        '''
        result = self._values.get("associate_with_parent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskInput]:
        '''The JSON input for the execution, same as that of StartExecution.

        :default: - The state input (JSON path '$')

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskInput], result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_memory(self) -> typing.Optional[jsii.Number]:
        '''Memory allocated to Lambda function, default 512.'''
        result = self._values.get("lambda_memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        '''Lambda Function Timeout in seconds, default 300.'''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the execution, same as that of StartExecution.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def textract_state_machine_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''how long can we wait for the process (default is 48 hours (60*48=2880)).'''
        result = self._values.get("textract_state_machine_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def workflow_tracing_enabled(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("workflow_tracing_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendGenericSyncSfnTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DocumentSplitter(
    aws_cdk.aws_stepfunctions.StateMachineFragment,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.DocumentSplitter",
):
    '''This construct takes in a manifest definition with just the s3Path:.

    example s3Path:
    {"s3Path": "s3://bucketname/prefix/image.png"}

    then it generated single page versions of the multi-page file.
    For PDF the output are single PDF files, for TIFF the output are single TIFF files.

    Example (Python::
    '''

    def __init__(
        self,
        parent: constructs.Construct,
        id: builtins.str,
        *,
        s3_output_bucket: builtins.str,
        s3_output_prefix: builtins.str,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param parent: -
        :param id: -
        :param s3_output_bucket: Bucketname to output data to.
        :param s3_output_prefix: The prefix to use to output files to.
        :param lambda_log_level: Lambda log level.
        :param lambda_memory_mb: Lambda function memory configuration (may need to increase for larger documents).
        :param lambda_timeout: Lambda function timeout (may need to increase for larger documents).
        '''
        if __debug__:
            def stub(
                parent: constructs.Construct,
                id: builtins.str,
                *,
                s3_output_bucket: builtins.str,
                s3_output_prefix: builtins.str,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DocumentSplitterProps(
            s3_output_bucket=s3_output_bucket,
            s3_output_prefix=s3_output_prefix,
            lambda_log_level=lambda_log_level,
            lambda_memory_mb=lambda_memory_mb,
            lambda_timeout=lambda_timeout,
        )

        jsii.create(self.__class__, self, [parent, id, props])

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[aws_cdk.aws_stepfunctions.INextable]:
        '''The states to chain onto if this fragment is used.'''
        return typing.cast(typing.List[aws_cdk.aws_stepfunctions.INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> aws_cdk.aws_stepfunctions.State:
        '''The start state of this state machine fragment.'''
        return typing.cast(aws_cdk.aws_stepfunctions.State, jsii.get(self, "startState"))


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.DocumentSplitterProps",
    jsii_struct_bases=[],
    name_mapping={
        "s3_output_bucket": "s3OutputBucket",
        "s3_output_prefix": "s3OutputPrefix",
        "lambda_log_level": "lambdaLogLevel",
        "lambda_memory_mb": "lambdaMemoryMB",
        "lambda_timeout": "lambdaTimeout",
    },
)
class DocumentSplitterProps:
    def __init__(
        self,
        *,
        s3_output_bucket: builtins.str,
        s3_output_prefix: builtins.str,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param s3_output_bucket: Bucketname to output data to.
        :param s3_output_prefix: The prefix to use to output files to.
        :param lambda_log_level: Lambda log level.
        :param lambda_memory_mb: Lambda function memory configuration (may need to increase for larger documents).
        :param lambda_timeout: Lambda function timeout (may need to increase for larger documents).
        '''
        if __debug__:
            def stub(
                *,
                s3_output_bucket: builtins.str,
                s3_output_prefix: builtins.str,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_output_bucket", value=s3_output_bucket, expected_type=type_hints["s3_output_bucket"])
            check_type(argname="argument s3_output_prefix", value=s3_output_prefix, expected_type=type_hints["s3_output_prefix"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument lambda_memory_mb", value=lambda_memory_mb, expected_type=type_hints["lambda_memory_mb"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_output_bucket": s3_output_bucket,
            "s3_output_prefix": s3_output_prefix,
        }
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if lambda_memory_mb is not None:
            self._values["lambda_memory_mb"] = lambda_memory_mb
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout

    @builtins.property
    def s3_output_bucket(self) -> builtins.str:
        '''Bucketname to output data to.'''
        result = self._values.get("s3_output_bucket")
        assert result is not None, "Required property 's3_output_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_output_prefix(self) -> builtins.str:
        '''The prefix to use to output files to.'''
        result = self._values.get("s3_output_prefix")
        assert result is not None, "Required property 's3_output_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        '''Lambda log level.'''
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''Lambda function memory configuration (may need to increase for larger documents).'''
        result = self._values.get("lambda_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        '''Lambda function timeout (may need to increase for larger documents).'''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocumentSplitterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RDSAuroraServerless(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.RDSAuroraServerless",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc: VPC to install the database into.
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                vpc: aws_cdk.aws_ec2.IVpc,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RDSAuroraServerlessProps(vpc=vpc)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "RDSAuroraServerlessProps":
        return typing.cast("RDSAuroraServerlessProps", jsii.get(self, "props"))

    @builtins.property
    @jsii.member(jsii_name="auroraSecurityGroup")
    def aurora_security_group(self) -> aws_cdk.aws_ec2.ISecurityGroup:
        return typing.cast(aws_cdk.aws_ec2.ISecurityGroup, jsii.get(self, "auroraSecurityGroup"))

    @aurora_security_group.setter
    def aurora_security_group(self, value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auroraSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="dbCluster")
    def db_cluster(self) -> aws_cdk.aws_rds.IServerlessCluster:
        return typing.cast(aws_cdk.aws_rds.IServerlessCluster, jsii.get(self, "dbCluster"))

    @db_cluster.setter
    def db_cluster(self, value: aws_cdk.aws_rds.IServerlessCluster) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_rds.IServerlessCluster) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbCluster", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaSecurityGroup")
    def lambda_security_group(self) -> aws_cdk.aws_ec2.ISecurityGroup:
        return typing.cast(aws_cdk.aws_ec2.ISecurityGroup, jsii.get(self, "lambdaSecurityGroup"))

    @lambda_security_group.setter
    def lambda_security_group(self, value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_ec2.ISecurityGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaSecurityGroup", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.RDSAuroraServerlessProps",
    jsii_struct_bases=[],
    name_mapping={"vpc": "vpc"},
)
class RDSAuroraServerlessProps:
    def __init__(self, *, vpc: aws_cdk.aws_ec2.IVpc) -> None:
        '''
        :param vpc: VPC to install the database into.
        '''
        if __debug__:
            def stub(*, vpc: aws_cdk.aws_ec2.IVpc) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {
            "vpc": vpc,
        }

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''VPC to install the database into.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RDSAuroraServerlessProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpacySfnTask(
    aws_cdk.aws_stepfunctions.TaskStateBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.SpacySfnTask",
):
    '''Deploys a Lambda Container with a Spacy NLP model to call textcat.

    Input: "textract_result"."txt_output_location"
    Output:  { "documentType": "AWS_PAYSTUBS" } (example will be at "classification"."documentType")

    Example (Python::

         spacy_classification_task = tcdk.SpacySfnTask(
             self,
             "Classification",
             integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
             lambda_log_level="DEBUG",
             timeout=Duration.hours(24),
             input=sfn.TaskInput.from_object({
                 "Token":
                 sfn.JsonPath.task_token,
                 "ExecutionId":
                 sfn.JsonPath.string_at('$$.Execution.Id'),
                 "Payload":
                 sfn.JsonPath.entire_payload,
             }),
             result_path="$.classification")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        docker_image_function: typing.Optional[aws_cdk.aws_lambda.IFunction] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        spacy_image_ecr_repository: typing.Optional[builtins.str] = None,
        spacy_lambda_memory_size: typing.Optional[jsii.Number] = None,
        spacy_lambda_timeout: typing.Optional[jsii.Number] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param docker_image_function: Docker Container (to use in DockerImageCode.from_ecr() call).
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param spacy_image_ecr_repository: ECR Container URI for Spacy classification.
        :param spacy_lambda_memory_size: memorySize for Lambda function calling Spacy NLP, default is 4096 MB.
        :param spacy_lambda_timeout: timeout for Lambda function calling Spacy NLP, default is 900 seconds.
        :param textract_state_machine_timeout_minutes: how long can we wait for the process (default is 48 hours (60*48=2880)).
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                docker_image_function: typing.Optional[aws_cdk.aws_lambda.IFunction] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                spacy_image_ecr_repository: typing.Optional[builtins.str] = None,
                spacy_lambda_memory_size: typing.Optional[jsii.Number] = None,
                spacy_lambda_timeout: typing.Optional[jsii.Number] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SpacySfnTaskProps(
            associate_with_parent=associate_with_parent,
            docker_image_function=docker_image_function,
            input=input,
            lambda_log_level=lambda_log_level,
            name=name,
            spacy_image_ecr_repository=spacy_image_ecr_repository,
            spacy_lambda_memory_size=spacy_lambda_memory_size,
            spacy_lambda_timeout=spacy_lambda_timeout,
            textract_state_machine_timeout_minutes=textract_state_machine_timeout_minutes,
            comment=comment,
            heartbeat=heartbeat,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig]:
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], jsii.get(self, "taskPolicies"))

    @builtins.property
    @jsii.member(jsii_name="spacyCallFunction")
    def spacy_call_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "spacyCallFunction"))

    @spacy_call_function.setter
    def spacy_call_function(self, value: aws_cdk.aws_lambda.IFunction) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacyCallFunction", value)

    @builtins.property
    @jsii.member(jsii_name="spacySyncLambdaLogGroup")
    def spacy_sync_lambda_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "spacySyncLambdaLogGroup"))

    @spacy_sync_lambda_log_group.setter
    def spacy_sync_lambda_log_group(self, value: aws_cdk.aws_logs.ILogGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_logs.ILogGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacySyncLambdaLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.IStateMachine, jsii.get(self, "stateMachine"))

    @state_machine.setter
    def state_machine(self, value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachine", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.SpacySfnTaskProps",
    jsii_struct_bases=[aws_cdk.aws_stepfunctions.TaskStateBaseProps],
    name_mapping={
        "comment": "comment",
        "heartbeat": "heartbeat",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "timeout": "timeout",
        "associate_with_parent": "associateWithParent",
        "docker_image_function": "dockerImageFunction",
        "input": "input",
        "lambda_log_level": "lambdaLogLevel",
        "name": "name",
        "spacy_image_ecr_repository": "spacyImageEcrRepository",
        "spacy_lambda_memory_size": "spacyLambdaMemorySize",
        "spacy_lambda_timeout": "spacyLambdaTimeout",
        "textract_state_machine_timeout_minutes": "textractStateMachineTimeoutMinutes",
    },
)
class SpacySfnTaskProps(aws_cdk.aws_stepfunctions.TaskStateBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        docker_image_function: typing.Optional[aws_cdk.aws_lambda.IFunction] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        spacy_image_ecr_repository: typing.Optional[builtins.str] = None,
        spacy_lambda_memory_size: typing.Optional[jsii.Number] = None,
        spacy_lambda_timeout: typing.Optional[jsii.Number] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param docker_image_function: Docker Container (to use in DockerImageCode.from_ecr() call).
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param spacy_image_ecr_repository: ECR Container URI for Spacy classification.
        :param spacy_lambda_memory_size: memorySize for Lambda function calling Spacy NLP, default is 4096 MB.
        :param spacy_lambda_timeout: timeout for Lambda function calling Spacy NLP, default is 900 seconds.
        :param textract_state_machine_timeout_minutes: how long can we wait for the process (default is 48 hours (60*48=2880)).
        '''
        if __debug__:
            def stub(
                *,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                docker_image_function: typing.Optional[aws_cdk.aws_lambda.IFunction] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                spacy_image_ecr_repository: typing.Optional[builtins.str] = None,
                spacy_lambda_memory_size: typing.Optional[jsii.Number] = None,
                spacy_lambda_timeout: typing.Optional[jsii.Number] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument associate_with_parent", value=associate_with_parent, expected_type=type_hints["associate_with_parent"])
            check_type(argname="argument docker_image_function", value=docker_image_function, expected_type=type_hints["docker_image_function"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument spacy_image_ecr_repository", value=spacy_image_ecr_repository, expected_type=type_hints["spacy_image_ecr_repository"])
            check_type(argname="argument spacy_lambda_memory_size", value=spacy_lambda_memory_size, expected_type=type_hints["spacy_lambda_memory_size"])
            check_type(argname="argument spacy_lambda_timeout", value=spacy_lambda_timeout, expected_type=type_hints["spacy_lambda_timeout"])
            check_type(argname="argument textract_state_machine_timeout_minutes", value=textract_state_machine_timeout_minutes, expected_type=type_hints["textract_state_machine_timeout_minutes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if timeout is not None:
            self._values["timeout"] = timeout
        if associate_with_parent is not None:
            self._values["associate_with_parent"] = associate_with_parent
        if docker_image_function is not None:
            self._values["docker_image_function"] = docker_image_function
        if input is not None:
            self._values["input"] = input
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if name is not None:
            self._values["name"] = name
        if spacy_image_ecr_repository is not None:
            self._values["spacy_image_ecr_repository"] = spacy_image_ecr_repository
        if spacy_lambda_memory_size is not None:
            self._values["spacy_lambda_memory_size"] = spacy_lambda_memory_size
        if spacy_lambda_timeout is not None:
            self._values["spacy_lambda_timeout"] = spacy_lambda_timeout
        if textract_state_machine_timeout_minutes is not None:
            self._values["textract_state_machine_timeout_minutes"] = textract_state_machine_timeout_minutes

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the heartbeat.

        :default: - None
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns

        :default: IntegrationPattern.REQUEST_RESPONSE

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the state machine.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def associate_with_parent(self) -> typing.Optional[builtins.bool]:
        '''Pass the execution ID from the context object to the execution input.

        This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines.

        If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely.

        :default: - false

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html#nested-execution-startid
        '''
        result = self._values.get("associate_with_parent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def docker_image_function(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        '''Docker Container (to use in DockerImageCode.from_ecr() call).'''
        result = self._values.get("docker_image_function")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.IFunction], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskInput]:
        '''The JSON input for the execution, same as that of StartExecution.

        :default: - The state input (JSON path '$')

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskInput], result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        '''log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL.'''
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the execution, same as that of StartExecution.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spacy_image_ecr_repository(self) -> typing.Optional[builtins.str]:
        '''ECR Container URI for Spacy classification.'''
        result = self._values.get("spacy_image_ecr_repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spacy_lambda_memory_size(self) -> typing.Optional[jsii.Number]:
        '''memorySize for Lambda function calling Spacy NLP, default is 4096 MB.'''
        result = self._values.get("spacy_lambda_memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spacy_lambda_timeout(self) -> typing.Optional[jsii.Number]:
        '''timeout for Lambda function calling Spacy NLP, default is 900 seconds.'''
        result = self._values.get("spacy_lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def textract_state_machine_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''how long can we wait for the process (default is 48 hours (60*48=2880)).'''
        result = self._values.get("textract_state_machine_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpacySfnTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TextractA2ISfnTask(
    aws_cdk.aws_stepfunctions.TaskStateBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.TextractA2ISfnTask",
):
    '''Calls and A2I endpoint arn with a task_token and waits for the A2I job to finish in order to continue the workflow.

    Basic implementation

    Input: "Payload"."a2iInputPath"
    Output::

       {
             'humanLoopStatus': human_loop_status,
             'humanLoopResultPath': human_loop_result,
             'humanLoopCreationTime': human_loop_creation_time,
         }

    Example::

       textract_a2i_task = tcdk.TextractA2ISfnTask(
             self,
             "TextractA2I",
             a2i_flow_definition_arn=
             "arn:aws:sagemaker:us-east-1:913165245630:flow-definition/textract-classifiction",
             integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
             lambda_log_level="DEBUG",
             timeout=Duration.hours(24),
             input=sfn.TaskInput.from_object({
                 "Token":
                 sfn.JsonPath.task_token,
                 "ExecutionId":
                 sfn.JsonPath.string_at('$$.Execution.Id'),
                 "Payload":
                 sfn.JsonPath.entire_payload,
             }),
             result_path="$.a2i_result")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        a2i_flow_definition_arn: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        task_token_table_name: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param a2i_flow_definition_arn: 
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param task_token_table_name: 
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                a2i_flow_definition_arn: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                task_token_table_name: typing.Optional[builtins.str] = None,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TextractA2ISfnTaskProps(
            a2i_flow_definition_arn=a2i_flow_definition_arn,
            associate_with_parent=associate_with_parent,
            input=input,
            lambda_log_level=lambda_log_level,
            name=name,
            task_token_table_name=task_token_table_name,
            comment=comment,
            heartbeat=heartbeat,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig]:
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], jsii.get(self, "taskPolicies"))

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.IStateMachine, jsii.get(self, "stateMachine"))

    @state_machine.setter
    def state_machine(self, value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachine", value)

    @builtins.property
    @jsii.member(jsii_name="taskTokenTableName")
    def task_token_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskTokenTableName"))

    @task_token_table_name.setter
    def task_token_table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskTokenTableName", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.TextractA2ISfnTaskProps",
    jsii_struct_bases=[aws_cdk.aws_stepfunctions.TaskStateBaseProps],
    name_mapping={
        "comment": "comment",
        "heartbeat": "heartbeat",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "timeout": "timeout",
        "a2i_flow_definition_arn": "a2iFlowDefinitionARN",
        "associate_with_parent": "associateWithParent",
        "input": "input",
        "lambda_log_level": "lambdaLogLevel",
        "name": "name",
        "task_token_table_name": "taskTokenTableName",
    },
)
class TextractA2ISfnTaskProps(aws_cdk.aws_stepfunctions.TaskStateBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        a2i_flow_definition_arn: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        task_token_table_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        :param a2i_flow_definition_arn: 
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param task_token_table_name: 
        '''
        if __debug__:
            def stub(
                *,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                a2i_flow_definition_arn: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                task_token_table_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument a2i_flow_definition_arn", value=a2i_flow_definition_arn, expected_type=type_hints["a2i_flow_definition_arn"])
            check_type(argname="argument associate_with_parent", value=associate_with_parent, expected_type=type_hints["associate_with_parent"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument task_token_table_name", value=task_token_table_name, expected_type=type_hints["task_token_table_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "a2i_flow_definition_arn": a2i_flow_definition_arn,
        }
        if comment is not None:
            self._values["comment"] = comment
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if timeout is not None:
            self._values["timeout"] = timeout
        if associate_with_parent is not None:
            self._values["associate_with_parent"] = associate_with_parent
        if input is not None:
            self._values["input"] = input
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if name is not None:
            self._values["name"] = name
        if task_token_table_name is not None:
            self._values["task_token_table_name"] = task_token_table_name

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the heartbeat.

        :default: - None
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns

        :default: IntegrationPattern.REQUEST_RESPONSE

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the state machine.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def a2i_flow_definition_arn(self) -> builtins.str:
        result = self._values.get("a2i_flow_definition_arn")
        assert result is not None, "Required property 'a2i_flow_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_with_parent(self) -> typing.Optional[builtins.bool]:
        '''Pass the execution ID from the context object to the execution input.

        This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines.

        If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely.

        :default: - false

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html#nested-execution-startid
        '''
        result = self._values.get("associate_with_parent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskInput]:
        '''The JSON input for the execution, same as that of StartExecution.

        :default: - The state input (JSON path '$')

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskInput], result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the execution, same as that of StartExecution.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_token_table_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("task_token_table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextractA2ISfnTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TextractAsyncToJSON(
    aws_cdk.aws_stepfunctions.StateMachineFragment,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.TextractAsyncToJSON",
):
    '''combines the potentially paginated response from async Textract calls and stores as one combines JSON.

    This construct is not memory optimzed (yet) and will combine all JSON by loading them to memory.
    Large responses could exceed the memory potentially, the memory size is set to Lambda max.

    Reduce the memory size to your needs if your processing does not yield large responses to save Lamda cost.

    Input: "textract_result"."TextractTempOutputJsonPath"
    Output: "TextractOutputJsonPath"

    Example (Python::

         textract_async_to_json = tcdk.TextractAsyncToJSON(
             self,
             "TextractAsyncToJSON2",
             s3_output_prefix=s3_output_prefix,
             s3_output_bucket=s3_output_bucket)
    '''

    def __init__(
        self,
        parent: constructs.Construct,
        id: builtins.str,
        *,
        s3_output_bucket: builtins.str,
        s3_output_prefix: builtins.str,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param parent: -
        :param id: -
        :param s3_output_bucket: 
        :param s3_output_prefix: The prefix to use for the output files.
        :param lambda_log_level: log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL.
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents), set to 10240 (max) atm, decrease for smaller workloads.
        :param lambda_timeout: memory of Lambda function (may need to increase for larger documents).
        '''
        if __debug__:
            def stub(
                parent: constructs.Construct,
                id: builtins.str,
                *,
                s3_output_bucket: builtins.str,
                s3_output_prefix: builtins.str,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TextractAsyncToJSONProps(
            s3_output_bucket=s3_output_bucket,
            s3_output_prefix=s3_output_prefix,
            lambda_log_level=lambda_log_level,
            lambda_memory_mb=lambda_memory_mb,
            lambda_timeout=lambda_timeout,
        )

        jsii.create(self.__class__, self, [parent, id, props])

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[aws_cdk.aws_stepfunctions.INextable]:
        '''The states to chain onto if this fragment is used.'''
        return typing.cast(typing.List[aws_cdk.aws_stepfunctions.INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> aws_cdk.aws_stepfunctions.State:
        '''The start state of this state machine fragment.'''
        return typing.cast(aws_cdk.aws_stepfunctions.State, jsii.get(self, "startState"))


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.TextractAsyncToJSONProps",
    jsii_struct_bases=[],
    name_mapping={
        "s3_output_bucket": "s3OutputBucket",
        "s3_output_prefix": "s3OutputPrefix",
        "lambda_log_level": "lambdaLogLevel",
        "lambda_memory_mb": "lambdaMemoryMB",
        "lambda_timeout": "lambdaTimeout",
    },
)
class TextractAsyncToJSONProps:
    def __init__(
        self,
        *,
        s3_output_bucket: builtins.str,
        s3_output_prefix: builtins.str,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param s3_output_bucket: 
        :param s3_output_prefix: The prefix to use for the output files.
        :param lambda_log_level: log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL.
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents), set to 10240 (max) atm, decrease for smaller workloads.
        :param lambda_timeout: memory of Lambda function (may need to increase for larger documents).
        '''
        if __debug__:
            def stub(
                *,
                s3_output_bucket: builtins.str,
                s3_output_prefix: builtins.str,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_output_bucket", value=s3_output_bucket, expected_type=type_hints["s3_output_bucket"])
            check_type(argname="argument s3_output_prefix", value=s3_output_prefix, expected_type=type_hints["s3_output_prefix"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument lambda_memory_mb", value=lambda_memory_mb, expected_type=type_hints["lambda_memory_mb"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_output_bucket": s3_output_bucket,
            "s3_output_prefix": s3_output_prefix,
        }
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if lambda_memory_mb is not None:
            self._values["lambda_memory_mb"] = lambda_memory_mb
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout

    @builtins.property
    def s3_output_bucket(self) -> builtins.str:
        result = self._values.get("s3_output_bucket")
        assert result is not None, "Required property 's3_output_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_output_prefix(self) -> builtins.str:
        '''The prefix to use for the output files.'''
        result = self._values.get("s3_output_prefix")
        assert result is not None, "Required property 's3_output_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        '''log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL.'''
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''memory of Lambda function (may need to increase for larger documents), set to 10240 (max) atm, decrease for smaller workloads.'''
        result = self._values.get("lambda_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        '''memory of Lambda function (may need to increase for larger documents).'''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextractAsyncToJSONProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TextractClassificationConfigurator(
    aws_cdk.aws_stepfunctions.StateMachineFragment,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.TextractClassificationConfigurator",
):
    '''Looks for a matching DOCYMENT_TYPE in the configurationTableName and sets the CONFIG value (when found) to the context, so subsequent calls to Textract use those values.

    This is an entry from the default config
    AWS_PAYSTUBS,"{""queriesConfig"": [{""alias"": ""PAYSTUB_PERIOD_START_DATE"", ""text"": ""What is the Pay Period Start Date?""}, {""alias"": ""PAYSTUB_PERIOD_END_DATE"", ""text"": ""What is the Pay Period End Date?""}, {""alias"": ""PAYSTUB_PERIOD_PAY_DATE"", ""text"": ""What is the Pay Date?""}, {""alias"": ""PAYSTUB_PERIOD_EMPLOYEE_NAME"", ""text"": ""What is the Employee Name?""}, {""alias"": ""PAYSTUB_PERIOD_COMPANY_NAME"", ""text"": ""What is the company Name?""}, {""alias"": ""PAYSTUB_PERIOD_CURRENT_GROSS_PAY"", ""text"": ""What is the Current Gross Pay?""}, {""alias"": ""PAYSTUB_PERIOD_YTD_GROSS_PAY"", ""text"": ""What is the YTD Gross Pay?""}, {""alias"": ""PAYSTUB_PERIOD_REGULAR_HOURLY_RATE"", ""text"": ""What is the regular hourly rate?""}, {""alias"": ""PAYSTUB_PERIOD_HOLIDAY_RATE"", ""text"": ""What is the holiday rate?""}], ""textractFeatures"": [""QUERIES""]}"

    So, if the "classification"."documentType" in the Step Function Input is AWS_PAYSTUBS
    then it will set the queriesConfig in the manifest for the subsequent Textract Calls in the Step Function flow

    Input: "classification"."documentType"
    Output: config set to manifest

    Example (Python::

         configurator_task = tcdk.TextractClassificationConfigurator(
             self, f"{workflow_name}-Configurator",
         )
    '''

    def __init__(
        self,
        parent: constructs.Construct,
        id: builtins.str,
        *,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param parent: -
        :param id: -
        :param lambda_log_level: 
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents).
        :param lambda_timeout: 
        '''
        if __debug__:
            def stub(
                parent: constructs.Construct,
                id: builtins.str,
                *,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TextractClassificationConfiguratorProps(
            lambda_log_level=lambda_log_level,
            lambda_memory_mb=lambda_memory_mb,
            lambda_timeout=lambda_timeout,
        )

        jsii.create(self.__class__, self, [parent, id, props])

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[aws_cdk.aws_stepfunctions.INextable]:
        '''The states to chain onto if this fragment is used.'''
        return typing.cast(typing.List[aws_cdk.aws_stepfunctions.INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> aws_cdk.aws_stepfunctions.State:
        '''The start state of this state machine fragment.'''
        return typing.cast(aws_cdk.aws_stepfunctions.State, jsii.get(self, "startState"))

    @builtins.property
    @jsii.member(jsii_name="configurationTableName")
    def configuration_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationTableName"))

    @configuration_table_name.setter
    def configuration_table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationTableName", value)

    @builtins.property
    @jsii.member(jsii_name="configuratorFunction")
    def configurator_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "configuratorFunction"))

    @configurator_function.setter
    def configurator_function(self, value: aws_cdk.aws_lambda.IFunction) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuratorFunction", value)

    @builtins.property
    @jsii.member(jsii_name="configuratorFunctionLogGroupName")
    def configurator_function_log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configuratorFunctionLogGroupName"))

    @configurator_function_log_group_name.setter
    def configurator_function_log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuratorFunctionLogGroupName", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.TextractClassificationConfiguratorProps",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_log_level": "lambdaLogLevel",
        "lambda_memory_mb": "lambdaMemoryMB",
        "lambda_timeout": "lambdaTimeout",
    },
)
class TextractClassificationConfiguratorProps:
    def __init__(
        self,
        *,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param lambda_log_level: 
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents).
        :param lambda_timeout: 
        '''
        if __debug__:
            def stub(
                *,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument lambda_memory_mb", value=lambda_memory_mb, expected_type=type_hints["lambda_memory_mb"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
        self._values: typing.Dict[str, typing.Any] = {}
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if lambda_memory_mb is not None:
            self._values["lambda_memory_mb"] = lambda_memory_mb
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''memory of Lambda function (may need to increase for larger documents).'''
        result = self._values.get("lambda_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextractClassificationConfiguratorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.TextractDPPOCDeciderProps",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_memory_mb": "lambdaMemoryMB",
        "lambda_timeout": "lambdaTimeout",
    },
)
class TextractDPPOCDeciderProps:
    def __init__(
        self,
        *,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents).
        :param lambda_timeout: 
        '''
        if __debug__:
            def stub(
                *,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument lambda_memory_mb", value=lambda_memory_mb, expected_type=type_hints["lambda_memory_mb"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
        self._values: typing.Dict[str, typing.Any] = {}
        if lambda_memory_mb is not None:
            self._values["lambda_memory_mb"] = lambda_memory_mb
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout

    @builtins.property
    def lambda_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''memory of Lambda function (may need to increase for larger documents).'''
        result = self._values.get("lambda_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextractDPPOCDeciderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TextractGenerateCSV(
    aws_cdk.aws_stepfunctions.TaskStateBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.TextractGenerateCSV",
):
    '''Generates a output based on Textract Forms and Queries. Supported output_types: "LINES" | "CSV".

    Input: "Payload"."textract_result"."TextractOutputJsonPath"
    Output: "TextractOutputCSVPath" TODO: rename

    Output as LINES
    Example (Python::

                generate_text = tcdk.TextractGenerateCSV(
                 self,
                 "GenerateText",
                 csv_s3_output_bucket=document_bucket.bucket_name,
                 csv_s3_output_prefix=s3_txt_output_prefix,
                 output_type='LINES',
                 lambda_log_level="DEBUG",
                 integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
                 input=sfn.TaskInput.from_object({
                     "Token":
                     sfn.JsonPath.task_token,
                     "ExecutionId":
                     sfn.JsonPath.string_at('$$.Execution.Id'),
                     "Payload":
                     sfn.JsonPath.entire_payload,
                 }),
                 result_path="$.txt_output_location")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        csv_s3_output_bucket: builtins.str,
        csv_s3_output_prefix: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        output_type: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param csv_s3_output_bucket: 
        :param csv_s3_output_prefix: 
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents).
        :param lambda_timeout: 
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param output_type: 
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                csv_s3_output_bucket: builtins.str,
                csv_s3_output_prefix: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                output_type: typing.Optional[builtins.str] = None,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TextractGenerateCSVProps(
            csv_s3_output_bucket=csv_s3_output_bucket,
            csv_s3_output_prefix=csv_s3_output_prefix,
            associate_with_parent=associate_with_parent,
            input=input,
            lambda_log_level=lambda_log_level,
            lambda_memory_mb=lambda_memory_mb,
            lambda_timeout=lambda_timeout,
            name=name,
            output_type=output_type,
            comment=comment,
            heartbeat=heartbeat,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="generateCSVLambda")
    def generate_csv_lambda(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "generateCSVLambda"))

    @builtins.property
    @jsii.member(jsii_name="generateCSVLogGroup")
    def generate_csv_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "generateCSVLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig]:
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], jsii.get(self, "taskPolicies"))

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.StateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.StateMachine, jsii.get(self, "stateMachine"))

    @state_machine.setter
    def state_machine(self, value: aws_cdk.aws_stepfunctions.StateMachine) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_stepfunctions.StateMachine) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachine", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.TextractGenerateCSVProps",
    jsii_struct_bases=[aws_cdk.aws_stepfunctions.TaskStateBaseProps],
    name_mapping={
        "comment": "comment",
        "heartbeat": "heartbeat",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "timeout": "timeout",
        "csv_s3_output_bucket": "csvS3OutputBucket",
        "csv_s3_output_prefix": "csvS3OutputPrefix",
        "associate_with_parent": "associateWithParent",
        "input": "input",
        "lambda_log_level": "lambdaLogLevel",
        "lambda_memory_mb": "lambdaMemoryMB",
        "lambda_timeout": "lambdaTimeout",
        "name": "name",
        "output_type": "outputType",
    },
)
class TextractGenerateCSVProps(aws_cdk.aws_stepfunctions.TaskStateBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        csv_s3_output_bucket: builtins.str,
        csv_s3_output_prefix: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        output_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        :param csv_s3_output_bucket: 
        :param csv_s3_output_prefix: 
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: 
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents).
        :param lambda_timeout: 
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param output_type: 
        '''
        if __debug__:
            def stub(
                *,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                csv_s3_output_bucket: builtins.str,
                csv_s3_output_prefix: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                output_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument csv_s3_output_bucket", value=csv_s3_output_bucket, expected_type=type_hints["csv_s3_output_bucket"])
            check_type(argname="argument csv_s3_output_prefix", value=csv_s3_output_prefix, expected_type=type_hints["csv_s3_output_prefix"])
            check_type(argname="argument associate_with_parent", value=associate_with_parent, expected_type=type_hints["associate_with_parent"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument lambda_memory_mb", value=lambda_memory_mb, expected_type=type_hints["lambda_memory_mb"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument output_type", value=output_type, expected_type=type_hints["output_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "csv_s3_output_bucket": csv_s3_output_bucket,
            "csv_s3_output_prefix": csv_s3_output_prefix,
        }
        if comment is not None:
            self._values["comment"] = comment
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if timeout is not None:
            self._values["timeout"] = timeout
        if associate_with_parent is not None:
            self._values["associate_with_parent"] = associate_with_parent
        if input is not None:
            self._values["input"] = input
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if lambda_memory_mb is not None:
            self._values["lambda_memory_mb"] = lambda_memory_mb
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout
        if name is not None:
            self._values["name"] = name
        if output_type is not None:
            self._values["output_type"] = output_type

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the heartbeat.

        :default: - None
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns

        :default: IntegrationPattern.REQUEST_RESPONSE

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the state machine.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def csv_s3_output_bucket(self) -> builtins.str:
        result = self._values.get("csv_s3_output_bucket")
        assert result is not None, "Required property 'csv_s3_output_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def csv_s3_output_prefix(self) -> builtins.str:
        result = self._values.get("csv_s3_output_prefix")
        assert result is not None, "Required property 'csv_s3_output_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_with_parent(self) -> typing.Optional[builtins.bool]:
        '''Pass the execution ID from the context object to the execution input.

        This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines.

        If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely.

        :default: - false

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html#nested-execution-startid
        '''
        result = self._values.get("associate_with_parent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskInput]:
        '''The JSON input for the execution, same as that of StartExecution.

        :default: - The state input (JSON path '$')

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskInput], result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''memory of Lambda function (may need to increase for larger documents).'''
        result = self._values.get("lambda_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the execution, same as that of StartExecution.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_type(self) -> typing.Optional[builtins.str]:
        result = self._values.get("output_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextractGenerateCSVProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TextractGenericAsyncSfnTask(
    aws_cdk.aws_stepfunctions.TaskStateBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.TextractGenericAsyncSfnTask",
):
    '''This Task calls the Textract through the asynchronous API.

    Which API to call is defined in

    When GENERIC is called with features in the manifest definition, will call the AnalzyeDocument API.

    Takes the configuration from "Payload"."manifest"

    Will retry on recoverable errors based on textractAsyncCallMaxRetries
    errors for retry: ['ThrottlingException', 'LimitExceededException', 'InternalServerError', 'ProvisionedThroughputExceededException'],

    Internally calls Start* calls with OutputConfig and SNSNotification.
    Another Lambda functions waits for SNS Notification event and notifies the Step Function flow with the task token.

    Step Function JSON input requirements

    **Input**: "Payload"."manifest"

    **Output**: "TextractTempOutputJsonPath" points to potentially paginated Textract JSON Schema output at "TextractTempOutputJsonPath" (using the example code it will be at: "textract_result"."TextractTempOutputJsonPath")

    Works together with TextractAsyncToJSON, which takes the s3_output_bucket/s3_temp_output_prefix location as input

    Example (Python::

         textract_async_task = tcdk.TextractGenericAsyncSfnTask(
             self,
             "TextractAsync",
             s3_output_bucket=s3_output_bucket,
             s3_temp_output_prefix=s3_temp_output_prefix,
             integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
             lambda_log_level="DEBUG",
             timeout=Duration.hours(24),
             input=sfn.TaskInput.from_object({
                 "Token":
                 sfn.JsonPath.task_token,
                 "ExecutionId":
                 sfn.JsonPath.string_at('$$.Execution.Id'),
                 "Payload":
                 sfn.JsonPath.entire_payload,
             }),
             result_path="$.textract_result")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        s3_output_bucket: builtins.str,
        s3_temp_output_prefix: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        textract_api: typing.Optional[builtins.str] = None,
        textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
        textract_async_call_interval: typing.Optional[jsii.Number] = None,
        textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param s3_output_bucket: Bucketname to output data to.
        :param s3_temp_output_prefix: The prefix to use for the temporary output files (e. g. output from async process before stiching together)
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param enable_cloud_watch_metrics_and_dashboard: enable CloudWatch Metrics and Dashboard. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL. Default: = DEBUG
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param textract_api: Which Textract API to call GENERIC and EXPENSE are supported. For GENERIC, when called without features (e. g. FORMS, TABLES, QUERIES), StartDetectText is called. For GENERIC, when called with a feature (e. g. FORMS, TABLES, QUERIES), StartAnalyzeDocument is called. Default: - GENERIC
        :param textract_async_call_backoff_rate: retyr backoff rate. Default: is 1.1
        :param textract_async_call_interval: time in seconds to wait before next retry. Default: is 1
        :param textract_async_call_max_retries: number of retries in Step Function flow. Default: is 100
        :param textract_state_machine_timeout_minutes: how long can we wait for the process. Default: - 2880 (48 hours (60 min * 48 hours = 2880))
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                s3_output_bucket: builtins.str,
                s3_temp_output_prefix: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                textract_api: typing.Optional[builtins.str] = None,
                textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
                textract_async_call_interval: typing.Optional[jsii.Number] = None,
                textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TextractGenericAsyncSfnTaskProps(
            s3_output_bucket=s3_output_bucket,
            s3_temp_output_prefix=s3_temp_output_prefix,
            associate_with_parent=associate_with_parent,
            enable_cloud_watch_metrics_and_dashboard=enable_cloud_watch_metrics_and_dashboard,
            input=input,
            lambda_log_level=lambda_log_level,
            name=name,
            textract_api=textract_api,
            textract_async_call_backoff_rate=textract_async_call_backoff_rate,
            textract_async_call_interval=textract_async_call_interval,
            textract_async_call_max_retries=textract_async_call_max_retries,
            textract_state_machine_timeout_minutes=textract_state_machine_timeout_minutes,
            comment=comment,
            heartbeat=heartbeat,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig]:
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], jsii.get(self, "taskPolicies"))

    @builtins.property
    @jsii.member(jsii_name="receiveStartSNSLambdaLogGroup")
    def receive_start_sns_lambda_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "receiveStartSNSLambdaLogGroup"))

    @receive_start_sns_lambda_log_group.setter
    def receive_start_sns_lambda_log_group(
        self,
        value: aws_cdk.aws_logs.ILogGroup,
    ) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_logs.ILogGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "receiveStartSNSLambdaLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="startTextractLambdaLogGroup")
    def start_textract_lambda_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "startTextractLambdaLogGroup"))

    @start_textract_lambda_log_group.setter
    def start_textract_lambda_log_group(
        self,
        value: aws_cdk.aws_logs.ILogGroup,
    ) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_logs.ILogGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTextractLambdaLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.IStateMachine, jsii.get(self, "stateMachine"))

    @state_machine.setter
    def state_machine(self, value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachine", value)

    @builtins.property
    @jsii.member(jsii_name="taskTokenTableName")
    def task_token_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskTokenTableName"))

    @task_token_table_name.setter
    def task_token_table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskTokenTableName", value)

    @builtins.property
    @jsii.member(jsii_name="textractAsyncCallFunction")
    def textract_async_call_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "textractAsyncCallFunction"))

    @textract_async_call_function.setter
    def textract_async_call_function(self, value: aws_cdk.aws_lambda.IFunction) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textractAsyncCallFunction", value)

    @builtins.property
    @jsii.member(jsii_name="textractAsyncReceiveSNSFunction")
    def textract_async_receive_sns_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "textractAsyncReceiveSNSFunction"))

    @textract_async_receive_sns_function.setter
    def textract_async_receive_sns_function(
        self,
        value: aws_cdk.aws_lambda.IFunction,
    ) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textractAsyncReceiveSNSFunction", value)

    @builtins.property
    @jsii.member(jsii_name="textractAsyncSNS")
    def textract_async_sns(self) -> aws_cdk.aws_sns.ITopic:
        return typing.cast(aws_cdk.aws_sns.ITopic, jsii.get(self, "textractAsyncSNS"))

    @textract_async_sns.setter
    def textract_async_sns(self, value: aws_cdk.aws_sns.ITopic) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_sns.ITopic) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textractAsyncSNS", value)

    @builtins.property
    @jsii.member(jsii_name="textractAsyncSNSRole")
    def textract_async_sns_role(self) -> aws_cdk.aws_iam.IRole:
        return typing.cast(aws_cdk.aws_iam.IRole, jsii.get(self, "textractAsyncSNSRole"))

    @textract_async_sns_role.setter
    def textract_async_sns_role(self, value: aws_cdk.aws_iam.IRole) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_iam.IRole) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textractAsyncSNSRole", value)

    @builtins.property
    @jsii.member(jsii_name="asyncDurationMetric")
    def async_duration_metric(self) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "asyncDurationMetric"))

    @async_duration_metric.setter
    def async_duration_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asyncDurationMetric", value)

    @builtins.property
    @jsii.member(jsii_name="asyncJobFinshedMetric")
    def async_job_finshed_metric(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "asyncJobFinshedMetric"))

    @async_job_finshed_metric.setter
    def async_job_finshed_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asyncJobFinshedMetric", value)

    @builtins.property
    @jsii.member(jsii_name="asyncJobStartedMetric")
    def async_job_started_metric(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "asyncJobStartedMetric"))

    @async_job_started_metric.setter
    def async_job_started_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asyncJobStartedMetric", value)

    @builtins.property
    @jsii.member(jsii_name="asyncNumberPagesMetric")
    def async_number_pages_metric(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "asyncNumberPagesMetric"))

    @async_number_pages_metric.setter
    def async_number_pages_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asyncNumberPagesMetric", value)

    @builtins.property
    @jsii.member(jsii_name="asyncNumberPagesSendMetric")
    def async_number_pages_send_metric(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "asyncNumberPagesSendMetric"))

    @async_number_pages_send_metric.setter
    def async_number_pages_send_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asyncNumberPagesSendMetric", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.TextractGenericAsyncSfnTaskProps",
    jsii_struct_bases=[aws_cdk.aws_stepfunctions.TaskStateBaseProps],
    name_mapping={
        "comment": "comment",
        "heartbeat": "heartbeat",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "timeout": "timeout",
        "s3_output_bucket": "s3OutputBucket",
        "s3_temp_output_prefix": "s3TempOutputPrefix",
        "associate_with_parent": "associateWithParent",
        "enable_cloud_watch_metrics_and_dashboard": "enableCloudWatchMetricsAndDashboard",
        "input": "input",
        "lambda_log_level": "lambdaLogLevel",
        "name": "name",
        "textract_api": "textractAPI",
        "textract_async_call_backoff_rate": "textractAsyncCallBackoffRate",
        "textract_async_call_interval": "textractAsyncCallInterval",
        "textract_async_call_max_retries": "textractAsyncCallMaxRetries",
        "textract_state_machine_timeout_minutes": "textractStateMachineTimeoutMinutes",
    },
)
class TextractGenericAsyncSfnTaskProps(aws_cdk.aws_stepfunctions.TaskStateBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        s3_output_bucket: builtins.str,
        s3_temp_output_prefix: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        textract_api: typing.Optional[builtins.str] = None,
        textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
        textract_async_call_interval: typing.Optional[jsii.Number] = None,
        textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        :param s3_output_bucket: Bucketname to output data to.
        :param s3_temp_output_prefix: The prefix to use for the temporary output files (e. g. output from async process before stiching together)
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param enable_cloud_watch_metrics_and_dashboard: enable CloudWatch Metrics and Dashboard. Default: - false
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL. Default: = DEBUG
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param textract_api: Which Textract API to call GENERIC and EXPENSE are supported. For GENERIC, when called without features (e. g. FORMS, TABLES, QUERIES), StartDetectText is called. For GENERIC, when called with a feature (e. g. FORMS, TABLES, QUERIES), StartAnalyzeDocument is called. Default: - GENERIC
        :param textract_async_call_backoff_rate: retyr backoff rate. Default: is 1.1
        :param textract_async_call_interval: time in seconds to wait before next retry. Default: is 1
        :param textract_async_call_max_retries: number of retries in Step Function flow. Default: is 100
        :param textract_state_machine_timeout_minutes: how long can we wait for the process. Default: - 2880 (48 hours (60 min * 48 hours = 2880))
        '''
        if __debug__:
            def stub(
                *,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                s3_output_bucket: builtins.str,
                s3_temp_output_prefix: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                textract_api: typing.Optional[builtins.str] = None,
                textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
                textract_async_call_interval: typing.Optional[jsii.Number] = None,
                textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument s3_output_bucket", value=s3_output_bucket, expected_type=type_hints["s3_output_bucket"])
            check_type(argname="argument s3_temp_output_prefix", value=s3_temp_output_prefix, expected_type=type_hints["s3_temp_output_prefix"])
            check_type(argname="argument associate_with_parent", value=associate_with_parent, expected_type=type_hints["associate_with_parent"])
            check_type(argname="argument enable_cloud_watch_metrics_and_dashboard", value=enable_cloud_watch_metrics_and_dashboard, expected_type=type_hints["enable_cloud_watch_metrics_and_dashboard"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument textract_api", value=textract_api, expected_type=type_hints["textract_api"])
            check_type(argname="argument textract_async_call_backoff_rate", value=textract_async_call_backoff_rate, expected_type=type_hints["textract_async_call_backoff_rate"])
            check_type(argname="argument textract_async_call_interval", value=textract_async_call_interval, expected_type=type_hints["textract_async_call_interval"])
            check_type(argname="argument textract_async_call_max_retries", value=textract_async_call_max_retries, expected_type=type_hints["textract_async_call_max_retries"])
            check_type(argname="argument textract_state_machine_timeout_minutes", value=textract_state_machine_timeout_minutes, expected_type=type_hints["textract_state_machine_timeout_minutes"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_output_bucket": s3_output_bucket,
            "s3_temp_output_prefix": s3_temp_output_prefix,
        }
        if comment is not None:
            self._values["comment"] = comment
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if timeout is not None:
            self._values["timeout"] = timeout
        if associate_with_parent is not None:
            self._values["associate_with_parent"] = associate_with_parent
        if enable_cloud_watch_metrics_and_dashboard is not None:
            self._values["enable_cloud_watch_metrics_and_dashboard"] = enable_cloud_watch_metrics_and_dashboard
        if input is not None:
            self._values["input"] = input
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if name is not None:
            self._values["name"] = name
        if textract_api is not None:
            self._values["textract_api"] = textract_api
        if textract_async_call_backoff_rate is not None:
            self._values["textract_async_call_backoff_rate"] = textract_async_call_backoff_rate
        if textract_async_call_interval is not None:
            self._values["textract_async_call_interval"] = textract_async_call_interval
        if textract_async_call_max_retries is not None:
            self._values["textract_async_call_max_retries"] = textract_async_call_max_retries
        if textract_state_machine_timeout_minutes is not None:
            self._values["textract_state_machine_timeout_minutes"] = textract_state_machine_timeout_minutes

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the heartbeat.

        :default: - None
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns

        :default: IntegrationPattern.REQUEST_RESPONSE

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the state machine.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def s3_output_bucket(self) -> builtins.str:
        '''Bucketname to output data to.'''
        result = self._values.get("s3_output_bucket")
        assert result is not None, "Required property 's3_output_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_temp_output_prefix(self) -> builtins.str:
        '''The prefix to use for the temporary output files (e.

        g. output from async process before stiching together)
        '''
        result = self._values.get("s3_temp_output_prefix")
        assert result is not None, "Required property 's3_temp_output_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_with_parent(self) -> typing.Optional[builtins.bool]:
        '''Pass the execution ID from the context object to the execution input.

        This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines.

        If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely.

        :default: - false

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html#nested-execution-startid
        '''
        result = self._values.get("associate_with_parent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_cloud_watch_metrics_and_dashboard(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''enable CloudWatch Metrics and Dashboard.

        :default: - false
        '''
        result = self._values.get("enable_cloud_watch_metrics_and_dashboard")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskInput]:
        '''The JSON input for the execution, same as that of StartExecution.

        :default: - The state input (JSON path '$')

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskInput], result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        '''log level for Lambda function, supports DEBUG|INFO|WARNING|ERROR|FATAL.

        :default: = DEBUG
        '''
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the execution, same as that of StartExecution.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def textract_api(self) -> typing.Optional[builtins.str]:
        '''Which Textract API to call GENERIC and EXPENSE are supported.

        For GENERIC, when called without features (e. g. FORMS, TABLES, QUERIES), StartDetectText is called.
        For GENERIC, when called with a feature (e. g. FORMS, TABLES, QUERIES),  StartAnalyzeDocument is called.

        :default: - GENERIC
        '''
        result = self._values.get("textract_api")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def textract_async_call_backoff_rate(self) -> typing.Optional[jsii.Number]:
        '''retyr backoff rate.

        :default: is 1.1
        '''
        result = self._values.get("textract_async_call_backoff_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def textract_async_call_interval(self) -> typing.Optional[jsii.Number]:
        '''time in seconds to wait before next retry.

        :default: is 1
        '''
        result = self._values.get("textract_async_call_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def textract_async_call_max_retries(self) -> typing.Optional[jsii.Number]:
        '''number of retries in Step Function flow.

        :default: is 100
        '''
        result = self._values.get("textract_async_call_max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def textract_state_machine_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''how long can we wait for the process.

        :default: - 2880 (48 hours (60 min * 48 hours = 2880))
        '''
        result = self._values.get("textract_state_machine_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextractGenericAsyncSfnTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TextractGenericSyncSfnTask(
    aws_cdk.aws_stepfunctions.TaskStateBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.TextractGenericSyncSfnTask",
):
    '''Calls Textract synchronous API.

    Supports the Textract APIs:  'GENERIC' | 'ANALYZEID' | 'EXPENSE'
    When GENERIC is called with features in the manifest definition, will call the AnalzyeDocument API.
    Takes the configuration from "Payload"."manifest"
    Will retry on recoverable errors based on textractAsyncCallMaxRetries
    errors for retry: ['ThrottlingException', 'LimitExceededException', 'InternalServerError', 'ProvisionedThroughputExceededException'],

    Input: "Payload"."manifest"
    Output: Textract JSON Schema at  s3_output_bucket/s3_output_prefix

    Example (Python::

                textract_sync_task = tcdk.TextractGenericSyncSfnTask(
                 self,
                 "TextractSync",
                 s3_output_bucket=document_bucket.bucket_name,
                 s3_output_prefix=s3_output_prefix,
                 integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
                 lambda_log_level="DEBUG",
                 timeout=Duration.hours(24),
                 input=sfn.TaskInput.from_object({
                     "Token":
                     sfn.JsonPath.task_token,
                     "ExecutionId":
                     sfn.JsonPath.string_at('$$.Execution.Id'),
                     "Payload":
                     sfn.JsonPath.entire_payload,
                 }),
                 result_path="$.textract_result")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        s3_output_bucket: builtins.str,
        s3_output_prefix: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        custom_function: typing.Optional[aws_cdk.aws_stepfunctions_tasks.LambdaInvoke] = None,
        enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
        enable_dashboard: typing.Optional[builtins.bool] = None,
        enable_monitoring: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        s3_input_bucket: typing.Optional[builtins.str] = None,
        s3_input_prefix: typing.Optional[builtins.str] = None,
        textract_api: typing.Optional[builtins.str] = None,
        textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
        textract_async_call_interval: typing.Optional[jsii.Number] = None,
        textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param s3_output_bucket: 
        :param s3_output_prefix: The prefix to use for the output files.
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param custom_function: not implemented yet.
        :param enable_cloud_watch_metrics_and_dashboard: enable CloudWatch Metrics and Dashboard. Default: - false
        :param enable_dashboard: not implemented yet.
        :param enable_monitoring: not implemented yet.
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: Log level, can be DEBUG, INFO, WARNING, ERROR, FATAL.
        :param lambda_memory: Memory allocated to Lambda function, default 512.
        :param lambda_timeout: Lambda Function Timeout in seconds, default 300.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param s3_input_bucket: location of input S3 objects - if left empty will generate rule for s3 access to all [*].
        :param s3_input_prefix: prefix for input S3 objects - if left empty will generate rule for s3 access to all [*].
        :param textract_api: 
        :param textract_async_call_backoff_rate: default is 1.1.
        :param textract_async_call_interval: default is 1.
        :param textract_async_call_max_retries: 
        :param textract_state_machine_timeout_minutes: how long can we wait for the process (default is 48 hours (60*48=2880)).
        :param workflow_tracing_enabled: 
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                s3_output_bucket: builtins.str,
                s3_output_prefix: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                custom_function: typing.Optional[aws_cdk.aws_stepfunctions_tasks.LambdaInvoke] = None,
                enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
                enable_dashboard: typing.Optional[builtins.bool] = None,
                enable_monitoring: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                s3_input_bucket: typing.Optional[builtins.str] = None,
                s3_input_prefix: typing.Optional[builtins.str] = None,
                textract_api: typing.Optional[builtins.str] = None,
                textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
                textract_async_call_interval: typing.Optional[jsii.Number] = None,
                textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TextractGenericSyncSfnTaskProps(
            s3_output_bucket=s3_output_bucket,
            s3_output_prefix=s3_output_prefix,
            associate_with_parent=associate_with_parent,
            custom_function=custom_function,
            enable_cloud_watch_metrics_and_dashboard=enable_cloud_watch_metrics_and_dashboard,
            enable_dashboard=enable_dashboard,
            enable_monitoring=enable_monitoring,
            input=input,
            lambda_log_level=lambda_log_level,
            lambda_memory=lambda_memory,
            lambda_timeout=lambda_timeout,
            name=name,
            s3_input_bucket=s3_input_bucket,
            s3_input_prefix=s3_input_prefix,
            textract_api=textract_api,
            textract_async_call_backoff_rate=textract_async_call_backoff_rate,
            textract_async_call_interval=textract_async_call_interval,
            textract_async_call_max_retries=textract_async_call_max_retries,
            textract_state_machine_timeout_minutes=textract_state_machine_timeout_minutes,
            workflow_tracing_enabled=workflow_tracing_enabled,
            comment=comment,
            heartbeat=heartbeat,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig]:
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], jsii.get(self, "taskPolicies"))

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.IStateMachine, jsii.get(self, "stateMachine"))

    @state_machine.setter
    def state_machine(self, value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_stepfunctions.IStateMachine) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachine", value)

    @builtins.property
    @jsii.member(jsii_name="textractSyncCallFunction")
    def textract_sync_call_function(self) -> aws_cdk.aws_lambda.IFunction:
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "textractSyncCallFunction"))

    @textract_sync_call_function.setter
    def textract_sync_call_function(self, value: aws_cdk.aws_lambda.IFunction) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_lambda.IFunction) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textractSyncCallFunction", value)

    @builtins.property
    @jsii.member(jsii_name="textractSyncLambdaLogGroup")
    def textract_sync_lambda_log_group(self) -> aws_cdk.aws_logs.ILogGroup:
        return typing.cast(aws_cdk.aws_logs.ILogGroup, jsii.get(self, "textractSyncLambdaLogGroup"))

    @textract_sync_lambda_log_group.setter
    def textract_sync_lambda_log_group(self, value: aws_cdk.aws_logs.ILogGroup) -> None:
        if __debug__:
            def stub(value: aws_cdk.aws_logs.ILogGroup) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textractSyncLambdaLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="syncDurationMetric")
    def sync_duration_metric(self) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "syncDurationMetric"))

    @sync_duration_metric.setter
    def sync_duration_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncDurationMetric", value)

    @builtins.property
    @jsii.member(jsii_name="syncNumberPagesMetric")
    def sync_number_pages_metric(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "syncNumberPagesMetric"))

    @sync_number_pages_metric.setter
    def sync_number_pages_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncNumberPagesMetric", value)

    @builtins.property
    @jsii.member(jsii_name="syncNumberPagesSendMetric")
    def sync_number_pages_send_metric(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "syncNumberPagesSendMetric"))

    @sync_number_pages_send_metric.setter
    def sync_number_pages_send_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncNumberPagesSendMetric", value)

    @builtins.property
    @jsii.member(jsii_name="syncTimedOutMetric")
    def sync_timed_out_metric(self) -> typing.Optional[aws_cdk.aws_cloudwatch.IMetric]:
        return typing.cast(typing.Optional[aws_cdk.aws_cloudwatch.IMetric], jsii.get(self, "syncTimedOutMetric"))

    @sync_timed_out_metric.setter
    def sync_timed_out_metric(
        self,
        value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncTimedOutMetric", value)


@jsii.data_type(
    jsii_type="amazon-textract-idp-cdk-constructs.TextractGenericSyncSfnTaskProps",
    jsii_struct_bases=[aws_cdk.aws_stepfunctions.TaskStateBaseProps],
    name_mapping={
        "comment": "comment",
        "heartbeat": "heartbeat",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "timeout": "timeout",
        "s3_output_bucket": "s3OutputBucket",
        "s3_output_prefix": "s3OutputPrefix",
        "associate_with_parent": "associateWithParent",
        "custom_function": "customFunction",
        "enable_cloud_watch_metrics_and_dashboard": "enableCloudWatchMetricsAndDashboard",
        "enable_dashboard": "enableDashboard",
        "enable_monitoring": "enableMonitoring",
        "input": "input",
        "lambda_log_level": "lambdaLogLevel",
        "lambda_memory": "lambdaMemory",
        "lambda_timeout": "lambdaTimeout",
        "name": "name",
        "s3_input_bucket": "s3InputBucket",
        "s3_input_prefix": "s3InputPrefix",
        "textract_api": "textractAPI",
        "textract_async_call_backoff_rate": "textractAsyncCallBackoffRate",
        "textract_async_call_interval": "textractAsyncCallInterval",
        "textract_async_call_max_retries": "textractAsyncCallMaxRetries",
        "textract_state_machine_timeout_minutes": "textractStateMachineTimeoutMinutes",
        "workflow_tracing_enabled": "workflowTracingEnabled",
    },
)
class TextractGenericSyncSfnTaskProps(aws_cdk.aws_stepfunctions.TaskStateBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        heartbeat: typing.Optional[aws_cdk.Duration] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        s3_output_bucket: builtins.str,
        s3_output_prefix: builtins.str,
        associate_with_parent: typing.Optional[builtins.bool] = None,
        custom_function: typing.Optional[aws_cdk.aws_stepfunctions_tasks.LambdaInvoke] = None,
        enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
        enable_dashboard: typing.Optional[builtins.bool] = None,
        enable_monitoring: typing.Optional[builtins.bool] = None,
        input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
        lambda_log_level: typing.Optional[builtins.str] = None,
        lambda_memory: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        s3_input_bucket: typing.Optional[builtins.str] = None,
        s3_input_prefix: typing.Optional[builtins.str] = None,
        textract_api: typing.Optional[builtins.str] = None,
        textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
        textract_async_call_interval: typing.Optional[jsii.Number] = None,
        textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
        textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
        workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param comment: An optional description for this state. Default: - No comment
        :param heartbeat: Timeout for the heartbeat. Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns Default: IntegrationPattern.REQUEST_RESPONSE
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param timeout: Timeout for the state machine. Default: - None
        :param s3_output_bucket: 
        :param s3_output_prefix: The prefix to use for the output files.
        :param associate_with_parent: Pass the execution ID from the context object to the execution input. This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines. If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely. Default: - false
        :param custom_function: not implemented yet.
        :param enable_cloud_watch_metrics_and_dashboard: enable CloudWatch Metrics and Dashboard. Default: - false
        :param enable_dashboard: not implemented yet.
        :param enable_monitoring: not implemented yet.
        :param input: The JSON input for the execution, same as that of StartExecution. Default: - The state input (JSON path '$')
        :param lambda_log_level: Log level, can be DEBUG, INFO, WARNING, ERROR, FATAL.
        :param lambda_memory: Memory allocated to Lambda function, default 512.
        :param lambda_timeout: Lambda Function Timeout in seconds, default 300.
        :param name: The name of the execution, same as that of StartExecution. Default: - None
        :param s3_input_bucket: location of input S3 objects - if left empty will generate rule for s3 access to all [*].
        :param s3_input_prefix: prefix for input S3 objects - if left empty will generate rule for s3 access to all [*].
        :param textract_api: 
        :param textract_async_call_backoff_rate: default is 1.1.
        :param textract_async_call_interval: default is 1.
        :param textract_async_call_max_retries: 
        :param textract_state_machine_timeout_minutes: how long can we wait for the process (default is 48 hours (60*48=2880)).
        :param workflow_tracing_enabled: 
        '''
        if __debug__:
            def stub(
                *,
                comment: typing.Optional[builtins.str] = None,
                heartbeat: typing.Optional[aws_cdk.Duration] = None,
                input_path: typing.Optional[builtins.str] = None,
                integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern] = None,
                output_path: typing.Optional[builtins.str] = None,
                result_path: typing.Optional[builtins.str] = None,
                result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                s3_output_bucket: builtins.str,
                s3_output_prefix: builtins.str,
                associate_with_parent: typing.Optional[builtins.bool] = None,
                custom_function: typing.Optional[aws_cdk.aws_stepfunctions_tasks.LambdaInvoke] = None,
                enable_cloud_watch_metrics_and_dashboard: typing.Optional[builtins.bool] = None,
                enable_dashboard: typing.Optional[builtins.bool] = None,
                enable_monitoring: typing.Optional[builtins.bool] = None,
                input: typing.Optional[aws_cdk.aws_stepfunctions.TaskInput] = None,
                lambda_log_level: typing.Optional[builtins.str] = None,
                lambda_memory: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
                s3_input_bucket: typing.Optional[builtins.str] = None,
                s3_input_prefix: typing.Optional[builtins.str] = None,
                textract_api: typing.Optional[builtins.str] = None,
                textract_async_call_backoff_rate: typing.Optional[jsii.Number] = None,
                textract_async_call_interval: typing.Optional[jsii.Number] = None,
                textract_async_call_max_retries: typing.Optional[jsii.Number] = None,
                textract_state_machine_timeout_minutes: typing.Optional[jsii.Number] = None,
                workflow_tracing_enabled: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument s3_output_bucket", value=s3_output_bucket, expected_type=type_hints["s3_output_bucket"])
            check_type(argname="argument s3_output_prefix", value=s3_output_prefix, expected_type=type_hints["s3_output_prefix"])
            check_type(argname="argument associate_with_parent", value=associate_with_parent, expected_type=type_hints["associate_with_parent"])
            check_type(argname="argument custom_function", value=custom_function, expected_type=type_hints["custom_function"])
            check_type(argname="argument enable_cloud_watch_metrics_and_dashboard", value=enable_cloud_watch_metrics_and_dashboard, expected_type=type_hints["enable_cloud_watch_metrics_and_dashboard"])
            check_type(argname="argument enable_dashboard", value=enable_dashboard, expected_type=type_hints["enable_dashboard"])
            check_type(argname="argument enable_monitoring", value=enable_monitoring, expected_type=type_hints["enable_monitoring"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument lambda_log_level", value=lambda_log_level, expected_type=type_hints["lambda_log_level"])
            check_type(argname="argument lambda_memory", value=lambda_memory, expected_type=type_hints["lambda_memory"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument s3_input_bucket", value=s3_input_bucket, expected_type=type_hints["s3_input_bucket"])
            check_type(argname="argument s3_input_prefix", value=s3_input_prefix, expected_type=type_hints["s3_input_prefix"])
            check_type(argname="argument textract_api", value=textract_api, expected_type=type_hints["textract_api"])
            check_type(argname="argument textract_async_call_backoff_rate", value=textract_async_call_backoff_rate, expected_type=type_hints["textract_async_call_backoff_rate"])
            check_type(argname="argument textract_async_call_interval", value=textract_async_call_interval, expected_type=type_hints["textract_async_call_interval"])
            check_type(argname="argument textract_async_call_max_retries", value=textract_async_call_max_retries, expected_type=type_hints["textract_async_call_max_retries"])
            check_type(argname="argument textract_state_machine_timeout_minutes", value=textract_state_machine_timeout_minutes, expected_type=type_hints["textract_state_machine_timeout_minutes"])
            check_type(argname="argument workflow_tracing_enabled", value=workflow_tracing_enabled, expected_type=type_hints["workflow_tracing_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_output_bucket": s3_output_bucket,
            "s3_output_prefix": s3_output_prefix,
        }
        if comment is not None:
            self._values["comment"] = comment
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if timeout is not None:
            self._values["timeout"] = timeout
        if associate_with_parent is not None:
            self._values["associate_with_parent"] = associate_with_parent
        if custom_function is not None:
            self._values["custom_function"] = custom_function
        if enable_cloud_watch_metrics_and_dashboard is not None:
            self._values["enable_cloud_watch_metrics_and_dashboard"] = enable_cloud_watch_metrics_and_dashboard
        if enable_dashboard is not None:
            self._values["enable_dashboard"] = enable_dashboard
        if enable_monitoring is not None:
            self._values["enable_monitoring"] = enable_monitoring
        if input is not None:
            self._values["input"] = input
        if lambda_log_level is not None:
            self._values["lambda_log_level"] = lambda_log_level
        if lambda_memory is not None:
            self._values["lambda_memory"] = lambda_memory
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout
        if name is not None:
            self._values["name"] = name
        if s3_input_bucket is not None:
            self._values["s3_input_bucket"] = s3_input_bucket
        if s3_input_prefix is not None:
            self._values["s3_input_prefix"] = s3_input_prefix
        if textract_api is not None:
            self._values["textract_api"] = textract_api
        if textract_async_call_backoff_rate is not None:
            self._values["textract_async_call_backoff_rate"] = textract_async_call_backoff_rate
        if textract_async_call_interval is not None:
            self._values["textract_async_call_interval"] = textract_async_call_interval
        if textract_async_call_max_retries is not None:
            self._values["textract_async_call_max_retries"] = textract_async_call_max_retries
        if textract_state_machine_timeout_minutes is not None:
            self._values["textract_state_machine_timeout_minutes"] = textract_state_machine_timeout_minutes
        if workflow_tracing_enabled is not None:
            self._values["workflow_tracing_enabled"] = workflow_tracing_enabled

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the heartbeat.

        :default: - None
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns

        :default: IntegrationPattern.REQUEST_RESPONSE

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''Timeout for the state machine.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def s3_output_bucket(self) -> builtins.str:
        result = self._values.get("s3_output_bucket")
        assert result is not None, "Required property 's3_output_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_output_prefix(self) -> builtins.str:
        '''The prefix to use for the output files.'''
        result = self._values.get("s3_output_prefix")
        assert result is not None, "Required property 's3_output_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_with_parent(self) -> typing.Optional[builtins.bool]:
        '''Pass the execution ID from the context object to the execution input.

        This allows the Step Functions UI to link child executions from parent executions, making it easier to trace execution flow across state machines.

        If you set this property to ``true``, the ``input`` property must be an object (provided by ``sfn.TaskInput.fromObject``) or omitted entirely.

        :default: - false

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html#nested-execution-startid
        '''
        result = self._values.get("associate_with_parent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def custom_function(
        self,
    ) -> typing.Optional[aws_cdk.aws_stepfunctions_tasks.LambdaInvoke]:
        '''not implemented yet.'''
        result = self._values.get("custom_function")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions_tasks.LambdaInvoke], result)

    @builtins.property
    def enable_cloud_watch_metrics_and_dashboard(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''enable CloudWatch Metrics and Dashboard.

        :default: - false
        '''
        result = self._values.get("enable_cloud_watch_metrics_and_dashboard")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_dashboard(self) -> typing.Optional[builtins.bool]:
        '''not implemented yet.'''
        result = self._values.get("enable_dashboard")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_monitoring(self) -> typing.Optional[builtins.bool]:
        '''not implemented yet.'''
        result = self._values.get("enable_monitoring")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_stepfunctions.TaskInput]:
        '''The JSON input for the execution, same as that of StartExecution.

        :default: - The state input (JSON path '$')

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_stepfunctions.TaskInput], result)

    @builtins.property
    def lambda_log_level(self) -> typing.Optional[builtins.str]:
        '''Log level, can be DEBUG, INFO, WARNING, ERROR, FATAL.'''
        result = self._values.get("lambda_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_memory(self) -> typing.Optional[jsii.Number]:
        '''Memory allocated to Lambda function, default 512.'''
        result = self._values.get("lambda_memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lambda_timeout(self) -> typing.Optional[jsii.Number]:
        '''Lambda Function Timeout in seconds, default 300.'''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the execution, same as that of StartExecution.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_input_bucket(self) -> typing.Optional[builtins.str]:
        '''location of input S3 objects - if left empty will generate rule for s3 access to all [*].'''
        result = self._values.get("s3_input_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_input_prefix(self) -> typing.Optional[builtins.str]:
        '''prefix for input S3 objects - if left empty will generate rule for s3 access to all [*].'''
        result = self._values.get("s3_input_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def textract_api(self) -> typing.Optional[builtins.str]:
        result = self._values.get("textract_api")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def textract_async_call_backoff_rate(self) -> typing.Optional[jsii.Number]:
        '''default is 1.1.'''
        result = self._values.get("textract_async_call_backoff_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def textract_async_call_interval(self) -> typing.Optional[jsii.Number]:
        '''default is 1.'''
        result = self._values.get("textract_async_call_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def textract_async_call_max_retries(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("textract_async_call_max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def textract_state_machine_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''how long can we wait for the process (default is 48 hours (60*48=2880)).'''
        result = self._values.get("textract_state_machine_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def workflow_tracing_enabled(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("workflow_tracing_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextractGenericSyncSfnTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TextractPOCDecider(
    aws_cdk.aws_stepfunctions.StateMachineFragment,
    metaclass=jsii.JSIIMeta,
    jsii_type="amazon-textract-idp-cdk-constructs.TextractPOCDecider",
):
    '''This construct takes in a manifest definition or a plain JSON with a s3Path:.

    example s3Path:
    {"s3Path": "s3://bucketname/prefix/image.png"}

    Then it generated the numberOfPages attribute and the mime on the context.
    The mime types checked against the supported mime types for Textract and if fails, will raise an Exception failing the workflow.

    Example (Python::

       decider_task_id = tcdk.TextractPOCDecider(
             self,
             f"InsuranceDecider",
       )
    '''

    def __init__(
        self,
        parent: constructs.Construct,
        id: builtins.str,
        *,
        lambda_memory_mb: typing.Optional[jsii.Number] = None,
        lambda_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param parent: -
        :param id: -
        :param lambda_memory_mb: memory of Lambda function (may need to increase for larger documents).
        :param lambda_timeout: 
        '''
        if __debug__:
            def stub(
                parent: constructs.Construct,
                id: builtins.str,
                *,
                lambda_memory_mb: typing.Optional[jsii.Number] = None,
                lambda_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TextractDPPOCDeciderProps(
            lambda_memory_mb=lambda_memory_mb, lambda_timeout=lambda_timeout
        )

        jsii.create(self.__class__, self, [parent, id, props])

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[aws_cdk.aws_stepfunctions.INextable]:
        '''The states to chain onto if this fragment is used.'''
        return typing.cast(typing.List[aws_cdk.aws_stepfunctions.INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> aws_cdk.aws_stepfunctions.State:
        '''The start state of this state machine fragment.'''
        return typing.cast(aws_cdk.aws_stepfunctions.State, jsii.get(self, "startState"))


__all__ = [
    "CSVToAuroraTask",
    "CSVToAuroraTaskProps",
    "ComprehendGenericSyncSfnTask",
    "ComprehendGenericSyncSfnTaskProps",
    "DocumentSplitter",
    "DocumentSplitterProps",
    "RDSAuroraServerless",
    "RDSAuroraServerlessProps",
    "SpacySfnTask",
    "SpacySfnTaskProps",
    "TextractA2ISfnTask",
    "TextractA2ISfnTaskProps",
    "TextractAsyncToJSON",
    "TextractAsyncToJSONProps",
    "TextractClassificationConfigurator",
    "TextractClassificationConfiguratorProps",
    "TextractDPPOCDeciderProps",
    "TextractGenerateCSV",
    "TextractGenerateCSVProps",
    "TextractGenericAsyncSfnTask",
    "TextractGenericAsyncSfnTaskProps",
    "TextractGenericSyncSfnTask",
    "TextractGenericSyncSfnTaskProps",
    "TextractPOCDecider",
]

publication.publish()
