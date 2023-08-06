import json
from concurrent.futures import Future, ThreadPoolExecutor
from typing import Dict, List, Optional

import boto3


class BotAWSLambdaPlugin:
    def __init__(self, region_name: str = 'us-east-1', use_credentials_file: Optional[bool] = True,
                 access_key_id: Optional[str] = None, secret_access_key: Optional[str] = None) -> None:
        """
        BotAWSLambdaPlugin

        Args:
            region_name (str): Default region when creating new connections.
            use_credentials_file (bool, optional): If set to True will make
                authentication via AWS credentials file.
            access_key_id (str, optional): AWS access key ID.
            secret_access_key (str, optional): AWS secret access key.
        """
        if use_credentials_file:
            self._client = boto3.client(service_name='lambda')
        else:
            self._client = boto3.client(
                service_name='lambda',
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name
            )

    @property
    def lambda_client(self):
        """
        Returns the aws client instance.

        Returns:
            boto3_instance: The aws client instance.
        """
        return self._client

    def list_functions(self, **kwargs) -> List[Dict]:
        """
        List all functions.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_functions)

        Returns:
            functions: The list of functions.
        """  # noqa
        response = self._client.list_functions(**kwargs)["Functions"]
        return [{
            'FunctionName': function["FunctionName"],
            'Runtime': function["Runtime"],
            'Timeout': function["Timeout"],
            'MemorySize': function["MemorySize"],
            'LastModified': function["LastModified"],
            'Version': function["Version"],
            'PackageType': function["PackageType"],
            'Architectures': function["Architectures"],
        } for function in response]

    def get_function(self, function_name: str, **kwargs) -> Dict[str, str]:
        """
        Get function info.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_function)

        Args:
            function_name (str): The function name-only or name with alias.
                my-function (name-only), my-function:v1 (with alias).

        Returns:
            function_info: The function info.
        """  # noqa
        response = self._client.get_function(
            FunctionName=function_name,
            **kwargs
        )["Configuration"]

        return {
            "FunctionName": response["FunctionName"],
            "FunctionArn": response["FunctionArn"],
            "Runtime": response["Runtime"],
            "Role": response["Role"],
            "Handler": response["Handler"],
            "Description": response["Description"],
            "Timeout": response["Timeout"],
            "MemorySize": response["MemorySize"],
            "LastModified": response["LastModified"],
            "Version": response["Version"],
            "PackageType": response["PackageType"],
            "Architectures": response["Architectures"],
        }

    def invoke_function(self, function_name: str, payload: Optional[Dict] = None, **kwargs):
        """
        Invoke lambda function.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke)

        Args:
            function_name (str): The function name-only or name with alias.
                my-function (name-only), my-function:v1 (with alias).
            payload (Dict, optional): The JSON that you want to provide to your Lambda function as input.

        Returns:
            response: The response of lambda execution.
        """  # noqa
        response = self._client.invoke(
            FunctionName=function_name,
            Payload=json.dumps(payload),
            **kwargs
        )

        return {
            "status-code": response["ResponseMetadata"]["HTTPStatusCode"],
            "headers": response["ResponseMetadata"]["HTTPHeaders"],
            "body": response["Payload"].read().decode("utf-8")
        }

    def future_invoke_function(self, function_name: str, payload: Optional[Dict] = None, **kwargs) -> Future:
        """
        Running lambda function and getting response in the future.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke)

        Args:
            function_name (str): The function name-only or name with alias.
                my-function (name-only), my-function:v1 (with alias).
            payload (Dict, optional): The JSON that you want to provide to your Lambda function as input.

        Returns:
            future: The future instance.
        """  # noqa
        return ThreadPoolExecutor().submit(self.invoke_function, function_name, payload, **kwargs)

    def list_aliases(self, function_name: str, **kwargs) -> List[Dict]:
        """
        Returns a list of aliases for a Lambda function.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_aliases)

        Args:
            function_name (str): The function name-only.

        Returns:
            aliases: A list of aliases for a Lambda function.
        """  # noqa
        return self._client.list_aliases(FunctionName=function_name, **kwargs)["Aliases"]

    def get_alias(self, function_name: str, alias_name: str, **kwargs):
        """
        Get alias info.

        [See Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_alias)

        Args:
            function_name (str): The function name-only.
            alias_name (str): The name of the alias.

        Returns:
            info: The alias info.
        """  # noqa
        response = self._client.get_alias(
            FunctionName=function_name,
            Name=alias_name,
            **kwargs
        )

        return {
            'AliasArn': response['AliasArn'],
            'Name': response['Name'],
            "FunctionVersion": response["FunctionVersion"],
            "Description": response["Description"],
            "RevisionId": response["RevisionId"]
        }
