'''
[![npm version](https://badge.fury.io/js/@pahud%2Fcdk-github-oidc.svg)](https://badge.fury.io/js/@pahud%2Fcdk-github-oidc)
[![PyPI version](https://badge.fury.io/py/pahud-cdk-github-oidc.svg)](https://badge.fury.io/py/pahud-cdk-github-oidc)
[![release](https://github.com/pahud/cdk-github-oidc/actions/workflows/release.yml/badge.svg)](https://github.com/pahud/cdk-github-oidc/actions/workflows/release.yml)

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

# cdk-github-oidc

Inspired by [aripalo/aws-cdk-github-oidc](https://github.com/aripalo/aws-cdk-github-oidc), this construct library allows you to create a `Github OpenID Connect Identity Provider` trust relationship with the `Provider` construct as well as federated IAM roles for one or multiple Github repositories.

This construct is still in `experimental` stage and may have breaking changes. However, we aim to make this library as simple as possible.

## Sample

```python
import { Provider } from '@pahud/cdk-github-oidc';

// create a new provider
const provider = new Provider(stack, 'GithubOpenIdConnectProvider')
// create an IAM role from this provider
provider.createRole('demo-role',
  // sharing this role across multiple repositories
  [
    { owner: 'octo-org', repo: 'first-repo' },
    { owner: 'octo-org', repo: 'second-repo' },
    { owner: 'octo-org', repo: 'third-repo' },
  ]
)
```

## Import the provider

Each AWS account can only have one GitHub OIDC identity provider. To import the existing one, use `Provider.fromAccount()`:

```python
// import the provider
const provider = Provider.fromAccount(stack, 'GithubOpenIdConnectProvider')
// create a iam role from the imported provider
provider.createRole(...)
```

## Workflow sample

```yaml
name: demo
on:
  workflow_dispatch: {}
jobs:
  deploy:
    name: Upload to Amazon S3
    runs-on: ubuntu-latest
    env:
      AWS_REGION: us-east-1
    permissions:
      id-token: write # needed to interact with GitHub's OIDC Token endpoint.
      contents: read
    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@master
      with:
        role-to-assume: ${{ secrets.AWS_ROLE_ARN_TO_ASSUME }}
        aws-region: ${{ env.AWS_REGION }}

    - name: Sync files to S3
      run: |
        aws s3 sync ./ s3://${{ secrets.AWS_BUCKET }}
```

## Projects using this library

* [pahud/gitpod-workspace](https://github.com/pahud/gitpod-workspace)
* [pahud/github-codespace](https://github.com/pahud/github-codespace)
* [pahud/vscode](https://github.com/pahud/vscode)

## Reference

* [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) from GitHub Docs
* [aripalo/aws-cdk-github-oidc](https://github.com/aripalo/aws-cdk-github-oidc) by [Ari Palo](https://github.com/aripalo)
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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import constructs as _constructs_77d1e7e8


class ProviderBase(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@pahud/cdk-github-oidc.ProviderBase",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bb3773158966ff7fb1ebad575da8fdb2bc7ff2cf5c4774cb2bcec8dfafa52c8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _aws_cdk_ceddda9d.ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createRole")
    def create_role(
        self,
        id: builtins.str,
        repo: typing.Sequence[typing.Union["RepositoryConfig", typing.Dict[builtins.str, typing.Any]]],
        *,
        assumed_by: _aws_cdk_aws_iam_ceddda9d.IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_iam_ceddda9d.PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> _aws_cdk_aws_iam_ceddda9d.Role:
        '''
        :param id: -
        :param repo: -
        :param assumed_by: The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_ids: List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d09d64c19149d51864a55e2496af85be51ff90e4e6779c023429f5f267e1c311)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        role_props = _aws_cdk_aws_iam_ceddda9d.RoleProps(
            assumed_by=assumed_by,
            description=description,
            external_ids=external_ids,
            inline_policies=inline_policies,
            managed_policies=managed_policies,
            max_session_duration=max_session_duration,
            path=path,
            permissions_boundary=permissions_boundary,
            role_name=role_name,
        )

        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Role, jsii.invoke(self, "createRole", [id, repo, role_props]))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProvider")
    @abc.abstractmethod
    def open_id_connect_provider(
        self,
    ) -> _aws_cdk_aws_iam_ceddda9d.IOpenIdConnectProvider:
        ...


