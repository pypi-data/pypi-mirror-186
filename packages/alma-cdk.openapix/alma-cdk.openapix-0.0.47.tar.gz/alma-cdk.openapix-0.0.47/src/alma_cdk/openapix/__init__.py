'''
<div align="center">
	<br/>
	<br/>
  <h1>
	<img height="140" src="assets/alma-cdk-openapix.svg" alt="Alma CDK OpenApiX" />
  <br/>
  <br/>
  </h1>

```sh
npm i -D @alma-cdk/openapix
```

  <div align="left">

Generate AWS Api Gateway REST APIs via [OpenAPI](https://www.openapis.org/) (formely known as “Swagger”) Schema Definitions by consuming "clean" OpenAPI schemas and inject `x-amazon-apigateway-` extensions *with type-safety*.

  </div>
  <br/>
</div><br/><div align="center">

![diagram](assets/diagram.svg)

</div><br/>

## 🚧   Project Stability

![experimental](https://img.shields.io/badge/stability-experimental-yellow)

This construct is still versioned with `v0` major version and breaking changes might be introduced if necessary (without a major version bump), though we aim to keep the API as stable as possible (even within `v0` development). We aim to publish `v1.0.0` soon and after that breaking changes will be introduced via major version bumps.

There are also some incomplete or buggy features, such as CORS and `CognitoUserPoolsAuthorizer`.

<br/>

## Getting Started

1. Install `npm i -D @alma-cdk/openapix`
2. Define your API OpenApi Schema Definition in a `.yaml` file<br/>*without* any `x-amazon-apigateway-` extensions
3. Use `openapix` constructs in CDK to consume the `.yaml` file and then assign API Gateway integrations using CDK

<br/>

## HTTP Integration

Given the following [`http-proxy.yaml` OpenApi schema definition](https://github.com/alma-cdk/openapix/blob/main/examples/http-proxy/schema/http-proxy.yaml), *without* any AWS API Gateway OpenApi extensions:

```yaml
openapi: 3.0.3
info:
  title: HTTP Proxy
  description: Proxies requests to example.com
  version: "0.0.1"
paths:
  "/":
    get:
      summary: proxy
      description: Proxies example.com
```

You may then define API Gateway HTTP integration (within your stack):

```python
new openapix.Api(this, 'HttpProxy', {
  source: path.join(__dirname, '../schema/http-proxy.yaml'),

  paths: {
    '/': {
      get: new openapix.HttpIntegration(this, 'http://example.com', {
          httpMethod: 'get',
      }),
    },
  },
});
```

See [`/examples/http-proxy`](https://github.com/alma-cdk/openapix/tree/main/examples/http-proxy) for full OpenApi definition (with response models) and an example within a CDK application.

<br/>

## Lambda Integration

Given the following [`hello-api.yaml` OpenApi schema definition](https://github.com/alma-cdk/openapix/blob/main/examples/hello-api/schema/hello-api.yaml), *without* any AWS API Gateway OpenApi extensions:

```yaml
openapi: 3.0.3
info:
  title: Hello API
  description: Defines an example “Hello World” API
  version: "0.0.1"
paths:
  "/":
    get:
      operationId: sayHello
      summary: Say Hello
      description: Prints out a greeting
      parameters:
      - name: name
        in: query
        required: false
        schema:
          type: string
          default: "World"
      responses:
        "200":
          description: Successful response
          content:
            "application/json":
              schema:
                $ref: "#/components/schemas/HelloResponse"

components:
  schemas:
    HelloResponse:
      description: Response body
      type: object
      properties:
        message:
          type: string
          description: Greeting
          example: Hello World!
```

You may then define API Gateway AWS Lambda integration (within your stack):

```python
const greetFn = new NodejsFunction(this, 'greet');

new openapix.Api(this, 'HelloApi', {
  source: path.join(__dirname, '../schema/hello-api.yaml'),
  paths: {
    '/': {
      get: new openapix.LambdaIntegration(this, greetFn),
    },
  },
})
```

See [`/examples/hello-api`](https://github.com/alma-cdk/openapix/tree/main/examples/hello-api) for full OpenApi definition (with response models) and an example within a CDK application.

<br/>

## AWS Service Integration

Given [`books-api.yaml` OpenApi schema definition](https://github.com/alma-cdk/openapix/blob/main/examples/books-api/schema/books-api.yaml), *without* any AWS API Gateway OpenApi extensions, You may then define API Gateway AWS service integration such as DynamoDB (within your stack):

```python
new openapix.Api(this, 'BooksApi', {
  source: path.join(__dirname, '../schema/books-api.yaml'),
  paths: {
    '/': {
      get: new openapix.AwsIntegration(this, {
        service: 'dynamodb',
        action: 'Scan',
        options: {
          credentialsRole: role, // role must have access to DynamoDB table
          requestTemplates: {
            'application/json': JSON.stringify({
              TableName: table.tableName,
            }),
          },
          integrationResponses: [
            {
              statusCode: '200',
              responseTemplates: {
                // See /examples/http-proxy/lib/list-books.vtl
                'application/json': readFileSync(__dirname+'/list-books.vtl', 'utf-8'),
              },
            }
          ],
        },
      }),
    },
    '/{isbn}': {
      get: new openapix.AwsIntegration(this, {
        service: 'dynamodb',
        action: 'GetItem',
        options: {
          credentialsRole: role, // role must have access to DynamoDB table
          requestTemplates: {
            'application/json': JSON.stringify({
              TableName: table.tableName,
              Key: {
                item: {
                  "S": "$input.params('isbn')"
                }
              }
            }),
          },
          integrationResponses: [
            {
              statusCode: '200',
              responseTemplates: {
                // See /examples/http-proxy/lib/get-book.vtl
                'application/json': readFileSync(__dirname+'/get-book.vtl', 'utf-8'),
              },
            }
          ],
        },
      }),
    },
  },
});
```

See [`/examples/books-api`](https://github.com/alma-cdk/openapix/tree/main/examples/books-api) for full OpenApi definition (with response models) and an example within a CDK application.

<br/>

## Mock Integration

Given the following [`mock-api.yaml` OpenApi schema definition](https://github.com/alma-cdk/openapix/blob/main/examples/mock-api/schema/mock-api.yaml), *without* any AWS API Gateway OpenApi extensions:

```yaml
openapi: 3.0.3
info:
  title: Hello API
  description: Defines an example “Hello World” API
  version: "0.0.1"
paths:
  "/":
    get:
      operationId: sayHello
      summary: Say Hello
      description: Prints out a greeting
      parameters:
      - name: name
        in: query
        required: false
        schema:
          type: string
          default: "World"
      responses:
        "200":
          description: Successful response
          content:
            "application/json":
              schema:
                $ref: "#/components/schemas/HelloResponse"

components:
  schemas:
    HelloResponse:
      description: Response body
      type: object
      properties:
        message:
          type: string
          description: Greeting
          example: Hello World!
```

You may then define API Gateway Mock integration (within your stack):

```python
new openapix.Api(this, 'MockApi', {
  source: path.join(__dirname, '../schema/mock-api.yaml'),
  paths: {
    '/': {
      get: new openapix.MockIntegration(this, {
        requestTemplates: {
          "application/json": JSON.stringify({ statusCode: 200 }),
        },
        passthroughBehavior: apigateway.PassthroughBehavior.NEVER,
        requestParameters: {
          'integration.request.querystring.name': 'method.request.querystring.name',
        },
        integrationResponses: [
          {
            statusCode: '200',
            responseTemplates: {
              // see /examples/mock-api/lib/greet.vtl
              'application/json': readFileSync(__dirname+'/greet.vtl', 'utf-8'),
            },
            responseParameters: {},
          },
        ],
      }),
    },
  },
});
```

See [`/examples/mock-api`](https://github.com/alma-cdk/openapix/tree/main/examples/mock-api) for full OpenApi definition (with response models) and an example within a CDK application.

<br/>

## Validators

API Gateway REST APIs can perform [request parameter and request body validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html). You can provide both default validator and integration specific validator (which will override the default for given integration).

See [`/examples/todo-api`](https://github.com/alma-cdk/openapix/tree/main/examples/todo-api) for complete example within a CDK application.

Given [`todo-api.yaml` OpenApi schema definition](https://github.com/alma-cdk/openapix/blob/main/examples/todo-api/schema/todo-api.yaml) you may define the API Gateway validators for your integration in CDK:

```python
new openapix.Api(this, 'MyApi', {
  source: path.join(__dirname, '../schema/todo-api.yaml'),

  validators: {
    'all': {
      validateRequestBody: true,
      validateRequestParameters: true,
      default: true, // set this as the "API level" default validator (there can be only one)
    },
    'params-only' : {
      validateRequestBody: false,
      validateRequestParameters: true,
    },
  },

  paths: {
    '/todos': {
      // this one uses the default 'all' validator
      post:  new openapix.HttpIntegration(this, baseUrl, { httpMethod: 'post' }),
    },
    '/todos/{todoId}': {
      // this one has validator override and uses 'params-only' validator
      get: new openapix.HttpIntegration(this, `${baseUrl}/{todoId}`, {
        validator: 'params-only',
        options: {
          requestParameters: {
            'integration.request.path.todoId': 'method.request.path.todoId',
          },
        },
      }),
    },
  },
})
```

<br/>

## Authorizers

🚧 Work-in-Progress

There are multiple ways to [control & manages access to API Gateway REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) such as [resource policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html), [IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) and [usage plans with API keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) but this section focuses on [Cognito User Pools ](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) and [Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).

<br/>

### Cognito Authorizers

In this example we're defining a Congito User Pool based authorizer.

Given the following `schema.yaml` OpenApi definition:

```yaml
openapi: 3.0.3
paths:
  /:
    get:
      security:
        - MyAuthorizer: ["test/read"] # add scope
components:
  securitySchemes:
    MyCognitoAuthorizer:
      type: apiKey
      name: Authorization
      in: header
```

You can define the Cognito Authorizer in CDK with:

```python
const userPool: cognito.IUserPool;

new openapix.Api(this, 'MyApi', {
  source: './schema.yaml',

  authorizers: [
    new openapix.CognitoUserPoolsAuthorizer(this, 'MyCognitoAuthorizer', {
      cognitoUserPools: [userPool],
      resultsCacheTtl: Duration.minutes(5),
    })
  ],
})
```

<br/>

### Lambda Authorizers

In this example we're defining a custom Lambda authorizer. The authorizer function code is not relevant for the example but the idea in the example is that an API caller sends some "secret code" in query parameters (`?code=example123456`) which then the authorizer function somehow evaluates.

Given the following `schema.yaml` OpenApi definition:

```yaml
openapi: 3.0.3
paths:
  /:
    get:
      security:
        - MyAuthorizer: [] # note the empty array
components:
  securitySchemes:
    MyCustomAuthorizer:
      type: apiKey
      name: code
      in: query
```

You can define the custom Lambda Authorizer in CDK with:

```python
const authFn: lambda.IFunction;

new openapix.Api(this, 'MyApi', {
  source: './schema.yaml',

  authorizers: [

    new openapix.LambdaAuthorizer(this, 'MyCustomAuthorizer', {
      fn: authFn,
      identitySource: apigateway.IdentitySource.queryString('code'),
      type: 'request',
      authType: 'custom',
      resultsCacheTtl: Duration.minutes(5),
    }),
  ],


})
```

<br/>

## Inject/Reject

You may modify the generated OpenAPI definition (which is used to define API Gateway REST API) by injecting or rejecting values from the source OpenAPI schema definition:

```python
new openapix.Api(this, 'MyApi', {
  source: './schema.yaml',

  // Add any OpenAPI v3 data.
  // Can be useful for passing values from CDK code.
  // See https://swagger.io/specification/
  injections: {
    "info.title": "FancyPantsAPI"
  },

  // Reject fields by absolute object path from generated definition
  rejections: ['info.description'],

  // Reject all matching fields from generated definition
  rejectionsDeep: ['example', 'examples'],
});
```

<br/>

## CORS

🚧 Work-in-Progress

Using `openapix.CorsIntegration` creates a Mock integration which responds with correct response headers:

```python
new openapix.Api(this, 'MyApi', {
  source: './schema.yaml',

  paths: {
    '/foo': {
      options: new openapix.CorsIntegration(this, {
        // using helper method to define explicit values:
        headers: CorsHeaders.from(this, 'Content-Type', 'X-Amz-Date', 'Authorization'),
        origins: CorsOrigins.from(this, 'https://www.example.com'),
        methods: CorsMethods.from(this, 'options','post','get'),
      }),
    },
    '/bar': {
      options: new openapix.CorsIntegration(this, {
        // using regular string values:
        headers: 'Content-Type,X-Amz-Date,Authorization',
        origins: '*',
        methods: 'options,get',
      }),
    },
    '/baz': {
      options: new openapix.CorsIntegration(this, {
        // using helper constant for wildcard values:
        headers: CorsHeaders.ANY,
        origins: CorsOrigins.ANY,
        methods: CorsMethods.ANY,
      }),
    },
  },
});
```

When specifying multiple `origins` the mock integration uses [VTL magic](https://medium.com/@srikanth650/use-api-gateway-with-mock-integration-to-allow-cors-from-multiple-origins-bdcb431d07d3) to respond with the correct `Access-Control-Allow-Origin` header.

### Default CORS

If you wish to define same CORS options to every path, you may do so by providing a default `cors` value:

```python
new openapix.Api(this, 'MyApi', {
  source: './schema.yaml',

  defaultCors: new openapix.CorsIntegration(this, {
    headers: CorsHeaders.ANY,
    origins: CorsOrigins.ANY,
    methods: CorsMethods.ANY,
  }),

  paths: {/*...*/},
});
```

This will apply the given `cors` configuration to *every* path as `options` method. You may still do path specific overrides by adding an `options` method to specific paths.

<br/>

## API Gateway EndpointType

AWS CDK API Gateway constructs default to [*Edge-optimized API endpoints*](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html#api-gateway-api-endpoint-types-edge-optimized) by using [`EndpointType.EDGE`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html#endpointtypes) as the default.

This construct `@alma-cdk/openapix` instead defaults to using [*Regional API endpoints*](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html#api-gateway-api-endpoint-types-regional) by setting `EndpointType.REGIONAL` as the default value. This is because we believe that in most cases you're better of by configuring your own CloudFront distribution in front the API. If you do that, you might also be interested in [`@alma-cdk/origin-verify` construct](https://github.com/alma-cdk/origin-verify).

You MAY override this default in `@alma-cdk/openapix` by providing your preferred endpoint types via `restApiProps`:

```python
new openapix.Api(this, 'MyApi', {
  source: './schema.yaml',

  paths: {/*...*/},

  restApiProps: {
    endpointConfiguration: {
      types: [ apigateway.EndpointType.EDGE ],
    },
  },
});
```
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
import aws_cdk.aws_apigateway
import aws_cdk.aws_cognito
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_s3_assets
import constructs


class Api(
    aws_cdk.aws_apigateway.SpecRestApi,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.Api",
):
    '''(experimental) AWS API Gateway REST API defined with OpenApi v3 schema.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rest_api_props: typing.Optional[typing.Union[aws_cdk.aws_apigateway.RestApiProps, typing.Dict[str, typing.Any]]] = None,
        source: typing.Union[builtins.str, "Schema"],
        authorizers: typing.Optional[typing.Sequence[typing.Union["AuthorizerConfig", typing.Dict[str, typing.Any]]]] = None,
        default_cors: typing.Optional["CorsIntegration"] = None,
        default_integration: typing.Optional["Integration"] = None,
        injections: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        paths: typing.Optional[typing.Union["Paths", typing.Dict[str, typing.Any]]] = None,
        rejections: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejections_deep: typing.Optional[typing.Sequence[builtins.str]] = None,
        upload: typing.Optional[builtins.bool] = None,
        validators: typing.Optional[typing.Mapping[builtins.str, typing.Union["Validator", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) Define a new API Gateway REST API using OpenApi v3 Schema definition.

        :param scope: -
        :param id: -
        :param rest_api_props: (experimental) Props to configure the underlying CDK ``apigateway.RestApi``.
        :param source: (experimental) OpenApi Schema Definition source configuration. Provide either string path to source or an instance of ``openapix.Schema``.
        :param authorizers: (experimental) Cognito User Pool or Custom Lambda based Authorizer configurations.
        :param default_cors: (experimental) Default CORS configuration. Applied to all path integrations. You can add path specific overrides by adding an ``options`` method with ``new openapix.CorsIntegration(...)`` integration.
        :param default_integration: (experimental) Add a default integration for paths without explicitly defined integrations.
        :param injections: (experimental) Inject any OpenApi v3 data to given schema definition object paths.
        :param paths: (experimental) Integrations for OpenApi Path definitions.
        :param rejections: (experimental) Reject fields by absolute object path from generated definition.
        :param rejections_deep: (experimental) Reject all matching fields from generated definition.
        :param upload: (experimental) Schema Definition location (inline vs. S3 location). Set ``true`` to upload to S3 or ``false`` (default) to inline it into resulting CloudFormation template. Default: false
        :param validators: (experimental) Configure availalbe request validators. API Gateway REST APIs can perform request parameter and request body validation. You can optionally specify one of them with ``default: true`` to promote it as the default validator applied to all integrations. For non-default validators, you must specify ``validator: '<name>'`` prop in every integration you wish to use the given validator.

        :stability: experimental

        Example::

            const fn: IFunction;
            
            new openapix.Api(this, 'MyApi', {
              source: './schema.yaml',
              paths: {
                '/foo': {
                  get: new openapix.MockIntegration(this),
                },
                '/bar': {
                  post: new openapix.LambdaIntegration(this, fn),
                },
              }
            })
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                rest_api_props: typing.Optional[typing.Union[aws_cdk.aws_apigateway.RestApiProps, typing.Dict[str, typing.Any]]] = None,
                source: typing.Union[builtins.str, "Schema"],
                authorizers: typing.Optional[typing.Sequence[typing.Union["AuthorizerConfig", typing.Dict[str, typing.Any]]]] = None,
                default_cors: typing.Optional["CorsIntegration"] = None,
                default_integration: typing.Optional["Integration"] = None,
                injections: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                paths: typing.Optional[typing.Union["Paths", typing.Dict[str, typing.Any]]] = None,
                rejections: typing.Optional[typing.Sequence[builtins.str]] = None,
                rejections_deep: typing.Optional[typing.Sequence[builtins.str]] = None,
                upload: typing.Optional[builtins.bool] = None,
                validators: typing.Optional[typing.Mapping[builtins.str, typing.Union["Validator", typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ApiProps(
            rest_api_props=rest_api_props,
            source=source,
            authorizers=authorizers,
            default_cors=default_cors,
            default_integration=default_integration,
            injections=injections,
            paths=paths,
            rejections=rejections,
            rejections_deep=rejections_deep,
            upload=upload,
            validators=validators,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> "IDocument":
        '''(experimental) The final OpenApi v3 document used to generate the AWS API Gateway.

        :stability: experimental
        '''
        return typing.cast("IDocument", jsii.get(self, "document"))


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ApiBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "authorizers": "authorizers",
        "default_cors": "defaultCors",
        "default_integration": "defaultIntegration",
        "injections": "injections",
        "paths": "paths",
        "rejections": "rejections",
        "rejections_deep": "rejectionsDeep",
        "upload": "upload",
        "validators": "validators",
    },
)
class ApiBaseProps:
    def __init__(
        self,
        *,
        source: typing.Union[builtins.str, "Schema"],
        authorizers: typing.Optional[typing.Sequence[typing.Union["AuthorizerConfig", typing.Dict[str, typing.Any]]]] = None,
        default_cors: typing.Optional["CorsIntegration"] = None,
        default_integration: typing.Optional["Integration"] = None,
        injections: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        paths: typing.Optional[typing.Union["Paths", typing.Dict[str, typing.Any]]] = None,
        rejections: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejections_deep: typing.Optional[typing.Sequence[builtins.str]] = None,
        upload: typing.Optional[builtins.bool] = None,
        validators: typing.Optional[typing.Mapping[builtins.str, typing.Union["Validator", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) BaseProps for the ``Api`` construct without ``RestApiProps``.

        :param source: (experimental) OpenApi Schema Definition source configuration. Provide either string path to source or an instance of ``openapix.Schema``.
        :param authorizers: (experimental) Cognito User Pool or Custom Lambda based Authorizer configurations.
        :param default_cors: (experimental) Default CORS configuration. Applied to all path integrations. You can add path specific overrides by adding an ``options`` method with ``new openapix.CorsIntegration(...)`` integration.
        :param default_integration: (experimental) Add a default integration for paths without explicitly defined integrations.
        :param injections: (experimental) Inject any OpenApi v3 data to given schema definition object paths.
        :param paths: (experimental) Integrations for OpenApi Path definitions.
        :param rejections: (experimental) Reject fields by absolute object path from generated definition.
        :param rejections_deep: (experimental) Reject all matching fields from generated definition.
        :param upload: (experimental) Schema Definition location (inline vs. S3 location). Set ``true`` to upload to S3 or ``false`` (default) to inline it into resulting CloudFormation template. Default: false
        :param validators: (experimental) Configure availalbe request validators. API Gateway REST APIs can perform request parameter and request body validation. You can optionally specify one of them with ``default: true`` to promote it as the default validator applied to all integrations. For non-default validators, you must specify ``validator: '<name>'`` prop in every integration you wish to use the given validator.

        :stability: experimental
        '''
        if isinstance(paths, dict):
            paths = Paths(**paths)
        if __debug__:
            def stub(
                *,
                source: typing.Union[builtins.str, "Schema"],
                authorizers: typing.Optional[typing.Sequence[typing.Union["AuthorizerConfig", typing.Dict[str, typing.Any]]]] = None,
                default_cors: typing.Optional["CorsIntegration"] = None,
                default_integration: typing.Optional["Integration"] = None,
                injections: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                paths: typing.Optional[typing.Union["Paths", typing.Dict[str, typing.Any]]] = None,
                rejections: typing.Optional[typing.Sequence[builtins.str]] = None,
                rejections_deep: typing.Optional[typing.Sequence[builtins.str]] = None,
                upload: typing.Optional[builtins.bool] = None,
                validators: typing.Optional[typing.Mapping[builtins.str, typing.Union["Validator", typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument authorizers", value=authorizers, expected_type=type_hints["authorizers"])
            check_type(argname="argument default_cors", value=default_cors, expected_type=type_hints["default_cors"])
            check_type(argname="argument default_integration", value=default_integration, expected_type=type_hints["default_integration"])
            check_type(argname="argument injections", value=injections, expected_type=type_hints["injections"])
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
            check_type(argname="argument rejections", value=rejections, expected_type=type_hints["rejections"])
            check_type(argname="argument rejections_deep", value=rejections_deep, expected_type=type_hints["rejections_deep"])
            check_type(argname="argument upload", value=upload, expected_type=type_hints["upload"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
        }
        if authorizers is not None:
            self._values["authorizers"] = authorizers
        if default_cors is not None:
            self._values["default_cors"] = default_cors
        if default_integration is not None:
            self._values["default_integration"] = default_integration
        if injections is not None:
            self._values["injections"] = injections
        if paths is not None:
            self._values["paths"] = paths
        if rejections is not None:
            self._values["rejections"] = rejections
        if rejections_deep is not None:
            self._values["rejections_deep"] = rejections_deep
        if upload is not None:
            self._values["upload"] = upload
        if validators is not None:
            self._values["validators"] = validators

    @builtins.property
    def source(self) -> typing.Union[builtins.str, "Schema"]:
        '''(experimental) OpenApi Schema Definition source configuration.

        Provide either string path to source or an instance of ``openapix.Schema``.

        :stability: experimental

        Example::

            const props: openapix.SchemaProps;
            new openapix.Schema(props)
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[builtins.str, "Schema"], result)

    @builtins.property
    def authorizers(self) -> typing.Optional[typing.List["AuthorizerConfig"]]:
        '''(experimental) Cognito User Pool or Custom Lambda based Authorizer configurations.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html
        :stability: experimental

        Example::

            [
              new openapix.CognitoUserPoolsAuthorizer(this, 'MyCognitoAuthorizer', {
                cognitoUserPools: [userPool],
                resultsCacheTtl: Duration.minutes(5),
              }),
            ]
        '''
        result = self._values.get("authorizers")
        return typing.cast(typing.Optional[typing.List["AuthorizerConfig"]], result)

    @builtins.property
    def default_cors(self) -> typing.Optional["CorsIntegration"]:
        '''(experimental) Default CORS configuration. Applied to all path integrations.

        You can add path specific overrides by adding an ``options`` method with
        ``new openapix.CorsIntegration(...)`` integration.

        :stability: experimental

        Example::

            new openapix.CorsIntegration(this, {
              headers: 'Content-Type,X-Amz-Date,Authorization',
              origins: '*',
              methods: 'options,get',
            }),
        '''
        result = self._values.get("default_cors")
        return typing.cast(typing.Optional["CorsIntegration"], result)

    @builtins.property
    def default_integration(self) -> typing.Optional["Integration"]:
        '''(experimental) Add a default integration for paths without explicitly defined integrations.

        :stability: experimental

        Example::

            {
              'defaultIntegration': new openapix.LambdaIntegration(this, fn),
            }
        '''
        result = self._values.get("default_integration")
        return typing.cast(typing.Optional["Integration"], result)

    @builtins.property
    def injections(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Inject any OpenApi v3 data to given schema definition object paths.

        :stability: experimental

        Example::

            {
              "info.title": "FancyPantsAPI"
            }
        '''
        result = self._values.get("injections")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def paths(self) -> typing.Optional["Paths"]:
        '''(experimental) Integrations for OpenApi Path definitions.

        :stability: experimental

        Example::

            {
              '/message': {
                post: new openapix.LambdaIntegration(this, fn),
              },
            }
        '''
        result = self._values.get("paths")
        return typing.cast(typing.Optional["Paths"], result)

    @builtins.property
    def rejections(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Reject fields by absolute object path from generated definition.

        :stability: experimental

        Example::

            ['info.description']
        '''
        result = self._values.get("rejections")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejections_deep(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Reject all matching fields from generated definition.

        :stability: experimental

        Example::

            ['example', 'examples']
        '''
        result = self._values.get("rejections_deep")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def upload(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Schema Definition location (inline vs.

        S3 location).
        Set ``true`` to upload to S3 or ``false`` (default) to inline it into resulting
        CloudFormation template.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("upload")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.Mapping[builtins.str, "Validator"]]:
        '''(experimental) Configure availalbe request validators. API Gateway REST APIs can perform request parameter and request body validation.

        You can optionally specify one of them with ``default: true`` to promote it
        as the default validator applied to all integrations.

        For non-default validators, you must specify ``validator: '<name>'`` prop in
        every integration you wish to use the given validator.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html
        :stability: experimental

        Example::

            {
              'all': {
                validateRequestBody: true,
                validateRequestParameters: true,
                default: true,
              },
              'params-only' : {
                validateRequestBody: false,
                validateRequestParameters: true,
              },
            }
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "Validator"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ApiProps",
    jsii_struct_bases=[ApiBaseProps],
    name_mapping={
        "source": "source",
        "authorizers": "authorizers",
        "default_cors": "defaultCors",
        "default_integration": "defaultIntegration",
        "injections": "injections",
        "paths": "paths",
        "rejections": "rejections",
        "rejections_deep": "rejectionsDeep",
        "upload": "upload",
        "validators": "validators",
        "rest_api_props": "restApiProps",
    },
)
class ApiProps(ApiBaseProps):
    def __init__(
        self,
        *,
        source: typing.Union[builtins.str, "Schema"],
        authorizers: typing.Optional[typing.Sequence[typing.Union["AuthorizerConfig", typing.Dict[str, typing.Any]]]] = None,
        default_cors: typing.Optional["CorsIntegration"] = None,
        default_integration: typing.Optional["Integration"] = None,
        injections: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        paths: typing.Optional[typing.Union["Paths", typing.Dict[str, typing.Any]]] = None,
        rejections: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejections_deep: typing.Optional[typing.Sequence[builtins.str]] = None,
        upload: typing.Optional[builtins.bool] = None,
        validators: typing.Optional[typing.Mapping[builtins.str, typing.Union["Validator", typing.Dict[str, typing.Any]]]] = None,
        rest_api_props: typing.Optional[typing.Union[aws_cdk.aws_apigateway.RestApiProps, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Props to configure ``new openapix.Api``.

        :param source: (experimental) OpenApi Schema Definition source configuration. Provide either string path to source or an instance of ``openapix.Schema``.
        :param authorizers: (experimental) Cognito User Pool or Custom Lambda based Authorizer configurations.
        :param default_cors: (experimental) Default CORS configuration. Applied to all path integrations. You can add path specific overrides by adding an ``options`` method with ``new openapix.CorsIntegration(...)`` integration.
        :param default_integration: (experimental) Add a default integration for paths without explicitly defined integrations.
        :param injections: (experimental) Inject any OpenApi v3 data to given schema definition object paths.
        :param paths: (experimental) Integrations for OpenApi Path definitions.
        :param rejections: (experimental) Reject fields by absolute object path from generated definition.
        :param rejections_deep: (experimental) Reject all matching fields from generated definition.
        :param upload: (experimental) Schema Definition location (inline vs. S3 location). Set ``true`` to upload to S3 or ``false`` (default) to inline it into resulting CloudFormation template. Default: false
        :param validators: (experimental) Configure availalbe request validators. API Gateway REST APIs can perform request parameter and request body validation. You can optionally specify one of them with ``default: true`` to promote it as the default validator applied to all integrations. For non-default validators, you must specify ``validator: '<name>'`` prop in every integration you wish to use the given validator.
        :param rest_api_props: (experimental) Props to configure the underlying CDK ``apigateway.RestApi``.

        :stability: experimental
        '''
        if isinstance(paths, dict):
            paths = Paths(**paths)
        if isinstance(rest_api_props, dict):
            rest_api_props = aws_cdk.aws_apigateway.RestApiProps(**rest_api_props)
        if __debug__:
            def stub(
                *,
                source: typing.Union[builtins.str, "Schema"],
                authorizers: typing.Optional[typing.Sequence[typing.Union["AuthorizerConfig", typing.Dict[str, typing.Any]]]] = None,
                default_cors: typing.Optional["CorsIntegration"] = None,
                default_integration: typing.Optional["Integration"] = None,
                injections: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                paths: typing.Optional[typing.Union["Paths", typing.Dict[str, typing.Any]]] = None,
                rejections: typing.Optional[typing.Sequence[builtins.str]] = None,
                rejections_deep: typing.Optional[typing.Sequence[builtins.str]] = None,
                upload: typing.Optional[builtins.bool] = None,
                validators: typing.Optional[typing.Mapping[builtins.str, typing.Union["Validator", typing.Dict[str, typing.Any]]]] = None,
                rest_api_props: typing.Optional[typing.Union[aws_cdk.aws_apigateway.RestApiProps, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument authorizers", value=authorizers, expected_type=type_hints["authorizers"])
            check_type(argname="argument default_cors", value=default_cors, expected_type=type_hints["default_cors"])
            check_type(argname="argument default_integration", value=default_integration, expected_type=type_hints["default_integration"])
            check_type(argname="argument injections", value=injections, expected_type=type_hints["injections"])
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
            check_type(argname="argument rejections", value=rejections, expected_type=type_hints["rejections"])
            check_type(argname="argument rejections_deep", value=rejections_deep, expected_type=type_hints["rejections_deep"])
            check_type(argname="argument upload", value=upload, expected_type=type_hints["upload"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
            check_type(argname="argument rest_api_props", value=rest_api_props, expected_type=type_hints["rest_api_props"])
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
        }
        if authorizers is not None:
            self._values["authorizers"] = authorizers
        if default_cors is not None:
            self._values["default_cors"] = default_cors
        if default_integration is not None:
            self._values["default_integration"] = default_integration
        if injections is not None:
            self._values["injections"] = injections
        if paths is not None:
            self._values["paths"] = paths
        if rejections is not None:
            self._values["rejections"] = rejections
        if rejections_deep is not None:
            self._values["rejections_deep"] = rejections_deep
        if upload is not None:
            self._values["upload"] = upload
        if validators is not None:
            self._values["validators"] = validators
        if rest_api_props is not None:
            self._values["rest_api_props"] = rest_api_props

    @builtins.property
    def source(self) -> typing.Union[builtins.str, "Schema"]:
        '''(experimental) OpenApi Schema Definition source configuration.

        Provide either string path to source or an instance of ``openapix.Schema``.

        :stability: experimental

        Example::

            const props: openapix.SchemaProps;
            new openapix.Schema(props)
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[builtins.str, "Schema"], result)

    @builtins.property
    def authorizers(self) -> typing.Optional[typing.List["AuthorizerConfig"]]:
        '''(experimental) Cognito User Pool or Custom Lambda based Authorizer configurations.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html
        :stability: experimental

        Example::

            [
              new openapix.CognitoUserPoolsAuthorizer(this, 'MyCognitoAuthorizer', {
                cognitoUserPools: [userPool],
                resultsCacheTtl: Duration.minutes(5),
              }),
            ]
        '''
        result = self._values.get("authorizers")
        return typing.cast(typing.Optional[typing.List["AuthorizerConfig"]], result)

    @builtins.property
    def default_cors(self) -> typing.Optional["CorsIntegration"]:
        '''(experimental) Default CORS configuration. Applied to all path integrations.

        You can add path specific overrides by adding an ``options`` method with
        ``new openapix.CorsIntegration(...)`` integration.

        :stability: experimental

        Example::

            new openapix.CorsIntegration(this, {
              headers: 'Content-Type,X-Amz-Date,Authorization',
              origins: '*',
              methods: 'options,get',
            }),
        '''
        result = self._values.get("default_cors")
        return typing.cast(typing.Optional["CorsIntegration"], result)

    @builtins.property
    def default_integration(self) -> typing.Optional["Integration"]:
        '''(experimental) Add a default integration for paths without explicitly defined integrations.

        :stability: experimental

        Example::

            {
              'defaultIntegration': new openapix.LambdaIntegration(this, fn),
            }
        '''
        result = self._values.get("default_integration")
        return typing.cast(typing.Optional["Integration"], result)

    @builtins.property
    def injections(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Inject any OpenApi v3 data to given schema definition object paths.

        :stability: experimental

        Example::

            {
              "info.title": "FancyPantsAPI"
            }
        '''
        result = self._values.get("injections")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def paths(self) -> typing.Optional["Paths"]:
        '''(experimental) Integrations for OpenApi Path definitions.

        :stability: experimental

        Example::

            {
              '/message': {
                post: new openapix.LambdaIntegration(this, fn),
              },
            }
        '''
        result = self._values.get("paths")
        return typing.cast(typing.Optional["Paths"], result)

    @builtins.property
    def rejections(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Reject fields by absolute object path from generated definition.

        :stability: experimental

        Example::

            ['info.description']
        '''
        result = self._values.get("rejections")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejections_deep(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Reject all matching fields from generated definition.

        :stability: experimental

        Example::

            ['example', 'examples']
        '''
        result = self._values.get("rejections_deep")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def upload(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Schema Definition location (inline vs.

        S3 location).
        Set ``true`` to upload to S3 or ``false`` (default) to inline it into resulting
        CloudFormation template.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("upload")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.Mapping[builtins.str, "Validator"]]:
        '''(experimental) Configure availalbe request validators. API Gateway REST APIs can perform request parameter and request body validation.

        You can optionally specify one of them with ``default: true`` to promote it
        as the default validator applied to all integrations.

        For non-default validators, you must specify ``validator: '<name>'`` prop in
        every integration you wish to use the given validator.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html
        :stability: experimental

        Example::

            {
              'all': {
                validateRequestBody: true,
                validateRequestParameters: true,
                default: true,
              },
              'params-only' : {
                validateRequestBody: false,
                validateRequestParameters: true,
              },
            }
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "Validator"]], result)

    @builtins.property
    def rest_api_props(self) -> typing.Optional[aws_cdk.aws_apigateway.RestApiProps]:
        '''(experimental) Props to configure the underlying CDK ``apigateway.RestApi``.

        :stability: experimental
        '''
        result = self._values.get("rest_api_props")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.RestApiProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.AuthorizerExtensions",
    jsii_struct_bases=[],
    name_mapping={
        "x_amazon_apigateway_authorizer": "xAmazonApigatewayAuthorizer",
        "x_amazon_apigateway_authtype": "xAmazonApigatewayAuthtype",
    },
)
class AuthorizerExtensions:
    def __init__(
        self,
        *,
        x_amazon_apigateway_authorizer: typing.Union["XAmazonApigatewayAuthorizer", typing.Dict[str, typing.Any]],
        x_amazon_apigateway_authtype: builtins.str,
    ) -> None:
        '''
        :param x_amazon_apigateway_authorizer: 
        :param x_amazon_apigateway_authtype: 

        :stability: experimental
        '''
        if isinstance(x_amazon_apigateway_authorizer, dict):
            x_amazon_apigateway_authorizer = XAmazonApigatewayAuthorizer(**x_amazon_apigateway_authorizer)
        if __debug__:
            def stub(
                *,
                x_amazon_apigateway_authorizer: typing.Union["XAmazonApigatewayAuthorizer", typing.Dict[str, typing.Any]],
                x_amazon_apigateway_authtype: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument x_amazon_apigateway_authorizer", value=x_amazon_apigateway_authorizer, expected_type=type_hints["x_amazon_apigateway_authorizer"])
            check_type(argname="argument x_amazon_apigateway_authtype", value=x_amazon_apigateway_authtype, expected_type=type_hints["x_amazon_apigateway_authtype"])
        self._values: typing.Dict[str, typing.Any] = {
            "x_amazon_apigateway_authorizer": x_amazon_apigateway_authorizer,
            "x_amazon_apigateway_authtype": x_amazon_apigateway_authtype,
        }

    @builtins.property
    def x_amazon_apigateway_authorizer(self) -> "XAmazonApigatewayAuthorizer":
        '''
        :stability: experimental
        '''
        result = self._values.get("x_amazon_apigateway_authorizer")
        assert result is not None, "Required property 'x_amazon_apigateway_authorizer' is missing"
        return typing.cast("XAmazonApigatewayAuthorizer", result)

    @builtins.property
    def x_amazon_apigateway_authtype(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("x_amazon_apigateway_authtype")
        assert result is not None, "Required property 'x_amazon_apigateway_authtype' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizerExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolsAuthorizer(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.CognitoUserPoolsAuthorizer",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cognito_user_pools: typing.Sequence[aws_cdk.aws_cognito.IUserPool],
        results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cognito_user_pools: 
        :param results_cache_ttl: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                cognito_user_pools: typing.Sequence[aws_cdk.aws_cognito.IUserPool],
                results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CognitoUserPoolsAuthorizerProps(
            cognito_user_pools=cognito_user_pools, results_cache_ttl=results_cache_ttl
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="xAmazonApigatewayAuthorizer")
    def x_amazon_apigateway_authorizer(self) -> "XAmazonApigatewayAuthorizer":
        '''
        :stability: experimental
        '''
        return typing.cast("XAmazonApigatewayAuthorizer", jsii.get(self, "xAmazonApigatewayAuthorizer"))

    @builtins.property
    @jsii.member(jsii_name="xAmazonApigatewayAuthtype")
    def x_amazon_apigateway_authtype(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "xAmazonApigatewayAuthtype"))


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.CognitoUserPoolsAuthorizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "cognito_user_pools": "cognitoUserPools",
        "results_cache_ttl": "resultsCacheTtl",
    },
)
class CognitoUserPoolsAuthorizerProps:
    def __init__(
        self,
        *,
        cognito_user_pools: typing.Sequence[aws_cdk.aws_cognito.IUserPool],
        results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param cognito_user_pools: 
        :param results_cache_ttl: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                cognito_user_pools: typing.Sequence[aws_cdk.aws_cognito.IUserPool],
                results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cognito_user_pools", value=cognito_user_pools, expected_type=type_hints["cognito_user_pools"])
            check_type(argname="argument results_cache_ttl", value=results_cache_ttl, expected_type=type_hints["results_cache_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "cognito_user_pools": cognito_user_pools,
        }
        if results_cache_ttl is not None:
            self._values["results_cache_ttl"] = results_cache_ttl

    @builtins.property
    def cognito_user_pools(self) -> typing.List[aws_cdk.aws_cognito.IUserPool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cognito_user_pools")
        assert result is not None, "Required property 'cognito_user_pools' is missing"
        return typing.cast(typing.List[aws_cdk.aws_cognito.IUserPool], result)

    @builtins.property
    def results_cache_ttl(self) -> typing.Optional[aws_cdk.Duration]:
        '''
        :stability: experimental
        '''
        result = self._values.get("results_cache_ttl")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolsAuthorizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.Extensible",
    jsii_struct_bases=[],
    name_mapping={},
)
class Extensible:
    def __init__(self) -> None:
        '''(experimental) Allow Open Api Extensions via ``x-`` prefixed values.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Extensible(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ExternalDocumentationObject",
    jsii_struct_bases=[Extensible],
    name_mapping={"url": "url", "description": "description"},
)
class ExternalDocumentationObject(Extensible):
    def __init__(
        self,
        *,
        url: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Allows referencing an external resource for extended documentation.

        :param url: (experimental) The URL for the target documentation. Value MUST be in the format of a URL.
        :param description: (experimental) A short description of the target documentation. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                url: builtins.str,
                description: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def url(self) -> builtins.str:
        '''(experimental) The URL for the target documentation.

        Value MUST be in the format of a URL.

        :stability: experimental
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description of the target documentation.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalDocumentationObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.HeaderObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "allow_empty_value": "allowEmptyValue",
        "deprecated": "deprecated",
        "description": "description",
        "required": "required",
    },
)
class HeaderObject(Extensible):
    def __init__(
        self,
        *,
        allow_empty_value: typing.Optional[builtins.bool] = None,
        deprecated: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        required: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) The Header Object follows the structure of the Parameter Object with the following changes:.

        1. name MUST NOT be specified, it is given in the corresponding headers map.
        2. in MUST NOT be specified, it is implicitly in header.
        3. All traits that are affected by the location MUST be applicable to a location of header (for example, style).

        :param allow_empty_value: (experimental) Sets the ability to pass empty-valued parameters. This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.
        :param deprecated: (experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage. Default value is false.
        :param description: (experimental) A brief description of the parameter. This could contain examples of use. CommonMark syntax MAY be used for rich text representation.
        :param required: (experimental) Determines whether this parameter is mandatory. If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                allow_empty_value: typing.Optional[builtins.bool] = None,
                deprecated: typing.Optional[builtins.bool] = None,
                description: typing.Optional[builtins.str] = None,
                required: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_empty_value", value=allow_empty_value, expected_type=type_hints["allow_empty_value"])
            check_type(argname="argument deprecated", value=deprecated, expected_type=type_hints["deprecated"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_empty_value is not None:
            self._values["allow_empty_value"] = allow_empty_value
        if deprecated is not None:
            self._values["deprecated"] = deprecated
        if description is not None:
            self._values["description"] = description
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def allow_empty_value(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Sets the ability to pass empty-valued parameters.

        This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.

        :stability: experimental
        '''
        result = self._values.get("allow_empty_value")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        result = self._values.get("deprecated")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the parameter.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether this parameter is mandatory.

        If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HeaderObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@alma-cdk/openapix.IBaseIntegration")
class IBaseIntegration(typing_extensions.Protocol):
    '''(experimental) Interface implemented by all integrations.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "InternalIntegrationType":
        '''(experimental) Identifier to enable internal type checks.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="xAmazonApigatewayIntegration")
    def x_amazon_apigateway_integration(self) -> "XAmazonApigatewayIntegration":
        '''
        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="validator")
    def validator(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        ...


class _IBaseIntegrationProxy:
    '''(experimental) Interface implemented by all integrations.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IBaseIntegration"

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "InternalIntegrationType":
        '''(experimental) Identifier to enable internal type checks.

        :stability: experimental
        '''
        return typing.cast("InternalIntegrationType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="xAmazonApigatewayIntegration")
    def x_amazon_apigateway_integration(self) -> "XAmazonApigatewayIntegration":
        '''
        :stability: experimental
        '''
        return typing.cast("XAmazonApigatewayIntegration", jsii.get(self, "xAmazonApigatewayIntegration"))

    @builtins.property
    @jsii.member(jsii_name="validator")
    def validator(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validator"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBaseIntegration).__jsii_proxy_class__ = lambda : _IBaseIntegrationProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IExtensible")
class IExtensible(typing_extensions.Protocol):
    '''(experimental) Allow Open Api Extensions via ``x-`` prefixed values.

    :stability: experimental
    '''

    pass


class _IExtensibleProxy:
    '''(experimental) Allow Open Api Extensions via ``x-`` prefixed values.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IExtensible"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExtensible).__jsii_proxy_class__ = lambda : _IExtensibleProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IExternalDocumentationObject")
class IExternalDocumentationObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Allows referencing an external resource for extended documentation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        '''(experimental) The URL for the target documentation.

        Value MUST be in the format of a URL.

        :stability: experimental
        '''
        ...

    @url.setter
    def url(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description of the target documentation.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IExternalDocumentationObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Allows referencing an external resource for extended documentation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IExternalDocumentationObject"

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        '''(experimental) The URL for the target documentation.

        Value MUST be in the format of a URL.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description of the target documentation.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExternalDocumentationObject).__jsii_proxy_class__ = lambda : _IExternalDocumentationObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IHeaderObject")
class IHeaderObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) The Header Object follows the structure of the Parameter Object with the following changes:.

    1. name MUST NOT be specified, it is given in the corresponding headers map.
    2. in MUST NOT be specified, it is implicitly in header.
    3. All traits that are affected by the location MUST be applicable to a location of header (for example, style).

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="allowEmptyValue")
    def allow_empty_value(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Sets the ability to pass empty-valued parameters.

        This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.

        :stability: experimental
        '''
        ...

    @allow_empty_value.setter
    def allow_empty_value(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        ...

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the parameter.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether this parameter is mandatory.

        If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        ...

    @required.setter
    def required(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _IHeaderObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) The Header Object follows the structure of the Parameter Object with the following changes:.

    1. name MUST NOT be specified, it is given in the corresponding headers map.
    2. in MUST NOT be specified, it is implicitly in header.
    3. All traits that are affected by the location MUST be applicable to a location of header (for example, style).

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IHeaderObject"

    @builtins.property
    @jsii.member(jsii_name="allowEmptyValue")
    def allow_empty_value(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Sets the ability to pass empty-valued parameters.

        This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "allowEmptyValue"))

    @allow_empty_value.setter
    def allow_empty_value(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowEmptyValue", value)

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "deprecated"))

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deprecated", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the parameter.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether this parameter is mandatory.

        If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHeaderObject).__jsii_proxy_class__ = lambda : _IHeaderObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IInfoObject")
class IInfoObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) The object provides metadata about the API.

    The metadata MAY be used by the clients if needed, and MAY be presented in editing or documentation generation tools for convenience.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        '''(experimental) The title of the API.

        :stability: experimental
        '''
        ...

    @title.setter
    def title(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version).

        :stability: experimental
        '''
        ...

    @version.setter
    def version(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="contact")
    def contact(self) -> typing.Optional["IContactObject"]:
        '''(experimental) The contact information for the exposed API.

        :stability: experimental
        '''
        ...

    @contact.setter
    def contact(self, value: typing.Optional["IContactObject"]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description of the API.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="license")
    def license(self) -> typing.Optional["ILicenseObject"]:
        '''(experimental) The license information for the exposed API.

        :stability: experimental
        '''
        ...

    @license.setter
    def license(self, value: typing.Optional["ILicenseObject"]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="termsOfService")
    def terms_of_service(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL to the Terms of Service for the API.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        ...

    @terms_of_service.setter
    def terms_of_service(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IInfoObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) The object provides metadata about the API.

    The metadata MAY be used by the clients if needed, and MAY be presented in editing or documentation generation tools for convenience.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IInfoObject"

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        '''(experimental) The title of the API.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version).

        :stability: experimental
        '''
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
    @jsii.member(jsii_name="contact")
    def contact(self) -> typing.Optional["IContactObject"]:
        '''(experimental) The contact information for the exposed API.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["IContactObject"], jsii.get(self, "contact"))

    @contact.setter
    def contact(self, value: typing.Optional["IContactObject"]) -> None:
        if __debug__:
            def stub(value: typing.Optional["IContactObject"]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contact", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description of the API.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="license")
    def license(self) -> typing.Optional["ILicenseObject"]:
        '''(experimental) The license information for the exposed API.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["ILicenseObject"], jsii.get(self, "license"))

    @license.setter
    def license(self, value: typing.Optional["ILicenseObject"]) -> None:
        if __debug__:
            def stub(value: typing.Optional["ILicenseObject"]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "license", value)

    @builtins.property
    @jsii.member(jsii_name="termsOfService")
    def terms_of_service(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL to the Terms of Service for the API.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "termsOfService"))

    @terms_of_service.setter
    def terms_of_service(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "termsOfService", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInfoObject).__jsii_proxy_class__ = lambda : _IInfoObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.ILicenseObject")
class ILicenseObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) The license information for the exposed API.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The license name used for the API.

        :stability: experimental
        '''
        ...

    @name.setter
    def name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL to the license used for the API.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        ...

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _ILicenseObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) The license information for the exposed API.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.ILicenseObject"

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The license name used for the API.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL to the license used for the API.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "url"))

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILicenseObject).__jsii_proxy_class__ = lambda : _ILicenseObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.ILinkObject")
class ILinkObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) The Link object represents a possible design-time link for a response.

    The presence of a link does not guarantee the caller's ability to successfully invoke it, rather it provides a known relationship and traversal mechanism between responses and other operations.
    Unlike dynamic links (i.e. links provided in the response payload), the OAS linking mechanism does not require link information in the runtime response.
    For computing links, and providing instructions to execute them, a runtime expression is used for accessing values in an operation and using them as parameters while invoking the linked operation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A description of the link.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="operationId")
    def operation_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of an existing, resolvable OAS operation, as defined with a unique operationId.

        This field is mutually exclusive of the operationRef field.

        :stability: experimental
        '''
        ...

    @operation_id.setter
    def operation_id(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="operationRef")
    def operation_ref(self) -> typing.Optional[builtins.str]:
        '''(experimental) A relative or absolute URI reference to an OAS operation.

        This field is mutually exclusive of the operationId field, and MUST point to an Operation Object. Relative operationRef values MAY be used to locate an existing Operation Object in the OpenAPI definition.

        :stability: experimental
        '''
        ...

    @operation_ref.setter
    def operation_ref(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) A map representing parameters to pass to an operation as specified with operationId or identified via operationRef.

        The key is the parameter name to be used, whereas the value can be a constant or an expression to be evaluated and passed to the linked operation. The parameter name can be qualified using the parameter location [{in}.]{name} for operations that use the same parameter name in different locations (e.g. path.id).

        :stability: experimental
        '''
        ...

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Any]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="requestBody")
    def request_body(self) -> typing.Any:
        '''(experimental) A literal value or {expression} to use as a request body when calling the target operation.

        :stability: experimental
        '''
        ...

    @request_body.setter
    def request_body(self, value: typing.Any) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> typing.Optional["IServerObject"]:
        '''(experimental) A server object to be used by the target operation.

        :stability: experimental
        '''
        ...

    @server.setter
    def server(self, value: typing.Optional["IServerObject"]) -> None:
        ...


