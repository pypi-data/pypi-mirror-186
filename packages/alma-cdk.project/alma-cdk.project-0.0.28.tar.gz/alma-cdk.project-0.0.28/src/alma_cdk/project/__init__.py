'''
<br/><br/><br/>

🚧 **Work-in-Progress**: Breaking changes may occur at any given point during `v0.x`.

<br/><br/><br/>

<div align="center">
	<br/>
	<br/>
  <h1>
	<img width="300" src="assets/alma-cdk-project.svg" alt="Alma CDK Project" />
  <br/>
  <br/>
  </h1>

```sh
npm i -D @alma-cdk/project
```

  <div align="left">

Opinionated CDK “framework” with constructs & utilities for:

* deploying multiple environments to multiple accounts (with many-to-many relationship)
* managing account configuration through standardized props (no more random config files)
* querying account and/or environment specific information within your CDK code
* enabling dynamic & short-lived “feature-environments”
* enabling well-defined tagging
* providing structure & common conventions to CDK projects
* choosing the target account & environment by passing in runtime context:

  ```sh
  npx cdk deploy -c account=dev -c environment=feature/abc-123
  ```

  ... which means you don't need to define all the possibile environments ahead of time!

  </div>
  <br/>
</div>

## Account Strategies

Depending on the use case, you may choose a configuration between 1-3 AWS accounts with the following environments:

1. **Shared account (`shared`)**:

   ![default-multi](assets/accounts-1x.svg)
   <br/>
2. **Multi-account (`dev`+`prod`)***– RECOMMENDED*:

   ![default-multi](assets/accounts-2x.svg)
   <br/>

<br/>
</details>

1. **Multi-account (`dev`+`preprod`+`prod`)**:

   ![default-multi](assets/accounts-3x.svg)
   <br/>

<br/>

## Getting Started

Steps required to define a *environmental* project resources; At first, it might seem complex but once you get into the habbit of defining your projects this way it starts to make sense:

1. Choose your [Account Strategy](#account-strategies)
2. Initialize a new `Project` instead of `cdk.App`:

   ```python
   // bin/app.ts
   import { Project, AccountStrategy } from '@alma-cdk/project';

   const project = new Project({
     // Basic info, you could also read these from package.json if you want
     name: 'my-cool-project',
     author: {
       organization: 'Acme Corp',
       name: 'Mad Scientists',
       email: 'mad.scientists@acme.example.com',
     },

     // If not set, defaults to one of: $CDK_DEFAULT_REGION, $AWS_REGION or us-east-1
     defaultRegion: 'eu-west-1',

     // Configures the project to use 2 AWS accounts (recommended)
     accounts: AccountStrategy.two({
       dev: {
         id: '111111111111',
         config: {
           // whatever you want here as [string]: any
           baseDomain: 'example.net',
         },
       },
       prod: {
         id: '222222222222',
         config: {
           // whatever you want here as [string]: any
           baseDomain: 'example.com',
         },
       },
     }),
   })
   ```
3. Define a stack which `extends SmartStack` with resources:

   ```python
   // lib/my-stack.ts
   import { Construct } from 'constructs';
   import { StackProps, RemovalPolicy } from 'aws-cdk-lib';
   import { SmartStack, Name, UrlName, PathName, EC } from '@alma-cdk/project';

   export class MyStack extends SmartStack {
     constructor(scope: Construct, id: string, props?: StackProps) {
       super(scope, id, props);

       new dynamodb.Table(this, 'Table', {
         removalPolicy: EC.isStable(this) ? RemovalPolicy.RETAIN : RemovalPolicy.DESTROY,

         tableName: Name.it(this, 'MyTable'),
         partitionKey: {
           type: dynamodb.AttributeType.STRING,
           name: 'pk',
         },
         // StagingMyTable
       });

       new events.EventBus(this, 'EventBus', {
         eventBusName: Name.withProject(this, 'MyEventBus'),
         // MyCoolProjectStagingMyEventBus
       });

       new s3.Bucket(this, 'Bucket', {

         removalPolicy: EC.isStable(this) ? RemovalPolicy.RETAIN : RemovalPolicy.DESTROY,
         autoDeleteObjects: EC.isStable(this) ? false : true,

         bucketName: UrlName.globally(this, 'MyBucket'),
         // acme-corp-my-cool-project-feature-foo-bar-my-bucket
       });

       new ssm.StringParameter(this, 'Parameter', {
         stringValue: 'Foo',
         tier: ssm.ParameterTier.ADVANCED,
         parameterName: PathName.withProject(this, 'MyNamespace/MyParameter'),
         // /MyCoolProject/Staging/MyNamespace/MyParameter
       });
     }
   }
   ```
4. Define a new *environmental* which `extends EnvironmentWrapper` and initialize all your environmental `SmartStack` stacks within:

   ```python
   // lib/environment.ts
   import { Construct } from 'constructs';
   import { EnvironmentWrapper } from '@alma-cdk/project';
   import { MyStack } from './my-stack';

   export class Environment extends EnvironmentWrapper {
     constructor(scope: Construct) {
       super(scope);
       new MyStack(this, 'MyStack', { description: 'This is required' });
     }
   }
   ```

   Resulting Stack properties (given `environment=staging`):

   |        Property         |                    Example value                     |
   | :---------------------- | :--------------------------------------------------- |
   | `stackName`             | `"MyCoolProject-Environment-Staging-MyExampleStack"` |
   | `terminationProtection` | `true`                                               |
   | `env.account`           | `"111111111111"`                                     |
   | `env.region`            | `"eu-west-1"`                                        |

   Resulting Tags for the Stack and its resources (given `environment=staging`):

   |        Property         |           Example value           |
   | :---------------------- | :-------------------------------- |
   | `Account`               | `dev`                             |
   | `Environment`           | `staging`                         |
   | `Project`               | `my-cool-project`                 |
   | `Author`                | `Mad Scientists`                  |
   | `Organization`          | `Acme Corp`                       |
   | `Contact`               | `mad.scientists@acme.example.com` |
5. Finally initialize the environment with the `Project` scope:

   ```python
   // bin/app.ts
   import { Project, Accounts } from '@alma-cdk/project';
   import { Environment } from '../lib/environment';

   const project = new Project({/* removed for brevity, see step 1 */})

   new Environment(project);
   ```

<br/>

## Documentation

See detailed documentation for specific classes & methods at [constructs.dev](http://constructs.dev/packages/@alma-cdk/project).

Generally speaking you would be most interested in the following:

* Project
* AccountStrategy
* SmartStack
* AccountWrapper & EnvironmentWrapper
* AccountContext (AC)
* EnvironmentContext (EC)
* Name / UrlName / PathName
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
import constructs


@jsii.data_type(
    jsii_type="@alma-cdk/project.Account",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "config": "config", "environments": "environments"},
)
class Account:
    def __init__(
        self,
        *,
        id: builtins.str,
        config: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        environments: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) AWS account configuration.

        :param id: (experimental) AWS Account ID.
        :param config: (experimental) AWS account specific configuration. For example VPC IDs (for existing VPCs), Direct Connect Gateway IDs, apex domain names (for Route53 Zone lookups), etc. Basically configuration for resources that are defined outside of this CDK application.
        :param environments: (experimental) List of accepted environments for the given account. List of strings or strings representing regexp initialization (passed onto ``new Regexp("^"+environment+"$", "i")``).

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                id: builtins.str,
                config: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                environments: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument environments", value=environments, expected_type=type_hints["environments"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if config is not None:
            self._values["config"] = config
        if environments is not None:
            self._values["environments"] = environments

    @builtins.property
    def id(self) -> builtins.str:
        '''(experimental) AWS Account ID.

        :stability: experimental

        Example::

            '123456789012'
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) AWS account specific configuration.

        For example VPC IDs (for existing VPCs), Direct Connect Gateway IDs, apex domain names (for Route53 Zone lookups), etc. Basically configuration for resources that are defined outside of this CDK application.

        :stability: experimental

        Example::

            {
              dev: {
                id: '111111111111',
                config: {
                  baseDomain: 'example.net',
                },
              },
              prod: {
                id: '222222222222',
                config: {
                  baseDomain: 'example.com',
                },
              },
            },
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def environments(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of accepted environments for the given account.

        List of strings or strings representing regexp initialization (passed onto ``new Regexp("^"+environment+"$", "i")``).

        :stability: experimental

        Example::

            ["development", "feature/.*"]
        '''
        result = self._values.get("environments")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Account(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/project.AccountConfiguration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "config": "config"},
)
class AccountConfiguration:
    def __init__(
        self,
        *,
        id: builtins.str,
        config: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''(experimental) Interface for a single account type configuration.

        :param id: 
        :param config: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                id: builtins.str,
                config: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if config is not None:
            self._values["config"] = config

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccountContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.AccountContext",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="getAccountConfig")
    @builtins.classmethod
    def get_account_config(
        cls,
        scope: constructs.Construct,
        key: builtins.str,
    ) -> typing.Any:
        '''
        :param scope: -
        :param key: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "getAccountConfig", [scope, key]))

    @jsii.member(jsii_name="getAccountId")
    @builtins.classmethod
    def get_account_id(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getAccountId", [scope]))

    @jsii.member(jsii_name="getAccountType")
    @builtins.classmethod
    def get_account_type(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getAccountType", [scope]))

    @jsii.member(jsii_name="isDev")
    @builtins.classmethod
    def is_dev(cls, scope: constructs.Construct) -> builtins.bool:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isDev", [scope]))

    @jsii.member(jsii_name="isMock")
    @builtins.classmethod
    def is_mock(cls, scope: constructs.Construct) -> builtins.bool:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isMock", [scope]))

    @jsii.member(jsii_name="isPreProd")
    @builtins.classmethod
    def is_pre_prod(cls, scope: constructs.Construct) -> builtins.bool:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isPreProd", [scope]))

    @jsii.member(jsii_name="isProd")
    @builtins.classmethod
    def is_prod(cls, scope: constructs.Construct) -> builtins.bool:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isProd", [scope]))

    @jsii.member(jsii_name="isShared")
    @builtins.classmethod
    def is_shared(cls, scope: constructs.Construct) -> builtins.bool:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isShared", [scope]))


class AccountStrategy(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@alma-cdk/project.AccountStrategy",
):
    '''(experimental) Use static methods of ``AccountStrategy`` abstract class to define your account strategy.

    Available strategies are:

    - One Account: ``shared``
    - Two Accounts: ``dev``+``prod`` – *recommended*
    - Three Accounts: ``dev``+``preprod``+``prod``

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="one")
    @builtins.classmethod
    def one(
        cls,
        *,
        shared: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
    ) -> typing.Mapping[builtins.str, Account]:
        '''(experimental) Enables single account strategy.

        1. ``shared`` account with environments:

           - development
           - feature/*
           - test
           - qaN
           - staging
           - preproduction
           - production

        :param shared: 
        :param mock: 

        :stability: experimental

        Example::

            AccountStrategy.one({
              shared: {
                id: '111111111111',
              },
            }),
        '''
        props = AccountStrategyOneProps(shared=shared, mock=mock)

        return typing.cast(typing.Mapping[builtins.str, Account], jsii.sinvoke(cls, "one", [props]))

    @jsii.member(jsii_name="three")
    @builtins.classmethod
    def three(
        cls,
        *,
        dev: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        preprod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        prod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
    ) -> typing.Mapping[builtins.str, Account]:
        '''(experimental) Enables triple account strategy.

        1. ``dev`` account with environments:

           - development
           - feature/*
           - test
           - staging

        2. ``preprod`` account with environments:

           - qaN
           - preproduction

        3. ``prod`` account with environments:

           - production

        :param dev: 
        :param preprod: 
        :param prod: 
        :param mock: 

        :stability: experimental

        Example::

            AccountStrategy.three({
              dev: {
                id: '111111111111',
              },
              preprod: {
                id: '222222222222',
              },
              prod: {
                id: '333333333333',
              },
            }),
        '''
        props = AccountStrategyThreeProps(
            dev=dev, preprod=preprod, prod=prod, mock=mock
        )

        return typing.cast(typing.Mapping[builtins.str, Account], jsii.sinvoke(cls, "three", [props]))

    @jsii.member(jsii_name="two")
    @builtins.classmethod
    def two(
        cls,
        *,
        dev: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        prod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
    ) -> typing.Mapping[builtins.str, Account]:
        '''(experimental) Enables dual account strategy.

        1. ``dev`` account with environments:

           - development
           - feature/*
           - test
           - qaN
           - staging

        2. ``prod`` account with environments:

           - preproduction
           - production

        :param dev: 
        :param prod: 
        :param mock: 

        :stability: experimental

        Example::

            AccountStrategy.two({
              dev: {
                id: '111111111111',
              },
              prod: {
                id: '222222222222',
              },
            }),
        '''
        props = AccountStrategyTwoProps(dev=dev, prod=prod, mock=mock)

        return typing.cast(typing.Mapping[builtins.str, Account], jsii.sinvoke(cls, "two", [props]))


class _AccountStrategyProxy(AccountStrategy):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AccountStrategy).__jsii_proxy_class__ = lambda : _AccountStrategyProxy


@jsii.data_type(
    jsii_type="@alma-cdk/project.AccountStrategyOneProps",
    jsii_struct_bases=[],
    name_mapping={"shared": "shared", "mock": "mock"},
)
class AccountStrategyOneProps:
    def __init__(
        self,
        *,
        shared: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Props ``AccountStrategy.one``.

        :param shared: 
        :param mock: 

        :stability: experimental
        '''
        if isinstance(shared, dict):
            shared = AccountConfiguration(**shared)
        if isinstance(mock, dict):
            mock = AccountConfiguration(**mock)
        if __debug__:
            def stub(
                *,
                shared: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
                mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument shared", value=shared, expected_type=type_hints["shared"])
            check_type(argname="argument mock", value=mock, expected_type=type_hints["mock"])
        self._values: typing.Dict[str, typing.Any] = {
            "shared": shared,
        }
        if mock is not None:
            self._values["mock"] = mock

    @builtins.property
    def shared(self) -> AccountConfiguration:
        '''
        :stability: experimental
        '''
        result = self._values.get("shared")
        assert result is not None, "Required property 'shared' is missing"
        return typing.cast(AccountConfiguration, result)

    @builtins.property
    def mock(self) -> typing.Optional[AccountConfiguration]:
        '''
        :stability: experimental
        '''
        result = self._values.get("mock")
        return typing.cast(typing.Optional[AccountConfiguration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountStrategyOneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/project.AccountStrategyThreeProps",
    jsii_struct_bases=[],
    name_mapping={"dev": "dev", "preprod": "preprod", "prod": "prod", "mock": "mock"},
)
class AccountStrategyThreeProps:
    def __init__(
        self,
        *,
        dev: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        preprod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        prod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Props ``AccountStrategy.three``.

        :param dev: 
        :param preprod: 
        :param prod: 
        :param mock: 

        :stability: experimental
        '''
        if isinstance(dev, dict):
            dev = AccountConfiguration(**dev)
        if isinstance(preprod, dict):
            preprod = AccountConfiguration(**preprod)
        if isinstance(prod, dict):
            prod = AccountConfiguration(**prod)
        if isinstance(mock, dict):
            mock = AccountConfiguration(**mock)
        if __debug__:
            def stub(
                *,
                dev: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
                preprod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
                prod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
                mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dev", value=dev, expected_type=type_hints["dev"])
            check_type(argname="argument preprod", value=preprod, expected_type=type_hints["preprod"])
            check_type(argname="argument prod", value=prod, expected_type=type_hints["prod"])
            check_type(argname="argument mock", value=mock, expected_type=type_hints["mock"])
        self._values: typing.Dict[str, typing.Any] = {
            "dev": dev,
            "preprod": preprod,
            "prod": prod,
        }
        if mock is not None:
            self._values["mock"] = mock

    @builtins.property
    def dev(self) -> AccountConfiguration:
        '''
        :stability: experimental
        '''
        result = self._values.get("dev")
        assert result is not None, "Required property 'dev' is missing"
        return typing.cast(AccountConfiguration, result)

    @builtins.property
    def preprod(self) -> AccountConfiguration:
        '''
        :stability: experimental
        '''
        result = self._values.get("preprod")
        assert result is not None, "Required property 'preprod' is missing"
        return typing.cast(AccountConfiguration, result)

    @builtins.property
    def prod(self) -> AccountConfiguration:
        '''
        :stability: experimental
        '''
        result = self._values.get("prod")
        assert result is not None, "Required property 'prod' is missing"
        return typing.cast(AccountConfiguration, result)

    @builtins.property
    def mock(self) -> typing.Optional[AccountConfiguration]:
        '''
        :stability: experimental
        '''
        result = self._values.get("mock")
        return typing.cast(typing.Optional[AccountConfiguration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountStrategyThreeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/project.AccountStrategyTwoProps",
    jsii_struct_bases=[],
    name_mapping={"dev": "dev", "prod": "prod", "mock": "mock"},
)
class AccountStrategyTwoProps:
    def __init__(
        self,
        *,
        dev: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        prod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
        mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Props ``AccountStrategy.two``.

        :param dev: 
        :param prod: 
        :param mock: 

        :stability: experimental
        '''
        if isinstance(dev, dict):
            dev = AccountConfiguration(**dev)
        if isinstance(prod, dict):
            prod = AccountConfiguration(**prod)
        if isinstance(mock, dict):
            mock = AccountConfiguration(**mock)
        if __debug__:
            def stub(
                *,
                dev: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
                prod: typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]],
                mock: typing.Optional[typing.Union[AccountConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dev", value=dev, expected_type=type_hints["dev"])
            check_type(argname="argument prod", value=prod, expected_type=type_hints["prod"])
            check_type(argname="argument mock", value=mock, expected_type=type_hints["mock"])
        self._values: typing.Dict[str, typing.Any] = {
            "dev": dev,
            "prod": prod,
        }
        if mock is not None:
            self._values["mock"] = mock

    @builtins.property
    def dev(self) -> AccountConfiguration:
        '''
        :stability: experimental
        '''
        result = self._values.get("dev")
        assert result is not None, "Required property 'dev' is missing"
        return typing.cast(AccountConfiguration, result)

    @builtins.property
    def prod(self) -> AccountConfiguration:
        '''
        :stability: experimental
        '''
        result = self._values.get("prod")
        assert result is not None, "Required property 'prod' is missing"
        return typing.cast(AccountConfiguration, result)

    @builtins.property
    def mock(self) -> typing.Optional[AccountConfiguration]:
        '''
        :stability: experimental
        '''
        result = self._values.get("mock")
        return typing.cast(typing.Optional[AccountConfiguration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountStrategyTwoProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccountType(metaclass=jsii.JSIIMeta, jsii_type="@alma-cdk/project.AccountType"):
    '''(experimental) Internal class to handle set/get operations for Account Type.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="get")
    @builtins.classmethod
    def get(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "get", [scope]))

    @jsii.member(jsii_name="matchFromEnvironment")
    @builtins.classmethod
    def match_from_environment(
        cls,
        scope: constructs.Construct,
        accounts: typing.Mapping[builtins.str, typing.Union[Account, typing.Dict[str, typing.Any]]],
        environment_type: builtins.str,
    ) -> builtins.str:
        '''
        :param scope: -
        :param accounts: -
        :param environment_type: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                accounts: typing.Mapping[builtins.str, typing.Union[Account, typing.Dict[str, typing.Any]]],
                environment_type: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
            check_type(argname="argument environment_type", value=environment_type, expected_type=type_hints["environment_type"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "matchFromEnvironment", [scope, accounts, environment_type]))

    @jsii.member(jsii_name="set")
    @builtins.classmethod
    def set(cls, scope: constructs.Construct, account_type: builtins.str) -> None:
        '''
        :param scope: -
        :param account_type: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, account_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument account_type", value=account_type, expected_type=type_hints["account_type"])
        return typing.cast(None, jsii.sinvoke(cls, "set", [scope, account_type]))


class AccountWrapper(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.AccountWrapper",
):
    '''(experimental) Wrapper for account-level stacks.

    :stability: experimental
    '''

    def __init__(self, scope: constructs.Construct) -> None:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        jsii.create(self.__class__, self, [scope])


@jsii.data_type(
    jsii_type="@alma-cdk/project.Author",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "email": "email", "organization": "organization"},
)
class Author:
    def __init__(
        self,
        *,
        name: builtins.str,
        email: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Author information.

        I.e. who owns/develops this project/service.

        :param name: (experimental) Human-readable name for the team/contact responsible for this project/service.
        :param email: (experimental) Email address for the team/contact responsible for this project/service.
        :param organization: (experimental) Human-readable name for the organization responsible for this project/service.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                email: typing.Optional[builtins.str] = None,
                organization: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if email is not None:
            self._values["email"] = email
        if organization is not None:
            self._values["organization"] = organization

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) Human-readable name for the team/contact responsible for this project/service.

        :stability: experimental

        Example::

            'Mad Scientists'
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''(experimental) Email address for the team/contact responsible for this project/service.

        :stability: experimental

        Example::

            'mad.scientists@acme.example.com'
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''(experimental) Human-readable name for the organization responsible for this project/service.

        :stability: experimental

        Example::

            'Acme Corp'
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Author(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvRegExp(metaclass=jsii.JSIIMeta, jsii_type="@alma-cdk/project.EnvRegExp"):
    '''
    :stability: experimental
    '''

    def __init__(self, base: builtins.str) -> None:
        '''
        :param base: -

        :stability: experimental
        '''
        if __debug__:
            def stub(base: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
        jsii.create(self.__class__, self, [base])

    @jsii.member(jsii_name="test")
    def test(self, value: builtins.str) -> builtins.bool:
        '''
        :param value: -

        :stability: experimental
        '''
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.bool, jsii.invoke(self, "test", [value]))


@jsii.enum(jsii_type="@alma-cdk/project.EnvironmentCategory")
class EnvironmentCategory(enum.Enum):
    '''(experimental) Availalbe Enviroment Categories.

    Categories are useful grouping to make distinction between ``stable``
    environments (``staging`` & ``production``) from ``feature`` or ``verification``
    environments (such as ``test`` or ``preproduction``).

    :stability: experimental
    '''

    MOCK = "MOCK"
    '''
    :stability: experimental
    '''
    DEVELOPMENT = "DEVELOPMENT"
    '''
    :stability: experimental
    '''
    FEATURE = "FEATURE"
    '''
    :stability: experimental
    '''
    VERIFICATION = "VERIFICATION"
    '''
    :stability: experimental
    '''
    STABLE = "STABLE"
    '''
    :stability: experimental
    '''


class EnvironmentContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.EnvironmentContext",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="getCategory")
    @builtins.classmethod
    def get_category(cls, scope: constructs.Construct) -> EnvironmentCategory:
        '''(experimental) Get Environment Category.

        Categories are useful grouping to make distinction between ``stable``
        environments (``staging`` & ``production``) from ``feature`` or ``verification``
        environments (such as ``test`` or ``preproduction``).

        :param scope: Construct.

        :return: Environment Category

        :stability: experimental

        Example::

            'mock'
            'development'
            'feature'
            'verification'
            'stable'
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(EnvironmentCategory, jsii.sinvoke(cls, "getCategory", [scope]))

    @jsii.member(jsii_name="getFeatureInfo")
    @builtins.classmethod
    def get_feature_info(cls, scope: constructs.Construct) -> builtins.str:
        '''(experimental) Get Feature Info.

        If environment belongs to ``feature`` category,
        this will return a string describing the feature (sting after ``feature/``-prefix).

        If environment is not a feature environment, will return an empty string.

        :param scope: Construct.

        :return: string indicating the feature this environment relates to, if not feature environment returns an empty string

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getFeatureInfo", [scope]))

    @jsii.member(jsii_name="getLabel")
    @builtins.classmethod
    def get_label(cls, scope: constructs.Construct) -> "EnvironmentLabel":
        '''(experimental) Get Environment Label.

        Labels are useful since Environment Name can be complex,
        such as ``feature/foo-bar`` or ``qa3``,
        but we need to be able to “label” all ``feature/*`` and ``qaN`` environments
        as either ``feature`` or ``qa``.

        :param scope: Construct.

        :return: Environment Label

        :stability: experimental

        Example::

            'mock'
            'development'
            'feature'
            'test'
            'staging'
            'qa'
            'preproduction'
            'production'
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("EnvironmentLabel", jsii.sinvoke(cls, "getLabel", [scope]))

    @jsii.member(jsii_name="getName")
    @builtins.classmethod
    def get_name(cls, scope: constructs.Construct) -> builtins.str:
        '''(experimental) Get Environment Name.

        :param scope: Construct.

        :return: Environment Name (as given via ``--context environment``)

        :stability: experimental

        Example::

            'mock1'
            'mock2'
            'mock3'
            'development'
            'feature/foo-bar'
            'feature/ABC-123/new-stuff'
            'test'
            'staging'
            'qa1'
            'qa2'
            'qa3'
            'preproduction'
            'production'
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getName", [scope]))

    @jsii.member(jsii_name="getUrlName")
    @builtins.classmethod
    def get_url_name(cls, scope: constructs.Construct) -> builtins.str:
        '''(experimental) Get Environment URL/DNS Compatible Name.

        :param scope: Construct.

        :return: Environment URL/DNS Compatible Name (as given via ``--context environment`` but ``param-cased``)

        :stability: experimental

        Example::

            'mock1'
            'mock2'
            'mock3'
            'development'
            'feature-foo-bar'
            'feature-abc-123-new-stuff'
            'test'
            'staging'
            'qa1'
            'qa2'
            'qa3'
            'preproduction'
            'production'
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getUrlName", [scope]))

    @jsii.member(jsii_name="isDevelopment")
    @builtins.classmethod
    def is_development(cls, scope: constructs.Construct) -> builtins.bool:
        '''(experimental) Check if Environment is part of ``development`` category.

        Returns true for ``development``, otherwise ``false``.

        :param scope: Construct.

        :return: boolean indicating does Environment belong to ``development`` category

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isDevelopment", [scope]))

    @jsii.member(jsii_name="isFeature")
    @builtins.classmethod
    def is_feature(cls, scope: constructs.Construct) -> builtins.bool:
        '''(experimental) Check if Environment is part of ``feature`` category.

        Returns ``true`` for environments with name beginning with ``feature/``-prefix, otherwise ``false``.

        :param scope: Construct.

        :return: boolean indicating does Environment belong to ``feature`` category

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isFeature", [scope]))

    @jsii.member(jsii_name="isMock")
    @builtins.classmethod
    def is_mock(cls, scope: constructs.Construct) -> builtins.bool:
        '''(experimental) Check if Environment is part of ``mock`` category.

        :param scope: Construct.

        :return: boolean indicating does Environment belong to ``mock`` category

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isMock", [scope]))

    @jsii.member(jsii_name="isStable")
    @builtins.classmethod
    def is_stable(cls, scope: constructs.Construct) -> builtins.bool:
        '''(experimental) Check if Environment is part of ``stable`` category.

        Returns ``true`` for ``staging`` & ``production``, otherwise ``false``.

        :param scope: Construct.

        :return: boolean indicating does Environment belong to ``stable`` category

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStable", [scope]))

    @jsii.member(jsii_name="isVerification")
    @builtins.classmethod
    def is_verification(cls, scope: constructs.Construct) -> builtins.bool:
        '''(experimental) Check if Environment is part of ``verification`` category.

        Returns ``true`` for ``test`` & ``preproduction``, otherwise ``false``.

        :param scope: Construct.

        :return: boolean indicating does Environment belong to ``verification`` category

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isVerification", [scope]))


@jsii.enum(jsii_type="@alma-cdk/project.EnvironmentLabel")
class EnvironmentLabel(enum.Enum):
    '''(experimental) Available Environment Labels.

    Labels are useful since Environment Name can be complex,
    such as ``feature/foo-bar`` or ``qa3``,
    but we need to be able to “label” all ``feature/*`` and ``qaN`` environments
    as either ``feature`` or ``qa``.

    :stability: experimental
    '''

    MOCK = "MOCK"
    '''
    :stability: experimental
    '''
    DEVELOPMENT = "DEVELOPMENT"
    '''
    :stability: experimental
    '''
    FEATURE = "FEATURE"
    '''
    :stability: experimental
    '''
    TEST = "TEST"
    '''
    :stability: experimental
    '''
    STAGING = "STAGING"
    '''
    :stability: experimental
    '''
    QA = "QA"
    '''
    :stability: experimental
    '''
    PREPRODUCTION = "PREPRODUCTION"
    '''
    :stability: experimental
    '''
    PRODUCTION = "PRODUCTION"
    '''
    :stability: experimental
    '''


class EnvironmentType(
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.EnvironmentType",
):
    '''(experimental) Internal class to handle set/get operations for Environment Type.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="get")
    @builtins.classmethod
    def get(
        cls,
        scope: constructs.Construct,
        allowed_environments: typing.Sequence[builtins.str],
    ) -> builtins.str:
        '''
        :param scope: -
        :param allowed_environments: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                allowed_environments: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument allowed_environments", value=allowed_environments, expected_type=type_hints["allowed_environments"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "get", [scope, allowed_environments]))

    @jsii.member(jsii_name="set")
    @builtins.classmethod
    def set(cls, scope: constructs.Construct, environment_type: builtins.str) -> None:
        '''
        :param scope: -
        :param environment_type: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                environment_type: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument environment_type", value=environment_type, expected_type=type_hints["environment_type"])
        return typing.cast(None, jsii.sinvoke(cls, "set", [scope, environment_type]))

    @jsii.member(jsii_name="tryGet")
    @builtins.classmethod
    def try_get(cls, scope: constructs.Construct) -> typing.Optional[builtins.str]:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(typing.Optional[builtins.str], jsii.sinvoke(cls, "tryGet", [scope]))


class EnvironmentWrapper(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.EnvironmentWrapper",
):
    '''(experimental) Wrapper for environmental stacks.

    :stability: experimental
    '''

    def __init__(self, scope: constructs.Construct) -> None:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        jsii.create(self.__class__, self, [scope])


class Name(metaclass=jsii.JSIIAbstractClass, jsii_type="@alma-cdk/project.Name"):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="globally")
    @builtins.classmethod
    def globally(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''(experimental) PascalCase naming with global prefixes (org, project…).

        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "globally", [scope, base_name, props]))

    @jsii.member(jsii_name="it")
    @builtins.classmethod
    def it(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "it", [scope, base_name, props]))

    @jsii.member(jsii_name="withProject")
    @builtins.classmethod
    def with_project(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "withProject", [scope, base_name, props]))


class _NameProxy(Name):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Name).__jsii_proxy_class__ = lambda : _NameProxy


@jsii.data_type(
    jsii_type="@alma-cdk/project.NameProps",
    jsii_struct_bases=[],
    name_mapping={"max_length": "maxLength", "trim": "trim"},
)
class NameProps:
    def __init__(
        self,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_length", value=max_length, expected_type=type_hints["max_length"])
            check_type(argname="argument trim", value=trim, expected_type=type_hints["trim"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_length is not None:
            self._values["max_length"] = max_length
        if trim is not None:
            self._values["trim"] = trim

    @builtins.property
    def max_length(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def trim(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("trim")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NameProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Project(
    aws_cdk.App,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.Project",
):
    '''(experimental) High-level wrapper for ``cdk.App`` with specific requirements for props.

    Use it like you would ``cdk.App`` and assign stacks into it.

    :stability: experimental

    Example::

        // new Project instead of new App
        const project = new Project({
          name: 'my-cool-project',
          author: {
            organization: 'Acme Corp',
            name: 'Mad Scientists',
            email: 'mad.scientists@acme.example.com',
        },
        defaultRegion: 'eu-west-1', // defaults to one of: $CDK_DEFAULT_REGION, $AWS_REGION or us-east-1
        accounts: {
        dev: {
         id: '111111111111',
         environments: ['development', 'feature/.*', 'staging'],
         config: {
           baseDomain: 'example.net',
         },
        },
        prod: {
         id: '222222222222',
         environments: ['production'],
         config: {
           baseDomain: 'example.com',
         },
        },
        },
        })
    '''

    def __init__(
        self,
        *,
        accounts: typing.Mapping[builtins.str, typing.Union[Account, typing.Dict[str, typing.Any]]],
        author: typing.Union[Author, typing.Dict[str, typing.Any]],
        name: builtins.str,
        default_region: typing.Optional[builtins.str] = None,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        auto_synth: typing.Optional[builtins.bool] = None,
        context: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        outdir: typing.Optional[builtins.str] = None,
        stack_traces: typing.Optional[builtins.bool] = None,
        tree_metadata: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Initializes a new Project (which can be used in place of cdk.App).

        :param accounts: (experimental) Dictionary of AWS account specific configuration. The key value can be anything (such as AWS Account alias), but it's recommended to keep it short such as ``dev`` or ``prod``.
        :param author: (experimental) Author information. I.e. who owns/develops this project/service.
        :param name: (experimental) Name of your project/service. Prefer ``hyphen-case``.
        :param default_region: (experimental) Specify default region you wish to use. If left empty will default to one of the following in order: 1. ``$CDK_DEFAULT_REGION`` 2. ``$AWS_REGION`` 3. 'us-east-1'
        :param analytics_reporting: Include runtime versioning information in the Stacks of this app. Default: Value of 'aws:cdk:version-reporting' context key
        :param auto_synth: Automatically call ``synth()`` before the program exits. If you set this, you don't have to call ``synth()`` explicitly. Note that this feature is only available for certain programming languages, and calling ``synth()`` is still recommended. Default: true if running via CDK CLI (``CDK_OUTDIR`` is set), ``false`` otherwise
        :param context: Additional context values for the application. Context set by the CLI or the ``context`` key in ``cdk.json`` has precedence. Context can be read from any construct using ``node.getContext(key)``. Default: - no additional context
        :param outdir: The output directory into which to emit synthesized artifacts. You should never need to set this value. By default, the value you pass to the CLI's ``--output`` flag will be used, and if you change it to a different directory the CLI will fail to pick up the generated Cloud Assembly. This property is intended for internal and testing use. Default: - If this value is *not* set, considers the environment variable ``CDK_OUTDIR``. If ``CDK_OUTDIR`` is not defined, uses a temp directory.
        :param stack_traces: Include construct creation stack trace in the ``aws:cdk:trace`` metadata key of all constructs. Default: true stack traces are included unless ``aws:cdk:disable-stack-trace`` is set in the context.
        :param tree_metadata: Include construct tree metadata as part of the Cloud Assembly. Default: true

        :stability: experimental
        '''
        props = ProjectProps(
            accounts=accounts,
            author=author,
            name=name,
            default_region=default_region,
            analytics_reporting=analytics_reporting,
            auto_synth=auto_synth,
            context=context,
            outdir=outdir,
            stack_traces=stack_traces,
            tree_metadata=tree_metadata,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="getAccount")
    @builtins.classmethod
    def get_account(
        cls,
        scope: constructs.Construct,
        account_type: builtins.str,
    ) -> Account:
        '''(experimental) Return account configuration.

        :param scope: -
        :param account_type: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, account_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument account_type", value=account_type, expected_type=type_hints["account_type"])
        return typing.cast(Account, jsii.sinvoke(cls, "getAccount", [scope, account_type]))

    @jsii.member(jsii_name="getConfiguration")
    @builtins.classmethod
    def get_configuration(cls, scope: constructs.Construct) -> "ProjectConfiguration":
        '''(experimental) Return the project configuration as given in ProjectProps.

        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("ProjectConfiguration", jsii.sinvoke(cls, "getConfiguration", [scope]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONTEXT_SCOPE")
    def CONTEXT_SCOPE(cls) -> builtins.str:
        '''(experimental) Namespace/key how this tool internally keeps track of the project configuration.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CONTEXT_SCOPE"))


@jsii.data_type(
    jsii_type="@alma-cdk/project.ProjectConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "accounts": "accounts",
        "author": "author",
        "name": "name",
        "default_region": "defaultRegion",
    },
)
class ProjectConfiguration:
    def __init__(
        self,
        *,
        accounts: typing.Mapping[builtins.str, typing.Union[Account, typing.Dict[str, typing.Any]]],
        author: typing.Union[Author, typing.Dict[str, typing.Any]],
        name: builtins.str,
        default_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accounts: (experimental) Dictionary of AWS account specific configuration. The key value can be anything (such as AWS Account alias), but it's recommended to keep it short such as ``dev`` or ``prod``.
        :param author: (experimental) Author information. I.e. who owns/develops this project/service.
        :param name: (experimental) Name of your project/service. Prefer ``hyphen-case``.
        :param default_region: (experimental) Specify default region you wish to use. If left empty will default to one of the following in order: 1. ``$CDK_DEFAULT_REGION`` 2. ``$AWS_REGION`` 3. 'us-east-1'

        :stability: experimental
        '''
        if isinstance(author, dict):
            author = Author(**author)
        if __debug__:
            def stub(
                *,
                accounts: typing.Mapping[builtins.str, typing.Union[Account, typing.Dict[str, typing.Any]]],
                author: typing.Union[Author, typing.Dict[str, typing.Any]],
                name: builtins.str,
                default_region: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
            check_type(argname="argument author", value=author, expected_type=type_hints["author"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_region", value=default_region, expected_type=type_hints["default_region"])
        self._values: typing.Dict[str, typing.Any] = {
            "accounts": accounts,
            "author": author,
            "name": name,
        }
        if default_region is not None:
            self._values["default_region"] = default_region

    @builtins.property
    def accounts(self) -> typing.Mapping[builtins.str, Account]:
        '''(experimental) Dictionary of AWS account specific configuration.

        The key value can be anything (such as AWS Account alias), but it's recommended to keep it short such as ``dev`` or ``prod``.

        :stability: experimental

        Example::

            accounts: {
              dev: {
                id: '111111111111',
                config: {
                  baseDomain: 'example.net',
                },
              },
              prod: {
                id: '222222222222',
                config: {
                  baseDomain: 'example.com',
                },
              },
            },
        '''
        result = self._values.get("accounts")
        assert result is not None, "Required property 'accounts' is missing"
        return typing.cast(typing.Mapping[builtins.str, Account], result)

    @builtins.property
    def author(self) -> Author:
        '''(experimental) Author information.

        I.e. who owns/develops this project/service.

        :stability: experimental
        '''
        result = self._values.get("author")
        assert result is not None, "Required property 'author' is missing"
        return typing.cast(Author, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) Name of your project/service.

        Prefer ``hyphen-case``.

        :stability: experimental

        Example::

            'my-cool-project'
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Specify default region you wish to use.

        If left empty will default to one of the following in order:

        1. ``$CDK_DEFAULT_REGION``
        2. ``$AWS_REGION``
        3. 'us-east-1'

        :stability: experimental
        '''
        result = self._values.get("default_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.ProjectContext",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="getAccountConfig")
    @builtins.classmethod
    def get_account_config(
        cls,
        scope: constructs.Construct,
        key: builtins.str,
        default_value: typing.Any = None,
    ) -> typing.Any:
        '''
        :param scope: -
        :param key: -
        :param default_value: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                key: builtins.str,
                default_value: typing.Any = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "getAccountConfig", [scope, key, default_value]))

    @jsii.member(jsii_name="getAccountId")
    @builtins.classmethod
    def get_account_id(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getAccountId", [scope]))

    @jsii.member(jsii_name="getAccountType")
    @builtins.classmethod
    def get_account_type(cls, scope: constructs.Construct) -> builtins.str:
        '''(experimental) Returns the account type given in runtime/CLI context.

        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getAccountType", [scope]))

    @jsii.member(jsii_name="getAllowedEnvironments")
    @builtins.classmethod
    def get_allowed_environments(
        cls,
        scope: constructs.Construct,
    ) -> typing.List[builtins.str]:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "getAllowedEnvironments", [scope]))

    @jsii.member(jsii_name="getAuthorEmail")
    @builtins.classmethod
    def get_author_email(
        cls,
        scope: constructs.Construct,
    ) -> typing.Optional[builtins.str]:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(typing.Optional[builtins.str], jsii.sinvoke(cls, "getAuthorEmail", [scope]))

    @jsii.member(jsii_name="getAuthorName")
    @builtins.classmethod
    def get_author_name(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getAuthorName", [scope]))

    @jsii.member(jsii_name="getAuthorOrganization")
    @builtins.classmethod
    def get_author_organization(
        cls,
        scope: constructs.Construct,
    ) -> typing.Optional[builtins.str]:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(typing.Optional[builtins.str], jsii.sinvoke(cls, "getAuthorOrganization", [scope]))

    @jsii.member(jsii_name="getDefaultRegion")
    @builtins.classmethod
    def get_default_region(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getDefaultRegion", [scope]))

    @jsii.member(jsii_name="getEnvironment")
    @builtins.classmethod
    def get_environment(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getEnvironment", [scope]))

    @jsii.member(jsii_name="getName")
    @builtins.classmethod
    def get_name(cls, scope: constructs.Construct) -> builtins.str:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getName", [scope]))

    @jsii.member(jsii_name="tryGetEnvironment")
    @builtins.classmethod
    def try_get_environment(
        cls,
        scope: constructs.Construct,
    ) -> typing.Optional[builtins.str]:
        '''
        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(typing.Optional[builtins.str], jsii.sinvoke(cls, "tryGetEnvironment", [scope]))


@jsii.data_type(
    jsii_type="@alma-cdk/project.ProjectProps",
    jsii_struct_bases=[ProjectConfiguration, aws_cdk.AppProps],
    name_mapping={
        "accounts": "accounts",
        "author": "author",
        "name": "name",
        "default_region": "defaultRegion",
        "analytics_reporting": "analyticsReporting",
        "auto_synth": "autoSynth",
        "context": "context",
        "outdir": "outdir",
        "stack_traces": "stackTraces",
        "tree_metadata": "treeMetadata",
    },
)
class ProjectProps(ProjectConfiguration, aws_cdk.AppProps):
    def __init__(
        self,
        *,
        accounts: typing.Mapping[builtins.str, typing.Union[Account, typing.Dict[str, typing.Any]]],
        author: typing.Union[Author, typing.Dict[str, typing.Any]],
        name: builtins.str,
        default_region: typing.Optional[builtins.str] = None,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        auto_synth: typing.Optional[builtins.bool] = None,
        context: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        outdir: typing.Optional[builtins.str] = None,
        stack_traces: typing.Optional[builtins.bool] = None,
        tree_metadata: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Props given to ``Project``.

        I.e. custom props for this construct and the usual props given to ``cdk.App``.

        :param accounts: (experimental) Dictionary of AWS account specific configuration. The key value can be anything (such as AWS Account alias), but it's recommended to keep it short such as ``dev`` or ``prod``.
        :param author: (experimental) Author information. I.e. who owns/develops this project/service.
        :param name: (experimental) Name of your project/service. Prefer ``hyphen-case``.
        :param default_region: (experimental) Specify default region you wish to use. If left empty will default to one of the following in order: 1. ``$CDK_DEFAULT_REGION`` 2. ``$AWS_REGION`` 3. 'us-east-1'
        :param analytics_reporting: Include runtime versioning information in the Stacks of this app. Default: Value of 'aws:cdk:version-reporting' context key
        :param auto_synth: Automatically call ``synth()`` before the program exits. If you set this, you don't have to call ``synth()`` explicitly. Note that this feature is only available for certain programming languages, and calling ``synth()`` is still recommended. Default: true if running via CDK CLI (``CDK_OUTDIR`` is set), ``false`` otherwise
        :param context: Additional context values for the application. Context set by the CLI or the ``context`` key in ``cdk.json`` has precedence. Context can be read from any construct using ``node.getContext(key)``. Default: - no additional context
        :param outdir: The output directory into which to emit synthesized artifacts. You should never need to set this value. By default, the value you pass to the CLI's ``--output`` flag will be used, and if you change it to a different directory the CLI will fail to pick up the generated Cloud Assembly. This property is intended for internal and testing use. Default: - If this value is *not* set, considers the environment variable ``CDK_OUTDIR``. If ``CDK_OUTDIR`` is not defined, uses a temp directory.
        :param stack_traces: Include construct creation stack trace in the ``aws:cdk:trace`` metadata key of all constructs. Default: true stack traces are included unless ``aws:cdk:disable-stack-trace`` is set in the context.
        :param tree_metadata: Include construct tree metadata as part of the Cloud Assembly. Default: true

        :stability: experimental
        '''
        if isinstance(author, dict):
            author = Author(**author)
        if __debug__:
            def stub(
                *,
                accounts: typing.Mapping[builtins.str, typing.Union[Account, typing.Dict[str, typing.Any]]],
                author: typing.Union[Author, typing.Dict[str, typing.Any]],
                name: builtins.str,
                default_region: typing.Optional[builtins.str] = None,
                analytics_reporting: typing.Optional[builtins.bool] = None,
                auto_synth: typing.Optional[builtins.bool] = None,
                context: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                outdir: typing.Optional[builtins.str] = None,
                stack_traces: typing.Optional[builtins.bool] = None,
                tree_metadata: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
            check_type(argname="argument author", value=author, expected_type=type_hints["author"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_region", value=default_region, expected_type=type_hints["default_region"])
            check_type(argname="argument analytics_reporting", value=analytics_reporting, expected_type=type_hints["analytics_reporting"])
            check_type(argname="argument auto_synth", value=auto_synth, expected_type=type_hints["auto_synth"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument outdir", value=outdir, expected_type=type_hints["outdir"])
            check_type(argname="argument stack_traces", value=stack_traces, expected_type=type_hints["stack_traces"])
            check_type(argname="argument tree_metadata", value=tree_metadata, expected_type=type_hints["tree_metadata"])
        self._values: typing.Dict[str, typing.Any] = {
            "accounts": accounts,
            "author": author,
            "name": name,
        }
        if default_region is not None:
            self._values["default_region"] = default_region
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if auto_synth is not None:
            self._values["auto_synth"] = auto_synth
        if context is not None:
            self._values["context"] = context
        if outdir is not None:
            self._values["outdir"] = outdir
        if stack_traces is not None:
            self._values["stack_traces"] = stack_traces
        if tree_metadata is not None:
            self._values["tree_metadata"] = tree_metadata

    @builtins.property
    def accounts(self) -> typing.Mapping[builtins.str, Account]:
        '''(experimental) Dictionary of AWS account specific configuration.

        The key value can be anything (such as AWS Account alias), but it's recommended to keep it short such as ``dev`` or ``prod``.

        :stability: experimental

        Example::

            accounts: {
              dev: {
                id: '111111111111',
                config: {
                  baseDomain: 'example.net',
                },
              },
              prod: {
                id: '222222222222',
                config: {
                  baseDomain: 'example.com',
                },
              },
            },
        '''
        result = self._values.get("accounts")
        assert result is not None, "Required property 'accounts' is missing"
        return typing.cast(typing.Mapping[builtins.str, Account], result)

    @builtins.property
    def author(self) -> Author:
        '''(experimental) Author information.

        I.e. who owns/develops this project/service.

        :stability: experimental
        '''
        result = self._values.get("author")
        assert result is not None, "Required property 'author' is missing"
        return typing.cast(Author, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) Name of your project/service.

        Prefer ``hyphen-case``.

        :stability: experimental

        Example::

            'my-cool-project'
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Specify default region you wish to use.

        If left empty will default to one of the following in order:

        1. ``$CDK_DEFAULT_REGION``
        2. ``$AWS_REGION``
        3. 'us-east-1'

        :stability: experimental
        '''
        result = self._values.get("default_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in the Stacks of this app.

        :default: Value of 'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def auto_synth(self) -> typing.Optional[builtins.bool]:
        '''Automatically call ``synth()`` before the program exits.

        If you set this, you don't have to call ``synth()`` explicitly. Note that
        this feature is only available for certain programming languages, and
        calling ``synth()`` is still recommended.

        :default:

        true if running via CDK CLI (``CDK_OUTDIR`` is set), ``false``
        otherwise
        '''
        result = self._values.get("auto_synth")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional context values for the application.

        Context set by the CLI or the ``context`` key in ``cdk.json`` has precedence.

        Context can be read from any construct using ``node.getContext(key)``.

        :default: - no additional context
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''The output directory into which to emit synthesized artifacts.

        You should never need to set this value. By default, the value you pass to
        the CLI's ``--output`` flag will be used, and if you change it to a different
        directory the CLI will fail to pick up the generated Cloud Assembly.

        This property is intended for internal and testing use.

        :default:

        - If this value is *not* set, considers the environment variable ``CDK_OUTDIR``.
        If ``CDK_OUTDIR`` is not defined, uses a temp directory.
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stack_traces(self) -> typing.Optional[builtins.bool]:
        '''Include construct creation stack trace in the ``aws:cdk:trace`` metadata key of all constructs.

        :default: true stack traces are included unless ``aws:cdk:disable-stack-trace`` is set in the context.
        '''
        result = self._values.get("stack_traces")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tree_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include construct tree metadata as part of the Cloud Assembly.

        :default: true
        '''
        result = self._values.get("tree_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SmartStack(
    aws_cdk.Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/project.SmartStack",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                analytics_reporting: typing.Optional[builtins.bool] = None,
                description: typing.Optional[builtins.str] = None,
                env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
                stack_name: typing.Optional[builtins.str] = None,
                synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                termination_protection: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = aws_cdk.StackProps(
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(self.__class__, self, [scope, id, props])


class UrlName(
    Name,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@alma-cdk/project.UrlName",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="globally")
    @builtins.classmethod
    def globally(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "globally", [scope, base_name, props]))

    @jsii.member(jsii_name="it")
    @builtins.classmethod
    def it(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "it", [scope, base_name, props]))

    @jsii.member(jsii_name="withProject")
    @builtins.classmethod
    def with_project(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "withProject", [scope, base_name, props]))


class _UrlNameProxy(
    UrlName,
    jsii.proxy_for(Name), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, UrlName).__jsii_proxy_class__ = lambda : _UrlNameProxy


class PathName(
    UrlName,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@alma-cdk/project.PathName",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="globally")
    @builtins.classmethod
    def globally(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "globally", [scope, base_name, props]))

    @jsii.member(jsii_name="it")
    @builtins.classmethod
    def it(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "it", [scope, base_name, props]))

    @jsii.member(jsii_name="withProject")
    @builtins.classmethod
    def with_project(
        cls,
        scope: constructs.Construct,
        base_name: builtins.str,
        *,
        max_length: typing.Optional[jsii.Number] = None,
        trim: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''
        :param scope: -
        :param base_name: -
        :param max_length: 
        :param trim: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                base_name: builtins.str,
                *,
                max_length: typing.Optional[jsii.Number] = None,
                trim: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument base_name", value=base_name, expected_type=type_hints["base_name"])
        props = NameProps(max_length=max_length, trim=trim)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "withProject", [scope, base_name, props]))


class _PathNameProxy(
    PathName,
    jsii.proxy_for(UrlName), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, PathName).__jsii_proxy_class__ = lambda : _PathNameProxy


__all__ = [
    "Account",
    "AccountConfiguration",
    "AccountContext",
    "AccountStrategy",
    "AccountStrategyOneProps",
    "AccountStrategyThreeProps",
    "AccountStrategyTwoProps",
    "AccountType",
    "AccountWrapper",
    "Author",
    "EnvRegExp",
    "EnvironmentCategory",
    "EnvironmentContext",
    "EnvironmentLabel",
    "EnvironmentType",
    "EnvironmentWrapper",
    "Name",
    "NameProps",
    "PathName",
    "Project",
    "ProjectConfiguration",
    "ProjectContext",
    "ProjectProps",
    "SmartStack",
    "UrlName",
]

publication.publish()