class _ProviderBaseProxy(
    ProviderBase,
    jsii.proxy_for(_aws_cdk_ceddda9d.Resource), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="openIdConnectProvider")
    def open_id_connect_provider(
        self,
    ) -> _aws_cdk_aws_iam_ceddda9d.IOpenIdConnectProvider:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IOpenIdConnectProvider, jsii.get(self, "openIdConnectProvider"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ProviderBase).__jsii_proxy_class__ = lambda : _ProviderBaseProxy


@jsii.data_type(
    jsii_type="@pahud/cdk-github-oidc.RepositoryConfig",
    jsii_struct_bases=[],
    name_mapping={"owner": "owner", "repo": "repo", "filter": "filter"},
)
class RepositoryConfig:
    def __init__(
        self,
        *,
        owner: builtins.str,
        repo: builtins.str,
        filter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Represents a GitHub repository.

        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :param filter: The sub prefix string from the JWT token used to be validated by AWS. Appended after ``repo:${owner}/${repo}:`` in an IAM role trust relationship. The default value '*' indicates all branches and all tags from this repo. Example: repo:octo-org/octo-repo:ref:refs/heads/demo-branch - only allowed from ``demo-branch`` repo:octo-org/octo-repo:ref:refs/tags/demo-tag - only allowed from ``demo-tag``. repo:octo-org/octo-repo:pull_request - only allowed from the ``pull_request`` event. repo:octo-org/octo-repo:environment:Production - only allowd from ``Production`` environment name. Default: '*'
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49925946471aec49946c0945e0448af69c5c2bf8ed5d208106a8727c6f87fb62)
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "owner": owner,
            "repo": repo,
        }
        if filter is not None:
            self._values["filter"] = filter

    @builtins.property
    def owner(self) -> builtins.str:
        '''The owner of the repository.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> builtins.str:
        '''The name of the repository.'''
        result = self._values.get("repo")
        assert result is not None, "Required property 'repo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''The sub prefix string from the JWT token used to be validated by AWS.

        Appended after ``repo:${owner}/${repo}:``
        in an IAM role trust relationship. The default value '*' indicates all branches and all tags from this repo.

        Example:
        repo:octo-org/octo-repo:ref:refs/heads/demo-branch - only allowed from ``demo-branch``
        repo:octo-org/octo-repo:ref:refs/tags/demo-tag - only allowed from ``demo-tag``.
        repo:octo-org/octo-repo:pull_request - only allowed from the ``pull_request`` event.
        repo:octo-org/octo-repo:environment:Production - only allowd from ``Production`` environment name.

        :default: '*'

        :see: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Provider(
    ProviderBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@pahud/cdk-github-oidc.Provider",
):
    '''The Github OpenID Connect Provider.'''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30aa2508db9ab16418bf9159b4f1ab34b78924bfd6b4795befda48a0c40497e1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="fromAccount")
    @builtins.classmethod
    def from_account(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
    ) -> ProviderBase:
        '''import the existing provider.

        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1377ec2421449852e564b1939f566c3d7913ca3c4de49e5f9aac244f45453a04)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(ProviderBase, jsii.sinvoke(cls, "fromAccount", [scope, id]))

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProvider")
    def open_id_connect_provider(
        self,
    ) -> _aws_cdk_aws_iam_ceddda9d.IOpenIdConnectProvider:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IOpenIdConnectProvider, jsii.get(self, "openIdConnectProvider"))


__all__ = [
    "Provider",
    "ProviderBase",
    "RepositoryConfig",
]

publication.publish()

def _typecheckingstub__0bb3773158966ff7fb1ebad575da8fdb2bc7ff2cf5c4774cb2bcec8dfafa52c8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d09d64c19149d51864a55e2496af85be51ff90e4e6779c023429f5f267e1c311(
    id: builtins.str,
    repo: typing.Sequence[typing.Union[RepositoryConfig, typing.Dict[builtins.str, typing.Any]]],
    *,
    assumed_by: _aws_cdk_aws_iam_ceddda9d.IPrincipal,
    description: typing.Optional[builtins.str] = None,
    external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    inline_policies: typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_iam_ceddda9d.PolicyDocument]] = None,
    managed_policies: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IManagedPolicy]] = None,
    max_session_duration: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IManagedPolicy] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49925946471aec49946c0945e0448af69c5c2bf8ed5d208106a8727c6f87fb62(
    *,
    owner: builtins.str,
    repo: builtins.str,
    filter: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30aa2508db9ab16418bf9159b4f1ab34b78924bfd6b4795befda48a0c40497e1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1377ec2421449852e564b1939f566c3d7913ca3c4de49e5f9aac244f45453a04(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