class _ILinkObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) The Link object represents a possible design-time link for a response.

    The presence of a link does not guarantee the caller's ability to successfully invoke it, rather it provides a known relationship and traversal mechanism between responses and other operations.
    Unlike dynamic links (i.e. links provided in the response payload), the OAS linking mechanism does not require link information in the runtime response.
    For computing links, and providing instructions to execute them, a runtime expression is used for accessing values in an operation and using them as parameters while invoking the linked operation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.ILinkObject"

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A description of the link.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="operationId")
    def operation_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of an existing, resolvable OAS operation, as defined with a unique operationId.

        This field is mutually exclusive of the operationRef field.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationId"))

    @operation_id.setter
    def operation_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationId", value)

    @builtins.property
    @jsii.member(jsii_name="operationRef")
    def operation_ref(self) -> typing.Optional[builtins.str]:
        '''(experimental) A relative or absolute URI reference to an OAS operation.

        This field is mutually exclusive of the operationId field, and MUST point to an Operation Object. Relative operationRef values MAY be used to locate an existing Operation Object in the OpenAPI definition.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationRef"))

    @operation_ref.setter
    def operation_ref(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationRef", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) A map representing parameters to pass to an operation as specified with operationId or identified via operationRef.

        The key is the parameter name to be used, whereas the value can be a constant or an expression to be evaluated and passed to the linked operation. The parameter name can be qualified using the parameter location [{in}.]{name} for operations that use the same parameter name in different locations (e.g. path.id).

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Any]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="requestBody")
    def request_body(self) -> typing.Any:
        '''(experimental) A literal value or {expression} to use as a request body when calling the target operation.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "requestBody"))

    @request_body.setter
    def request_body(self, value: typing.Any) -> None:
        if __debug__:
            def stub(value: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestBody", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> typing.Optional["IServerObject"]:
        '''(experimental) A server object to be used by the target operation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["IServerObject"], jsii.get(self, "server"))

    @server.setter
    def server(self, value: typing.Optional["IServerObject"]) -> None:
        if __debug__:
            def stub(value: typing.Optional["IServerObject"]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILinkObject).__jsii_proxy_class__ = lambda : _ILinkObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IMediaTypeObject")
class IMediaTypeObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Each Media Type Object provides schema and examples for the media type identified by its key.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "IEncodingObject"]]:
        '''(experimental) A map between a property name and its encoding information.

        The key, being the property name, MUST exist in the schema as a property. The encoding object SHALL only apply to requestBody objects when the media type is multipart or application/x-www-form-urlencoded.

        :stability: experimental
        '''
        ...

    @encoding.setter
    def encoding(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, "IEncodingObject"]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> typing.Any:
        '''(experimental) Example of the media type.

        The example object SHOULD be in the correct format as specified by the media type. The example field is mutually exclusive of the examples field. Furthermore, if referencing a schema which contains an example, the example value SHALL override the example provided by the schema.

        :stability: experimental
        '''
        ...

    @example.setter
    def example(self, value: typing.Any) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="examples")
    def examples(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "IExampleObject"]]]:
        '''(experimental) Examples of the media type.

        Each example object SHOULD match the media type and specified schema if present. The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema which contains an example, the examples value SHALL override the example provided by the schema.

        :stability: experimental
        '''
        ...

    @examples.setter
    def examples(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "IExampleObject"]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> typing.Optional[typing.Union["IReferenceObject", "ISchemaObject"]]:
        '''(experimental) The schema defining the content of the request, response, or parameter.

        :stability: experimental
        '''
        ...

    @schema.setter
    def schema(
        self,
        value: typing.Optional[typing.Union["IReferenceObject", "ISchemaObject"]],
    ) -> None:
        ...


class _IMediaTypeObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Each Media Type Object provides schema and examples for the media type identified by its key.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IMediaTypeObject"

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "IEncodingObject"]]:
        '''(experimental) A map between a property name and its encoding information.

        The key, being the property name, MUST exist in the schema as a property. The encoding object SHALL only apply to requestBody objects when the media type is multipart or application/x-www-form-urlencoded.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "IEncodingObject"]], jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, "IEncodingObject"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, "IEncodingObject"]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> typing.Any:
        '''(experimental) Example of the media type.

        The example object SHOULD be in the correct format as specified by the media type. The example field is mutually exclusive of the examples field. Furthermore, if referencing a schema which contains an example, the example value SHALL override the example provided by the schema.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "example"))

    @example.setter
    def example(self, value: typing.Any) -> None:
        if __debug__:
            def stub(value: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "example", value)

    @builtins.property
    @jsii.member(jsii_name="examples")
    def examples(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "IExampleObject"]]]:
        '''(experimental) Examples of the media type.

        Each example object SHOULD match the media type and specified schema if present. The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema which contains an example, the examples value SHALL override the example provided by the schema.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "IExampleObject"]]], jsii.get(self, "examples"))

    @examples.setter
    def examples(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "IExampleObject"]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "IExampleObject"]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "examples", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> typing.Optional[typing.Union["IReferenceObject", "ISchemaObject"]]:
        '''(experimental) The schema defining the content of the request, response, or parameter.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Union["IReferenceObject", "ISchemaObject"]], jsii.get(self, "schema"))

    @schema.setter
    def schema(
        self,
        value: typing.Optional[typing.Union["IReferenceObject", "ISchemaObject"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union["IReferenceObject", "ISchemaObject"]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMediaTypeObject).__jsii_proxy_class__ = lambda : _IMediaTypeObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IOAuthFlowObject")
class IOAuthFlowObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Configuration details for a supported OAuth Flow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) The available scopes for the OAuth2 security scheme.

        A map between the scope name and a short description for it. The map MAY be empty.

        :stability: experimental
        '''
        ...

    @scopes.setter
    def scopes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="authorizationUrl")
    def authorization_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The authorization URL to be used for this flow.

        This MUST be in the form of a URL.
        REQUIRED for oauth2 ("implicit", "authorizationCode").

        :stability: experimental
        '''
        ...

    @authorization_url.setter
    def authorization_url(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="refreshUrl")
    def refresh_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL to be used for obtaining refresh tokens.

        This MUST be in the form of a URL.

        :stability: experimental
        '''
        ...

    @refresh_url.setter
    def refresh_url(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The token URL to be used for this flow.

        This MUST be in the form of a URL.
        REQUIRED for oauth2 ("password", "clientCredentials", "authorizationCode").

        :stability: experimental
        '''
        ...

    @token_url.setter
    def token_url(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IOAuthFlowObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Configuration details for a supported OAuth Flow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IOAuthFlowObject"

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) The available scopes for the OAuth2 security scheme.

        A map between the scope name and a short description for it. The map MAY be empty.

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "scopes"))

    @scopes.setter
    def scopes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopes", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationUrl")
    def authorization_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The authorization URL to be used for this flow.

        This MUST be in the form of a URL.
        REQUIRED for oauth2 ("implicit", "authorizationCode").

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationUrl"))

    @authorization_url.setter
    def authorization_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="refreshUrl")
    def refresh_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL to be used for obtaining refresh tokens.

        This MUST be in the form of a URL.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshUrl"))

    @refresh_url.setter
    def refresh_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshUrl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The token URL to be used for this flow.

        This MUST be in the form of a URL.
        REQUIRED for oauth2 ("password", "clientCredentials", "authorizationCode").

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUrl"))

    @token_url.setter
    def token_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrl", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOAuthFlowObject).__jsii_proxy_class__ = lambda : _IOAuthFlowObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IOAuthFlowsObject")
class IOAuthFlowsObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Allows configuration of the supported OAuth Flows.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="authorizationCode")
    def authorization_code(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Authorization Code flow.

        Previously called accessCode in OpenAPI 2.0.

        :stability: experimental
        '''
        ...

    @authorization_code.setter
    def authorization_code(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="clientCredentials")
    def client_credentials(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Client Credentials flow.

        Previously called application in OpenAPI 2.0.

        :stability: experimental
        '''
        ...

    @client_credentials.setter
    def client_credentials(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="implicit")
    def implicit(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Implicit flow.

        :stability: experimental
        '''
        ...

    @implicit.setter
    def implicit(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Resource Owner Password flow.

        :stability: experimental
        '''
        ...

    @password.setter
    def password(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        ...


class _IOAuthFlowsObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Allows configuration of the supported OAuth Flows.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IOAuthFlowsObject"

    @builtins.property
    @jsii.member(jsii_name="authorizationCode")
    def authorization_code(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Authorization Code flow.

        Previously called accessCode in OpenAPI 2.0.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOAuthFlowObject], jsii.get(self, "authorizationCode"))

    @authorization_code.setter
    def authorization_code(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOAuthFlowObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationCode", value)

    @builtins.property
    @jsii.member(jsii_name="clientCredentials")
    def client_credentials(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Client Credentials flow.

        Previously called application in OpenAPI 2.0.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOAuthFlowObject], jsii.get(self, "clientCredentials"))

    @client_credentials.setter
    def client_credentials(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOAuthFlowObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="implicit")
    def implicit(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Implicit flow.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOAuthFlowObject], jsii.get(self, "implicit"))

    @implicit.setter
    def implicit(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOAuthFlowObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "implicit", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[IOAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Resource Owner Password flow.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOAuthFlowObject], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[IOAuthFlowObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOAuthFlowObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOAuthFlowsObject).__jsii_proxy_class__ = lambda : _IOAuthFlowsObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IOperationObject")
class IOperationObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Describes a single API operation on a path.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="responses")
    def responses(self) -> "IResponsesObject":
        '''(experimental) The list of possible responses as they are returned from executing this operation.

        :stability: experimental
        '''
        ...

    @responses.setter
    def responses(self, value: "IResponsesObject") -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="callbacks")
    def callbacks(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "ICallbackObject"]]]:
        '''(experimental) A map of possible out-of band callbacks related to the parent operation.

        The key is a unique identifier for the Callback Object. Each value in the map is a Callback Object that describes a request that may be initiated by the API provider and the expected responses.

        :stability: experimental
        '''
        ...

    @callbacks.setter
    def callbacks(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "ICallbackObject"]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Declares this operation to be deprecated.

        Consumers SHOULD refrain from usage of the declared operation. Default value is false.

        :stability: experimental
        '''
        ...

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A verbose explanation of the operation behavior.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this operation.

        :stability: experimental
        '''
        ...

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="operationId")
    def operation_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Unique string used to identify the operation.

        The id MUST be unique among all operations described in the API. The operationId value is case-sensitive. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions.

        :stability: experimental
        '''
        ...

    @operation_id.setter
    def operation_id(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.List[typing.Union["IReferenceObject", "IParameterObject"]]]:
        '''(experimental) A list of parameters that are applicable for this operation.

        If a parameter is already defined at the Path Item, the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.

        :stability: experimental
        '''
        ...

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.List[typing.Union["IReferenceObject", "IParameterObject"]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="requestBody")
    def request_body(
        self,
    ) -> typing.Optional[typing.Union["IReferenceObject", "IRequestBodyObject"]]:
        '''(experimental) The request body applicable for this operation.

        The requestBody is only supported in HTTP methods where the HTTP 1.1 specification RFC7231 has explicitly defined semantics for request bodies. In other cases where the HTTP spec is vague, requestBody SHALL be ignored by consumers.

        :stability: experimental
        '''
        ...

    @request_body.setter
    def request_body(
        self,
        value: typing.Optional[typing.Union["IReferenceObject", "IRequestBodyObject"]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> typing.Optional[typing.List["ISecurityRequirementObject"]]:
        '''(experimental) A declaration of which security mechanisms can be used for this operation.

        The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement ({}) can be included in the array. This definition overrides any declared top-level security. To remove a top-level security declaration, an empty array can be used.

        :stability: experimental
        '''
        ...

    @security.setter
    def security(
        self,
        value: typing.Optional[typing.List["ISecurityRequirementObject"]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short summary of what the operation does.

        :stability: experimental
        '''
        ...

    @summary.setter
    def summary(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A list of tags for API documentation control.

        Tags can be used for logical grouping of operations by resources or any other qualifier.

        :stability: experimental
        '''
        ...

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        ...


class _IOperationObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Describes a single API operation on a path.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IOperationObject"

    @builtins.property
    @jsii.member(jsii_name="responses")
    def responses(self) -> "IResponsesObject":
        '''(experimental) The list of possible responses as they are returned from executing this operation.

        :stability: experimental
        '''
        return typing.cast("IResponsesObject", jsii.get(self, "responses"))

    @responses.setter
    def responses(self, value: "IResponsesObject") -> None:
        if __debug__:
            def stub(value: "IResponsesObject") -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responses", value)

    @builtins.property
    @jsii.member(jsii_name="callbacks")
    def callbacks(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "ICallbackObject"]]]:
        '''(experimental) A map of possible out-of band callbacks related to the parent operation.

        The key is a unique identifier for the Callback Object. Each value in the map is a Callback Object that describes a request that may be initiated by the API provider and the expected responses.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "ICallbackObject"]]], jsii.get(self, "callbacks"))

    @callbacks.setter
    def callbacks(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "ICallbackObject"]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union["IReferenceObject", "ICallbackObject"]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callbacks", value)

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Declares this operation to be deprecated.

        Consumers SHOULD refrain from usage of the declared operation. Default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "deprecated"))

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deprecated", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A verbose explanation of the operation behavior.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this operation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IExternalDocumentationObject], jsii.get(self, "externalDocs"))

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[IExternalDocumentationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalDocs", value)

    @builtins.property
    @jsii.member(jsii_name="operationId")
    def operation_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Unique string used to identify the operation.

        The id MUST be unique among all operations described in the API. The operationId value is case-sensitive. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationId"))

    @operation_id.setter
    def operation_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationId", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.List[typing.Union["IReferenceObject", "IParameterObject"]]]:
        '''(experimental) A list of parameters that are applicable for this operation.

        If a parameter is already defined at the Path Item, the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[typing.Union["IReferenceObject", "IParameterObject"]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.List[typing.Union["IReferenceObject", "IParameterObject"]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.List[typing.Union["IReferenceObject", "IParameterObject"]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="requestBody")
    def request_body(
        self,
    ) -> typing.Optional[typing.Union["IReferenceObject", "IRequestBodyObject"]]:
        '''(experimental) The request body applicable for this operation.

        The requestBody is only supported in HTTP methods where the HTTP 1.1 specification RFC7231 has explicitly defined semantics for request bodies. In other cases where the HTTP spec is vague, requestBody SHALL be ignored by consumers.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Union["IReferenceObject", "IRequestBodyObject"]], jsii.get(self, "requestBody"))

    @request_body.setter
    def request_body(
        self,
        value: typing.Optional[typing.Union["IReferenceObject", "IRequestBodyObject"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union["IReferenceObject", "IRequestBodyObject"]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestBody", value)

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> typing.Optional[typing.List["ISecurityRequirementObject"]]:
        '''(experimental) A declaration of which security mechanisms can be used for this operation.

        The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement ({}) can be included in the array. This definition overrides any declared top-level security. To remove a top-level security declaration, an empty array can be used.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List["ISecurityRequirementObject"]], jsii.get(self, "security"))

    @security.setter
    def security(
        self,
        value: typing.Optional[typing.List["ISecurityRequirementObject"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.List["ISecurityRequirementObject"]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "security", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short summary of what the operation does.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A list of tags for API documentation control.

        Tags can be used for logical grouping of operations by resources or any other qualifier.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOperationObject).__jsii_proxy_class__ = lambda : _IOperationObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IParameterObject")
class IParameterObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Describes a single operation parameter.

    A unique parameter is defined by a combination of a name and location.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="in")
    def in_(self) -> builtins.str:
        '''(experimental) The location of the parameter.

        Possible values are "query", "header", "path" or "cookie".

        :stability: experimental
        '''
        ...

    @in_.setter
    def in_(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The name of the parameter. Parameter names are case sensitive.

        If in is "path", the name field MUST correspond to a template expression occurring within the path field in the Paths Object. See Path Templating for further information.
        If in is "header" and the name field is "Accept", "Content-Type" or "Authorization", the parameter definition SHALL be ignored.
        For all other cases, the name corresponds to the parameter name used by the in property.

        :stability: experimental
        '''
        ...

    @name.setter
    def name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="allowEmptyValue")
    def allow_empty_value(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Sets the ability to pass empty-valued parameters.

        This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.

        :stability: experimental
        '''
        ...

    @allow_empty_value.setter
    def allow_empty_value(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        ...

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the parameter.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether this parameter is mandatory.

        If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        ...

    @required.setter
    def required(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _IParameterObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Describes a single operation parameter.

    A unique parameter is defined by a combination of a name and location.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IParameterObject"

    @builtins.property
    @jsii.member(jsii_name="in")
    def in_(self) -> builtins.str:
        '''(experimental) The location of the parameter.

        Possible values are "query", "header", "path" or "cookie".

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "in"))

    @in_.setter
    def in_(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "in", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The name of the parameter. Parameter names are case sensitive.

        If in is "path", the name field MUST correspond to a template expression occurring within the path field in the Paths Object. See Path Templating for further information.
        If in is "header" and the name field is "Accept", "Content-Type" or "Authorization", the parameter definition SHALL be ignored.
        For all other cases, the name corresponds to the parameter name used by the in property.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="allowEmptyValue")
    def allow_empty_value(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Sets the ability to pass empty-valued parameters.

        This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "allowEmptyValue"))

    @allow_empty_value.setter
    def allow_empty_value(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowEmptyValue", value)

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "deprecated"))

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deprecated", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the parameter.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether this parameter is mandatory.

        If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterObject).__jsii_proxy_class__ = lambda : _IParameterObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IPathItemObject")
class IPathItemObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Describes the operations available on a single path.

    A Path Item MAY be empty, due to ACL constraints. The path itself is still exposed to the documentation viewer but they will not know which operations and parameters are available.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a DELETE operation on this path.

        :stability: experimental
        '''
        ...

    @delete.setter
    def delete(self, value: typing.Optional[IOperationObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional, string description, intended to apply to all operations in this path.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="get")
    def get(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a GET operation on this path.

        :stability: experimental
        '''
        ...

    @get.setter
    def get(self, value: typing.Optional[IOperationObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="head")
    def head(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a HEAD operation on this path.

        :stability: experimental
        '''
        ...

    @head.setter
    def head(self, value: typing.Optional[IOperationObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a OPTIONS operation on this path.

        :stability: experimental
        '''
        ...

    @options.setter
    def options(self, value: typing.Optional[IOperationObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.List[typing.Union["IReferenceObject", IParameterObject]]]:
        '''(experimental) A list of parameters that are applicable for all the operations described under this path.

        These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.

        :stability: experimental
        '''
        ...

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.List[typing.Union["IReferenceObject", IParameterObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="patch")
    def patch(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a PATCH operation on this path.

        :stability: experimental
        '''
        ...

    @patch.setter
    def patch(self, value: typing.Optional[IOperationObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="post")
    def post(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a POST operation on this path.

        :stability: experimental
        '''
        ...

    @post.setter
    def post(self, value: typing.Optional[IOperationObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="put")
    def put(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a PUT operation on this path.

        :stability: experimental
        '''
        ...

    @put.setter
    def put(self, value: typing.Optional[IOperationObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional, string summary, intended to apply to all operations in this path.

        :stability: experimental
        '''
        ...

    @summary.setter
    def summary(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="trace")
    def trace(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a TRACE operation on this path.

        :stability: experimental
        '''
        ...

    @trace.setter
    def trace(self, value: typing.Optional[IOperationObject]) -> None:
        ...


class _IPathItemObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Describes the operations available on a single path.

    A Path Item MAY be empty, due to ACL constraints. The path itself is still exposed to the documentation viewer but they will not know which operations and parameters are available.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IPathItemObject"

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a DELETE operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional, string description, intended to apply to all operations in this path.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="get")
    def get(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a GET operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "get"))

    @get.setter
    def get(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "get", value)

    @builtins.property
    @jsii.member(jsii_name="head")
    def head(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a HEAD operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "head"))

    @head.setter
    def head(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "head", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a OPTIONS operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.List[typing.Union["IReferenceObject", IParameterObject]]]:
        '''(experimental) A list of parameters that are applicable for all the operations described under this path.

        These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[typing.Union["IReferenceObject", IParameterObject]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.List[typing.Union["IReferenceObject", IParameterObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.List[typing.Union["IReferenceObject", IParameterObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="patch")
    def patch(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a PATCH operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "patch"))

    @patch.setter
    def patch(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patch", value)

    @builtins.property
    @jsii.member(jsii_name="post")
    def post(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a POST operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "post"))

    @post.setter
    def post(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "post", value)

    @builtins.property
    @jsii.member(jsii_name="put")
    def put(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a PUT operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "put"))

    @put.setter
    def put(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "put", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional, string summary, intended to apply to all operations in this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="trace")
    def trace(self) -> typing.Optional[IOperationObject]:
        '''(experimental) A definition of a TRACE operation on this path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOperationObject], jsii.get(self, "trace"))

    @trace.setter
    def trace(self, value: typing.Optional[IOperationObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOperationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trace", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPathItemObject).__jsii_proxy_class__ = lambda : _IPathItemObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IPathsObject")
class IPathsObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Holds the relative paths to the individual endpoints and their operations.

    The path is appended to the URL from the Server Object in order to construct the full URL. The Paths MAY be empty, due to ACL constraints.

    :stability: experimental
    '''

    pass


class _IPathsObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Holds the relative paths to the individual endpoints and their operations.

    The path is appended to the URL from the Server Object in order to construct the full URL. The Paths MAY be empty, due to ACL constraints.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IPathsObject"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPathsObject).__jsii_proxy_class__ = lambda : _IPathsObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IReferenceObject")
class IReferenceObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) A simple object to allow referencing other components in the specification, internally and externally.

    :stability: experimental
    '''

    pass


class _IReferenceObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) A simple object to allow referencing other components in the specification, internally and externally.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IReferenceObject"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReferenceObject).__jsii_proxy_class__ = lambda : _IReferenceObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IRequestBodyObject")
class IRequestBodyObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Describes a single request body.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Mapping[builtins.str, IMediaTypeObject]:
        '''(experimental) The content of the request body.

        The key is a media type or media type range and the value describes it. For requests that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*

        :stability: experimental
        '''
        ...

    @content.setter
    def content(self, value: typing.Mapping[builtins.str, IMediaTypeObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the request body.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines if the request body is required in the request.

        Defaults to false.

        :stability: experimental
        '''
        ...

    @required.setter
    def required(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _IRequestBodyObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Describes a single request body.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IRequestBodyObject"

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Mapping[builtins.str, IMediaTypeObject]:
        '''(experimental) The content of the request body.

        The key is a media type or media type range and the value describes it. For requests that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, IMediaTypeObject], jsii.get(self, "content"))

    @content.setter
    def content(self, value: typing.Mapping[builtins.str, IMediaTypeObject]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, IMediaTypeObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the request body.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines if the request body is required in the request.

        Defaults to false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRequestBodyObject).__jsii_proxy_class__ = lambda : _IRequestBodyObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IResponseObject")
class IResponseObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Describes a single response from an API Operation, including design-time, static links to operations based on the response.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''(experimental) A short description of the response.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IMediaTypeObject]]]:
        '''(experimental) A map containing descriptions of potential response payloads.

        The key is a media type or media type range and the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*

        :stability: experimental
        '''
        ...

    @content.setter
    def content(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IMediaTypeObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]]:
        '''(experimental) Maps a header name to its definition.

        RFC7230 states header names are case insensitive. If a response header is defined with the name "Content-Type", it SHALL be ignored.

        :stability: experimental
        '''
        ...

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]]:
        '''(experimental) A map of operations links that can be followed from the response.

        The key of the map is a short name for the link, following the naming constraints of the names for Component Objects.

        :stability: experimental
        '''
        ...

    @links.setter
    def links(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]],
    ) -> None:
        ...


class _IResponseObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Describes a single response from an API Operation, including design-time, static links to operations based on the response.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IResponseObject"

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''(experimental) A short description of the response.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IMediaTypeObject]]]:
        '''(experimental) A map containing descriptions of potential response payloads.

        The key is a media type or media type range and the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IMediaTypeObject]]], jsii.get(self, "content"))

    @content.setter
    def content(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IMediaTypeObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IMediaTypeObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]]:
        '''(experimental) Maps a header name to its definition.

        RFC7230 states header names are case insensitive. If a response header is defined with the name "Content-Type", it SHALL be ignored.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]], jsii.get(self, "headers"))

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]]:
        '''(experimental) A map of operations links that can be followed from the response.

        The key of the map is a short name for the link, following the naming constraints of the names for Component Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]], jsii.get(self, "links"))

    @links.setter
    def links(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "links", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResponseObject).__jsii_proxy_class__ = lambda : _IResponseObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IResponsesObject")
class IResponsesObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) A container for the expected responses of an operation.

    The container maps a HTTP response code to the expected response.
    The documentation is not necessarily expected to cover all possible HTTP response codes because they may not be known in advance. However, documentation is expected to cover a successful operation response and any known errors.
    The default MAY be used as a default response object for all HTTP codes that are not covered individually by the specification.
    The Responses Object MUST contain at least one response code, and it SHOULD be the response for a successful operation call.

    :stability: experimental
    '''

    pass


