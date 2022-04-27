# Blazemeter Action
This action allows you to run Blazemeter existing test and create a new test.
## Inputs
### `apikey` **required**
- The API key of Blazemeter.
### `apisecret` **required**
- The API secret key of Blazemeter.
### `testid`
- The Test Id of Blazemeter.
### `showtaillog`
- If **true**, shows a running log in real-time in the Github action console.
### `createtest`
- If **true**, creates a new test in BlazeMeter
### `testname`
- Name of the BlazeMeter Test
### `inputallfiles`
- Used when uploading multiple files while creating or updating the test
### `inputstartfile`
- Used when uploading single start file while test creation
### `Uploadfilechk`
- When Used in conjunction with inputallfiles, this must be set to true
### `totalusers`
- Number of target concurrent virtual users
### `duration`
- Time to hold target concurrency (in minutes)
### `projectid`
- BlazeMeter Project ID
### `rampup`
- Ramp-up time to reach target concurrency (in minutes)
### `ContinuePipeline`
- When set to false, the pipeline waits until the test execution completes
### `multitests`
- If the test being kicked off is a multi-test, this value must be set to true
### `functionaltest`
- If a functional test suite is being kicked off, this value must be set to true
### `modeldata`
- Used in cases where the variables inside the Test Data Model need to be updated
### `env_variable`
- Used to update any variables in an existing Taurus .yaml file by passing key value pair
### `jmeterproperties`
- Used to add Jmeter Properties
### `reportname`
- Report Name in BlazeMeter
### `note`
- Notes section of a given report in BlazeMeter
### `iterations_config`
- Run a test based on iterations and not duration
### `iterations`
- In case of iterations based test, set the number of iterations
### `testRunByTestName`
- Run a test by its name as opposed to its ID
### `ignoreSLA`
- When set to true, the job always returns a **Success**
### `webhookURL`
- Used when send microsoft teams notification for test start, internal report url, public report url, test end and test status
### `webhookMetaData`
- Used when send custom metadata through a microsoft teams notification
## Example
**1. Run Existing Test**
```
uses: BlazeRunner-BZR/Github-Action@v5
with:
   apikey: 'xxx'
   apisecret: 'xxx'
   testid: 'xxx'
```
**2. Create New Test**
```
uses: BlazeRunner-BZR/Github-Action@v5
with:
   apikey: 'xxx'
   apisecret: 'xxx'
   createtest: 'xxx'
   inputstartfile: 'xxx'
   testname: 'xxx'
   projectid: 'xxxx' 
 ```
