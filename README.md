# Run Blazemeter Test Action

This action allows you to run Blazemeter existing Test

## Inputs

## `apikey`
**Required** The API key of Blazemeter.
## `apisecret`
**Required** The API secret of Blazemeter.
## `testid`
**Required** The Test Id of Blazemeter.



## Example usage

uses: actions/DockerAction@v1
with:
   apikey: 'xxx'
   apisecret: 'xxx'
   testid: 'xxx'