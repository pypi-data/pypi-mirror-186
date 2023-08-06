# Elasticstack Resource Provider

The Elasticstack Resource Provider lets you manage [Elasticstack](http://example.com) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @tonkean-public/pulumi-elasticstack
```

or `yarn`:

```bash
yarn add @tonkean-public/pulumi-elasticstack
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_elasticstack
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/tonkean/pulumi-elasticstack/sdk/go/...
```

## Configuration

Python example use:
```
import pulumi_elasticstack

pulumi_elasticstack.Provider(
    resource_name='test_Provider',
    elasticsearch=pulumi_elasticstack.ProviderElasticsearchArgs(
        username='USERNAME',
        password='PASSWORD',
        endpoints=['http://localhost:9200']
    )
)
```


## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/foo/api-docs/).