class _IResponsesObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) A container for the expected responses of an operation.

    The container maps a HTTP response code to the expected response.
    The documentation is not necessarily expected to cover all possible HTTP response codes because they may not be known in advance. However, documentation is expected to cover a successful operation response and any known errors.
    The default MAY be used as a default response object for all HTTP codes that are not covered individually by the specification.
    The Responses Object MUST contain at least one response code, and it SHOULD be the response for a successful operation call.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IResponsesObject"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResponsesObject).__jsii_proxy_class__ = lambda : _IResponsesObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.ISchemaObject")
class ISchemaObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) The Schema Object allows the definition of input and output data types.

    These types can be objects, but also primitives and arrays. This object is an extended subset of the JSON Schema Specification Wright Draft 00. For more information about the properties, see JSON Schema Core and JSON Schema Validation. Unless stated otherwise, the property definitions follow the JSON Schema.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a schema is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        ...

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="discriminator")
    def discriminator(self) -> typing.Optional["IDiscriminatorObject"]:
        '''(experimental) Adds support for polymorphism.

        The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.

        :stability: experimental
        '''
        ...

    @discriminator.setter
    def discriminator(self, value: typing.Optional["IDiscriminatorObject"]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> typing.Any:
        '''(experimental) A free-form property to include an example of an instance for this schema.

        To represent examples that cannot be naturally represented in JSON or YAML, a string value can be used to contain the example with escaping where necessary.

        :stability: experimental
        '''
        ...

    @example.setter
    def example(self, value: typing.Any) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this schema.

        :stability: experimental
        '''
        ...

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) A true value adds "null" to the allowed type specified by the type keyword, only if type is explicitly defined within the same Schema Object.

        Other Schema Object constraints retain their defined behavior, and therefore may disallow the use of null as a value. A false value leaves the specified or default type unmodified. The default value is false.

        :stability: experimental
        '''
        ...

    @nullable.setter
    def nullable(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Relevant only for Schema "properties" definitions.

        Declares the property as "read only". This means that it MAY be sent as part of a response but SHOULD NOT be sent as part of the request. If the property is marked as being true and is in the required list, the required will take effect on the response only. A property MUST NOT be marked as both and writeOnly being true. Default value is false.

        :stability: experimental
        '''
        ...

    @read_only.setter
    def read_only(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="writeOnly")
    def write_only(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Relevant only for Schema "properties" definitions.

        Declares the property as "write only". Therefore, it MAY be sent as part of a request but SHOULD NOT be sent as part of the response. If the property is marked as writeOnly being true and is in the required list, the required will take effect on the request only. A property MUST NOT be marked as both and writeOnly being true. Default value is false.

        :stability: experimental
        '''
        ...

    @write_only.setter
    def write_only(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="xml")
    def xml(self) -> typing.Optional["IXmlObject"]:
        '''(experimental) This MAY be used only on properties schemas.

        It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.

        :stability: experimental
        '''
        ...

    @xml.setter
    def xml(self, value: typing.Optional["IXmlObject"]) -> None:
        ...


class _ISchemaObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) The Schema Object allows the definition of input and output data types.

    These types can be objects, but also primitives and arrays. This object is an extended subset of the JSON Schema Specification Wright Draft 00. For more information about the properties, see JSON Schema Core and JSON Schema Validation. Unless stated otherwise, the property definitions follow the JSON Schema.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.ISchemaObject"

    @builtins.property
    @jsii.member(jsii_name="deprecated")
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a schema is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "deprecated"))

    @deprecated.setter
    def deprecated(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deprecated", value)

    @builtins.property
    @jsii.member(jsii_name="discriminator")
    def discriminator(self) -> typing.Optional["IDiscriminatorObject"]:
        '''(experimental) Adds support for polymorphism.

        The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["IDiscriminatorObject"], jsii.get(self, "discriminator"))

    @discriminator.setter
    def discriminator(self, value: typing.Optional["IDiscriminatorObject"]) -> None:
        if __debug__:
            def stub(value: typing.Optional["IDiscriminatorObject"]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "discriminator", value)

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> typing.Any:
        '''(experimental) A free-form property to include an example of an instance for this schema.

        To represent examples that cannot be naturally represented in JSON or YAML, a string value can be used to contain the example with escaping where necessary.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "example"))

    @example.setter
    def example(self, value: typing.Any) -> None:
        if __debug__:
            def stub(value: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "example", value)

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this schema.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IExternalDocumentationObject], jsii.get(self, "externalDocs"))

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[IExternalDocumentationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalDocs", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) A true value adds "null" to the allowed type specified by the type keyword, only if type is explicitly defined within the same Schema Object.

        Other Schema Object constraints retain their defined behavior, and therefore may disallow the use of null as a value. A false value leaves the specified or default type unmodified. The default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Relevant only for Schema "properties" definitions.

        Declares the property as "read only". This means that it MAY be sent as part of a response but SHOULD NOT be sent as part of the request. If the property is marked as being true and is in the required list, the required will take effect on the response only. A property MUST NOT be marked as both and writeOnly being true. Default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="writeOnly")
    def write_only(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Relevant only for Schema "properties" definitions.

        Declares the property as "write only". Therefore, it MAY be sent as part of a request but SHOULD NOT be sent as part of the response. If the property is marked as writeOnly being true and is in the required list, the required will take effect on the request only. A property MUST NOT be marked as both and writeOnly being true. Default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "writeOnly"))

    @write_only.setter
    def write_only(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOnly", value)

    @builtins.property
    @jsii.member(jsii_name="xml")
    def xml(self) -> typing.Optional["IXmlObject"]:
        '''(experimental) This MAY be used only on properties schemas.

        It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["IXmlObject"], jsii.get(self, "xml"))

    @xml.setter
    def xml(self, value: typing.Optional["IXmlObject"]) -> None:
        if __debug__:
            def stub(value: typing.Optional["IXmlObject"]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xml", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaObject).__jsii_proxy_class__ = lambda : _ISchemaObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.ISecurityRequirementObject")
class ISecurityRequirementObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Lists the required security schemes to execute this operation.

    The name used for each property MUST correspond to a security scheme declared in the Security Schemes under the Components Object.
    Security Requirement Objects that contain multiple schemes require that all schemes MUST be satisfied for a request to be authorized. This enables support for scenarios where multiple query parameters or HTTP headers are required to convey security information.
    When a list of Security Requirement Objects is defined on the OpenAPI Object or Operation Object, only one of the Security Requirement Objects in the list needs to be satisfied to authorize the request.

    :stability: experimental
    '''

    pass


class _ISecurityRequirementObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Lists the required security schemes to execute this operation.

    The name used for each property MUST correspond to a security scheme declared in the Security Schemes under the Components Object.
    Security Requirement Objects that contain multiple schemes require that all schemes MUST be satisfied for a request to be authorized. This enables support for scenarios where multiple query parameters or HTTP headers are required to convey security information.
    When a list of Security Requirement Objects is defined on the OpenAPI Object or Operation Object, only one of the Security Requirement Objects in the list needs to be satisfied to authorize the request.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.ISecurityRequirementObject"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityRequirementObject).__jsii_proxy_class__ = lambda : _ISecurityRequirementObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.ISecuritySchemeObject")
class ISecuritySchemeObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Defines a security scheme that can be used by the operations.

    Supported schemes are HTTP authentication, an API key (either as a header, a cookie parameter or as a query parameter), OAuth2's common flows (implicit, password, client credentials and authorization code) as defined in RFC6749, and OpenID Connect Discovery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''(experimental) The type of the security scheme.

        Valid values are "apiKey", "http", "oauth2", "openIdConnect".

        :stability: experimental
        '''
        ...

    @type.setter
    def type(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="bearerFormat")
    def bearer_format(self) -> typing.Optional[builtins.str]:
        '''(experimental) A hint to the client to identify how the bearer token is formatted.

        Bearer tokens are usually generated by an authorization server, so this information is primarily for documentation purposes.

        :stability: experimental
        '''
        ...

    @bearer_format.setter
    def bearer_format(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description for security scheme.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="flow")
    def flow(self) -> typing.Optional[IOAuthFlowsObject]:
        '''(experimental) An object containing configuration information for the flow types supported.

        REQUIRED for oauth2.

        :stability: experimental
        '''
        ...

    @flow.setter
    def flow(self, value: typing.Optional[IOAuthFlowsObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="in")
    def in_(self) -> typing.Optional[builtins.str]:
        '''(experimental) The location of the API key.

        Valid values are "query", "header" or "cookie".
        REQUIRED for apiKey.

        :stability: experimental
        '''
        ...

    @in_.setter
    def in_(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the header, query or cookie parameter to be used.

        REQUIRED for apiKey.

        :stability: experimental
        '''
        ...

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="openIdConnectUrl")
    def open_id_connect_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) OpenId Connect URL to discover OAuth2 configuration values.

        This MUST be in the form of a URL.
        REQUIRED for openIdConnect.

        :stability: experimental
        '''
        ...

    @open_id_connect_url.setter
    def open_id_connect_url(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235.

        The values used SHOULD be registered in the IANA Authentication Scheme registry.
        REQUIRED for http.

        :stability: experimental
        '''
        ...

    @scheme.setter
    def scheme(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _ISecuritySchemeObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Defines a security scheme that can be used by the operations.

    Supported schemes are HTTP authentication, an API key (either as a header, a cookie parameter or as a query parameter), OAuth2's common flows (implicit, password, client credentials and authorization code) as defined in RFC6749, and OpenID Connect Discovery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.ISecuritySchemeObject"

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''(experimental) The type of the security scheme.

        Valid values are "apiKey", "http", "oauth2", "openIdConnect".

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="bearerFormat")
    def bearer_format(self) -> typing.Optional[builtins.str]:
        '''(experimental) A hint to the client to identify how the bearer token is formatted.

        Bearer tokens are usually generated by an authorization server, so this information is primarily for documentation purposes.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bearerFormat"))

    @bearer_format.setter
    def bearer_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bearerFormat", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description for security scheme.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="flow")
    def flow(self) -> typing.Optional[IOAuthFlowsObject]:
        '''(experimental) An object containing configuration information for the flow types supported.

        REQUIRED for oauth2.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IOAuthFlowsObject], jsii.get(self, "flow"))

    @flow.setter
    def flow(self, value: typing.Optional[IOAuthFlowsObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IOAuthFlowsObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flow", value)

    @builtins.property
    @jsii.member(jsii_name="in")
    def in_(self) -> typing.Optional[builtins.str]:
        '''(experimental) The location of the API key.

        Valid values are "query", "header" or "cookie".
        REQUIRED for apiKey.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "in"))

    @in_.setter
    def in_(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "in", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the header, query or cookie parameter to be used.

        REQUIRED for apiKey.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="openIdConnectUrl")
    def open_id_connect_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) OpenId Connect URL to discover OAuth2 configuration values.

        This MUST be in the form of a URL.
        REQUIRED for openIdConnect.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "openIdConnectUrl"))

    @open_id_connect_url.setter
    def open_id_connect_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openIdConnectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235.

        The values used SHOULD be registered in the IANA Authentication Scheme registry.
        REQUIRED for http.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecuritySchemeObject).__jsii_proxy_class__ = lambda : _ISecuritySchemeObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IServerObject")
class IServerObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) An object representing a Server.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        '''(experimental) REQUIRED.

        A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.

        :stability: experimental
        '''
        ...

    @url.setter
    def url(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional string describing the host designated by the URL.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "IServerVariableObject"]]:
        '''(experimental) A map between a variable name and its value.

        The value is used for substitution in the server's URL template.

        :stability: experimental
        '''
        ...

    @variables.setter
    def variables(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, "IServerVariableObject"]],
    ) -> None:
        ...


class _IServerObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) An object representing a Server.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IServerObject"

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        '''(experimental) REQUIRED.

        A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional string describing the host designated by the URL.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "IServerVariableObject"]]:
        '''(experimental) A map between a variable name and its value.

        The value is used for substitution in the server's URL template.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "IServerVariableObject"]], jsii.get(self, "variables"))

    @variables.setter
    def variables(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, "IServerVariableObject"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, "IServerVariableObject"]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variables", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerObject).__jsii_proxy_class__ = lambda : _IServerObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IServerVariableObject")
class IServerVariableObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) An object representing a Server Variable for server URL template substitution.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        '''(experimental) The default value to use for substitution, which SHALL be sent if an alternate value is not supplied.

        Note this behavior is different than the Schema Object's treatment of default values, because in those cases parameter values are optional. If the enum is defined, the value SHOULD exist in the enum's values.

        :stability: experimental
        '''
        ...

    @default.setter
    def default(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional description for the server variable.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="enum")
    def enum(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An enumeration of string values to be used if the substitution options are from a limited set.

        The array SHOULD NOT be empty.

        :stability: experimental
        '''
        ...

    @enum.setter
    def enum(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        ...


class _IServerVariableObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) An object representing a Server Variable for server URL template substitution.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IServerVariableObject"

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        '''(experimental) The default value to use for substitution, which SHALL be sent if an alternate value is not supplied.

        Note this behavior is different than the Schema Object's treatment of default values, because in those cases parameter values are optional. If the enum is defined, the value SHOULD exist in the enum's values.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional description for the server variable.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enum")
    def enum(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An enumeration of string values to be used if the substitution options are from a limited set.

        The array SHOULD NOT be empty.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enum"))

    @enum.setter
    def enum(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enum", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerVariableObject).__jsii_proxy_class__ = lambda : _IServerVariableObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.ITagObject")
class ITagObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Adds metadata to a single tag that is used by the Operation Object.

    It is not mandatory to have a Tag Object per tag defined in the Operation Object instances.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The name of the tag.

        :stability: experimental
        '''
        ...

    @name.setter
    def name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description for the tag.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this tag.

        :stability: experimental
        '''
        ...

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        ...


class _ITagObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Adds metadata to a single tag that is used by the Operation Object.

    It is not mandatory to have a Tag Object per tag defined in the Operation Object instances.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.ITagObject"

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The name of the tag.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description for the tag.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this tag.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IExternalDocumentationObject], jsii.get(self, "externalDocs"))

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[IExternalDocumentationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalDocs", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITagObject).__jsii_proxy_class__ = lambda : _ITagObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IXmlObject")
class IXmlObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) A metadata object that allows for more fine-tuned XML model definitions.

    When using arrays, XML element names are not inferred (for singular/plural forms) and the name property SHOULD be used to add that information. See examples for expected behavior.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Declares whether the property definition translates to an attribute instead of an element.

        Default value is false.

        :stability: experimental
        '''
        ...

    @attribute.setter
    def attribute(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Replaces the name of the element/attribute used for the described schema property.

        When defined within items, it will affect the name of the individual XML elements within the list. When defined alongside type being array (outside the items), it will affect the wrapping element and only if wrapped is true. If wrapped is false, it will be ignored.

        :stability: experimental
        '''
        ...

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URI of the namespace definition.

        Value MUST be in the form of an absolute URI.

        :stability: experimental
        '''
        ...

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> typing.Optional[builtins.str]:
        '''(experimental) The prefix to be used for the name.

        :stability: experimental
        '''
        ...

    @prefix.setter
    def prefix(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="wrapped")
    def wrapped(self) -> typing.Optional[builtins.bool]:
        '''(experimental) MAY be used only for an array definition.

        Signifies whether the array is wrapped (for example, ) or unwrapped (). Default value is false. The definition takes effect only when defined alongside type being array (outside the items).

        :stability: experimental
        '''
        ...

    @wrapped.setter
    def wrapped(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _IXmlObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) A metadata object that allows for more fine-tuned XML model definitions.

    When using arrays, XML element names are not inferred (for singular/plural forms) and the name property SHOULD be used to add that information. See examples for expected behavior.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IXmlObject"

    @builtins.property
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Declares whether the property definition translates to an attribute instead of an element.

        Default value is false.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "attribute"))

    @attribute.setter
    def attribute(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attribute", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Replaces the name of the element/attribute used for the described schema property.

        When defined within items, it will affect the name of the individual XML elements within the list. When defined alongside type being array (outside the items), it will affect the wrapping element and only if wrapped is true. If wrapped is false, it will be ignored.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URI of the namespace definition.

        Value MUST be in the form of an absolute URI.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> typing.Optional[builtins.str]:
        '''(experimental) The prefix to be used for the name.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="wrapped")
    def wrapped(self) -> typing.Optional[builtins.bool]:
        '''(experimental) MAY be used only for an array definition.

        Signifies whether the array is wrapped (for example, ) or unwrapped (). Default value is false. The definition takes effect only when defined alongside type being array (outside the items).

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "wrapped"))

    @wrapped.setter
    def wrapped(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapped", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IXmlObject).__jsii_proxy_class__ = lambda : _IXmlObjectProxy


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.InfoObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "title": "title",
        "version": "version",
        "contact": "contact",
        "description": "description",
        "license": "license",
        "terms_of_service": "termsOfService",
    },
)
class InfoObject(Extensible):
    def __init__(
        self,
        *,
        title: builtins.str,
        version: builtins.str,
        contact: typing.Optional[typing.Union["ContactObject", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        license: typing.Optional[typing.Union["LicenseObject", typing.Dict[str, typing.Any]]] = None,
        terms_of_service: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) The object provides metadata about the API.

        The metadata MAY be used by the clients if needed, and MAY be presented in editing or documentation generation tools for convenience.

        :param title: (experimental) The title of the API.
        :param version: (experimental) The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version).
        :param contact: (experimental) The contact information for the exposed API.
        :param description: (experimental) A short description of the API. CommonMark syntax MAY be used for rich text representation.
        :param license: (experimental) The license information for the exposed API.
        :param terms_of_service: (experimental) A URL to the Terms of Service for the API. MUST be in the format of a URL.

        :stability: experimental
        '''
        if isinstance(contact, dict):
            contact = ContactObject(**contact)
        if isinstance(license, dict):
            license = LicenseObject(**license)
        if __debug__:
            def stub(
                *,
                title: builtins.str,
                version: builtins.str,
                contact: typing.Optional[typing.Union["ContactObject", typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                license: typing.Optional[typing.Union["LicenseObject", typing.Dict[str, typing.Any]]] = None,
                terms_of_service: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument contact", value=contact, expected_type=type_hints["contact"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument license", value=license, expected_type=type_hints["license"])
            check_type(argname="argument terms_of_service", value=terms_of_service, expected_type=type_hints["terms_of_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "title": title,
            "version": version,
        }
        if contact is not None:
            self._values["contact"] = contact
        if description is not None:
            self._values["description"] = description
        if license is not None:
            self._values["license"] = license
        if terms_of_service is not None:
            self._values["terms_of_service"] = terms_of_service

    @builtins.property
    def title(self) -> builtins.str:
        '''(experimental) The title of the API.

        :stability: experimental
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''(experimental) The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version).

        :stability: experimental
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact(self) -> typing.Optional["ContactObject"]:
        '''(experimental) The contact information for the exposed API.

        :stability: experimental
        '''
        result = self._values.get("contact")
        return typing.cast(typing.Optional["ContactObject"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description of the API.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license(self) -> typing.Optional["LicenseObject"]:
        '''(experimental) The license information for the exposed API.

        :stability: experimental
        '''
        result = self._values.get("license")
        return typing.cast(typing.Optional["LicenseObject"], result)

    @builtins.property
    def terms_of_service(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL to the Terms of Service for the API.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        result = self._values.get("terms_of_service")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InfoObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IBaseIntegration)
class Integration(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@alma-cdk/openapix.Integration",
):
    '''(experimental) Essentially responsible for converting CDK ``IntegrationProps`` into API Gateway OpenApi integration extension ()``XAmazonApigatewayIntegration``).

    Also defines few basic methods (``getIntegration`` & ``getValidatorId``) used
    by derivative classes.

    :stability: experimental
    '''

    def __init__(
        self,
        props: typing.Union[aws_cdk.aws_apigateway.IntegrationProps, typing.Dict[str, typing.Any]],
        *,
        type: "InternalIntegrationType",
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Construc a new integration.

        :param props: -
        :param type: 
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                props: typing.Union[aws_cdk.aws_apigateway.IntegrationProps, typing.Dict[str, typing.Any]],
                *,
                type: "InternalIntegrationType",
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        config = IntegrationConfig(type=type, validator=validator)

        jsii.create(self.__class__, self, [props, config])

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "InternalIntegrationType":
        '''(experimental) Identifier to enable internal type checks.

        :stability: experimental
        '''
        return typing.cast("InternalIntegrationType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="xAmazonApigatewayIntegration")
    def x_amazon_apigateway_integration(self) -> "XAmazonApigatewayIntegration":
        '''
        :stability: experimental
        '''
        return typing.cast("XAmazonApigatewayIntegration", jsii.get(self, "xAmazonApigatewayIntegration"))

    @builtins.property
    @jsii.member(jsii_name="validator")
    def validator(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validator"))


class _IntegrationProxy(Integration):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Integration).__jsii_proxy_class__ = lambda : _IntegrationProxy


@jsii.enum(jsii_type="@alma-cdk/openapix.InternalIntegrationType")
class InternalIntegrationType(enum.Enum):
    '''
    :stability: experimental
    '''

    AWS = "AWS"
    '''
    :stability: experimental
    '''
    CORS = "CORS"
    '''
    :stability: experimental
    '''
    HTTP = "HTTP"
    '''
    :stability: experimental
    '''
    LAMBDA = "LAMBDA"
    '''
    :stability: experimental
    '''
    MOCK = "MOCK"
    '''
    :stability: experimental
    '''


class LambdaAuthorizer(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.LambdaAuthorizer",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        auth_type: builtins.str,
        fn: aws_cdk.aws_lambda.IFunction,
        identity_source: builtins.str,
        type: builtins.str,
        results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param auth_type: 
        :param fn: 
        :param identity_source: 
        :param type: 
        :param results_cache_ttl: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                auth_type: builtins.str,
                fn: aws_cdk.aws_lambda.IFunction,
                identity_source: builtins.str,
                type: builtins.str,
                results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaAuthorizerProps(
            auth_type=auth_type,
            fn=fn,
            identity_source=identity_source,
            type=type,
            results_cache_ttl=results_cache_ttl,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="grantFunctionInvoke")
    def grant_function_invoke(self, api: aws_cdk.aws_apigateway.IRestApi) -> None:
        '''(experimental) Allow Lambda invoke action to be performed by given identity.

        The ARN format for authorizers is different compared to integrations when granting permissions,
        ex. arn:aws:execute-api:us-east-1:123456789012:api-id/authorizers/authorizer-id

        :param api: -

        :stability: experimental
        '''
        if __debug__:
            def stub(api: aws_cdk.aws_apigateway.IRestApi) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        return typing.cast(None, jsii.invoke(self, "grantFunctionInvoke", [api]))

    @builtins.property
    @jsii.member(jsii_name="fn")
    def fn(self) -> aws_cdk.aws_lambda.IFunction:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "fn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="xAmazonApigatewayAuthorizer")
    def x_amazon_apigateway_authorizer(self) -> "XAmazonApigatewayAuthorizer":
        '''
        :stability: experimental
        '''
        return typing.cast("XAmazonApigatewayAuthorizer", jsii.get(self, "xAmazonApigatewayAuthorizer"))

    @builtins.property
    @jsii.member(jsii_name="xAmazonApigatewayAuthtype")
    def x_amazon_apigateway_authtype(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "xAmazonApigatewayAuthtype"))


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.LambdaAuthorizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "auth_type": "authType",
        "fn": "fn",
        "identity_source": "identitySource",
        "type": "type",
        "results_cache_ttl": "resultsCacheTtl",
    },
)
class LambdaAuthorizerProps:
    def __init__(
        self,
        *,
        auth_type: builtins.str,
        fn: aws_cdk.aws_lambda.IFunction,
        identity_source: builtins.str,
        type: builtins.str,
        results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''
        :param auth_type: 
        :param fn: 
        :param identity_source: 
        :param type: 
        :param results_cache_ttl: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                auth_type: builtins.str,
                fn: aws_cdk.aws_lambda.IFunction,
                identity_source: builtins.str,
                type: builtins.str,
                results_cache_ttl: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
            check_type(argname="argument identity_source", value=identity_source, expected_type=type_hints["identity_source"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument results_cache_ttl", value=results_cache_ttl, expected_type=type_hints["results_cache_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "auth_type": auth_type,
            "fn": fn,
            "identity_source": identity_source,
            "type": type,
        }
        if results_cache_ttl is not None:
            self._values["results_cache_ttl"] = results_cache_ttl

    @builtins.property
    def auth_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("auth_type")
        assert result is not None, "Required property 'auth_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fn(self) -> aws_cdk.aws_lambda.IFunction:
        '''
        :stability: experimental
        '''
        result = self._values.get("fn")
        assert result is not None, "Required property 'fn' is missing"
        return typing.cast(aws_cdk.aws_lambda.IFunction, result)

    @builtins.property
    def identity_source(self) -> builtins.str:
        '''
        :stability: experimental

        Example::

            apigateway.IdentitySource.header('Authorization')
        '''
        result = self._values.get("identity_source")
        assert result is not None, "Required property 'identity_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def results_cache_ttl(self) -> typing.Optional[aws_cdk.Duration]:
        '''
        :stability: experimental
        '''
        result = self._values.get("results_cache_ttl")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaAuthorizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaIntegration(
    Integration,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.LambdaIntegration",
):
    '''(experimental) Defines an AWS Lambda integration.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        fn: aws_cdk.aws_lambda.IFunction,
        *,
        allow_test_invoke: typing.Optional[builtins.bool] = None,
        proxy: typing.Optional[builtins.bool] = None,
        validator: typing.Optional[builtins.str] = None,
        cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_namespace: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
        content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
        credentials_passthrough: typing.Optional[builtins.bool] = None,
        credentials_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        integration_responses: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_apigateway.IntegrationResponse, typing.Dict[str, typing.Any]]]] = None,
        passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc_link: typing.Optional[aws_cdk.aws_apigateway.IVpcLink] = None,
    ) -> None:
        '''(experimental) Defines an AWS Lambda integration.

        :param scope: -
        :param fn: -
        :param allow_test_invoke: Allow invoking method from AWS Console UI (for testing purposes). This will add another permission to the AWS Lambda resource policy which will allow the ``test-invoke-stage`` stage to invoke this handler. If this is set to ``false``, the function will only be usable from the deployment endpoint. Default: true
        :param proxy: Use proxy integration or normal (request/response mapping) integration. Default: true
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.
        :param cache_key_parameters: A list of request parameters whose values are to be cached. It determines request parameters that will make it into the cache key.
        :param cache_namespace: An API-specific tag group of related cached parameters.
        :param connection_type: The type of network connection to the integration endpoint. Default: - ConnectionType.VPC_LINK if ``vpcLink`` property is configured; ConnectionType.Internet otherwise.
        :param content_handling: Specifies how to handle request payload content type conversions. Default: none if this property isn't defined, the request payload is passed through from the method request to the integration request without modification, provided that the ``passthroughBehaviors`` property is configured to support payload pass-through.
        :param credentials_passthrough: Requires that the caller's identity be passed through from the request. Default: Caller identity is not passed through
        :param credentials_role: An IAM role that API Gateway assumes. Mutually exclusive with ``credentialsPassThrough``. Default: A role is not assumed
        :param integration_responses: The response that API Gateway provides after a method's backend completes processing a request. API Gateway intercepts the response from the backend so that you can control how API Gateway surfaces backend responses. For example, you can map the backend status codes to codes that you define.
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
        :param request_parameters: The request parameters that API Gateway sends with the backend request. Specify request parameters as key-value pairs (string-to-string mappings), with a destination as the key and a source as the value. Specify the destination by using the following pattern integration.request.location.name, where location is querystring, path, or header, and name is a valid, unique parameter name. The source must be an existing method request parameter or a static value. You must enclose static values in single quotation marks and pre-encode these values based on their destination in the request.
        :param request_templates: A map of Apache Velocity templates that are applied on the request payload. The template that API Gateway uses is based on the value of the Content-Type header that's sent by the client. The content type value is the key, and the template is the value (specified as a string), such as the following snippet:: { "application/json": "{ \\"statusCode\\": 200 }" }
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)
        :param vpc_link: The VpcLink used for the integration. Required if connectionType is VPC_LINK

        :stability: experimental

        Example::

            '/message': {
               'POST': new openapix.LambdaIntegration(this, fn),
            },
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                fn: aws_cdk.aws_lambda.IFunction,
                *,
                allow_test_invoke: typing.Optional[builtins.bool] = None,
                proxy: typing.Optional[builtins.bool] = None,
                validator: typing.Optional[builtins.str] = None,
                cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
                cache_namespace: typing.Optional[builtins.str] = None,
                connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
                content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
                credentials_passthrough: typing.Optional[builtins.bool] = None,
                credentials_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                integration_responses: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_apigateway.IntegrationResponse, typing.Dict[str, typing.Any]]]] = None,
                passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
                request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc_link: typing.Optional[aws_cdk.aws_apigateway.IVpcLink] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        props = LambdaIntegrationOptions(
            allow_test_invoke=allow_test_invoke,
            proxy=proxy,
            validator=validator,
            cache_key_parameters=cache_key_parameters,
            cache_namespace=cache_namespace,
            connection_type=connection_type,
            content_handling=content_handling,
            credentials_passthrough=credentials_passthrough,
            credentials_role=credentials_role,
            integration_responses=integration_responses,
            passthrough_behavior=passthrough_behavior,
            request_parameters=request_parameters,
            request_templates=request_templates,
            timeout=timeout,
            vpc_link=vpc_link,
        )

        jsii.create(self.__class__, self, [scope, fn, props])

    @jsii.member(jsii_name="grantFunctionInvoke")
    def grant_function_invoke(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        principal: aws_cdk.aws_iam.ServicePrincipal,
    ) -> None:
        '''(experimental) Allow Lambda invoke action to be performed by given identity.

        :param scope: -
        :param id: -
        :param principal: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                principal: aws_cdk.aws_iam.ServicePrincipal,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        return typing.cast(None, jsii.invoke(self, "grantFunctionInvoke", [scope, id, principal]))

    @builtins.property
    @jsii.member(jsii_name="fn")
    def fn(self) -> aws_cdk.aws_lambda.IFunction:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "fn"))


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.LicenseObject",
    jsii_struct_bases=[Extensible],
    name_mapping={"name": "name", "url": "url"},
)
class LicenseObject(Extensible):
    def __init__(
        self,
        *,
        name: builtins.str,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) The license information for the exposed API.

        :param name: (experimental) The license name used for the API.
        :param url: (experimental) A URL to the license used for the API. MUST be in the format of a URL.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                url: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The license name used for the API.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL to the license used for the API.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LicenseObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.LinkObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "description": "description",
        "operation_id": "operationId",
        "operation_ref": "operationRef",
        "parameters": "parameters",
        "request_body": "requestBody",
        "server": "server",
    },
)
class LinkObject(Extensible):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        operation_id: typing.Optional[builtins.str] = None,
        operation_ref: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        request_body: typing.Any = None,
        server: typing.Optional[typing.Union["ServerObject", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) The Link object represents a possible design-time link for a response.

        The presence of a link does not guarantee the caller's ability to successfully invoke it, rather it provides a known relationship and traversal mechanism between responses and other operations.
        Unlike dynamic links (i.e. links provided in the response payload), the OAS linking mechanism does not require link information in the runtime response.
        For computing links, and providing instructions to execute them, a runtime expression is used for accessing values in an operation and using them as parameters while invoking the linked operation.

        :param description: (experimental) A description of the link. CommonMark syntax MAY be used for rich text representation.
        :param operation_id: (experimental) The name of an existing, resolvable OAS operation, as defined with a unique operationId. This field is mutually exclusive of the operationRef field.
        :param operation_ref: (experimental) A relative or absolute URI reference to an OAS operation. This field is mutually exclusive of the operationId field, and MUST point to an Operation Object. Relative operationRef values MAY be used to locate an existing Operation Object in the OpenAPI definition.
        :param parameters: (experimental) A map representing parameters to pass to an operation as specified with operationId or identified via operationRef. The key is the parameter name to be used, whereas the value can be a constant or an expression to be evaluated and passed to the linked operation. The parameter name can be qualified using the parameter location [{in}.]{name} for operations that use the same parameter name in different locations (e.g. path.id).
        :param request_body: (experimental) A literal value or {expression} to use as a request body when calling the target operation.
        :param server: (experimental) A server object to be used by the target operation.

        :stability: experimental
        '''
        if isinstance(server, dict):
            server = ServerObject(**server)
        if __debug__:
            def stub(
                *,
                description: typing.Optional[builtins.str] = None,
                operation_id: typing.Optional[builtins.str] = None,
                operation_ref: typing.Optional[builtins.str] = None,
                parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
                request_body: typing.Any = None,
                server: typing.Optional[typing.Union["ServerObject", typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument operation_id", value=operation_id, expected_type=type_hints["operation_id"])
            check_type(argname="argument operation_ref", value=operation_ref, expected_type=type_hints["operation_ref"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument request_body", value=request_body, expected_type=type_hints["request_body"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if operation_id is not None:
            self._values["operation_id"] = operation_id
        if operation_ref is not None:
            self._values["operation_ref"] = operation_ref
        if parameters is not None:
            self._values["parameters"] = parameters
        if request_body is not None:
            self._values["request_body"] = request_body
        if server is not None:
            self._values["server"] = server

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A description of the link.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of an existing, resolvable OAS operation, as defined with a unique operationId.

        This field is mutually exclusive of the operationRef field.

        :stability: experimental
        '''
        result = self._values.get("operation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_ref(self) -> typing.Optional[builtins.str]:
        '''(experimental) A relative or absolute URI reference to an OAS operation.

        This field is mutually exclusive of the operationId field, and MUST point to an Operation Object. Relative operationRef values MAY be used to locate an existing Operation Object in the OpenAPI definition.

        :stability: experimental
        '''
        result = self._values.get("operation_ref")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) A map representing parameters to pass to an operation as specified with operationId or identified via operationRef.

        The key is the parameter name to be used, whereas the value can be a constant or an expression to be evaluated and passed to the linked operation. The parameter name can be qualified using the parameter location [{in}.]{name} for operations that use the same parameter name in different locations (e.g. path.id).

        :stability: experimental
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def request_body(self) -> typing.Any:
        '''(experimental) A literal value or {expression} to use as a request body when calling the target operation.

        :stability: experimental
        '''
        result = self._values.get("request_body")
        return typing.cast(typing.Any, result)

    @builtins.property
    def server(self) -> typing.Optional["ServerObject"]:
        '''(experimental) A server object to be used by the target operation.

        :stability: experimental
        '''
        result = self._values.get("server")
        return typing.cast(typing.Optional["ServerObject"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinkObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.MediaTypeObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "encoding": "encoding",
        "example": "example",
        "examples": "examples",
        "schema": "schema",
    },
)
class MediaTypeObject(Extensible):
    def __init__(
        self,
        *,
        encoding: typing.Optional[typing.Mapping[builtins.str, typing.Union["EncodingObject", typing.Dict[str, typing.Any]]]] = None,
        example: typing.Any = None,
        examples: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["ExampleObject", typing.Dict[str, typing.Any]]]]] = None,
        schema: typing.Optional[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["SchemaObject", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) Each Media Type Object provides schema and examples for the media type identified by its key.

        :param encoding: (experimental) A map between a property name and its encoding information. The key, being the property name, MUST exist in the schema as a property. The encoding object SHALL only apply to requestBody objects when the media type is multipart or application/x-www-form-urlencoded.
        :param example: (experimental) Example of the media type. The example object SHOULD be in the correct format as specified by the media type. The example field is mutually exclusive of the examples field. Furthermore, if referencing a schema which contains an example, the example value SHALL override the example provided by the schema.
        :param examples: (experimental) Examples of the media type. Each example object SHOULD match the media type and specified schema if present. The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema which contains an example, the examples value SHALL override the example provided by the schema.
        :param schema: (experimental) The schema defining the content of the request, response, or parameter.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                encoding: typing.Optional[typing.Mapping[builtins.str, typing.Union["EncodingObject", typing.Dict[str, typing.Any]]]] = None,
                example: typing.Any = None,
                examples: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["ExampleObject", typing.Dict[str, typing.Any]]]]] = None,
                schema: typing.Optional[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["SchemaObject", typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument examples", value=examples, expected_type=type_hints["examples"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[str, typing.Any] = {}
        if encoding is not None:
            self._values["encoding"] = encoding
        if example is not None:
            self._values["example"] = example
        if examples is not None:
            self._values["examples"] = examples
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def encoding(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "EncodingObject"]]:
        '''(experimental) A map between a property name and its encoding information.

        The key, being the property name, MUST exist in the schema as a property. The encoding object SHALL only apply to requestBody objects when the media type is multipart or application/x-www-form-urlencoded.

        :stability: experimental
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "EncodingObject"]], result)

    @builtins.property
    def example(self) -> typing.Any:
        '''(experimental) Example of the media type.

        The example object SHOULD be in the correct format as specified by the media type. The example field is mutually exclusive of the examples field. Furthermore, if referencing a schema which contains an example, the example value SHALL override the example provided by the schema.

        :stability: experimental
        '''
        result = self._values.get("example")
        return typing.cast(typing.Any, result)

    @builtins.property
    def examples(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union["ReferenceObject", "ExampleObject"]]]:
        '''(experimental) Examples of the media type.

        Each example object SHOULD match the media type and specified schema if present. The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema which contains an example, the examples value SHALL override the example provided by the schema.

        :stability: experimental
        '''
        result = self._values.get("examples")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union["ReferenceObject", "ExampleObject"]]], result)

    @builtins.property
    def schema(
        self,
    ) -> typing.Optional[typing.Union["ReferenceObject", "SchemaObject"]]:
        '''(experimental) The schema defining the content of the request, response, or parameter.

        :stability: experimental
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[typing.Union["ReferenceObject", "SchemaObject"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTypeObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MockIntegration(
    Integration,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.MockIntegration",
):
    '''(experimental) Defines Mock integration.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_namespace: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
        content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
        credentials_passthrough: typing.Optional[builtins.bool] = None,
        credentials_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        integration_responses: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_apigateway.IntegrationResponse, typing.Dict[str, typing.Any]]]] = None,
        passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc_link: typing.Optional[aws_cdk.aws_apigateway.IVpcLink] = None,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Defines Mock integration.

        :param cache_key_parameters: A list of request parameters whose values are to be cached. It determines request parameters that will make it into the cache key.
        :param cache_namespace: An API-specific tag group of related cached parameters.
        :param connection_type: The type of network connection to the integration endpoint. Default: - ConnectionType.VPC_LINK if ``vpcLink`` property is configured; ConnectionType.Internet otherwise.
        :param content_handling: Specifies how to handle request payload content type conversions. Default: none if this property isn't defined, the request payload is passed through from the method request to the integration request without modification, provided that the ``passthroughBehaviors`` property is configured to support payload pass-through.
        :param credentials_passthrough: Requires that the caller's identity be passed through from the request. Default: Caller identity is not passed through
        :param credentials_role: An IAM role that API Gateway assumes. Mutually exclusive with ``credentialsPassThrough``. Default: A role is not assumed
        :param integration_responses: The response that API Gateway provides after a method's backend completes processing a request. API Gateway intercepts the response from the backend so that you can control how API Gateway surfaces backend responses. For example, you can map the backend status codes to codes that you define.
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
        :param request_parameters: The request parameters that API Gateway sends with the backend request. Specify request parameters as key-value pairs (string-to-string mappings), with a destination as the key and a source as the value. Specify the destination by using the following pattern integration.request.location.name, where location is querystring, path, or header, and name is a valid, unique parameter name. The source must be an existing method request parameter or a static value. You must enclose static values in single quotation marks and pre-encode these values based on their destination in the request.
        :param request_templates: A map of Apache Velocity templates that are applied on the request payload. The template that API Gateway uses is based on the value of the Content-Type header that's sent by the client. The content type value is the key, and the template is the value (specified as a string), such as the following snippet:: { "application/json": "{ \\"statusCode\\": 200 }" }
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)
        :param vpc_link: The VpcLink used for the integration. Required if connectionType is VPC_LINK
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental

        Example::

            '/mock': {
              'GET': new openapix.MockIntegration(this),
            },
        '''
        props = MockIntegrationProps(
            cache_key_parameters=cache_key_parameters,
            cache_namespace=cache_namespace,
            connection_type=connection_type,
            content_handling=content_handling,
            credentials_passthrough=credentials_passthrough,
            credentials_role=credentials_role,
            integration_responses=integration_responses,
            passthrough_behavior=passthrough_behavior,
            request_parameters=request_parameters,
            request_templates=request_templates,
            timeout=timeout,
            vpc_link=vpc_link,
            validator=validator,
        )

        jsii.create(self.__class__, self, [props])


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.OAuthFlowObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "scopes": "scopes",
        "authorization_url": "authorizationUrl",
        "refresh_url": "refreshUrl",
        "token_url": "tokenUrl",
    },
)
class OAuthFlowObject(Extensible):
    def __init__(
        self,
        *,
        scopes: typing.Mapping[builtins.str, builtins.str],
        authorization_url: typing.Optional[builtins.str] = None,
        refresh_url: typing.Optional[builtins.str] = None,
        token_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Configuration details for a supported OAuth Flow.

        :param scopes: (experimental) The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.
        :param authorization_url: (experimental) The authorization URL to be used for this flow. This MUST be in the form of a URL. REQUIRED for oauth2 ("implicit", "authorizationCode").
        :param refresh_url: (experimental) The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL.
        :param token_url: (experimental) The token URL to be used for this flow. This MUST be in the form of a URL. REQUIRED for oauth2 ("password", "clientCredentials", "authorizationCode").

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                scopes: typing.Mapping[builtins.str, builtins.str],
                authorization_url: typing.Optional[builtins.str] = None,
                refresh_url: typing.Optional[builtins.str] = None,
                token_url: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            check_type(argname="argument authorization_url", value=authorization_url, expected_type=type_hints["authorization_url"])
            check_type(argname="argument refresh_url", value=refresh_url, expected_type=type_hints["refresh_url"])
            check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "scopes": scopes,
        }
        if authorization_url is not None:
            self._values["authorization_url"] = authorization_url
        if refresh_url is not None:
            self._values["refresh_url"] = refresh_url
        if token_url is not None:
            self._values["token_url"] = token_url

    @builtins.property
    def scopes(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) The available scopes for the OAuth2 security scheme.

        A map between the scope name and a short description for it. The map MAY be empty.

        :stability: experimental
        '''
        result = self._values.get("scopes")
        assert result is not None, "Required property 'scopes' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def authorization_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The authorization URL to be used for this flow.

        This MUST be in the form of a URL.
        REQUIRED for oauth2 ("implicit", "authorizationCode").

        :stability: experimental
        '''
        result = self._values.get("authorization_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def refresh_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL to be used for obtaining refresh tokens.

        This MUST be in the form of a URL.

        :stability: experimental
        '''
        result = self._values.get("refresh_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The token URL to be used for this flow.

        This MUST be in the form of a URL.
        REQUIRED for oauth2 ("password", "clientCredentials", "authorizationCode").

        :stability: experimental
        '''
        result = self._values.get("token_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OAuthFlowObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.OAuthFlowsObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "authorization_code": "authorizationCode",
        "client_credentials": "clientCredentials",
        "implicit": "implicit",
        "password": "password",
    },
)
class OAuthFlowsObject(Extensible):
    def __init__(
        self,
        *,
        authorization_code: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
        client_credentials: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
        implicit: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
        password: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Allows configuration of the supported OAuth Flows.

        :param authorization_code: (experimental) Configuration for the OAuth Authorization Code flow. Previously called accessCode in OpenAPI 2.0.
        :param client_credentials: (experimental) Configuration for the OAuth Client Credentials flow. Previously called application in OpenAPI 2.0.
        :param implicit: (experimental) Configuration for the OAuth Implicit flow.
        :param password: (experimental) Configuration for the OAuth Resource Owner Password flow.

        :stability: experimental
        '''
        if isinstance(authorization_code, dict):
            authorization_code = OAuthFlowObject(**authorization_code)
        if isinstance(client_credentials, dict):
            client_credentials = OAuthFlowObject(**client_credentials)
        if isinstance(implicit, dict):
            implicit = OAuthFlowObject(**implicit)
        if isinstance(password, dict):
            password = OAuthFlowObject(**password)
        if __debug__:
            def stub(
                *,
                authorization_code: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
                client_credentials: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
                implicit: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
                password: typing.Optional[typing.Union[OAuthFlowObject, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument authorization_code", value=authorization_code, expected_type=type_hints["authorization_code"])
            check_type(argname="argument client_credentials", value=client_credentials, expected_type=type_hints["client_credentials"])
            check_type(argname="argument implicit", value=implicit, expected_type=type_hints["implicit"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authorization_code is not None:
            self._values["authorization_code"] = authorization_code
        if client_credentials is not None:
            self._values["client_credentials"] = client_credentials
        if implicit is not None:
            self._values["implicit"] = implicit
        if password is not None:
            self._values["password"] = password

    @builtins.property
    def authorization_code(self) -> typing.Optional[OAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Authorization Code flow.

        Previously called accessCode in OpenAPI 2.0.

        :stability: experimental
        '''
        result = self._values.get("authorization_code")
        return typing.cast(typing.Optional[OAuthFlowObject], result)

    @builtins.property
    def client_credentials(self) -> typing.Optional[OAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Client Credentials flow.

        Previously called application in OpenAPI 2.0.

        :stability: experimental
        '''
        result = self._values.get("client_credentials")
        return typing.cast(typing.Optional[OAuthFlowObject], result)

    @builtins.property
    def implicit(self) -> typing.Optional[OAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Implicit flow.

        :stability: experimental
        '''
        result = self._values.get("implicit")
        return typing.cast(typing.Optional[OAuthFlowObject], result)

    @builtins.property
    def password(self) -> typing.Optional[OAuthFlowObject]:
        '''(experimental) Configuration for the OAuth Resource Owner Password flow.

        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[OAuthFlowObject], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OAuthFlowsObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.OperationObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "responses": "responses",
        "callbacks": "callbacks",
        "deprecated": "deprecated",
        "description": "description",
        "external_docs": "externalDocs",
        "operation_id": "operationId",
        "parameters": "parameters",
        "request_body": "requestBody",
        "security": "security",
        "summary": "summary",
        "tags": "tags",
    },
)
class OperationObject(Extensible):
    def __init__(
        self,
        *,
        responses: typing.Union["ResponsesObject", typing.Dict[str, typing.Any]],
        callbacks: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["CallbackObject", typing.Dict[str, typing.Any]]]]] = None,
        deprecated: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
        operation_id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Sequence[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["ParameterObject", typing.Dict[str, typing.Any]]]]] = None,
        request_body: typing.Optional[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["RequestBodyObject", typing.Dict[str, typing.Any]]]] = None,
        security: typing.Optional[typing.Sequence[typing.Union["SecurityRequirementObject", typing.Dict[str, typing.Any]]]] = None,
        summary: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Describes a single API operation on a path.

        :param responses: (experimental) The list of possible responses as they are returned from executing this operation.
        :param callbacks: (experimental) A map of possible out-of band callbacks related to the parent operation. The key is a unique identifier for the Callback Object. Each value in the map is a Callback Object that describes a request that may be initiated by the API provider and the expected responses.
        :param deprecated: (experimental) Declares this operation to be deprecated. Consumers SHOULD refrain from usage of the declared operation. Default value is false.
        :param description: (experimental) A verbose explanation of the operation behavior. CommonMark syntax MAY be used for rich text representation.
        :param external_docs: (experimental) Additional external documentation for this operation.
        :param operation_id: (experimental) Unique string used to identify the operation. The id MUST be unique among all operations described in the API. The operationId value is case-sensitive. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions.
        :param parameters: (experimental) A list of parameters that are applicable for this operation. If a parameter is already defined at the Path Item, the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.
        :param request_body: (experimental) The request body applicable for this operation. The requestBody is only supported in HTTP methods where the HTTP 1.1 specification RFC7231 has explicitly defined semantics for request bodies. In other cases where the HTTP spec is vague, requestBody SHALL be ignored by consumers.
        :param security: (experimental) A declaration of which security mechanisms can be used for this operation. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement ({}) can be included in the array. This definition overrides any declared top-level security. To remove a top-level security declaration, an empty array can be used.
        :param summary: (experimental) A short summary of what the operation does.
        :param tags: (experimental) A list of tags for API documentation control. Tags can be used for logical grouping of operations by resources or any other qualifier.

        :stability: experimental
        '''
        if isinstance(responses, dict):
            responses = ResponsesObject(**responses)
        if isinstance(external_docs, dict):
            external_docs = ExternalDocumentationObject(**external_docs)
        if __debug__:
            def stub(
                *,
                responses: typing.Union["ResponsesObject", typing.Dict[str, typing.Any]],
                callbacks: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["CallbackObject", typing.Dict[str, typing.Any]]]]] = None,
                deprecated: typing.Optional[builtins.bool] = None,
                description: typing.Optional[builtins.str] = None,
                external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
                operation_id: typing.Optional[builtins.str] = None,
                parameters: typing.Optional[typing.Sequence[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["ParameterObject", typing.Dict[str, typing.Any]]]]] = None,
                request_body: typing.Optional[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union["RequestBodyObject", typing.Dict[str, typing.Any]]]] = None,
                security: typing.Optional[typing.Sequence[typing.Union["SecurityRequirementObject", typing.Dict[str, typing.Any]]]] = None,
                summary: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument responses", value=responses, expected_type=type_hints["responses"])
            check_type(argname="argument callbacks", value=callbacks, expected_type=type_hints["callbacks"])
            check_type(argname="argument deprecated", value=deprecated, expected_type=type_hints["deprecated"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_docs", value=external_docs, expected_type=type_hints["external_docs"])
            check_type(argname="argument operation_id", value=operation_id, expected_type=type_hints["operation_id"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument request_body", value=request_body, expected_type=type_hints["request_body"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "responses": responses,
        }
        if callbacks is not None:
            self._values["callbacks"] = callbacks
        if deprecated is not None:
            self._values["deprecated"] = deprecated
        if description is not None:
            self._values["description"] = description
        if external_docs is not None:
            self._values["external_docs"] = external_docs
        if operation_id is not None:
            self._values["operation_id"] = operation_id
        if parameters is not None:
            self._values["parameters"] = parameters
        if request_body is not None:
            self._values["request_body"] = request_body
        if security is not None:
            self._values["security"] = security
        if summary is not None:
            self._values["summary"] = summary
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def responses(self) -> "ResponsesObject":
        '''(experimental) The list of possible responses as they are returned from executing this operation.

        :stability: experimental
        '''
        result = self._values.get("responses")
        assert result is not None, "Required property 'responses' is missing"
        return typing.cast("ResponsesObject", result)

    @builtins.property
    def callbacks(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union["ReferenceObject", "CallbackObject"]]]:
        '''(experimental) A map of possible out-of band callbacks related to the parent operation.

        The key is a unique identifier for the Callback Object. Each value in the map is a Callback Object that describes a request that may be initiated by the API provider and the expected responses.

        :stability: experimental
        '''
        result = self._values.get("callbacks")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union["ReferenceObject", "CallbackObject"]]], result)

    @builtins.property
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Declares this operation to be deprecated.

        Consumers SHOULD refrain from usage of the declared operation. Default value is false.

        :stability: experimental
        '''
        result = self._values.get("deprecated")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A verbose explanation of the operation behavior.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_docs(self) -> typing.Optional[ExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this operation.

        :stability: experimental
        '''
        result = self._values.get("external_docs")
        return typing.cast(typing.Optional[ExternalDocumentationObject], result)

    @builtins.property
    def operation_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Unique string used to identify the operation.

        The id MUST be unique among all operations described in the API. The operationId value is case-sensitive. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions.

        :stability: experimental
        '''
        result = self._values.get("operation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.List[typing.Union["ReferenceObject", "ParameterObject"]]]:
        '''(experimental) A list of parameters that are applicable for this operation.

        If a parameter is already defined at the Path Item, the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.List[typing.Union["ReferenceObject", "ParameterObject"]]], result)

    @builtins.property
    def request_body(
        self,
    ) -> typing.Optional[typing.Union["ReferenceObject", "RequestBodyObject"]]:
        '''(experimental) The request body applicable for this operation.

        The requestBody is only supported in HTTP methods where the HTTP 1.1 specification RFC7231 has explicitly defined semantics for request bodies. In other cases where the HTTP spec is vague, requestBody SHALL be ignored by consumers.

        :stability: experimental
        '''
        result = self._values.get("request_body")
        return typing.cast(typing.Optional[typing.Union["ReferenceObject", "RequestBodyObject"]], result)

    @builtins.property
    def security(self) -> typing.Optional[typing.List["SecurityRequirementObject"]]:
        '''(experimental) A declaration of which security mechanisms can be used for this operation.

        The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement ({}) can be included in the array. This definition overrides any declared top-level security. To remove a top-level security declaration, an empty array can be used.

        :stability: experimental
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.List["SecurityRequirementObject"]], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short summary of what the operation does.

        :stability: experimental
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A list of tags for API documentation control.

        Tags can be used for logical grouping of operations by resources or any other qualifier.

        :stability: experimental
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OperationObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ParameterObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "in_": "in",
        "name": "name",
        "allow_empty_value": "allowEmptyValue",
        "deprecated": "deprecated",
        "description": "description",
        "required": "required",
    },
)
class ParameterObject(Extensible):
    def __init__(
        self,
        *,
        in_: builtins.str,
        name: builtins.str,
        allow_empty_value: typing.Optional[builtins.bool] = None,
        deprecated: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        required: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Describes a single operation parameter.

        A unique parameter is defined by a combination of a name and location.

        :param in_: (experimental) The location of the parameter. Possible values are "query", "header", "path" or "cookie".
        :param name: (experimental) The name of the parameter. Parameter names are case sensitive. If in is "path", the name field MUST correspond to a template expression occurring within the path field in the Paths Object. See Path Templating for further information. If in is "header" and the name field is "Accept", "Content-Type" or "Authorization", the parameter definition SHALL be ignored. For all other cases, the name corresponds to the parameter name used by the in property.
        :param allow_empty_value: (experimental) Sets the ability to pass empty-valued parameters. This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.
        :param deprecated: (experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage. Default value is false.
        :param description: (experimental) A brief description of the parameter. This could contain examples of use. CommonMark syntax MAY be used for rich text representation.
        :param required: (experimental) Determines whether this parameter is mandatory. If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                in_: builtins.str,
                name: builtins.str,
                allow_empty_value: typing.Optional[builtins.bool] = None,
                deprecated: typing.Optional[builtins.bool] = None,
                description: typing.Optional[builtins.str] = None,
                required: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument in_", value=in_, expected_type=type_hints["in_"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allow_empty_value", value=allow_empty_value, expected_type=type_hints["allow_empty_value"])
            check_type(argname="argument deprecated", value=deprecated, expected_type=type_hints["deprecated"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {
            "in_": in_,
            "name": name,
        }
        if allow_empty_value is not None:
            self._values["allow_empty_value"] = allow_empty_value
        if deprecated is not None:
            self._values["deprecated"] = deprecated
        if description is not None:
            self._values["description"] = description
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def in_(self) -> builtins.str:
        '''(experimental) The location of the parameter.

        Possible values are "query", "header", "path" or "cookie".

        :stability: experimental
        '''
        result = self._values.get("in_")
        assert result is not None, "Required property 'in_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The name of the parameter. Parameter names are case sensitive.

        If in is "path", the name field MUST correspond to a template expression occurring within the path field in the Paths Object. See Path Templating for further information.
        If in is "header" and the name field is "Accept", "Content-Type" or "Authorization", the parameter definition SHALL be ignored.
        For all other cases, the name corresponds to the parameter name used by the in property.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_empty_value(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Sets the ability to pass empty-valued parameters.

        This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.

        :stability: experimental
        '''
        result = self._values.get("allow_empty_value")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a parameter is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        result = self._values.get("deprecated")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the parameter.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether this parameter is mandatory.

        If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.

        :stability: experimental
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.PathItemObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "delete": "delete",
        "description": "description",
        "get": "get",
        "head": "head",
        "options": "options",
        "parameters": "parameters",
        "patch": "patch",
        "post": "post",
        "put": "put",
        "summary": "summary",
        "trace": "trace",
    },
)
class PathItemObject(Extensible):
    def __init__(
        self,
        *,
        delete: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        get: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
        head: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
        options: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Sequence[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union[ParameterObject, typing.Dict[str, typing.Any]]]]] = None,
        patch: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
        post: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
        put: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
        summary: typing.Optional[builtins.str] = None,
        trace: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Describes the operations available on a single path.

        A Path Item MAY be empty, due to ACL constraints. The path itself is still exposed to the documentation viewer but they will not know which operations and parameters are available.

        :param delete: (experimental) A definition of a DELETE operation on this path.
        :param description: (experimental) An optional, string description, intended to apply to all operations in this path. CommonMark syntax MAY be used for rich text representation.
        :param get: (experimental) A definition of a GET operation on this path.
        :param head: (experimental) A definition of a HEAD operation on this path.
        :param options: (experimental) A definition of a OPTIONS operation on this path.
        :param parameters: (experimental) A list of parameters that are applicable for all the operations described under this path. These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.
        :param patch: (experimental) A definition of a PATCH operation on this path.
        :param post: (experimental) A definition of a POST operation on this path.
        :param put: (experimental) A definition of a PUT operation on this path.
        :param summary: (experimental) An optional, string summary, intended to apply to all operations in this path.
        :param trace: (experimental) A definition of a TRACE operation on this path.

        :stability: experimental
        '''
        if isinstance(delete, dict):
            delete = OperationObject(**delete)
        if isinstance(get, dict):
            get = OperationObject(**get)
        if isinstance(head, dict):
            head = OperationObject(**head)
        if isinstance(options, dict):
            options = OperationObject(**options)
        if isinstance(patch, dict):
            patch = OperationObject(**patch)
        if isinstance(post, dict):
            post = OperationObject(**post)
        if isinstance(put, dict):
            put = OperationObject(**put)
        if isinstance(trace, dict):
            trace = OperationObject(**trace)
        if __debug__:
            def stub(
                *,
                delete: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                get: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
                head: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
                options: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
                parameters: typing.Optional[typing.Sequence[typing.Union[typing.Union["ReferenceObject", typing.Dict[str, typing.Any]], typing.Union[ParameterObject, typing.Dict[str, typing.Any]]]]] = None,
                patch: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
                post: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
                put: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
                summary: typing.Optional[builtins.str] = None,
                trace: typing.Optional[typing.Union[OperationObject, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument get", value=get, expected_type=type_hints["get"])
            check_type(argname="argument head", value=head, expected_type=type_hints["head"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument patch", value=patch, expected_type=type_hints["patch"])
            check_type(argname="argument post", value=post, expected_type=type_hints["post"])
            check_type(argname="argument put", value=put, expected_type=type_hints["put"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete is not None:
            self._values["delete"] = delete
        if description is not None:
            self._values["description"] = description
        if get is not None:
            self._values["get"] = get
        if head is not None:
            self._values["head"] = head
        if options is not None:
            self._values["options"] = options
        if parameters is not None:
            self._values["parameters"] = parameters
        if patch is not None:
            self._values["patch"] = patch
        if post is not None:
            self._values["post"] = post
        if put is not None:
            self._values["put"] = put
        if summary is not None:
            self._values["summary"] = summary
        if trace is not None:
            self._values["trace"] = trace

    @builtins.property
    def delete(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a DELETE operation on this path.

        :stability: experimental
        '''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[OperationObject], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional, string description, intended to apply to all operations in this path.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def get(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a GET operation on this path.

        :stability: experimental
        '''
        result = self._values.get("get")
        return typing.cast(typing.Optional[OperationObject], result)

    @builtins.property
    def head(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a HEAD operation on this path.

        :stability: experimental
        '''
        result = self._values.get("head")
        return typing.cast(typing.Optional[OperationObject], result)

    @builtins.property
    def options(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a OPTIONS operation on this path.

        :stability: experimental
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[OperationObject], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.List[typing.Union["ReferenceObject", ParameterObject]]]:
        '''(experimental) A list of parameters that are applicable for all the operations described under this path.

        These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.List[typing.Union["ReferenceObject", ParameterObject]]], result)

    @builtins.property
    def patch(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a PATCH operation on this path.

        :stability: experimental
        '''
        result = self._values.get("patch")
        return typing.cast(typing.Optional[OperationObject], result)

    @builtins.property
    def post(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a POST operation on this path.

        :stability: experimental
        '''
        result = self._values.get("post")
        return typing.cast(typing.Optional[OperationObject], result)

    @builtins.property
    def put(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a PUT operation on this path.

        :stability: experimental
        '''
        result = self._values.get("put")
        return typing.cast(typing.Optional[OperationObject], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional, string summary, intended to apply to all operations in this path.

        :stability: experimental
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trace(self) -> typing.Optional[OperationObject]:
        '''(experimental) A definition of a TRACE operation on this path.

        :stability: experimental
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional[OperationObject], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PathItemObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.Paths",
    jsii_struct_bases=[],
    name_mapping={},
)
class Paths:
    def __init__(self) -> None:
        '''(experimental) Paths with methods containing integrations.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Paths(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.PathsObject",
    jsii_struct_bases=[Extensible],
    name_mapping={},
)
class PathsObject(Extensible):
    def __init__(self) -> None:
        '''(experimental) Holds the relative paths to the individual endpoints and their operations.

        The path is appended to the URL from the Server Object in order to construct the full URL. The Paths MAY be empty, due to ACL constraints.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PathsObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ReferenceObject",
    jsii_struct_bases=[Extensible],
    name_mapping={},
)
class ReferenceObject(Extensible):
    def __init__(self) -> None:
        '''(experimental) A simple object to allow referencing other components in the specification, internally and externally.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReferenceObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.RequestBodyObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "content": "content",
        "description": "description",
        "required": "required",
    },
)
class RequestBodyObject(Extensible):
    def __init__(
        self,
        *,
        content: typing.Mapping[builtins.str, typing.Union[MediaTypeObject, typing.Dict[str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        required: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Describes a single request body.

        :param content: (experimental) The content of the request body. The key is a media type or media type range and the value describes it. For requests that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*
        :param description: (experimental) A brief description of the request body. This could contain examples of use. CommonMark syntax MAY be used for rich text representation.
        :param required: (experimental) Determines if the request body is required in the request. Defaults to false.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                content: typing.Mapping[builtins.str, typing.Union[MediaTypeObject, typing.Dict[str, typing.Any]]],
                description: typing.Optional[builtins.str] = None,
                required: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if description is not None:
            self._values["description"] = description
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def content(self) -> typing.Mapping[builtins.str, MediaTypeObject]:
        '''(experimental) The content of the request body.

        The key is a media type or media type range and the value describes it. For requests that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*

        :stability: experimental
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Mapping[builtins.str, MediaTypeObject], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A brief description of the request body.

        This could contain examples of use. CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def required(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines if the request body is required in the request.

        Defaults to false.

        :stability: experimental
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestBodyObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ResponseObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "description": "description",
        "content": "content",
        "headers": "headers",
        "links": "links",
    },
)
class ResponseObject(Extensible):
    def __init__(
        self,
        *,
        description: builtins.str,
        content: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[MediaTypeObject, typing.Dict[str, typing.Any]]]]] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[HeaderObject, typing.Dict[str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[LinkObject, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''(experimental) Describes a single response from an API Operation, including design-time, static links to operations based on the response.

        :param description: (experimental) A short description of the response. CommonMark syntax MAY be used for rich text representation.
        :param content: (experimental) A map containing descriptions of potential response payloads. The key is a media type or media type range and the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*
        :param headers: (experimental) Maps a header name to its definition. RFC7230 states header names are case insensitive. If a response header is defined with the name "Content-Type", it SHALL be ignored.
        :param links: (experimental) A map of operations links that can be followed from the response. The key of the map is a short name for the link, following the naming constraints of the names for Component Objects.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                description: builtins.str,
                content: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[MediaTypeObject, typing.Dict[str, typing.Any]]]]] = None,
                headers: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[HeaderObject, typing.Dict[str, typing.Any]]]]] = None,
                links: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[LinkObject, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
        }
        if content is not None:
            self._values["content"] = content
        if headers is not None:
            self._values["headers"] = headers
        if links is not None:
            self._values["links"] = links

    @builtins.property
    def description(self) -> builtins.str:
        '''(experimental) A short description of the response.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, MediaTypeObject]]]:
        '''(experimental) A map containing descriptions of potential response payloads.

        The key is a media type or media type range and the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*

        :stability: experimental
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, MediaTypeObject]]], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, HeaderObject]]]:
        '''(experimental) Maps a header name to its definition.

        RFC7230 states header names are case insensitive. If a response header is defined with the name "Content-Type", it SHALL be ignored.

        :stability: experimental
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, HeaderObject]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, LinkObject]]]:
        '''(experimental) A map of operations links that can be followed from the response.

        The key of the map is a short name for the link, following the naming constraints of the names for Component Objects.

        :stability: experimental
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, LinkObject]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResponseObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ResponsesObject",
    jsii_struct_bases=[Extensible],
    name_mapping={},
)
class ResponsesObject(Extensible):
    def __init__(self) -> None:
        '''(experimental) A container for the expected responses of an operation.

        The container maps a HTTP response code to the expected response.
        The documentation is not necessarily expected to cover all possible HTTP response codes because they may not be known in advance. However, documentation is expected to cover a successful operation response and any known errors.
        The default MAY be used as a default response object for all HTTP codes that are not covered individually by the specification.
        The Responses Object MUST contain at least one response code, and it SHOULD be the response for a successful operation call.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResponsesObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Schema(metaclass=jsii.JSIIMeta, jsii_type="@alma-cdk/openapix.Schema"):
    '''(experimental) Represents an OpenApi v3 Schema which can be deserialized from YAML-file, modified and then serialized back to YAML.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        info: typing.Union[InfoObject, typing.Dict[str, typing.Any]],
        openapi: builtins.str,
        paths: typing.Union[PathsObject, typing.Dict[str, typing.Any]],
        components: typing.Optional[typing.Union["ComponentsObject", typing.Dict[str, typing.Any]]] = None,
        external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
        security: typing.Optional[typing.Sequence[typing.Union["SecurityRequirementObject", typing.Dict[str, typing.Any]]]] = None,
        servers: typing.Optional[typing.Sequence[typing.Union["ServerObject", typing.Dict[str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagObject", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) Construct a new Schema instance from OpenApi v3 JSON.

        :param info: (experimental) Provides metadata about the API. The metadata MAY be used by tooling as required.
        :param openapi: (experimental) This string MUST be the semantic version number of the OpenAPI Specification version that the OpenAPI document uses. The openapi field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is not related to the API info.version string.
        :param paths: (experimental) The available paths and operations for the API.
        :param components: (experimental) An element to hold various schemas for the specification.
        :param external_docs: (experimental) Additional external documentation.
        :param security: (experimental) A declaration of which security mechanisms can be used across the API. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement ({}) can be included in the array.
        :param servers: (experimental) An array of Server Objects, which provide connectivity information to a target server. If the servers property is not provided, or is an empty array, the default value would be a Server Object with a url value of /.
        :param tags: (experimental) A list of tags used by the specification with additional metadata. The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique.

        :stability: experimental
        '''
        props = SchemaProps(
            info=info,
            openapi=openapi,
            paths=paths,
            components=components,
            external_docs=external_docs,
            security=security,
            servers=servers,
            tags=tags,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(cls, path: builtins.str) -> "Schema":
        '''(experimental) Parse OpenApi v3 schema by loading a YAML file from given path.

        :param path: -

        :stability: experimental
        '''
        if __debug__:
            def stub(path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast("Schema", jsii.sinvoke(cls, "fromAsset", [path]))

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(cls, content: builtins.str) -> "Schema":
        '''(experimental) Parse OpenApi v3 schema from inline YAML content.

        :param content: -

        :stability: experimental
        '''
        if __debug__:
            def stub(content: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
        return typing.cast("Schema", jsii.sinvoke(cls, "fromInline", [content]))

    @jsii.member(jsii_name="get")
    def get(self, path: builtins.str) -> typing.Any:
        '''(experimental) Get a value from given object path.

        :param path: -

        :stability: experimental
        '''
        if __debug__:
            def stub(path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(typing.Any, jsii.invoke(self, "get", [path]))

    @jsii.member(jsii_name="has")
    def has(self, path: builtins.str) -> builtins.bool:
        '''(experimental) Check if definition has a value in given object path.

        :param path: -

        :stability: experimental
        '''
        if __debug__:
            def stub(path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(builtins.bool, jsii.invoke(self, "has", [path]))

    @jsii.member(jsii_name="inject")
    def inject(
        self,
        records: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''(experimental) Inject multiple values to given paths.

        :param records: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                records: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument records", value=records, expected_type=type_hints["records"])
        return typing.cast(None, jsii.invoke(self, "inject", [records]))

    @jsii.member(jsii_name="reject")
    def reject(
        self,
        paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Reject – i.e. remove values – from given object paths.

        :param paths: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                paths: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
        return typing.cast(None, jsii.invoke(self, "reject", [paths]))

    @jsii.member(jsii_name="rejectDeep")
    def reject_deep(
        self,
        paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Reject deep within object – i.e. remove all nested object paths.

        :param paths: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                paths: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
        return typing.cast(None, jsii.invoke(self, "rejectDeep", [paths]))

    @jsii.member(jsii_name="set")
    def set(self, path: builtins.str, value: typing.Any) -> None:
        '''(experimental) Set a value to given object path.

        :param path: -
        :param value: -

        :stability: experimental
        '''
        if __debug__:
            def stub(path: builtins.str, value: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "set", [path, value]))

    @jsii.member(jsii_name="toAsset")
    def to_asset(
        self,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> aws_cdk.aws_s3_assets.Asset:
        '''(experimental) Return the OpenApi v3 document as an S3 Asset.

        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(aws_cdk.aws_s3_assets.Asset, jsii.invoke(self, "toAsset", [scope, id]))

    @jsii.member(jsii_name="toDocument")
    def to_document(self) -> "IDocument":
        '''(experimental) Return the actual OpenApi v3 document.

        :stability: experimental
        '''
        return typing.cast("IDocument", jsii.invoke(self, "toDocument", []))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> builtins.str:
        '''(experimental) Serialize to JSON string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toJson", []))

    @jsii.member(jsii_name="toYaml")
    def to_yaml(self) -> builtins.str:
        '''(experimental) Serialize to YAML string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toYaml", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="openApiSupportedVersions")
    def open_api_supported_versions(cls) -> builtins.str:  # pyright: ignore [reportGeneralTypeIssues]
        '''(experimental) A string representing supported SemVer range.

        :see: https://github.com/npm/node-semver
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "openApiSupportedVersions"))

    @open_api_supported_versions.setter # type: ignore[no-redef]
    def open_api_supported_versions(cls, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.sset(cls, "openApiSupportedVersions", value)

    @builtins.property
    @jsii.member(jsii_name="openApiVersion")
    def open_api_version(self) -> builtins.str:
        '''(experimental) OpenApi version used by schema document.

        :stability: experimental

        Example::

            '3.0.3'
        '''
        return typing.cast(builtins.str, jsii.get(self, "openApiVersion"))

    @open_api_version.setter
    def open_api_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openApiVersion", value)


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.SchemaObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "deprecated": "deprecated",
        "discriminator": "discriminator",
        "example": "example",
        "external_docs": "externalDocs",
        "nullable": "nullable",
        "read_only": "readOnly",
        "write_only": "writeOnly",
        "xml": "xml",
    },
)
class SchemaObject(Extensible):
    def __init__(
        self,
        *,
        deprecated: typing.Optional[builtins.bool] = None,
        discriminator: typing.Optional[typing.Union["DiscriminatorObject", typing.Dict[str, typing.Any]]] = None,
        example: typing.Any = None,
        external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
        nullable: typing.Optional[builtins.bool] = None,
        read_only: typing.Optional[builtins.bool] = None,
        write_only: typing.Optional[builtins.bool] = None,
        xml: typing.Optional[typing.Union["XmlObject", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) The Schema Object allows the definition of input and output data types.

        These types can be objects, but also primitives and arrays. This object is an extended subset of the JSON Schema Specification Wright Draft 00. For more information about the properties, see JSON Schema Core and JSON Schema Validation. Unless stated otherwise, the property definitions follow the JSON Schema.

        :param deprecated: (experimental) Specifies that a schema is deprecated and SHOULD be transitioned out of usage. Default value is false.
        :param discriminator: (experimental) Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.
        :param example: (experimental) A free-form property to include an example of an instance for this schema. To represent examples that cannot be naturally represented in JSON or YAML, a string value can be used to contain the example with escaping where necessary.
        :param external_docs: (experimental) Additional external documentation for this schema.
        :param nullable: (experimental) A true value adds "null" to the allowed type specified by the type keyword, only if type is explicitly defined within the same Schema Object. Other Schema Object constraints retain their defined behavior, and therefore may disallow the use of null as a value. A false value leaves the specified or default type unmodified. The default value is false.
        :param read_only: (experimental) Relevant only for Schema "properties" definitions. Declares the property as "read only". This means that it MAY be sent as part of a response but SHOULD NOT be sent as part of the request. If the property is marked as readOnly being true and is in the required list, the required will take effect on the response only. A property MUST NOT be marked as both readOnly and writeOnly being true. Default value is false.
        :param write_only: (experimental) Relevant only for Schema "properties" definitions. Declares the property as "write only". Therefore, it MAY be sent as part of a request but SHOULD NOT be sent as part of the response. If the property is marked as writeOnly being true and is in the required list, the required will take effect on the request only. A property MUST NOT be marked as both readOnly and writeOnly being true. Default value is false.
        :param xml: (experimental) This MAY be used only on properties schemas. It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.

        :stability: experimental
        '''
        if isinstance(discriminator, dict):
            discriminator = DiscriminatorObject(**discriminator)
        if isinstance(external_docs, dict):
            external_docs = ExternalDocumentationObject(**external_docs)
        if isinstance(xml, dict):
            xml = XmlObject(**xml)
        if __debug__:
            def stub(
                *,
                deprecated: typing.Optional[builtins.bool] = None,
                discriminator: typing.Optional[typing.Union["DiscriminatorObject", typing.Dict[str, typing.Any]]] = None,
                example: typing.Any = None,
                external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
                nullable: typing.Optional[builtins.bool] = None,
                read_only: typing.Optional[builtins.bool] = None,
                write_only: typing.Optional[builtins.bool] = None,
                xml: typing.Optional[typing.Union["XmlObject", typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument deprecated", value=deprecated, expected_type=type_hints["deprecated"])
            check_type(argname="argument discriminator", value=discriminator, expected_type=type_hints["discriminator"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument external_docs", value=external_docs, expected_type=type_hints["external_docs"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument write_only", value=write_only, expected_type=type_hints["write_only"])
            check_type(argname="argument xml", value=xml, expected_type=type_hints["xml"])
        self._values: typing.Dict[str, typing.Any] = {}
        if deprecated is not None:
            self._values["deprecated"] = deprecated
        if discriminator is not None:
            self._values["discriminator"] = discriminator
        if example is not None:
            self._values["example"] = example
        if external_docs is not None:
            self._values["external_docs"] = external_docs
        if nullable is not None:
            self._values["nullable"] = nullable
        if read_only is not None:
            self._values["read_only"] = read_only
        if write_only is not None:
            self._values["write_only"] = write_only
        if xml is not None:
            self._values["xml"] = xml

    @builtins.property
    def deprecated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies that a schema is deprecated and SHOULD be transitioned out of usage.

        Default value is false.

        :stability: experimental
        '''
        result = self._values.get("deprecated")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def discriminator(self) -> typing.Optional["DiscriminatorObject"]:
        '''(experimental) Adds support for polymorphism.

        The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.

        :stability: experimental
        '''
        result = self._values.get("discriminator")
        return typing.cast(typing.Optional["DiscriminatorObject"], result)

    @builtins.property
    def example(self) -> typing.Any:
        '''(experimental) A free-form property to include an example of an instance for this schema.

        To represent examples that cannot be naturally represented in JSON or YAML, a string value can be used to contain the example with escaping where necessary.

        :stability: experimental
        '''
        result = self._values.get("example")
        return typing.cast(typing.Any, result)

    @builtins.property
    def external_docs(self) -> typing.Optional[ExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this schema.

        :stability: experimental
        '''
        result = self._values.get("external_docs")
        return typing.cast(typing.Optional[ExternalDocumentationObject], result)

    @builtins.property
    def nullable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) A true value adds "null" to the allowed type specified by the type keyword, only if type is explicitly defined within the same Schema Object.

        Other Schema Object constraints retain their defined behavior, and therefore may disallow the use of null as a value. A false value leaves the specified or default type unmodified. The default value is false.

        :stability: experimental
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_only(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Relevant only for Schema "properties" definitions.

        Declares the property as "read only". This means that it MAY be sent as part of a response but SHOULD NOT be sent as part of the request. If the property is marked as readOnly being true and is in the required list, the required will take effect on the response only. A property MUST NOT be marked as both readOnly and writeOnly being true. Default value is false.

        :stability: experimental
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def write_only(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Relevant only for Schema "properties" definitions.

        Declares the property as "write only". Therefore, it MAY be sent as part of a request but SHOULD NOT be sent as part of the response. If the property is marked as writeOnly being true and is in the required list, the required will take effect on the request only. A property MUST NOT be marked as both readOnly and writeOnly being true. Default value is false.

        :stability: experimental
        '''
        result = self._values.get("write_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def xml(self) -> typing.Optional["XmlObject"]:
        '''(experimental) This MAY be used only on properties schemas.

        It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.

        :stability: experimental
        '''
        result = self._values.get("xml")
        return typing.cast(typing.Optional["XmlObject"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.SchemaProps",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "info": "info",
        "openapi": "openapi",
        "paths": "paths",
        "components": "components",
        "external_docs": "externalDocs",
        "security": "security",
        "servers": "servers",
        "tags": "tags",
    },
)
class SchemaProps(Extensible):
    def __init__(
        self,
        *,
        info: typing.Union[InfoObject, typing.Dict[str, typing.Any]],
        openapi: builtins.str,
        paths: typing.Union[PathsObject, typing.Dict[str, typing.Any]],
        components: typing.Optional[typing.Union["ComponentsObject", typing.Dict[str, typing.Any]]] = None,
        external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
        security: typing.Optional[typing.Sequence[typing.Union["SecurityRequirementObject", typing.Dict[str, typing.Any]]]] = None,
        servers: typing.Optional[typing.Sequence[typing.Union["ServerObject", typing.Dict[str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagObject", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) Props given to ``new Schema``.

        Essentially an OpenApi v3 "source" without
        ``x-amazon-apigateway-`` extensions.

        :param info: (experimental) Provides metadata about the API. The metadata MAY be used by tooling as required.
        :param openapi: (experimental) This string MUST be the semantic version number of the OpenAPI Specification version that the OpenAPI document uses. The openapi field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is not related to the API info.version string.
        :param paths: (experimental) The available paths and operations for the API.
        :param components: (experimental) An element to hold various schemas for the specification.
        :param external_docs: (experimental) Additional external documentation.
        :param security: (experimental) A declaration of which security mechanisms can be used across the API. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement ({}) can be included in the array.
        :param servers: (experimental) An array of Server Objects, which provide connectivity information to a target server. If the servers property is not provided, or is an empty array, the default value would be a Server Object with a url value of /.
        :param tags: (experimental) A list of tags used by the specification with additional metadata. The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique.

        :stability: experimental
        '''
        if isinstance(info, dict):
            info = InfoObject(**info)
        if isinstance(paths, dict):
            paths = PathsObject(**paths)
        if isinstance(components, dict):
            components = ComponentsObject(**components)
        if isinstance(external_docs, dict):
            external_docs = ExternalDocumentationObject(**external_docs)
        if __debug__:
            def stub(
                *,
                info: typing.Union[InfoObject, typing.Dict[str, typing.Any]],
                openapi: builtins.str,
                paths: typing.Union[PathsObject, typing.Dict[str, typing.Any]],
                components: typing.Optional[typing.Union["ComponentsObject", typing.Dict[str, typing.Any]]] = None,
                external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
                security: typing.Optional[typing.Sequence[typing.Union["SecurityRequirementObject", typing.Dict[str, typing.Any]]]] = None,
                servers: typing.Optional[typing.Sequence[typing.Union["ServerObject", typing.Dict[str, typing.Any]]]] = None,
                tags: typing.Optional[typing.Sequence[typing.Union["TagObject", typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument info", value=info, expected_type=type_hints["info"])
            check_type(argname="argument openapi", value=openapi, expected_type=type_hints["openapi"])
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument external_docs", value=external_docs, expected_type=type_hints["external_docs"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument servers", value=servers, expected_type=type_hints["servers"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "info": info,
            "openapi": openapi,
            "paths": paths,
        }
        if components is not None:
            self._values["components"] = components
        if external_docs is not None:
            self._values["external_docs"] = external_docs
        if security is not None:
            self._values["security"] = security
        if servers is not None:
            self._values["servers"] = servers
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def info(self) -> InfoObject:
        '''(experimental) Provides metadata about the API.

        The metadata MAY be used by tooling as required.

        :stability: experimental

        Example::

            {
              title: "FancyPants API",
              version: "1.23.105",
            }
        '''
        result = self._values.get("info")
        assert result is not None, "Required property 'info' is missing"
        return typing.cast(InfoObject, result)

    @builtins.property
    def openapi(self) -> builtins.str:
        '''(experimental) This string MUST be the semantic version number of the OpenAPI Specification version that the OpenAPI document uses.

        The openapi field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is not related to the API info.version string.

        :stability: experimental

        Example::

            '3.0.0'
        '''
        result = self._values.get("openapi")
        assert result is not None, "Required property 'openapi' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def paths(self) -> PathsObject:
        '''(experimental) The available paths and operations for the API.

        :stability: experimental
        '''
        result = self._values.get("paths")
        assert result is not None, "Required property 'paths' is missing"
        return typing.cast(PathsObject, result)

    @builtins.property
    def components(self) -> typing.Optional["ComponentsObject"]:
        '''(experimental) An element to hold various schemas for the specification.

        :stability: experimental
        '''
        result = self._values.get("components")
        return typing.cast(typing.Optional["ComponentsObject"], result)

    @builtins.property
    def external_docs(self) -> typing.Optional[ExternalDocumentationObject]:
        '''(experimental) Additional external documentation.

        :stability: experimental
        '''
        result = self._values.get("external_docs")
        return typing.cast(typing.Optional[ExternalDocumentationObject], result)

    @builtins.property
    def security(self) -> typing.Optional[typing.List["SecurityRequirementObject"]]:
        '''(experimental) A declaration of which security mechanisms can be used across the API.

        The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement ({}) can be included in the array.

        :stability: experimental
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.List["SecurityRequirementObject"]], result)

    @builtins.property
    def servers(self) -> typing.Optional[typing.List["ServerObject"]]:
        '''(experimental) An array of Server Objects, which provide connectivity information to a target server.

        If the servers property is not provided, or is an empty array, the default value would be a Server Object with a url value of /.

        :stability: experimental
        '''
        result = self._values.get("servers")
        return typing.cast(typing.Optional[typing.List["ServerObject"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["TagObject"]]:
        '''(experimental) A list of tags used by the specification with additional metadata.

        The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique.

        :stability: experimental
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["TagObject"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.SecurityRequirementObject",
    jsii_struct_bases=[Extensible],
    name_mapping={},
)
class SecurityRequirementObject(Extensible):
    def __init__(self) -> None:
        '''(experimental) Lists the required security schemes to execute this operation.

        The name used for each property MUST correspond to a security scheme declared in the Security Schemes under the Components Object.
        Security Requirement Objects that contain multiple schemes require that all schemes MUST be satisfied for a request to be authorized. This enables support for scenarios where multiple query parameters or HTTP headers are required to convey security information.
        When a list of Security Requirement Objects is defined on the OpenAPI Object or Operation Object, only one of the Security Requirement Objects in the list needs to be satisfied to authorize the request.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityRequirementObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.SecuritySchemeObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "type": "type",
        "bearer_format": "bearerFormat",
        "description": "description",
        "flow": "flow",
        "in_": "in",
        "name": "name",
        "open_id_connect_url": "openIdConnectUrl",
        "scheme": "scheme",
    },
)
class SecuritySchemeObject(Extensible):
    def __init__(
        self,
        *,
        type: builtins.str,
        bearer_format: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        flow: typing.Optional[typing.Union[OAuthFlowsObject, typing.Dict[str, typing.Any]]] = None,
        in_: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        open_id_connect_url: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Defines a security scheme that can be used by the operations.

        Supported schemes are HTTP authentication, an API key (either as a header, a cookie parameter or as a query parameter), OAuth2's common flows (implicit, password, client credentials and authorization code) as defined in RFC6749, and OpenID Connect Discovery.

        :param type: (experimental) The type of the security scheme. Valid values are "apiKey", "http", "oauth2", "openIdConnect".
        :param bearer_format: (experimental) A hint to the client to identify how the bearer token is formatted. Bearer tokens are usually generated by an authorization server, so this information is primarily for documentation purposes.
        :param description: (experimental) A short description for security scheme. CommonMark syntax MAY be used for rich text representation.
        :param flow: (experimental) An object containing configuration information for the flow types supported. REQUIRED for oauth2.
        :param in_: (experimental) The location of the API key. Valid values are "query", "header" or "cookie". REQUIRED for apiKey.
        :param name: (experimental) The name of the header, query or cookie parameter to be used. REQUIRED for apiKey.
        :param open_id_connect_url: (experimental) OpenId Connect URL to discover OAuth2 configuration values. This MUST be in the form of a URL. REQUIRED for openIdConnect.
        :param scheme: (experimental) The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235. The values used SHOULD be registered in the IANA Authentication Scheme registry. REQUIRED for http.

        :stability: experimental
        '''
        if isinstance(flow, dict):
            flow = OAuthFlowsObject(**flow)
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                bearer_format: typing.Optional[builtins.str] = None,
                description: typing.Optional[builtins.str] = None,
                flow: typing.Optional[typing.Union[OAuthFlowsObject, typing.Dict[str, typing.Any]]] = None,
                in_: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                open_id_connect_url: typing.Optional[builtins.str] = None,
                scheme: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bearer_format", value=bearer_format, expected_type=type_hints["bearer_format"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flow", value=flow, expected_type=type_hints["flow"])
            check_type(argname="argument in_", value=in_, expected_type=type_hints["in_"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument open_id_connect_url", value=open_id_connect_url, expected_type=type_hints["open_id_connect_url"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if bearer_format is not None:
            self._values["bearer_format"] = bearer_format
        if description is not None:
            self._values["description"] = description
        if flow is not None:
            self._values["flow"] = flow
        if in_ is not None:
            self._values["in_"] = in_
        if name is not None:
            self._values["name"] = name
        if open_id_connect_url is not None:
            self._values["open_id_connect_url"] = open_id_connect_url
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def type(self) -> builtins.str:
        '''(experimental) The type of the security scheme.

        Valid values are "apiKey", "http", "oauth2", "openIdConnect".

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bearer_format(self) -> typing.Optional[builtins.str]:
        '''(experimental) A hint to the client to identify how the bearer token is formatted.

        Bearer tokens are usually generated by an authorization server, so this information is primarily for documentation purposes.

        :stability: experimental
        '''
        result = self._values.get("bearer_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description for security scheme.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow(self) -> typing.Optional[OAuthFlowsObject]:
        '''(experimental) An object containing configuration information for the flow types supported.

        REQUIRED for oauth2.

        :stability: experimental
        '''
        result = self._values.get("flow")
        return typing.cast(typing.Optional[OAuthFlowsObject], result)

    @builtins.property
    def in_(self) -> typing.Optional[builtins.str]:
        '''(experimental) The location of the API key.

        Valid values are "query", "header" or "cookie".
        REQUIRED for apiKey.

        :stability: experimental
        '''
        result = self._values.get("in_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the header, query or cookie parameter to be used.

        REQUIRED for apiKey.

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def open_id_connect_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) OpenId Connect URL to discover OAuth2 configuration values.

        This MUST be in the form of a URL.
        REQUIRED for openIdConnect.

        :stability: experimental
        '''
        result = self._values.get("open_id_connect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235.

        The values used SHOULD be registered in the IANA Authentication Scheme registry.
        REQUIRED for http.

        :stability: experimental
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecuritySchemeObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ServerObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "url": "url",
        "description": "description",
        "variables": "variables",
    },
)
class ServerObject(Extensible):
    def __init__(
        self,
        *,
        url: builtins.str,
        description: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Mapping[builtins.str, typing.Union["ServerVariableObject", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) An object representing a Server.

        :param url: (experimental) REQUIRED. A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.
        :param description: (experimental) An optional string describing the host designated by the URL. CommonMark syntax MAY be used for rich text representation.
        :param variables: (experimental) A map between a variable name and its value. The value is used for substitution in the server's URL template.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                url: builtins.str,
                description: typing.Optional[builtins.str] = None,
                variables: typing.Optional[typing.Mapping[builtins.str, typing.Union["ServerVariableObject", typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if description is not None:
            self._values["description"] = description
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def url(self) -> builtins.str:
        '''(experimental) REQUIRED.

        A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.

        :stability: experimental
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional string describing the host designated by the URL.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "ServerVariableObject"]]:
        '''(experimental) A map between a variable name and its value.

        The value is used for substitution in the server's URL template.

        :stability: experimental
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "ServerVariableObject"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ServerVariableObject",
    jsii_struct_bases=[Extensible],
    name_mapping={"default": "default", "description": "description", "enum": "enum"},
)
class ServerVariableObject(Extensible):
    def __init__(
        self,
        *,
        default: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enum: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) An object representing a Server Variable for server URL template substitution.

        :param default: (experimental) The default value to use for substitution, which SHALL be sent if an alternate value is not supplied. Note this behavior is different than the Schema Object's treatment of default values, because in those cases parameter values are optional. If the enum is defined, the value SHOULD exist in the enum's values.
        :param description: (experimental) An optional description for the server variable. CommonMark syntax MAY be used for rich text representation.
        :param enum: (experimental) An enumeration of string values to be used if the substitution options are from a limited set. The array SHOULD NOT be empty.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                default: builtins.str,
                description: typing.Optional[builtins.str] = None,
                enum: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enum", value=enum, expected_type=type_hints["enum"])
        self._values: typing.Dict[str, typing.Any] = {
            "default": default,
        }
        if description is not None:
            self._values["description"] = description
        if enum is not None:
            self._values["enum"] = enum

    @builtins.property
    def default(self) -> builtins.str:
        '''(experimental) The default value to use for substitution, which SHALL be sent if an alternate value is not supplied.

        Note this behavior is different than the Schema Object's treatment of default values, because in those cases parameter values are optional. If the enum is defined, the value SHOULD exist in the enum's values.

        :stability: experimental
        '''
        result = self._values.get("default")
        assert result is not None, "Required property 'default' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional description for the server variable.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enum(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An enumeration of string values to be used if the substitution options are from a limited set.

        The array SHOULD NOT be empty.

        :stability: experimental
        '''
        result = self._values.get("enum")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerVariableObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.TagObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_docs": "externalDocs",
    },
)
class TagObject(Extensible):
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Adds metadata to a single tag that is used by the Operation Object.

        It is not mandatory to have a Tag Object per tag defined in the Operation Object instances.

        :param name: (experimental) The name of the tag.
        :param description: (experimental) A short description for the tag. CommonMark syntax MAY be used for rich text representation.
        :param external_docs: (experimental) Additional external documentation for this tag.

        :stability: experimental
        '''
        if isinstance(external_docs, dict):
            external_docs = ExternalDocumentationObject(**external_docs)
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                description: typing.Optional[builtins.str] = None,
                external_docs: typing.Optional[typing.Union[ExternalDocumentationObject, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_docs", value=external_docs, expected_type=type_hints["external_docs"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_docs is not None:
            self._values["external_docs"] = external_docs

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The name of the tag.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A short description for the tag.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_docs(self) -> typing.Optional[ExternalDocumentationObject]:
        '''(experimental) Additional external documentation for this tag.

        :stability: experimental
        '''
        result = self._values.get("external_docs")
        return typing.cast(typing.Optional[ExternalDocumentationObject], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ValidatorConfig",
    jsii_struct_bases=[],
    name_mapping={"validator": "validator"},
)
class ValidatorConfig:
    def __init__(self, *, validator: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) Method integration validator configuration.

        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        if __debug__:
            def stub(*, validator: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validator", value=validator, expected_type=type_hints["validator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def validator(self) -> typing.Optional[builtins.str]:
        '''(experimental) Validator identifier for method integration. This will override the default validator if one configured.

        Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        result = self._values.get("validator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayAuthorizer",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "authorizer_credentials": "authorizerCredentials",
        "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
        "authorizer_uri": "authorizerUri",
        "identity_source": "identitySource",
        "identity_validation_expression": "identityValidationExpression",
        "provider_ar_ns": "providerARNs",
    },
)
class XAmazonApigatewayAuthorizer:
    def __init__(
        self,
        *,
        type: builtins.str,
        authorizer_credentials: typing.Optional[builtins.str] = None,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        authorizer_uri: typing.Optional[builtins.str] = None,
        identity_source: typing.Optional[builtins.str] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
        provider_ar_ns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Describes the ``x-amazon-apigateway-authorizer`` value.

        :param type: (experimental) The type of the authorizer. This is a required property. For REST APIs, specify ``token`` for an authorizer with the caller identity embedded in an authorization token. Specify ``request`` for an authorizer with the caller identity contained in request parameters.
        :param authorizer_credentials: (experimental) The credentials required for invoking the authorizer, if any, in the form of an ARN of an IAM execution role.
        :param authorizer_result_ttl_in_seconds: (experimental) The number of seconds during which authorizer result is cached.
        :param authorizer_uri: (experimental) The Uniform Resource Identifier (URI) of the authorizer Lambda function.
        :param identity_source: (experimental) A comma-separated list of mapping expressions of the request parameters as the identity source. Applicable for the authorizer of the ``request`` and ``jwt`` type only.
        :param identity_validation_expression: (experimental) A regular expression for validating the token as the incoming identity.
        :param provider_ar_ns: (experimental) List of Cognito User Pool ARNs. Applicable for the authorizer of the ``cognito_user_pools`` type only.

        :see: https://awslabs.github.io/smithy/1.0/spec/aws/amazon-apigateway.html
        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                authorizer_credentials: typing.Optional[builtins.str] = None,
                authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
                authorizer_uri: typing.Optional[builtins.str] = None,
                identity_source: typing.Optional[builtins.str] = None,
                identity_validation_expression: typing.Optional[builtins.str] = None,
                provider_ar_ns: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument authorizer_credentials", value=authorizer_credentials, expected_type=type_hints["authorizer_credentials"])
            check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
            check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
            check_type(argname="argument identity_source", value=identity_source, expected_type=type_hints["identity_source"])
            check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
            check_type(argname="argument provider_ar_ns", value=provider_ar_ns, expected_type=type_hints["provider_ar_ns"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if authorizer_credentials is not None:
            self._values["authorizer_credentials"] = authorizer_credentials
        if authorizer_result_ttl_in_seconds is not None:
            self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if authorizer_uri is not None:
            self._values["authorizer_uri"] = authorizer_uri
        if identity_source is not None:
            self._values["identity_source"] = identity_source
        if identity_validation_expression is not None:
            self._values["identity_validation_expression"] = identity_validation_expression
        if provider_ar_ns is not None:
            self._values["provider_ar_ns"] = provider_ar_ns

    @builtins.property
    def type(self) -> builtins.str:
        '''(experimental) The type of the authorizer. This is a required property.

        For REST APIs, specify ``token`` for an authorizer with the caller identity embedded in an authorization token.
        Specify ``request`` for an authorizer with the caller identity contained in request parameters.

        :stability: experimental

        Example::

            'token'
            'request'
            'cognito_user_pools'
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_credentials(self) -> typing.Optional[builtins.str]:
        '''(experimental) The credentials required for invoking the authorizer, if any, in the form of an ARN of an IAM execution role.

        :stability: experimental

        Example::

            'arn:aws:iam::123456789012:role/MyRole'
        '''
        result = self._values.get("authorizer_credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of seconds during which authorizer result is cached.

        :stability: experimental

        Example::

            60
        '''
        result = self._values.get("authorizer_result_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def authorizer_uri(self) -> typing.Optional[builtins.str]:
        '''(experimental) The Uniform Resource Identifier (URI) of the authorizer Lambda function.

        :stability: experimental

        Example::

            'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:account-id:function:auth_function_name/invocations'
        '''
        result = self._values.get("authorizer_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_source(self) -> typing.Optional[builtins.str]:
        '''(experimental) A comma-separated list of mapping expressions of the request parameters as the identity source.

        Applicable for the authorizer of the ``request`` and ``jwt`` type only.

        :stability: experimental

        Example::

            'method.request.header.Authorization'
            'method.request.header.Authorization, context.identity.sourceIp'
            'method.request.header.Auth, method.request.querystring.Name'
        '''
        result = self._values.get("identity_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_validation_expression(self) -> typing.Optional[builtins.str]:
        '''(experimental) A regular expression for validating the token as the incoming identity.

        :stability: experimental

        Example::

            '^x-[a-z]+'
        '''
        result = self._values.get("identity_validation_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_ar_ns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of Cognito User Pool ARNs.

        Applicable for the authorizer of the ``cognito_user_pools`` type only.

        :stability: experimental

        Example::

            ['arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}]
        '''
        result = self._values.get("provider_ar_ns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayAuthorizer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegration",
    jsii_struct_bases=[],
    name_mapping={
        "http_method": "httpMethod",
        "type": "type",
        "uri": "uri",
        "cache_key_parameters": "cacheKeyParameters",
        "cache_namespace": "cacheNamespace",
        "connection_id": "connectionId",
        "connection_type": "connectionType",
        "content_handling": "contentHandling",
        "credentials": "credentials",
        "passthrough_behavior": "passthroughBehavior",
        "request_parameters": "requestParameters",
        "request_templates": "requestTemplates",
        "responses": "responses",
        "timeout_in_millis": "timeoutInMillis",
        "tls_config": "tlsConfig",
    },
)
class XAmazonApigatewayIntegration:
    def __init__(
        self,
        *,
        http_method: builtins.str,
        type: aws_cdk.aws_apigateway.IntegrationType,
        uri: builtins.str,
        cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_namespace: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
        content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
        credentials: typing.Optional[builtins.str] = None,
        passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
        request_parameters: typing.Optional[typing.Union["XAmazonApigatewayIntegrationRequestParameters", typing.Dict[str, typing.Any]]] = None,
        request_templates: typing.Optional[typing.Union["XAmazonApigatewayIntegrationRequestTemplates", typing.Dict[str, typing.Any]]] = None,
        responses: typing.Optional[typing.Union["XAmazonApigatewayIntegrationResponses", typing.Dict[str, typing.Any]]] = None,
        timeout_in_millis: typing.Optional[jsii.Number] = None,
        tls_config: typing.Optional[typing.Union["XAmazonApigatewayIntegrationTlsConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Specifies details of the backend integration used for this method.

        This extension is an extended property of the OpenAPI Operation object.
        The result is an API Gateway integration object.

        :param http_method: (experimental) The HTTP method used in the integration request. For Lambda function invocations, the value must be POST. Default: 'POST'
        :param type: (experimental) The type of integration with the specified backend. Valid values are: - ``http`` or ``http_proxy``, for integration with an HTTP backend. - ``aws_proxy``, for integration with AWS Lambda functions. - ``aws``, for integration with AWS Lambda functions or other AWS services, such as Amazon DynamoDB, Amazon Simple Notification Service, or Amazon Simple Queue Service. - ``mock``, for integration with API Gateway without invoking any backend.
        :param uri: (experimental) The endpoint URI of the backend. For integrations of the aws type, this is an ARN value. For the HTTP integration, this is the URL of the HTTP endpoint including the https or http scheme.
        :param cache_key_parameters: (experimental) A list of request parameters whose values are to be cached.
        :param cache_namespace: (experimental) An API-specific tag group of related cached parameters.
        :param connection_id: (experimental) The ID of a VpcLink for the private integration.
        :param connection_type: (experimental) The integration connection type. The valid value is "VPC_LINK" for private integration or "INTERNET", otherwise.
        :param content_handling: (experimental) Response payload encoding conversion types. Valid values are 1. CONVERT_TO_TEXT, for converting a binary payload into a base64-encoded string or converting a text payload into a utf-8-encoded string or passing through the text payload natively without modification, and 2. CONVERT_TO_BINARY, for converting a text payload into a base64-decoded blob or passing through a binary payload natively without modification.
        :param credentials: (experimental) For AWS IAM role-based credentials, specify the ARN of an appropriate IAM role. If unspecified, credentials default to resource-based permissions that must be added manually to allow the API to access the resource. For more information, see Granting Permissions Using a Resource Policy. Note: When using IAM credentials, make sure that AWS STS Regional endpoints are enabled for the Region where this API is deployed for best performance.
        :param passthrough_behavior: (experimental) Specifies how a request payload of unmapped content type is passed through the integration request without modification. Supported values are when_no_templates, when_no_match, and never
        :param request_parameters: (experimental) Specifies mappings from method request parameters to integration request parameters. Supported request parameters are querystring, path, header, and body.
        :param request_templates: (experimental) Mapping templates for a request payload of specified MIME types.
        :param responses: (experimental) Defines the method's responses and specifies desired parameter mappings or payload mappings from integration responses to method responses.
        :param timeout_in_millis: (experimental) Integration timeouts between 50 ms and 29,000 ms.
        :param tls_config: (experimental) Specifies the TLS configuration for an integration.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html
        :stability: experimental
        '''
        if isinstance(request_parameters, dict):
            request_parameters = XAmazonApigatewayIntegrationRequestParameters(**request_parameters)
        if isinstance(request_templates, dict):
            request_templates = XAmazonApigatewayIntegrationRequestTemplates(**request_templates)
        if isinstance(responses, dict):
            responses = XAmazonApigatewayIntegrationResponses(**responses)
        if isinstance(tls_config, dict):
            tls_config = XAmazonApigatewayIntegrationTlsConfig(**tls_config)
        if __debug__:
            def stub(
                *,
                http_method: builtins.str,
                type: aws_cdk.aws_apigateway.IntegrationType,
                uri: builtins.str,
                cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
                cache_namespace: typing.Optional[builtins.str] = None,
                connection_id: typing.Optional[builtins.str] = None,
                connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
                content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
                credentials: typing.Optional[builtins.str] = None,
                passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
                request_parameters: typing.Optional[typing.Union["XAmazonApigatewayIntegrationRequestParameters", typing.Dict[str, typing.Any]]] = None,
                request_templates: typing.Optional[typing.Union["XAmazonApigatewayIntegrationRequestTemplates", typing.Dict[str, typing.Any]]] = None,
                responses: typing.Optional[typing.Union["XAmazonApigatewayIntegrationResponses", typing.Dict[str, typing.Any]]] = None,
                timeout_in_millis: typing.Optional[jsii.Number] = None,
                tls_config: typing.Optional[typing.Union["XAmazonApigatewayIntegrationTlsConfig", typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument cache_key_parameters", value=cache_key_parameters, expected_type=type_hints["cache_key_parameters"])
            check_type(argname="argument cache_namespace", value=cache_namespace, expected_type=type_hints["cache_namespace"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
            check_type(argname="argument content_handling", value=content_handling, expected_type=type_hints["content_handling"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument passthrough_behavior", value=passthrough_behavior, expected_type=type_hints["passthrough_behavior"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument request_templates", value=request_templates, expected_type=type_hints["request_templates"])
            check_type(argname="argument responses", value=responses, expected_type=type_hints["responses"])
            check_type(argname="argument timeout_in_millis", value=timeout_in_millis, expected_type=type_hints["timeout_in_millis"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_method": http_method,
            "type": type,
            "uri": uri,
        }
        if cache_key_parameters is not None:
            self._values["cache_key_parameters"] = cache_key_parameters
        if cache_namespace is not None:
            self._values["cache_namespace"] = cache_namespace
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if content_handling is not None:
            self._values["content_handling"] = content_handling
        if credentials is not None:
            self._values["credentials"] = credentials
        if passthrough_behavior is not None:
            self._values["passthrough_behavior"] = passthrough_behavior
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if request_templates is not None:
            self._values["request_templates"] = request_templates
        if responses is not None:
            self._values["responses"] = responses
        if timeout_in_millis is not None:
            self._values["timeout_in_millis"] = timeout_in_millis
        if tls_config is not None:
            self._values["tls_config"] = tls_config

    @builtins.property
    def http_method(self) -> builtins.str:
        '''(experimental) The HTTP method used in the integration request.

        For Lambda function invocations, the value must be POST.

        :default: 'POST'

        :stability: experimental
        '''
        result = self._values.get("http_method")
        assert result is not None, "Required property 'http_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> aws_cdk.aws_apigateway.IntegrationType:
        '''(experimental) The type of integration with the specified backend.

        Valid values are:

        - ``http`` or ``http_proxy``, for integration with an HTTP backend.
        - ``aws_proxy``, for integration with AWS Lambda functions.
        - ``aws``, for integration with AWS Lambda functions or other AWS services, such as Amazon DynamoDB, Amazon Simple Notification Service, or Amazon Simple Queue Service.
        - ``mock``, for integration with API Gateway without invoking any backend.

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(aws_cdk.aws_apigateway.IntegrationType, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''(experimental) The endpoint URI of the backend.

        For integrations of the aws type, this is an ARN value.
        For the HTTP integration, this is the URL of the HTTP endpoint including the https or http scheme.

        :stability: experimental
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_key_parameters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A list of request parameters whose values are to be cached.

        :stability: experimental
        '''
        result = self._values.get("cache_key_parameters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_namespace(self) -> typing.Optional[builtins.str]:
        '''(experimental) An API-specific tag group of related cached parameters.

        :stability: experimental
        '''
        result = self._values.get("cache_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) The ID of a VpcLink for the private integration.

        :stability: experimental
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[aws_cdk.aws_apigateway.ConnectionType]:
        '''(experimental) The integration connection type.

        The valid value is "VPC_LINK" for private integration
        or "INTERNET", otherwise.

        :stability: experimental

        Example::

            'VPC_LINK'
        '''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.ConnectionType], result)

    @builtins.property
    def content_handling(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.ContentHandling]:
        '''(experimental) Response payload encoding conversion types.

        Valid values are

        1. CONVERT_TO_TEXT, for converting a binary payload into a base64-encoded string or converting a text payload into a utf-8-encoded string or passing through the text payload natively without modification, and
        2. CONVERT_TO_BINARY, for converting a text payload into a base64-decoded blob or passing through a binary payload natively without modification.

        :stability: experimental
        '''
        result = self._values.get("content_handling")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.ContentHandling], result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''(experimental) For AWS IAM role-based credentials, specify the ARN of an appropriate IAM role.

        If unspecified, credentials default to resource-based permissions
        that must be added manually to allow the API to access the resource.
        For more information, see Granting Permissions Using a Resource Policy.

        Note: When using IAM credentials, make sure that AWS STS Regional endpoints
        are enabled for the Region where this API is deployed for best performance.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#intro-permission-model-access-policy
        :stability: experimental
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def passthrough_behavior(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior]:
        '''(experimental) Specifies how a request payload of unmapped content type is passed through the integration request without modification.

        Supported values are
        when_no_templates, when_no_match, and never

        :stability: experimental
        '''
        result = self._values.get("passthrough_behavior")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior], result)

    @builtins.property
    def request_parameters(
        self,
    ) -> typing.Optional["XAmazonApigatewayIntegrationRequestParameters"]:
        '''(experimental) Specifies mappings from method request parameters to integration request parameters.

        Supported request parameters are querystring, path, header, and body.

        :stability: experimental
        '''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Optional["XAmazonApigatewayIntegrationRequestParameters"], result)

    @builtins.property
    def request_templates(
        self,
    ) -> typing.Optional["XAmazonApigatewayIntegrationRequestTemplates"]:
        '''(experimental) Mapping templates for a request payload of specified MIME types.

        :stability: experimental
        '''
        result = self._values.get("request_templates")
        return typing.cast(typing.Optional["XAmazonApigatewayIntegrationRequestTemplates"], result)

    @builtins.property
    def responses(self) -> typing.Optional["XAmazonApigatewayIntegrationResponses"]:
        '''(experimental) Defines the method's responses and specifies desired parameter mappings or payload mappings from integration responses to method responses.

        :stability: experimental
        '''
        result = self._values.get("responses")
        return typing.cast(typing.Optional["XAmazonApigatewayIntegrationResponses"], result)

    @builtins.property
    def timeout_in_millis(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Integration timeouts between 50 ms and 29,000 ms.

        :stability: experimental

        Example::

            1000
        '''
        result = self._values.get("timeout_in_millis")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls_config(self) -> typing.Optional["XAmazonApigatewayIntegrationTlsConfig"]:
        '''(experimental) Specifies the TLS configuration for an integration.

        :stability: experimental
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Optional["XAmazonApigatewayIntegrationTlsConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegrationRequestParameters",
    jsii_struct_bases=[],
    name_mapping={},
)
class XAmazonApigatewayIntegrationRequestParameters:
    def __init__(self) -> None:
        '''(experimental) Specifies mappings from named method request parameters to integration request parameters.

        The method request parameters must be defined before being referenced.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestParameters.html
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegrationRequestParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegrationRequestTemplates",
    jsii_struct_bases=[],
    name_mapping={},
)
class XAmazonApigatewayIntegrationRequestTemplates:
    def __init__(self) -> None:
        '''(experimental) Specifies mapping templates for a request payload of the specified MIME types.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegrationRequestTemplates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegrationResponse",
    jsii_struct_bases=[],
    name_mapping={
        "status_code": "statusCode",
        "content_handling": "contentHandling",
        "response_parameters": "responseParameters",
        "response_templates": "responseTemplates",
    },
)
class XAmazonApigatewayIntegrationResponse:
    def __init__(
        self,
        *,
        status_code: builtins.str,
        content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
        response_parameters: typing.Optional[typing.Union["XAmazonApigatewayIntegrationResponseParameters", typing.Dict[str, typing.Any]]] = None,
        response_templates: typing.Optional[typing.Union["XAmazonApigatewayIntegrationResponseTemplates", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Defines a response and specifies parameter mappings or payload mappings from the integration response to the method response.

        :param status_code: (experimental) HTTP status code for the method response. This must correspond to a matching response in the OpenAPI Operation responses field.
        :param content_handling: (experimental) Response payload encoding conversion types. Valid values are 1. CONVERT_TO_TEXT, for converting a binary payload into a base64-encoded string or converting a text payload into a utf-8-encoded string or passing through the text payload natively without modification, and 2. CONVERT_TO_BINARY, for converting a text payload into a base64-decoded blob or passing through a binary payload natively without modification.
        :param response_parameters: (experimental) Specifies parameter mappings for the response. Only the header and body parameters of the integration response can be mapped to the header parameters of the method.
        :param response_templates: (experimental) Specifies MIME type-specific mapping templates for the response’s payload.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-response.html
        :stability: experimental
        '''
        if isinstance(response_parameters, dict):
            response_parameters = XAmazonApigatewayIntegrationResponseParameters(**response_parameters)
        if isinstance(response_templates, dict):
            response_templates = XAmazonApigatewayIntegrationResponseTemplates(**response_templates)
        if __debug__:
            def stub(
                *,
                status_code: builtins.str,
                content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
                response_parameters: typing.Optional[typing.Union["XAmazonApigatewayIntegrationResponseParameters", typing.Dict[str, typing.Any]]] = None,
                response_templates: typing.Optional[typing.Union["XAmazonApigatewayIntegrationResponseTemplates", typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument content_handling", value=content_handling, expected_type=type_hints["content_handling"])
            check_type(argname="argument response_parameters", value=response_parameters, expected_type=type_hints["response_parameters"])
            check_type(argname="argument response_templates", value=response_templates, expected_type=type_hints["response_templates"])
        self._values: typing.Dict[str, typing.Any] = {
            "status_code": status_code,
        }
        if content_handling is not None:
            self._values["content_handling"] = content_handling
        if response_parameters is not None:
            self._values["response_parameters"] = response_parameters
        if response_templates is not None:
            self._values["response_templates"] = response_templates

    @builtins.property
    def status_code(self) -> builtins.str:
        '''(experimental) HTTP status code for the method response.

        This must correspond to a matching response in the OpenAPI Operation responses field.

        :stability: experimental

        Example::

            '200'
        '''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_handling(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.ContentHandling]:
        '''(experimental) Response payload encoding conversion types.

        Valid values are

        1. CONVERT_TO_TEXT, for converting a binary payload into a base64-encoded string or converting a text payload into a utf-8-encoded string or passing through the text payload natively without modification, and
        2. CONVERT_TO_BINARY, for converting a text payload into a base64-decoded blob or passing through a binary payload natively without modification.

        :stability: experimental
        '''
        result = self._values.get("content_handling")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.ContentHandling], result)

    @builtins.property
    def response_parameters(
        self,
    ) -> typing.Optional["XAmazonApigatewayIntegrationResponseParameters"]:
        '''(experimental) Specifies parameter mappings for the response.

        Only the header and body parameters of the integration response
        can be mapped to the header parameters of the method.

        :stability: experimental
        '''
        result = self._values.get("response_parameters")
        return typing.cast(typing.Optional["XAmazonApigatewayIntegrationResponseParameters"], result)

    @builtins.property
    def response_templates(
        self,
    ) -> typing.Optional["XAmazonApigatewayIntegrationResponseTemplates"]:
        '''(experimental) Specifies MIME type-specific mapping templates for the response’s payload.

        :stability: experimental

        Example::

            {
              'application/json': '#set ($root=$input.path('$')) { \"stage\": \"$root.name\", \"user-id\": \"$root.key\" }',
            }
        '''
        result = self._values.get("response_templates")
        return typing.cast(typing.Optional["XAmazonApigatewayIntegrationResponseTemplates"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegrationResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegrationResponseParameters",
    jsii_struct_bases=[],
    name_mapping={},
)
class XAmazonApigatewayIntegrationResponseParameters:
    def __init__(self) -> None:
        '''(experimental) Specifies mappings from integration method response parameters to method response parameters.

        You can map header, body, or static values to the header type of the method response.

        :stability: experimental

        Example::

            {
              'method.response.header.Location' : 'integration.response.body.redirect.url',
              'method.response.header.x-user-id' : 'integration.response.header.x-userid'
            }
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegrationResponseParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegrationResponseTemplates",
    jsii_struct_bases=[],
    name_mapping={},
)
class XAmazonApigatewayIntegrationResponseTemplates:
    def __init__(self) -> None:
        '''(experimental) Specifies a mapping template to transform the integration response body to the method response body for a given MIME type.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html#models-mappings-mappings
        :stability: experimental

        Example::

            {
              'application/json': '#set ($root=$input.path('$')) { \"stage\": \"$root.name\", \"user-id\": \"$root.key\" }',
            }
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegrationResponseTemplates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegrationResponses",
    jsii_struct_bases=[],
    name_mapping={},
)
class XAmazonApigatewayIntegrationResponses:
    def __init__(self) -> None:
        '''(experimental) Defines the method's responses and specifies parameter mappings or payload mappings from integration responses to method responses.

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responses.html
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegrationResponses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayIntegrationTlsConfig",
    jsii_struct_bases=[],
    name_mapping={"insecure_skip_verification": "insecureSkipVerification"},
)
class XAmazonApigatewayIntegrationTlsConfig:
    def __init__(self, *, insecure_skip_verification: builtins.bool) -> None:
        '''(experimental) Specifies the TLS configuration for an integration.

        :param insecure_skip_verification: (experimental) Specifies whether or not API Gateway skips verification that the certificate for an integration endpoint is issued by a supported c ertificate authority. This isn’t recommended, but it enables you to use certificates that are signed by private certificate authorities, or certificates that are self-signed. If enabled, API Gateway still performs basic certificate validation, which includes checking the certificate's expiration date, hostname, and presence of a root certificate authority. Supported only for HTTP and HTTP_PROXY integrations.

        :stability: experimental
        '''
        if __debug__:
            def stub(*, insecure_skip_verification: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument insecure_skip_verification", value=insecure_skip_verification, expected_type=type_hints["insecure_skip_verification"])
        self._values: typing.Dict[str, typing.Any] = {
            "insecure_skip_verification": insecure_skip_verification,
        }

    @builtins.property
    def insecure_skip_verification(self) -> builtins.bool:
        '''(experimental) Specifies whether or not API Gateway skips verification that the certificate for an integration endpoint is issued by a supported c ertificate authority.

        This isn’t recommended, but it enables you to
        use certificates that are signed by private certificate authorities,
        or certificates that are self-signed. If enabled, API Gateway still
        performs basic certificate validation, which includes checking the
        certificate's expiration date, hostname, and presence of a root certificate
        authority. Supported only for HTTP and HTTP_PROXY integrations.

        :stability: experimental
        '''
        result = self._values.get("insecure_skip_verification")
        assert result is not None, "Required property 'insecure_skip_verification' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayIntegrationTlsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XAmazonApigatewayRequestValidator",
    jsii_struct_bases=[],
    name_mapping={
        "validate_request_body": "validateRequestBody",
        "validate_request_parameters": "validateRequestParameters",
    },
)
class XAmazonApigatewayRequestValidator:
    def __init__(
        self,
        *,
        validate_request_body: builtins.bool,
        validate_request_parameters: builtins.bool,
    ) -> None:
        '''(experimental) Request validator configuration.

        :param validate_request_body: 
        :param validate_request_parameters: 

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validators.html
        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                validate_request_body: builtins.bool,
                validate_request_parameters: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validate_request_body", value=validate_request_body, expected_type=type_hints["validate_request_body"])
            check_type(argname="argument validate_request_parameters", value=validate_request_parameters, expected_type=type_hints["validate_request_parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "validate_request_body": validate_request_body,
            "validate_request_parameters": validate_request_parameters,
        }

    @builtins.property
    def validate_request_body(self) -> builtins.bool:
        '''
        :stability: experimental
        '''
        result = self._values.get("validate_request_body")
        assert result is not None, "Required property 'validate_request_body' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def validate_request_parameters(self) -> builtins.bool:
        '''
        :stability: experimental
        '''
        result = self._values.get("validate_request_parameters")
        assert result is not None, "Required property 'validate_request_parameters' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XAmazonApigatewayRequestValidator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.XmlObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "attribute": "attribute",
        "name": "name",
        "namespace": "namespace",
        "prefix": "prefix",
        "wrapped": "wrapped",
    },
)
class XmlObject(Extensible):
    def __init__(
        self,
        *,
        attribute: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        wrapped: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) A metadata object that allows for more fine-tuned XML model definitions.

        When using arrays, XML element names are not inferred (for singular/plural forms) and the name property SHOULD be used to add that information. See examples for expected behavior.

        :param attribute: (experimental) Declares whether the property definition translates to an attribute instead of an element. Default value is false.
        :param name: (experimental) Replaces the name of the element/attribute used for the described schema property. When defined within items, it will affect the name of the individual XML elements within the list. When defined alongside type being array (outside the items), it will affect the wrapping element and only if wrapped is true. If wrapped is false, it will be ignored.
        :param namespace: (experimental) The URI of the namespace definition. Value MUST be in the form of an absolute URI.
        :param prefix: (experimental) The prefix to be used for the name.
        :param wrapped: (experimental) MAY be used only for an array definition. Signifies whether the array is wrapped (for example, ) or unwrapped (). Default value is false. The definition takes effect only when defined alongside type being array (outside the items).

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                attribute: typing.Optional[builtins.bool] = None,
                name: typing.Optional[builtins.str] = None,
                namespace: typing.Optional[builtins.str] = None,
                prefix: typing.Optional[builtins.str] = None,
                wrapped: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument wrapped", value=wrapped, expected_type=type_hints["wrapped"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute is not None:
            self._values["attribute"] = attribute
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if prefix is not None:
            self._values["prefix"] = prefix
        if wrapped is not None:
            self._values["wrapped"] = wrapped

    @builtins.property
    def attribute(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Declares whether the property definition translates to an attribute instead of an element.

        Default value is false.

        :stability: experimental
        '''
        result = self._values.get("attribute")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Replaces the name of the element/attribute used for the described schema property.

        When defined within items, it will affect the name of the individual XML elements within the list. When defined alongside type being array (outside the items), it will affect the wrapping element and only if wrapped is true. If wrapped is false, it will be ignored.

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URI of the namespace definition.

        Value MUST be in the form of an absolute URI.

        :stability: experimental
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''(experimental) The prefix to be used for the name.

        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wrapped(self) -> typing.Optional[builtins.bool]:
        '''(experimental) MAY be used only for an array definition.

        Signifies whether the array is wrapped (for example, ) or unwrapped (). Default value is false. The definition takes effect only when defined alongside type being array (outside the items).

        :stability: experimental
        '''
        result = self._values.get("wrapped")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XmlObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.AuthorizerConfig",
    jsii_struct_bases=[AuthorizerExtensions],
    name_mapping={
        "x_amazon_apigateway_authorizer": "xAmazonApigatewayAuthorizer",
        "x_amazon_apigateway_authtype": "xAmazonApigatewayAuthtype",
        "id": "id",
    },
)
class AuthorizerConfig(AuthorizerExtensions):
    def __init__(
        self,
        *,
        x_amazon_apigateway_authorizer: typing.Union[XAmazonApigatewayAuthorizer, typing.Dict[str, typing.Any]],
        x_amazon_apigateway_authtype: builtins.str,
        id: builtins.str,
    ) -> None:
        '''
        :param x_amazon_apigateway_authorizer: 
        :param x_amazon_apigateway_authtype: 
        :param id: 

        :stability: experimental
        '''
        if isinstance(x_amazon_apigateway_authorizer, dict):
            x_amazon_apigateway_authorizer = XAmazonApigatewayAuthorizer(**x_amazon_apigateway_authorizer)
        if __debug__:
            def stub(
                *,
                x_amazon_apigateway_authorizer: typing.Union[XAmazonApigatewayAuthorizer, typing.Dict[str, typing.Any]],
                x_amazon_apigateway_authtype: builtins.str,
                id: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument x_amazon_apigateway_authorizer", value=x_amazon_apigateway_authorizer, expected_type=type_hints["x_amazon_apigateway_authorizer"])
            check_type(argname="argument x_amazon_apigateway_authtype", value=x_amazon_apigateway_authtype, expected_type=type_hints["x_amazon_apigateway_authtype"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "x_amazon_apigateway_authorizer": x_amazon_apigateway_authorizer,
            "x_amazon_apigateway_authtype": x_amazon_apigateway_authtype,
            "id": id,
        }

    @builtins.property
    def x_amazon_apigateway_authorizer(self) -> XAmazonApigatewayAuthorizer:
        '''
        :stability: experimental
        '''
        result = self._values.get("x_amazon_apigateway_authorizer")
        assert result is not None, "Required property 'x_amazon_apigateway_authorizer' is missing"
        return typing.cast(XAmazonApigatewayAuthorizer, result)

    @builtins.property
    def x_amazon_apigateway_authtype(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("x_amazon_apigateway_authtype")
        assert result is not None, "Required property 'x_amazon_apigateway_authtype' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsIntegration(
    Integration,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.AwsIntegration",
):
    '''(experimental) Defines direct AWS service integration.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        service: builtins.str,
        action: typing.Optional[builtins.str] = None,
        action_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        integration_http_method: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        proxy: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subdomain: typing.Optional[builtins.str] = None,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Defines direct AWS service integration.

        :param scope: -
        :param service: The name of the integrated AWS service (e.g. ``s3``).
        :param action: The AWS action to perform in the integration. Use ``actionParams`` to specify key-value params for the action. Mutually exclusive with ``path``.
        :param action_parameters: Parameters for the action. ``action`` must be set, and ``path`` must be undefined. The action params will be URL encoded.
        :param integration_http_method: The integration's HTTP method type. Default: POST
        :param options: Integration options, such as content handling, request/response mapping, etc.
        :param path: The path to use for path-base APIs. For example, for S3 GET, you can set path to ``bucket/key``. For lambda, you can set path to ``2015-03-31/functions/${function-arn}/invocations`` Mutually exclusive with the ``action`` options.
        :param proxy: Use AWS_PROXY integration. Default: false
        :param region: The region of the integrated AWS service. Default: - same region as the stack
        :param subdomain: A designated subdomain supported by certain AWS service for fast host-name lookup.
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental

        Example::

            '/item': {
              'GET': new openapix.AwsIntegration(this, {
                service: 'dynamodb',
                action: 'GetItem',
                options: {
                  credentialsRole: role,
                  requestTemplates: {
                    'application/json': JSON.stringify({
                      "TableName": table.tableName,
                      "Key": {
                        'PK': {
                          "S": "$input.params('item')"
                        }
                      }
                    }),
                  },
                },
              }),
            },
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                *,
                service: builtins.str,
                action: typing.Optional[builtins.str] = None,
                action_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                integration_http_method: typing.Optional[builtins.str] = None,
                options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
                path: typing.Optional[builtins.str] = None,
                proxy: typing.Optional[builtins.bool] = None,
                region: typing.Optional[builtins.str] = None,
                subdomain: typing.Optional[builtins.str] = None,
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        props = AwsIntegrationProps(
            service=service,
            action=action,
            action_parameters=action_parameters,
            integration_http_method=integration_http_method,
            options=options,
            path=path,
            proxy=proxy,
            region=region,
            subdomain=subdomain,
            validator=validator,
        )

        jsii.create(self.__class__, self, [scope, props])


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.AwsIntegrationProps",
    jsii_struct_bases=[aws_cdk.aws_apigateway.AwsIntegrationProps, ValidatorConfig],
    name_mapping={
        "service": "service",
        "action": "action",
        "action_parameters": "actionParameters",
        "integration_http_method": "integrationHttpMethod",
        "options": "options",
        "path": "path",
        "proxy": "proxy",
        "region": "region",
        "subdomain": "subdomain",
        "validator": "validator",
    },
)
class AwsIntegrationProps(aws_cdk.aws_apigateway.AwsIntegrationProps, ValidatorConfig):
    def __init__(
        self,
        *,
        service: builtins.str,
        action: typing.Optional[builtins.str] = None,
        action_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        integration_http_method: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        proxy: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subdomain: typing.Optional[builtins.str] = None,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: The name of the integrated AWS service (e.g. ``s3``).
        :param action: The AWS action to perform in the integration. Use ``actionParams`` to specify key-value params for the action. Mutually exclusive with ``path``.
        :param action_parameters: Parameters for the action. ``action`` must be set, and ``path`` must be undefined. The action params will be URL encoded.
        :param integration_http_method: The integration's HTTP method type. Default: POST
        :param options: Integration options, such as content handling, request/response mapping, etc.
        :param path: The path to use for path-base APIs. For example, for S3 GET, you can set path to ``bucket/key``. For lambda, you can set path to ``2015-03-31/functions/${function-arn}/invocations`` Mutually exclusive with the ``action`` options.
        :param proxy: Use AWS_PROXY integration. Default: false
        :param region: The region of the integrated AWS service. Default: - same region as the stack
        :param subdomain: A designated subdomain supported by certain AWS service for fast host-name lookup.
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        if isinstance(options, dict):
            options = aws_cdk.aws_apigateway.IntegrationOptions(**options)
        if __debug__:
            def stub(
                *,
                service: builtins.str,
                action: typing.Optional[builtins.str] = None,
                action_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                integration_http_method: typing.Optional[builtins.str] = None,
                options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
                path: typing.Optional[builtins.str] = None,
                proxy: typing.Optional[builtins.bool] = None,
                region: typing.Optional[builtins.str] = None,
                subdomain: typing.Optional[builtins.str] = None,
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument action_parameters", value=action_parameters, expected_type=type_hints["action_parameters"])
            check_type(argname="argument integration_http_method", value=integration_http_method, expected_type=type_hints["integration_http_method"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subdomain", value=subdomain, expected_type=type_hints["subdomain"])
            check_type(argname="argument validator", value=validator, expected_type=type_hints["validator"])
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if action is not None:
            self._values["action"] = action
        if action_parameters is not None:
            self._values["action_parameters"] = action_parameters
        if integration_http_method is not None:
            self._values["integration_http_method"] = integration_http_method
        if options is not None:
            self._values["options"] = options
        if path is not None:
            self._values["path"] = path
        if proxy is not None:
            self._values["proxy"] = proxy
        if region is not None:
            self._values["region"] = region
        if subdomain is not None:
            self._values["subdomain"] = subdomain
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def service(self) -> builtins.str:
        '''The name of the integrated AWS service (e.g. ``s3``).'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''The AWS action to perform in the integration.

        Use ``actionParams`` to specify key-value params for the action.

        Mutually exclusive with ``path``.
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Parameters for the action.

        ``action`` must be set, and ``path`` must be undefined.
        The action params will be URL encoded.
        '''
        result = self._values.get("action_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def integration_http_method(self) -> typing.Optional[builtins.str]:
        '''The integration's HTTP method type.

        :default: POST
        '''
        result = self._values.get("integration_http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[aws_cdk.aws_apigateway.IntegrationOptions]:
        '''Integration options, such as content handling, request/response mapping, etc.'''
        result = self._values.get("options")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.IntegrationOptions], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to use for path-base APIs.

        For example, for S3 GET, you can set path to ``bucket/key``.
        For lambda, you can set path to ``2015-03-31/functions/${function-arn}/invocations``

        Mutually exclusive with the ``action`` options.
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy(self) -> typing.Optional[builtins.bool]:
        '''Use AWS_PROXY integration.

        :default: false
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region of the integrated AWS service.

        :default: - same region as the stack
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdomain(self) -> typing.Optional[builtins.str]:
        '''A designated subdomain supported by certain AWS service for fast host-name lookup.'''
        result = self._values.get("subdomain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validator(self) -> typing.Optional[builtins.str]:
        '''(experimental) Validator identifier for method integration. This will override the default validator if one configured.

        Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        result = self._values.get("validator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.CallbackObject",
    jsii_struct_bases=[Extensible],
    name_mapping={},
)
class CallbackObject(Extensible):
    def __init__(self) -> None:
        '''(experimental) A map of possible out-of band callbacks related to the parent operation.

        Each value in the map is a Path Item Object that describes a set of requests that may be initiated by the API provider and the expected responses. The key value used to identify the path item object is an expression, evaluated at runtime, that identifies a URL to use for the callback operation.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CallbackObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ComponentsObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "callbacks": "callbacks",
        "examples": "examples",
        "headers": "headers",
        "links": "links",
        "parameters": "parameters",
        "request_bodies": "requestBodies",
        "responses": "responses",
        "schemas": "schemas",
        "security_schemes": "securitySchemes",
    },
)
class ComponentsObject(Extensible):
    def __init__(
        self,
        *,
        callbacks: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[CallbackObject, typing.Dict[str, typing.Any]]]]] = None,
        examples: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union["ExampleObject", typing.Dict[str, typing.Any]]]]] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[HeaderObject, typing.Dict[str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[LinkObject, typing.Dict[str, typing.Any]]]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[ParameterObject, typing.Dict[str, typing.Any]]]]] = None,
        request_bodies: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[RequestBodyObject, typing.Dict[str, typing.Any]]]]] = None,
        responses: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[ResponseObject, typing.Dict[str, typing.Any]]]]] = None,
        schemas: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[SchemaObject, typing.Dict[str, typing.Any]]]]] = None,
        security_schemes: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[SecuritySchemeObject, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''(experimental) Holds a set of reusable objects for different aspects of the OAS.

        All objects defined within the components object will have no effect on the API unless they are explicitly referenced from properties outside the components object.

        :param callbacks: (experimental) An object to hold reusable Callback Objects.
        :param examples: (experimental) An object to hold reusable Example Objects.
        :param headers: (experimental) An object to hold reusable Header Objects.
        :param links: (experimental) An object to hold reusable Link Objects.
        :param parameters: (experimental) An object to hold reusable Parameter Objects.
        :param request_bodies: (experimental) An object to hold reusable Request Body Objects.
        :param responses: (experimental) An object to hold reusable Response Objects.
        :param schemas: (experimental) An object to hold reusable Schema Objects.
        :param security_schemes: (experimental) An object to hold reusable Security Scheme Objects.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                callbacks: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[CallbackObject, typing.Dict[str, typing.Any]]]]] = None,
                examples: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union["ExampleObject", typing.Dict[str, typing.Any]]]]] = None,
                headers: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[HeaderObject, typing.Dict[str, typing.Any]]]]] = None,
                links: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[LinkObject, typing.Dict[str, typing.Any]]]]] = None,
                parameters: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[ParameterObject, typing.Dict[str, typing.Any]]]]] = None,
                request_bodies: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[RequestBodyObject, typing.Dict[str, typing.Any]]]]] = None,
                responses: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[ResponseObject, typing.Dict[str, typing.Any]]]]] = None,
                schemas: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[SchemaObject, typing.Dict[str, typing.Any]]]]] = None,
                security_schemes: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[SecuritySchemeObject, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument callbacks", value=callbacks, expected_type=type_hints["callbacks"])
            check_type(argname="argument examples", value=examples, expected_type=type_hints["examples"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument request_bodies", value=request_bodies, expected_type=type_hints["request_bodies"])
            check_type(argname="argument responses", value=responses, expected_type=type_hints["responses"])
            check_type(argname="argument schemas", value=schemas, expected_type=type_hints["schemas"])
            check_type(argname="argument security_schemes", value=security_schemes, expected_type=type_hints["security_schemes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if callbacks is not None:
            self._values["callbacks"] = callbacks
        if examples is not None:
            self._values["examples"] = examples
        if headers is not None:
            self._values["headers"] = headers
        if links is not None:
            self._values["links"] = links
        if parameters is not None:
            self._values["parameters"] = parameters
        if request_bodies is not None:
            self._values["request_bodies"] = request_bodies
        if responses is not None:
            self._values["responses"] = responses
        if schemas is not None:
            self._values["schemas"] = schemas
        if security_schemes is not None:
            self._values["security_schemes"] = security_schemes

    @builtins.property
    def callbacks(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, CallbackObject]]]:
        '''(experimental) An object to hold reusable Callback Objects.

        :stability: experimental
        '''
        result = self._values.get("callbacks")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, CallbackObject]]], result)

    @builtins.property
    def examples(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, "ExampleObject"]]]:
        '''(experimental) An object to hold reusable Example Objects.

        :stability: experimental
        '''
        result = self._values.get("examples")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, "ExampleObject"]]], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, HeaderObject]]]:
        '''(experimental) An object to hold reusable Header Objects.

        :stability: experimental
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, HeaderObject]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, LinkObject]]]:
        '''(experimental) An object to hold reusable Link Objects.

        :stability: experimental
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, LinkObject]]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, ParameterObject]]]:
        '''(experimental) An object to hold reusable Parameter Objects.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, ParameterObject]]], result)

    @builtins.property
    def request_bodies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, RequestBodyObject]]]:
        '''(experimental) An object to hold reusable Request Body Objects.

        :stability: experimental
        '''
        result = self._values.get("request_bodies")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, RequestBodyObject]]], result)

    @builtins.property
    def responses(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, ResponseObject]]]:
        '''(experimental) An object to hold reusable Response Objects.

        :stability: experimental
        '''
        result = self._values.get("responses")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, ResponseObject]]], result)

    @builtins.property
    def schemas(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, SchemaObject]]]:
        '''(experimental) An object to hold reusable Schema Objects.

        :stability: experimental
        '''
        result = self._values.get("schemas")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, SchemaObject]]], result)

    @builtins.property
    def security_schemes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, SecuritySchemeObject]]]:
        '''(experimental) An object to hold reusable Security Scheme Objects.

        :stability: experimental
        '''
        result = self._values.get("security_schemes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, SecuritySchemeObject]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComponentsObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ContactObject",
    jsii_struct_bases=[Extensible],
    name_mapping={"email": "email", "name": "name", "url": "url"},
)
class ContactObject(Extensible):
    def __init__(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) The contact information for the exposed API.

        :param email: (experimental) The email address of the contact person/organization. MUST be in the format of an email address.
        :param name: (experimental) The identifying name of the contact person/organization.
        :param url: (experimental) The URL pointing to the contact information. MUST be in the format of a URL.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                email: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                url: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if name is not None:
            self._values["name"] = name
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''(experimental) The email address of the contact person/organization.

        MUST be in the format of an email address.

        :stability: experimental
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The identifying name of the contact person/organization.

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL pointing to the contact information.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CorsIntegration(
    Integration,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.CorsIntegration",
):
    '''(experimental) Defines ``OPTIONS`` integration used in Cross-Origin Resource Sharing (CORS).

    :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html#mapping-response-parameters
    :stability: experimental
    :srikanth650: /use-api-gateway-with-mock-integration-to-allow-cors-from-multiple-origins-bdcb431d07d3
    '''

    def __init__(
        self,
        _: constructs.Construct,
        *,
        headers: builtins.str,
        methods: builtins.str,
        origins: builtins.str,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Defines ``OPTIONS`` integration used in Cross-Origin Resource Sharing (CORS).

        :param _: -
        :param headers: 
        :param methods: 
        :param origins: 
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental

        Example::

            '/bar': {
              'OPTIONS': new openapix.CorsIntegration(this, {
                headers: 'Content-Type,X-Amz-Date,Authorization',
                origins: '*',
                methods: 'OPTIONS,GET',
              }),
            },
        '''
        if __debug__:
            def stub(
                _: constructs.Construct,
                *,
                headers: builtins.str,
                methods: builtins.str,
                origins: builtins.str,
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
        props = CorsIntegrationProps(
            headers=headers, methods=methods, origins=origins, validator=validator
        )

        jsii.create(self.__class__, self, [_, props])


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.CorsIntegrationProps",
    jsii_struct_bases=[ValidatorConfig],
    name_mapping={
        "validator": "validator",
        "headers": "headers",
        "methods": "methods",
        "origins": "origins",
    },
)
class CorsIntegrationProps(ValidatorConfig):
    def __init__(
        self,
        *,
        validator: typing.Optional[builtins.str] = None,
        headers: builtins.str,
        methods: builtins.str,
        origins: builtins.str,
    ) -> None:
        '''
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.
        :param headers: 
        :param methods: 
        :param origins: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                validator: typing.Optional[builtins.str] = None,
                headers: builtins.str,
                methods: builtins.str,
                origins: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validator", value=validator, expected_type=type_hints["validator"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument methods", value=methods, expected_type=type_hints["methods"])
            check_type(argname="argument origins", value=origins, expected_type=type_hints["origins"])
        self._values: typing.Dict[str, typing.Any] = {
            "headers": headers,
            "methods": methods,
            "origins": origins,
        }
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def validator(self) -> typing.Optional[builtins.str]:
        '''(experimental) Validator identifier for method integration. This will override the default validator if one configured.

        Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        result = self._values.get("validator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("headers")
        assert result is not None, "Required property 'headers' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def methods(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("methods")
        assert result is not None, "Required property 'methods' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origins(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("origins")
        assert result is not None, "Required property 'origins' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CorsIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.DiscriminatorObject",
    jsii_struct_bases=[Extensible],
    name_mapping={"property_name": "propertyName", "mapping": "mapping"},
)
class DiscriminatorObject(Extensible):
    def __init__(
        self,
        *,
        property_name: builtins.str,
        mapping: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''(experimental) When request bodies or response payloads may be one of a number of different schemas, a discriminator object can be used to aid in serialization, deserialization, and validation.

        The discriminator is a specific object in a schema which is used to inform the consumer of the specification of an alternative schema based on the value associated with it. When using the discriminator, inline schemas will not be considered.

        :param property_name: (experimental) The name of the property in the payload that will hold the discriminator value.
        :param mapping: (experimental) An object to hold mappings between payload values and schema names or references.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                property_name: builtins.str,
                mapping: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument property_name", value=property_name, expected_type=type_hints["property_name"])
            check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
        self._values: typing.Dict[str, typing.Any] = {
            "property_name": property_name,
        }
        if mapping is not None:
            self._values["mapping"] = mapping

    @builtins.property
    def property_name(self) -> builtins.str:
        '''(experimental) The name of the property in the payload that will hold the discriminator value.

        :stability: experimental
        '''
        result = self._values.get("property_name")
        assert result is not None, "Required property 'property_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) An object to hold mappings between payload values and schema names or references.

        :stability: experimental
        '''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiscriminatorObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.EncodingObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "allow_reserved": "allowReserved",
        "content_type": "contentType",
        "explode": "explode",
        "headers": "headers",
        "style": "style",
    },
)
class EncodingObject(Extensible):
    def __init__(
        self,
        *,
        allow_reserved: typing.Optional[builtins.bool] = None,
        content_type: typing.Optional[builtins.str] = None,
        explode: typing.Optional[builtins.bool] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[HeaderObject, typing.Dict[str, typing.Any]]]]] = None,
        style: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) A single encoding definition applied to a single schema property.

        :param allow_reserved: (experimental) Determines whether the parameter value SHOULD allow reserved characters, as defined by RFC3986 :/?#[]@!$&'()*+,;= to be included without percent-encoding. The default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.
        :param content_type: (experimental) The Content-Type for encoding a specific property. Default value depends on the property type: for string with format being binary – application/octet-stream; for other primitive types – text/plain; for object - application/json; for array – the default is defined based on the inner type. The value can be a specific media type (e.g. application/json), a wildcard media type (e.g. image/*), or a comma-separated list of the two types.
        :param explode: (experimental) When this is true, property values of type array or object generate separate parameters for each value of the array, or key-value-pair of the map. For other types of properties this property has no effect. When style is form, the default value is true. For all other styles, the default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.
        :param headers: (experimental) A map allowing additional information to be provided as headers, for example Content-Disposition. Content-Type is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body media type is not a multipart.
        :param style: (experimental) Describes how a specific property value will be serialized depending on its type. See Parameter Object for details on the style property. The behavior follows the same values as query parameters, including default values. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                allow_reserved: typing.Optional[builtins.bool] = None,
                content_type: typing.Optional[builtins.str] = None,
                explode: typing.Optional[builtins.bool] = None,
                headers: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Union[ReferenceObject, typing.Dict[str, typing.Any]], typing.Union[HeaderObject, typing.Dict[str, typing.Any]]]]] = None,
                style: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_reserved", value=allow_reserved, expected_type=type_hints["allow_reserved"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument explode", value=explode, expected_type=type_hints["explode"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument style", value=style, expected_type=type_hints["style"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_reserved is not None:
            self._values["allow_reserved"] = allow_reserved
        if content_type is not None:
            self._values["content_type"] = content_type
        if explode is not None:
            self._values["explode"] = explode
        if headers is not None:
            self._values["headers"] = headers
        if style is not None:
            self._values["style"] = style

    @builtins.property
    def allow_reserved(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether the parameter value SHOULD allow reserved characters, as defined by RFC3986 :/?#[]@!$&'()*+,;= to be included without percent-encoding. The default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        result = self._values.get("allow_reserved")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) The Content-Type for encoding a specific property.

        Default value depends on the property type: for string with format being binary – application/octet-stream; for other primitive types – text/plain; for object - application/json; for array – the default is defined based on the inner type. The value can be a specific media type (e.g. application/json), a wildcard media type (e.g. image/*), or a comma-separated list of the two types.

        :stability: experimental
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def explode(self) -> typing.Optional[builtins.bool]:
        '''(experimental) When this is true, property values of type array or object generate separate parameters for each value of the array, or key-value-pair of the map.

        For other types of properties this property has no effect. When style is form, the default value is true. For all other styles, the default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        result = self._values.get("explode")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, HeaderObject]]]:
        '''(experimental) A map allowing additional information to be provided as headers, for example Content-Disposition.

        Content-Type is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body media type is not a multipart.

        :stability: experimental
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[ReferenceObject, HeaderObject]]], result)

    @builtins.property
    def style(self) -> typing.Optional[builtins.str]:
        '''(experimental) Describes how a specific property value will be serialized depending on its type.

        See Parameter Object for details on the style property. The behavior follows the same values as query parameters, including default values. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        result = self._values.get("style")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncodingObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.ExampleObject",
    jsii_struct_bases=[Extensible],
    name_mapping={
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ExampleObject(Extensible):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Any = None,
    ) -> None:
        '''(experimental) Example Object.

        :param description: (experimental) Long description for the example. CommonMark syntax MAY be used for rich text representation.
        :param external_value: (experimental) A URL that points to the literal example. This provides the capability to reference examples that cannot easily be included in JSON or YAML documents. The value field and externalValue field are mutually exclusive.
        :param summary: (experimental) Short description for the example.
        :param value: (experimental) Embedded literal example. The value field and externalValue field are mutually exclusive. To represent examples of media types that cannot naturally represented in JSON or YAML, use a string value to contain the example, escaping where necessary.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                description: typing.Optional[builtins.str] = None,
                external_value: typing.Optional[builtins.str] = None,
                summary: typing.Optional[builtins.str] = None,
                value: typing.Any = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Long description for the example.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL that points to the literal example.

        This provides the capability to reference examples that cannot easily be included in JSON or YAML documents. The value field and externalValue field are mutually exclusive.

        :stability: experimental
        '''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) Short description for the example.

        :stability: experimental
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Any:
        '''(experimental) Embedded literal example.

        The value field and externalValue field are mutually exclusive. To represent examples of media types that cannot naturally represented in JSON or YAML, use a string value to contain the example, escaping where necessary.

        :stability: experimental
        '''
        result = self._values.get("value")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExampleObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpIntegration(
    Integration,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/openapix.HttpIntegration",
):
    '''(experimental) Defines a HTTP(S) integration.

    :stability: experimental
    '''

    def __init__(
        self,
        _: constructs.Construct,
        url: builtins.str,
        *,
        http_method: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
        proxy: typing.Optional[builtins.bool] = None,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Defines a HTTP(S) integration.

        :param _: -
        :param url: -
        :param http_method: HTTP method to use when invoking the backend URL. Default: GET
        :param options: Integration options, such as request/resopnse mapping, content handling, etc. Default: defaults based on ``IntegrationOptions`` defaults
        :param proxy: Determines whether to use proxy integration or custom integration. Default: true
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental

        Example::

            '/ext': {
              'ANY': new openapix.HttpIntegration(this, "https://example.com"),
            },
        '''
        if __debug__:
            def stub(
                _: constructs.Construct,
                url: builtins.str,
                *,
                http_method: typing.Optional[builtins.str] = None,
                options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
                proxy: typing.Optional[builtins.bool] = None,
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        props = HttpIntegrationProps(
            http_method=http_method, options=options, proxy=proxy, validator=validator
        )

        jsii.create(self.__class__, self, [_, url, props])


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.HttpIntegrationProps",
    jsii_struct_bases=[aws_cdk.aws_apigateway.HttpIntegrationProps, ValidatorConfig],
    name_mapping={
        "http_method": "httpMethod",
        "options": "options",
        "proxy": "proxy",
        "validator": "validator",
    },
)
class HttpIntegrationProps(
    aws_cdk.aws_apigateway.HttpIntegrationProps,
    ValidatorConfig,
):
    def __init__(
        self,
        *,
        http_method: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
        proxy: typing.Optional[builtins.bool] = None,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_method: HTTP method to use when invoking the backend URL. Default: GET
        :param options: Integration options, such as request/resopnse mapping, content handling, etc. Default: defaults based on ``IntegrationOptions`` defaults
        :param proxy: Determines whether to use proxy integration or custom integration. Default: true
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        if isinstance(options, dict):
            options = aws_cdk.aws_apigateway.IntegrationOptions(**options)
        if __debug__:
            def stub(
                *,
                http_method: typing.Optional[builtins.str] = None,
                options: typing.Optional[typing.Union[aws_cdk.aws_apigateway.IntegrationOptions, typing.Dict[str, typing.Any]]] = None,
                proxy: typing.Optional[builtins.bool] = None,
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument validator", value=validator, expected_type=type_hints["validator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_method is not None:
            self._values["http_method"] = http_method
        if options is not None:
            self._values["options"] = options
        if proxy is not None:
            self._values["proxy"] = proxy
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''HTTP method to use when invoking the backend URL.

        :default: GET
        '''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[aws_cdk.aws_apigateway.IntegrationOptions]:
        '''Integration options, such as request/resopnse mapping, content handling, etc.

        :default: defaults based on ``IntegrationOptions`` defaults
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.IntegrationOptions], result)

    @builtins.property
    def proxy(self) -> typing.Optional[builtins.bool]:
        '''Determines whether to use proxy integration or custom integration.

        :default: true
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validator(self) -> typing.Optional[builtins.str]:
        '''(experimental) Validator identifier for method integration. This will override the default validator if one configured.

        Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        result = self._values.get("validator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@alma-cdk/openapix.ICallbackObject")
class ICallbackObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) A map of possible out-of band callbacks related to the parent operation.

    Each value in the map is a Path Item Object that describes a set of requests that may be initiated by the API provider and the expected responses. The key value used to identify the path item object is an expression, evaluated at runtime, that identifies a URL to use for the callback operation.

    :stability: experimental
    '''

    pass


class _ICallbackObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) A map of possible out-of band callbacks related to the parent operation.

    Each value in the map is a Path Item Object that describes a set of requests that may be initiated by the API provider and the expected responses. The key value used to identify the path item object is an expression, evaluated at runtime, that identifies a URL to use for the callback operation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.ICallbackObject"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICallbackObject).__jsii_proxy_class__ = lambda : _ICallbackObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IComponentsObject")
class IComponentsObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Holds a set of reusable objects for different aspects of the OAS.

    All objects defined within the components object will have no effect on the API unless they are explicitly referenced from properties outside the components object.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="callbacks")
    def callbacks(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ICallbackObject]]]:
        '''(experimental) An object to hold reusable Callback Objects.

        :stability: experimental
        '''
        ...

    @callbacks.setter
    def callbacks(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ICallbackObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="examples")
    def examples(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, "IExampleObject"]]]:
        '''(experimental) An object to hold reusable Example Objects.

        :stability: experimental
        '''
        ...

    @examples.setter
    def examples(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, "IExampleObject"]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]]:
        '''(experimental) An object to hold reusable Header Objects.

        :stability: experimental
        '''
        ...

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]]:
        '''(experimental) An object to hold reusable Link Objects.

        :stability: experimental
        '''
        ...

    @links.setter
    def links(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IParameterObject]]]:
        '''(experimental) An object to hold reusable Parameter Objects.

        :stability: experimental
        '''
        ...

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IParameterObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="requestBodies")
    def request_bodies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IRequestBodyObject]]]:
        '''(experimental) An object to hold reusable Request Body Objects.

        :stability: experimental
        '''
        ...

    @request_bodies.setter
    def request_bodies(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IRequestBodyObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="responses")
    def responses(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IResponseObject]]]:
        '''(experimental) An object to hold reusable Response Objects.

        :stability: experimental
        '''
        ...

    @responses.setter
    def responses(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IResponseObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="schemas")
    def schemas(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISchemaObject]]]:
        '''(experimental) An object to hold reusable Schema Objects.

        :stability: experimental
        '''
        ...

    @schemas.setter
    def schemas(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISchemaObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="securitySchemes")
    def security_schemes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISecuritySchemeObject]]]:
        '''(experimental) An object to hold reusable Security Scheme Objects.

        :stability: experimental
        '''
        ...

    @security_schemes.setter
    def security_schemes(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISecuritySchemeObject]]],
    ) -> None:
        ...


class _IComponentsObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Holds a set of reusable objects for different aspects of the OAS.

    All objects defined within the components object will have no effect on the API unless they are explicitly referenced from properties outside the components object.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IComponentsObject"

    @builtins.property
    @jsii.member(jsii_name="callbacks")
    def callbacks(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ICallbackObject]]]:
        '''(experimental) An object to hold reusable Callback Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ICallbackObject]]], jsii.get(self, "callbacks"))

    @callbacks.setter
    def callbacks(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ICallbackObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ICallbackObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callbacks", value)

    @builtins.property
    @jsii.member(jsii_name="examples")
    def examples(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, "IExampleObject"]]]:
        '''(experimental) An object to hold reusable Example Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, "IExampleObject"]]], jsii.get(self, "examples"))

    @examples.setter
    def examples(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, "IExampleObject"]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, "IExampleObject"]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "examples", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]]:
        '''(experimental) An object to hold reusable Header Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]], jsii.get(self, "headers"))

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]]:
        '''(experimental) An object to hold reusable Link Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]], jsii.get(self, "links"))

    @links.setter
    def links(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ILinkObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "links", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IParameterObject]]]:
        '''(experimental) An object to hold reusable Parameter Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IParameterObject]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IParameterObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IParameterObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="requestBodies")
    def request_bodies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IRequestBodyObject]]]:
        '''(experimental) An object to hold reusable Request Body Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IRequestBodyObject]]], jsii.get(self, "requestBodies"))

    @request_bodies.setter
    def request_bodies(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IRequestBodyObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IRequestBodyObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestBodies", value)

    @builtins.property
    @jsii.member(jsii_name="responses")
    def responses(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IResponseObject]]]:
        '''(experimental) An object to hold reusable Response Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IResponseObject]]], jsii.get(self, "responses"))

    @responses.setter
    def responses(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IResponseObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IResponseObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responses", value)

    @builtins.property
    @jsii.member(jsii_name="schemas")
    def schemas(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISchemaObject]]]:
        '''(experimental) An object to hold reusable Schema Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISchemaObject]]], jsii.get(self, "schemas"))

    @schemas.setter
    def schemas(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISchemaObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISchemaObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemas", value)

    @builtins.property
    @jsii.member(jsii_name="securitySchemes")
    def security_schemes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISecuritySchemeObject]]]:
        '''(experimental) An object to hold reusable Security Scheme Objects.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISecuritySchemeObject]]], jsii.get(self, "securitySchemes"))

    @security_schemes.setter
    def security_schemes(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISecuritySchemeObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, ISecuritySchemeObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securitySchemes", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComponentsObject).__jsii_proxy_class__ = lambda : _IComponentsObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IContactObject")
class IContactObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) The contact information for the exposed API.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.Optional[builtins.str]:
        '''(experimental) The email address of the contact person/organization.

        MUST be in the format of an email address.

        :stability: experimental
        '''
        ...

    @email.setter
    def email(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The identifying name of the contact person/organization.

        :stability: experimental
        '''
        ...

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL pointing to the contact information.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        ...

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IContactObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) The contact information for the exposed API.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IContactObject"

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.Optional[builtins.str]:
        '''(experimental) The email address of the contact person/organization.

        MUST be in the format of an email address.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The identifying name of the contact person/organization.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL pointing to the contact information.

        MUST be in the format of a URL.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "url"))

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactObject).__jsii_proxy_class__ = lambda : _IContactObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IDiscriminatorObject")
class IDiscriminatorObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) When request bodies or response payloads may be one of a number of different schemas, a discriminator object can be used to aid in serialization, deserialization, and validation.

    The discriminator is a specific object in a schema which is used to inform the consumer of the specification of an alternative schema based on the value associated with it. When using the discriminator, inline schemas will not be considered.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="propertyName")
    def property_name(self) -> builtins.str:
        '''(experimental) The name of the property in the payload that will hold the discriminator value.

        :stability: experimental
        '''
        ...

    @property_name.setter
    def property_name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) An object to hold mappings between payload values and schema names or references.

        :stability: experimental
        '''
        ...

    @mapping.setter
    def mapping(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        ...


class _IDiscriminatorObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) When request bodies or response payloads may be one of a number of different schemas, a discriminator object can be used to aid in serialization, deserialization, and validation.

    The discriminator is a specific object in a schema which is used to inform the consumer of the specification of an alternative schema based on the value associated with it. When using the discriminator, inline schemas will not be considered.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IDiscriminatorObject"

    @builtins.property
    @jsii.member(jsii_name="propertyName")
    def property_name(self) -> builtins.str:
        '''(experimental) The name of the property in the payload that will hold the discriminator value.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "propertyName"))

    @property_name.setter
    def property_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyName", value)

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) An object to hold mappings between payload values and schema names or references.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "mapping"))

    @mapping.setter
    def mapping(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiscriminatorObject).__jsii_proxy_class__ = lambda : _IDiscriminatorObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IDocument")
class IDocument(IExtensible, typing_extensions.Protocol):
    '''(experimental) Describes a mutable OpenApi v3 Document.

    Essentially the same as ``SchemaProps`` but without ``readonly`` definitions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> IInfoObject:
        '''(experimental) Provides metadata about the API.

        The metadata MAY be used by tooling as required.

        :stability: experimental

        Example::

            {
              title: "FancyPants API",
              version: "1.23.105",
            }
        '''
        ...

    @info.setter
    def info(self, value: IInfoObject) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="openapi")
    def openapi(self) -> builtins.str:
        '''(experimental) This string MUST be the semantic version number of the OpenAPI Specification version that the OpenAPI document uses.

        The openapi field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is not related to the API info.version string.

        :stability: experimental

        Example::

            '3.0.0'
        '''
        ...

    @openapi.setter
    def openapi(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> IPathsObject:
        '''(experimental) The available paths and operations for the API.

        :stability: experimental
        '''
        ...

    @paths.setter
    def paths(self, value: IPathsObject) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(self) -> typing.Optional[IComponentsObject]:
        '''(experimental) An element to hold various schemas for the specification.

        :stability: experimental
        '''
        ...

    @components.setter
    def components(self, value: typing.Optional[IComponentsObject]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation.

        :stability: experimental
        '''
        ...

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> typing.Optional[typing.List[ISecurityRequirementObject]]:
        '''(experimental) A declaration of which security mechanisms can be used across the API.

        The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement ({}) can be included in the array.

        :stability: experimental
        '''
        ...

    @security.setter
    def security(
        self,
        value: typing.Optional[typing.List[ISecurityRequirementObject]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="servers")
    def servers(self) -> typing.Optional[typing.List[IServerObject]]:
        '''(experimental) An array of Server Objects, which provide connectivity information to a target server.

        If the servers property is not provided, or is an empty array, the default value would be a Server Object with a url value of /.

        :stability: experimental
        '''
        ...

    @servers.setter
    def servers(self, value: typing.Optional[typing.List[IServerObject]]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[ITagObject]]:
        '''(experimental) A list of tags used by the specification with additional metadata.

        The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique.

        :stability: experimental
        '''
        ...

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[ITagObject]]) -> None:
        ...


class _IDocumentProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Describes a mutable OpenApi v3 Document.

    Essentially the same as ``SchemaProps`` but without ``readonly`` definitions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IDocument"

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> IInfoObject:
        '''(experimental) Provides metadata about the API.

        The metadata MAY be used by tooling as required.

        :stability: experimental

        Example::

            {
              title: "FancyPants API",
              version: "1.23.105",
            }
        '''
        return typing.cast(IInfoObject, jsii.get(self, "info"))

    @info.setter
    def info(self, value: IInfoObject) -> None:
        if __debug__:
            def stub(value: IInfoObject) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "info", value)

    @builtins.property
    @jsii.member(jsii_name="openapi")
    def openapi(self) -> builtins.str:
        '''(experimental) This string MUST be the semantic version number of the OpenAPI Specification version that the OpenAPI document uses.

        The openapi field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is not related to the API info.version string.

        :stability: experimental

        Example::

            '3.0.0'
        '''
        return typing.cast(builtins.str, jsii.get(self, "openapi"))

    @openapi.setter
    def openapi(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openapi", value)

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> IPathsObject:
        '''(experimental) The available paths and operations for the API.

        :stability: experimental
        '''
        return typing.cast(IPathsObject, jsii.get(self, "paths"))

    @paths.setter
    def paths(self, value: IPathsObject) -> None:
        if __debug__:
            def stub(value: IPathsObject) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paths", value)

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(self) -> typing.Optional[IComponentsObject]:
        '''(experimental) An element to hold various schemas for the specification.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IComponentsObject], jsii.get(self, "components"))

    @components.setter
    def components(self, value: typing.Optional[IComponentsObject]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IComponentsObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="externalDocs")
    def external_docs(self) -> typing.Optional[IExternalDocumentationObject]:
        '''(experimental) Additional external documentation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IExternalDocumentationObject], jsii.get(self, "externalDocs"))

    @external_docs.setter
    def external_docs(
        self,
        value: typing.Optional[IExternalDocumentationObject],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[IExternalDocumentationObject]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalDocs", value)

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> typing.Optional[typing.List[ISecurityRequirementObject]]:
        '''(experimental) A declaration of which security mechanisms can be used across the API.

        The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement ({}) can be included in the array.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[ISecurityRequirementObject]], jsii.get(self, "security"))

    @security.setter
    def security(
        self,
        value: typing.Optional[typing.List[ISecurityRequirementObject]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.List[ISecurityRequirementObject]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "security", value)

    @builtins.property
    @jsii.member(jsii_name="servers")
    def servers(self) -> typing.Optional[typing.List[IServerObject]]:
        '''(experimental) An array of Server Objects, which provide connectivity information to a target server.

        If the servers property is not provided, or is an empty array, the default value would be a Server Object with a url value of /.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[IServerObject]], jsii.get(self, "servers"))

    @servers.setter
    def servers(self, value: typing.Optional[typing.List[IServerObject]]) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[IServerObject]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servers", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[ITagObject]]:
        '''(experimental) A list of tags used by the specification with additional metadata.

        The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[ITagObject]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[ITagObject]]) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[ITagObject]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDocument).__jsii_proxy_class__ = lambda : _IDocumentProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IEncodingObject")
class IEncodingObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) A single encoding definition applied to a single schema property.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="allowReserved")
    def allow_reserved(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether the parameter value SHOULD allow reserved characters, as defined by RFC3986 :/?#[]@!$&'()*+,;= to be included without percent-encoding. The default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        ...

    @allow_reserved.setter
    def allow_reserved(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) The Content-Type for encoding a specific property.

        Default value depends on the property type: for string with format being binary – application/octet-stream; for other primitive types – text/plain; for object - application/json; for array – the default is defined based on the inner type. The value can be a specific media type (e.g. application/json), a wildcard media type (e.g. image/*), or a comma-separated list of the two types.

        :stability: experimental
        '''
        ...

    @content_type.setter
    def content_type(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="explode")
    def explode(self) -> typing.Optional[builtins.bool]:
        '''(experimental) When this is true, property values of type array or object generate separate parameters for each value of the array, or key-value-pair of the map.

        For other types of properties this property has no effect. When style is form, the default value is true. For all other styles, the default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        ...

    @explode.setter
    def explode(self, value: typing.Optional[builtins.bool]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]]:
        '''(experimental) A map allowing additional information to be provided as headers, for example Content-Disposition.

        Content-Type is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body media type is not a multipart.

        :stability: experimental
        '''
        ...

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="style")
    def style(self) -> typing.Optional[builtins.str]:
        '''(experimental) Describes how a specific property value will be serialized depending on its type.

        See Parameter Object for details on the style property. The behavior follows the same values as query parameters, including default values. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        ...

    @style.setter
    def style(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IEncodingObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) A single encoding definition applied to a single schema property.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IEncodingObject"

    @builtins.property
    @jsii.member(jsii_name="allowReserved")
    def allow_reserved(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines whether the parameter value SHOULD allow reserved characters, as defined by RFC3986 :/?#[]@!$&'()*+,;= to be included without percent-encoding. The default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "allowReserved"))

    @allow_reserved.setter
    def allow_reserved(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowReserved", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) The Content-Type for encoding a specific property.

        Default value depends on the property type: for string with format being binary – application/octet-stream; for other primitive types – text/plain; for object - application/json; for array – the default is defined based on the inner type. The value can be a specific media type (e.g. application/json), a wildcard media type (e.g. image/*), or a comma-separated list of the two types.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="explode")
    def explode(self) -> typing.Optional[builtins.bool]:
        '''(experimental) When this is true, property values of type array or object generate separate parameters for each value of the array, or key-value-pair of the map.

        For other types of properties this property has no effect. When style is form, the default value is true. For all other styles, the default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "explode"))

    @explode.setter
    def explode(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "explode", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]]:
        '''(experimental) A map allowing additional information to be provided as headers, for example Content-Disposition.

        Content-Type is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body media type is not a multipart.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]], jsii.get(self, "headers"))

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Mapping[builtins.str, typing.Union[IReferenceObject, IHeaderObject]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="style")
    def style(self) -> typing.Optional[builtins.str]:
        '''(experimental) Describes how a specific property value will be serialized depending on its type.

        See Parameter Object for details on the style property. The behavior follows the same values as query parameters, including default values. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "style"))

    @style.setter
    def style(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "style", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEncodingObject).__jsii_proxy_class__ = lambda : _IEncodingObjectProxy


@jsii.interface(jsii_type="@alma-cdk/openapix.IExampleObject")
class IExampleObject(IExtensible, typing_extensions.Protocol):
    '''(experimental) Example Object.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Long description for the example.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL that points to the literal example.

        This provides the capability to reference examples that cannot easily be included in JSON or YAML documents. The value field and externalValue field are mutually exclusive.

        :stability: experimental
        '''
        ...

    @external_value.setter
    def external_value(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) Short description for the example.

        :stability: experimental
        '''
        ...

    @summary.setter
    def summary(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Embedded literal example.

        The value field and externalValue field are mutually exclusive. To represent examples of media types that cannot naturally represented in JSON or YAML, use a string value to contain the example, escaping where necessary.

        :stability: experimental
        '''
        ...

    @value.setter
    def value(self, value: typing.Any) -> None:
        ...


class _IExampleObjectProxy(
    jsii.proxy_for(IExtensible), # type: ignore[misc]
):
    '''(experimental) Example Object.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/openapix.IExampleObject"

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Long description for the example.

        CommonMark syntax MAY be used for rich text representation.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> typing.Optional[builtins.str]:
        '''(experimental) A URL that points to the literal example.

        This provides the capability to reference examples that cannot easily be included in JSON or YAML documents. The value field and externalValue field are mutually exclusive.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> typing.Optional[builtins.str]:
        '''(experimental) Short description for the example.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Embedded literal example.

        The value field and externalValue field are mutually exclusive. To represent examples of media types that cannot naturally represented in JSON or YAML, use a string value to contain the example, escaping where necessary.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.Any) -> None:
        if __debug__:
            def stub(value: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExampleObject).__jsii_proxy_class__ = lambda : _IExampleObjectProxy


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.IntegrationConfig",
    jsii_struct_bases=[ValidatorConfig],
    name_mapping={"validator": "validator", "type": "type"},
)
class IntegrationConfig(ValidatorConfig):
    def __init__(
        self,
        *,
        validator: typing.Optional[builtins.str] = None,
        type: InternalIntegrationType,
    ) -> None:
        '''(experimental) Base integration config.

        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.
        :param type: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                validator: typing.Optional[builtins.str] = None,
                type: InternalIntegrationType,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validator", value=validator, expected_type=type_hints["validator"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def validator(self) -> typing.Optional[builtins.str]:
        '''(experimental) Validator identifier for method integration. This will override the default validator if one configured.

        Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        result = self._values.get("validator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> InternalIntegrationType:
        '''
        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(InternalIntegrationType, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.LambdaIntegrationOptions",
    jsii_struct_bases=[
        aws_cdk.aws_apigateway.LambdaIntegrationOptions, ValidatorConfig
    ],
    name_mapping={
        "cache_key_parameters": "cacheKeyParameters",
        "cache_namespace": "cacheNamespace",
        "connection_type": "connectionType",
        "content_handling": "contentHandling",
        "credentials_passthrough": "credentialsPassthrough",
        "credentials_role": "credentialsRole",
        "integration_responses": "integrationResponses",
        "passthrough_behavior": "passthroughBehavior",
        "request_parameters": "requestParameters",
        "request_templates": "requestTemplates",
        "timeout": "timeout",
        "vpc_link": "vpcLink",
        "allow_test_invoke": "allowTestInvoke",
        "proxy": "proxy",
        "validator": "validator",
    },
)
class LambdaIntegrationOptions(
    aws_cdk.aws_apigateway.LambdaIntegrationOptions,
    ValidatorConfig,
):
    def __init__(
        self,
        *,
        cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_namespace: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
        content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
        credentials_passthrough: typing.Optional[builtins.bool] = None,
        credentials_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        integration_responses: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_apigateway.IntegrationResponse, typing.Dict[str, typing.Any]]]] = None,
        passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc_link: typing.Optional[aws_cdk.aws_apigateway.IVpcLink] = None,
        allow_test_invoke: typing.Optional[builtins.bool] = None,
        proxy: typing.Optional[builtins.bool] = None,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cache_key_parameters: A list of request parameters whose values are to be cached. It determines request parameters that will make it into the cache key.
        :param cache_namespace: An API-specific tag group of related cached parameters.
        :param connection_type: The type of network connection to the integration endpoint. Default: - ConnectionType.VPC_LINK if ``vpcLink`` property is configured; ConnectionType.Internet otherwise.
        :param content_handling: Specifies how to handle request payload content type conversions. Default: none if this property isn't defined, the request payload is passed through from the method request to the integration request without modification, provided that the ``passthroughBehaviors`` property is configured to support payload pass-through.
        :param credentials_passthrough: Requires that the caller's identity be passed through from the request. Default: Caller identity is not passed through
        :param credentials_role: An IAM role that API Gateway assumes. Mutually exclusive with ``credentialsPassThrough``. Default: A role is not assumed
        :param integration_responses: The response that API Gateway provides after a method's backend completes processing a request. API Gateway intercepts the response from the backend so that you can control how API Gateway surfaces backend responses. For example, you can map the backend status codes to codes that you define.
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
        :param request_parameters: The request parameters that API Gateway sends with the backend request. Specify request parameters as key-value pairs (string-to-string mappings), with a destination as the key and a source as the value. Specify the destination by using the following pattern integration.request.location.name, where location is querystring, path, or header, and name is a valid, unique parameter name. The source must be an existing method request parameter or a static value. You must enclose static values in single quotation marks and pre-encode these values based on their destination in the request.
        :param request_templates: A map of Apache Velocity templates that are applied on the request payload. The template that API Gateway uses is based on the value of the Content-Type header that's sent by the client. The content type value is the key, and the template is the value (specified as a string), such as the following snippet:: { "application/json": "{ \\"statusCode\\": 200 }" }
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)
        :param vpc_link: The VpcLink used for the integration. Required if connectionType is VPC_LINK
        :param allow_test_invoke: Allow invoking method from AWS Console UI (for testing purposes). This will add another permission to the AWS Lambda resource policy which will allow the ``test-invoke-stage`` stage to invoke this handler. If this is set to ``false``, the function will only be usable from the deployment endpoint. Default: true
        :param proxy: Use proxy integration or normal (request/response mapping) integration. Default: true
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
                cache_namespace: typing.Optional[builtins.str] = None,
                connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
                content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
                credentials_passthrough: typing.Optional[builtins.bool] = None,
                credentials_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                integration_responses: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_apigateway.IntegrationResponse, typing.Dict[str, typing.Any]]]] = None,
                passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
                request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc_link: typing.Optional[aws_cdk.aws_apigateway.IVpcLink] = None,
                allow_test_invoke: typing.Optional[builtins.bool] = None,
                proxy: typing.Optional[builtins.bool] = None,
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cache_key_parameters", value=cache_key_parameters, expected_type=type_hints["cache_key_parameters"])
            check_type(argname="argument cache_namespace", value=cache_namespace, expected_type=type_hints["cache_namespace"])
            check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
            check_type(argname="argument content_handling", value=content_handling, expected_type=type_hints["content_handling"])
            check_type(argname="argument credentials_passthrough", value=credentials_passthrough, expected_type=type_hints["credentials_passthrough"])
            check_type(argname="argument credentials_role", value=credentials_role, expected_type=type_hints["credentials_role"])
            check_type(argname="argument integration_responses", value=integration_responses, expected_type=type_hints["integration_responses"])
            check_type(argname="argument passthrough_behavior", value=passthrough_behavior, expected_type=type_hints["passthrough_behavior"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument request_templates", value=request_templates, expected_type=type_hints["request_templates"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc_link", value=vpc_link, expected_type=type_hints["vpc_link"])
            check_type(argname="argument allow_test_invoke", value=allow_test_invoke, expected_type=type_hints["allow_test_invoke"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument validator", value=validator, expected_type=type_hints["validator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cache_key_parameters is not None:
            self._values["cache_key_parameters"] = cache_key_parameters
        if cache_namespace is not None:
            self._values["cache_namespace"] = cache_namespace
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if content_handling is not None:
            self._values["content_handling"] = content_handling
        if credentials_passthrough is not None:
            self._values["credentials_passthrough"] = credentials_passthrough
        if credentials_role is not None:
            self._values["credentials_role"] = credentials_role
        if integration_responses is not None:
            self._values["integration_responses"] = integration_responses
        if passthrough_behavior is not None:
            self._values["passthrough_behavior"] = passthrough_behavior
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if request_templates is not None:
            self._values["request_templates"] = request_templates
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc_link is not None:
            self._values["vpc_link"] = vpc_link
        if allow_test_invoke is not None:
            self._values["allow_test_invoke"] = allow_test_invoke
        if proxy is not None:
            self._values["proxy"] = proxy
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def cache_key_parameters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of request parameters whose values are to be cached.

        It determines
        request parameters that will make it into the cache key.
        '''
        result = self._values.get("cache_key_parameters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_namespace(self) -> typing.Optional[builtins.str]:
        '''An API-specific tag group of related cached parameters.'''
        result = self._values.get("cache_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[aws_cdk.aws_apigateway.ConnectionType]:
        '''The type of network connection to the integration endpoint.

        :default: - ConnectionType.VPC_LINK if ``vpcLink`` property is configured; ConnectionType.Internet otherwise.
        '''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.ConnectionType], result)

    @builtins.property
    def content_handling(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.ContentHandling]:
        '''Specifies how to handle request payload content type conversions.

        :default:

        none if this property isn't defined, the request payload is passed
        through from the method request to the integration request without
        modification, provided that the ``passthroughBehaviors`` property is
        configured to support payload pass-through.
        '''
        result = self._values.get("content_handling")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.ContentHandling], result)

    @builtins.property
    def credentials_passthrough(self) -> typing.Optional[builtins.bool]:
        '''Requires that the caller's identity be passed through from the request.

        :default: Caller identity is not passed through
        '''
        result = self._values.get("credentials_passthrough")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def credentials_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''An IAM role that API Gateway assumes.

        Mutually exclusive with ``credentialsPassThrough``.

        :default: A role is not assumed
        '''
        result = self._values.get("credentials_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def integration_responses(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_apigateway.IntegrationResponse]]:
        '''The response that API Gateway provides after a method's backend completes processing a request.

        API Gateway intercepts the response from the
        backend so that you can control how API Gateway surfaces backend
        responses. For example, you can map the backend status codes to codes
        that you define.
        '''
        result = self._values.get("integration_responses")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_apigateway.IntegrationResponse]], result)

    @builtins.property
    def passthrough_behavior(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior]:
        '''Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource.

        There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and
        NEVER.
        '''
        result = self._values.get("passthrough_behavior")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior], result)

    @builtins.property
    def request_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The request parameters that API Gateway sends with the backend request.

        Specify request parameters as key-value pairs (string-to-string
        mappings), with a destination as the key and a source as the value.

        Specify the destination by using the following pattern
        integration.request.location.name, where location is querystring, path,
        or header, and name is a valid, unique parameter name.

        The source must be an existing method request parameter or a static
        value. You must enclose static values in single quotation marks and
        pre-encode these values based on their destination in the request.
        '''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_templates(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of Apache Velocity templates that are applied on the request payload.

        The template that API Gateway uses is based on the value of the
        Content-Type header that's sent by the client. The content type value is
        the key, and the template is the value (specified as a string), such as
        the following snippet::

              { "application/json": "{ \\"statusCode\\": 200 }" }

        :see: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html
        '''
        result = self._values.get("request_templates")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''The maximum amount of time an integration will run before it returns without a response.

        Must be between 50 milliseconds and 29 seconds.

        :default: Duration.seconds(29)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc_link(self) -> typing.Optional[aws_cdk.aws_apigateway.IVpcLink]:
        '''The VpcLink used for the integration.

        Required if connectionType is VPC_LINK
        '''
        result = self._values.get("vpc_link")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.IVpcLink], result)

    @builtins.property
    def allow_test_invoke(self) -> typing.Optional[builtins.bool]:
        '''Allow invoking method from AWS Console UI (for testing purposes).

        This will add another permission to the AWS Lambda resource policy which
        will allow the ``test-invoke-stage`` stage to invoke this handler. If this
        is set to ``false``, the function will only be usable from the deployment
        endpoint.

        :default: true
        '''
        result = self._values.get("allow_test_invoke")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def proxy(self) -> typing.Optional[builtins.bool]:
        '''Use proxy integration or normal (request/response mapping) integration.

        :default: true

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validator(self) -> typing.Optional[builtins.str]:
        '''(experimental) Validator identifier for method integration. This will override the default validator if one configured.

        Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        result = self._values.get("validator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaIntegrationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.MockIntegrationProps",
    jsii_struct_bases=[aws_cdk.aws_apigateway.IntegrationOptions, ValidatorConfig],
    name_mapping={
        "cache_key_parameters": "cacheKeyParameters",
        "cache_namespace": "cacheNamespace",
        "connection_type": "connectionType",
        "content_handling": "contentHandling",
        "credentials_passthrough": "credentialsPassthrough",
        "credentials_role": "credentialsRole",
        "integration_responses": "integrationResponses",
        "passthrough_behavior": "passthroughBehavior",
        "request_parameters": "requestParameters",
        "request_templates": "requestTemplates",
        "timeout": "timeout",
        "vpc_link": "vpcLink",
        "validator": "validator",
    },
)
class MockIntegrationProps(aws_cdk.aws_apigateway.IntegrationOptions, ValidatorConfig):
    def __init__(
        self,
        *,
        cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_namespace: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
        content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
        credentials_passthrough: typing.Optional[builtins.bool] = None,
        credentials_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        integration_responses: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_apigateway.IntegrationResponse, typing.Dict[str, typing.Any]]]] = None,
        passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc_link: typing.Optional[aws_cdk.aws_apigateway.IVpcLink] = None,
        validator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cache_key_parameters: A list of request parameters whose values are to be cached. It determines request parameters that will make it into the cache key.
        :param cache_namespace: An API-specific tag group of related cached parameters.
        :param connection_type: The type of network connection to the integration endpoint. Default: - ConnectionType.VPC_LINK if ``vpcLink`` property is configured; ConnectionType.Internet otherwise.
        :param content_handling: Specifies how to handle request payload content type conversions. Default: none if this property isn't defined, the request payload is passed through from the method request to the integration request without modification, provided that the ``passthroughBehaviors`` property is configured to support payload pass-through.
        :param credentials_passthrough: Requires that the caller's identity be passed through from the request. Default: Caller identity is not passed through
        :param credentials_role: An IAM role that API Gateway assumes. Mutually exclusive with ``credentialsPassThrough``. Default: A role is not assumed
        :param integration_responses: The response that API Gateway provides after a method's backend completes processing a request. API Gateway intercepts the response from the backend so that you can control how API Gateway surfaces backend responses. For example, you can map the backend status codes to codes that you define.
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
        :param request_parameters: The request parameters that API Gateway sends with the backend request. Specify request parameters as key-value pairs (string-to-string mappings), with a destination as the key and a source as the value. Specify the destination by using the following pattern integration.request.location.name, where location is querystring, path, or header, and name is a valid, unique parameter name. The source must be an existing method request parameter or a static value. You must enclose static values in single quotation marks and pre-encode these values based on their destination in the request.
        :param request_templates: A map of Apache Velocity templates that are applied on the request payload. The template that API Gateway uses is based on the value of the Content-Type header that's sent by the client. The content type value is the key, and the template is the value (specified as a string), such as the following snippet:: { "application/json": "{ \\"statusCode\\": 200 }" }
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)
        :param vpc_link: The VpcLink used for the integration. Required if connectionType is VPC_LINK
        :param validator: (experimental) Validator identifier for method integration. This will override the default validator if one configured. Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
                cache_namespace: typing.Optional[builtins.str] = None,
                connection_type: typing.Optional[aws_cdk.aws_apigateway.ConnectionType] = None,
                content_handling: typing.Optional[aws_cdk.aws_apigateway.ContentHandling] = None,
                credentials_passthrough: typing.Optional[builtins.bool] = None,
                credentials_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                integration_responses: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_apigateway.IntegrationResponse, typing.Dict[str, typing.Any]]]] = None,
                passthrough_behavior: typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior] = None,
                request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc_link: typing.Optional[aws_cdk.aws_apigateway.IVpcLink] = None,
                validator: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cache_key_parameters", value=cache_key_parameters, expected_type=type_hints["cache_key_parameters"])
            check_type(argname="argument cache_namespace", value=cache_namespace, expected_type=type_hints["cache_namespace"])
            check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
            check_type(argname="argument content_handling", value=content_handling, expected_type=type_hints["content_handling"])
            check_type(argname="argument credentials_passthrough", value=credentials_passthrough, expected_type=type_hints["credentials_passthrough"])
            check_type(argname="argument credentials_role", value=credentials_role, expected_type=type_hints["credentials_role"])
            check_type(argname="argument integration_responses", value=integration_responses, expected_type=type_hints["integration_responses"])
            check_type(argname="argument passthrough_behavior", value=passthrough_behavior, expected_type=type_hints["passthrough_behavior"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument request_templates", value=request_templates, expected_type=type_hints["request_templates"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc_link", value=vpc_link, expected_type=type_hints["vpc_link"])
            check_type(argname="argument validator", value=validator, expected_type=type_hints["validator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cache_key_parameters is not None:
            self._values["cache_key_parameters"] = cache_key_parameters
        if cache_namespace is not None:
            self._values["cache_namespace"] = cache_namespace
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if content_handling is not None:
            self._values["content_handling"] = content_handling
        if credentials_passthrough is not None:
            self._values["credentials_passthrough"] = credentials_passthrough
        if credentials_role is not None:
            self._values["credentials_role"] = credentials_role
        if integration_responses is not None:
            self._values["integration_responses"] = integration_responses
        if passthrough_behavior is not None:
            self._values["passthrough_behavior"] = passthrough_behavior
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if request_templates is not None:
            self._values["request_templates"] = request_templates
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc_link is not None:
            self._values["vpc_link"] = vpc_link
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def cache_key_parameters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of request parameters whose values are to be cached.

        It determines
        request parameters that will make it into the cache key.
        '''
        result = self._values.get("cache_key_parameters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_namespace(self) -> typing.Optional[builtins.str]:
        '''An API-specific tag group of related cached parameters.'''
        result = self._values.get("cache_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[aws_cdk.aws_apigateway.ConnectionType]:
        '''The type of network connection to the integration endpoint.

        :default: - ConnectionType.VPC_LINK if ``vpcLink`` property is configured; ConnectionType.Internet otherwise.
        '''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.ConnectionType], result)

    @builtins.property
    def content_handling(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.ContentHandling]:
        '''Specifies how to handle request payload content type conversions.

        :default:

        none if this property isn't defined, the request payload is passed
        through from the method request to the integration request without
        modification, provided that the ``passthroughBehaviors`` property is
        configured to support payload pass-through.
        '''
        result = self._values.get("content_handling")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.ContentHandling], result)

    @builtins.property
    def credentials_passthrough(self) -> typing.Optional[builtins.bool]:
        '''Requires that the caller's identity be passed through from the request.

        :default: Caller identity is not passed through
        '''
        result = self._values.get("credentials_passthrough")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def credentials_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''An IAM role that API Gateway assumes.

        Mutually exclusive with ``credentialsPassThrough``.

        :default: A role is not assumed
        '''
        result = self._values.get("credentials_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def integration_responses(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_apigateway.IntegrationResponse]]:
        '''The response that API Gateway provides after a method's backend completes processing a request.

        API Gateway intercepts the response from the
        backend so that you can control how API Gateway surfaces backend
        responses. For example, you can map the backend status codes to codes
        that you define.
        '''
        result = self._values.get("integration_responses")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_apigateway.IntegrationResponse]], result)

    @builtins.property
    def passthrough_behavior(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior]:
        '''Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource.

        There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and
        NEVER.
        '''
        result = self._values.get("passthrough_behavior")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.PassthroughBehavior], result)

    @builtins.property
    def request_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The request parameters that API Gateway sends with the backend request.

        Specify request parameters as key-value pairs (string-to-string
        mappings), with a destination as the key and a source as the value.

        Specify the destination by using the following pattern
        integration.request.location.name, where location is querystring, path,
        or header, and name is a valid, unique parameter name.

        The source must be an existing method request parameter or a static
        value. You must enclose static values in single quotation marks and
        pre-encode these values based on their destination in the request.
        '''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_templates(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of Apache Velocity templates that are applied on the request payload.

        The template that API Gateway uses is based on the value of the
        Content-Type header that's sent by the client. The content type value is
        the key, and the template is the value (specified as a string), such as
        the following snippet::

              { "application/json": "{ \\"statusCode\\": 200 }" }

        :see: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html
        '''
        result = self._values.get("request_templates")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''The maximum amount of time an integration will run before it returns without a response.

        Must be between 50 milliseconds and 29 seconds.

        :default: Duration.seconds(29)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc_link(self) -> typing.Optional[aws_cdk.aws_apigateway.IVpcLink]:
        '''The VpcLink used for the integration.

        Required if connectionType is VPC_LINK
        '''
        result = self._values.get("vpc_link")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.IVpcLink], result)

    @builtins.property
    def validator(self) -> typing.Optional[builtins.str]:
        '''(experimental) Validator identifier for method integration. This will override the default validator if one configured.

        Should match a key from OpenApi schema ``components.securitySchemas``.

        :stability: experimental
        '''
        result = self._values.get("validator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MockIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@alma-cdk/openapix.Validator",
    jsii_struct_bases=[XAmazonApigatewayRequestValidator],
    name_mapping={
        "validate_request_body": "validateRequestBody",
        "validate_request_parameters": "validateRequestParameters",
        "default": "default",
    },
)
class Validator(XAmazonApigatewayRequestValidator):
    def __init__(
        self,
        *,
        validate_request_body: builtins.bool,
        validate_request_parameters: builtins.bool,
        default: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Validator configuration.

        :param validate_request_body: 
        :param validate_request_parameters: 
        :param default: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                validate_request_body: builtins.bool,
                validate_request_parameters: builtins.bool,
                default: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validate_request_body", value=validate_request_body, expected_type=type_hints["validate_request_body"])
            check_type(argname="argument validate_request_parameters", value=validate_request_parameters, expected_type=type_hints["validate_request_parameters"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {
            "validate_request_body": validate_request_body,
            "validate_request_parameters": validate_request_parameters,
        }
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def validate_request_body(self) -> builtins.bool:
        '''
        :stability: experimental
        '''
        result = self._values.get("validate_request_body")
        assert result is not None, "Required property 'validate_request_body' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def validate_request_parameters(self) -> builtins.bool:
        '''
        :stability: experimental
        '''
        result = self._values.get("validate_request_parameters")
        assert result is not None, "Required property 'validate_request_parameters' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Validator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Api",
    "ApiBaseProps",
    "ApiProps",
    "AuthorizerConfig",
    "AuthorizerExtensions",
    "AwsIntegration",
    "AwsIntegrationProps",
    "CallbackObject",
    "CognitoUserPoolsAuthorizer",
    "CognitoUserPoolsAuthorizerProps",
    "ComponentsObject",
    "ContactObject",
    "CorsIntegration",
    "CorsIntegrationProps",
    "DiscriminatorObject",
    "EncodingObject",
    "ExampleObject",
    "Extensible",
    "ExternalDocumentationObject",
    "HeaderObject",
    "HttpIntegration",
    "HttpIntegrationProps",
    "IBaseIntegration",
    "ICallbackObject",
    "IComponentsObject",
    "IContactObject",
    "IDiscriminatorObject",
    "IDocument",
    "IEncodingObject",
    "IExampleObject",
    "IExtensible",
    "IExternalDocumentationObject",
    "IHeaderObject",
    "IInfoObject",
    "ILicenseObject",
    "ILinkObject",
    "IMediaTypeObject",
    "IOAuthFlowObject",
    "IOAuthFlowsObject",
    "IOperationObject",
    "IParameterObject",
    "IPathItemObject",
    "IPathsObject",
    "IReferenceObject",
    "IRequestBodyObject",
    "IResponseObject",
    "IResponsesObject",
    "ISchemaObject",
    "ISecurityRequirementObject",
    "ISecuritySchemeObject",
    "IServerObject",
    "IServerVariableObject",
    "ITagObject",
    "IXmlObject",
    "InfoObject",
    "Integration",
    "IntegrationConfig",
    "InternalIntegrationType",
    "LambdaAuthorizer",
    "LambdaAuthorizerProps",
    "LambdaIntegration",
    "LambdaIntegrationOptions",
    "LicenseObject",
    "LinkObject",
    "MediaTypeObject",
    "MockIntegration",
    "MockIntegrationProps",
    "OAuthFlowObject",
    "OAuthFlowsObject",
    "OperationObject",
    "ParameterObject",
    "PathItemObject",
    "Paths",
    "PathsObject",
    "ReferenceObject",
    "RequestBodyObject",
    "ResponseObject",
    "ResponsesObject",
    "Schema",
    "SchemaObject",
    "SchemaProps",
    "SecurityRequirementObject",
    "SecuritySchemeObject",
    "ServerObject",
    "ServerVariableObject",
    "TagObject",
    "Validator",
    "ValidatorConfig",
    "XAmazonApigatewayAuthorizer",
    "XAmazonApigatewayIntegration",
    "XAmazonApigatewayIntegrationRequestParameters",
    "XAmazonApigatewayIntegrationRequestTemplates",
    "XAmazonApigatewayIntegrationResponse",
    "XAmazonApigatewayIntegrationResponseParameters",
    "XAmazonApigatewayIntegrationResponseTemplates",
    "XAmazonApigatewayIntegrationResponses",
    "XAmazonApigatewayIntegrationTlsConfig",
    "XAmazonApigatewayRequestValidator",
    "XmlObject",
]

publication.publish()
