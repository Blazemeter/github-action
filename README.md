# Blazemeter Action
This action allows you to run Blazemeter existing test and create a new test.
## Inputs
### `apiKey` **required**
- The API key of Blazemeter.
### `apiSecret` **required**
- The API secret key of Blazemeter.
### `testID`
- The Test ID of Blazemeter.
### `showTailLog`
- If **true**, shows a running log in real-time in the Github action console.
### `createTest`
- If **true**, creates a new test in BlazeMeter
### `testName`
- Name of the BlazeMeter Test
### `inputAllFiles`
- Used when uploading multiple files while creating or updating the test
### `inputStartFile`
- Used when uploading single start file while test creation
### `uploadFileCheck`
- When Used in conjunction with inputallfiles, this must be set to true
### `totalUsers`
- Number of target concurrent virtual users
### `duration`
- Time to hold target concurrency (in minutes)
### `projectID`
- BlazeMeter Project ID
### `rampUp`
- Ramp-up time to reach target concurrency (in minutes)
### `continuePipeline`
- When set to false, the pipeline waits until the test execution completes
### `multiTests`
- If the test being kicked off is a multi-test, this value must be set to true
### `functionalTest`
- If a functional test suite is being kicked off, this value must be set to true
### `modelData`
- Used in cases where the variables inside the Test Data Model need to be updated
### `envVariable`
- Used to update any variables in an existing Taurus .yaml file by passing key value pair
### `jmeterProperties`
- Used to add Jmeter Properties
### `reportName`
- Report Name in BlazeMeter
### `notes`
- Notes section of a given report in BlazeMeter
### `iterationsConfig`
- Run a test based on iterations and not duration
### `iterations`
- In case of iterations based test, set the number of iterations
### `testRunByTestName`
- Run a test by its name as opposed to its ID
### `ignoreSLA`
- When set to true, the job always returns a **Success**
### `webhookURL`
- Used when send microsoft teams notification for blazemeter test status
### `enablePublicReportURL`
- Used when send public report url through a microsoft teams notification
### `locations`
- Comma separated location IDs as String. Ex., "asia-east1-a,australia-southeast1-a". All supported locationIDs can be found at https://api.blazemeter.com/performance/#list-of-google-cloud-locations
- For Private locations(OPLs), use ID as "harbor-661f7af50d8f6f8f0d014359". Just append the 'harbor-' prefix to the ID of the OPL.
### `dedicatedIP`
- A boolean value defaulted to **false**. When set to **true**, dedicatedIPs will be used if available.

### `disableLoadConfig`

- Select this to disable load configuration for existing JMeter based test. Load configuration will be taken from the Script.

### `steps`

- You can configure your test to ramp up in steps. This is the number of steps to reach the total users. Default is disabled(empty field). To enable it, use any number greater than 0. Once enabled, use 0 to disable it.

### `throughput`

- You can limit the number of requests per second (RPS) for your test. Default is disabled(empty field). To enable it, use any number greater than 1. Once enabled, use 0 to disable it.

### `concurrencyControlEnabled`

- Select this to allow users to change no. of users at runtime. Default is false(empty field). Keep it selected to enable this option.

### `iterationsEnabled`

- Select this to use iterations instead of duration. If selected, iteration will be used not duration. If not selected, duration will be used.

## Example
**1. Run Existing Test**
```
uses: Blazemeter/github-action@v8.4
with:
   apiKey: ""
   apiSecret: ""
   testID: ""
```
**2. Create New Test**
```
uses: Blazemeter/github-action@v8.4
with:
   apiKey: ""
   apiSecret: ""
   createTest: ""
   inputStartFile: ""
   testName: ""
   projectID: "" 
 ```
**3. Send microsoft teams notification**
```
uses: Blazemeter/github-action@v8.4
with:
   apiKey: ""
   apiSecret: ""
   testID: ""
   webhookURL : ""
   continuePipeline: "false"
 ```
**4. Run Existing Test with load Parameter**

```
uses: BlazeRunner-BZR/Github-Action@v8
with:
   apiKey: 'xxx'
   apiSecret: 'xxx'
   testID: 'xxx'
   totalUsers: "31"
   duration: "7"
   rampUp: "2"
   steps: "2"
   throughput: "4"
   concurrencyControlEnabled: "true"
```

**5. Run Existing Test with disabled load Parameter(For JMETER test only)**

```
uses: BlazeRunner-BZR/Github-Action@v8
with:
   apiKey: 'xxx'
   apiSecret: 'xxx'
   testID: 'xxx'
   totalUsers: "31"
   disableLoadConfig: "true"
```

**6. Run Existing Test with iterations instead of duration**

```
uses: BlazeRunner-BZR/Github-Action@v8
with:
   apiKey: 'xxx'
   apiSecret: 'xxx'
   testID: 'xxx'
   iterationsEnabled: "true"
   iterations: "10"
```

**7. Create New Test with load parameters**

```
uses: BlazeRunner-BZR/Github-Action@v8
with:
   apiKey: 'xxx'
   apiSecret: 'xxx'
   createTest: 'xxx'
   inputStartFile: 'xxx'
   testName: 'xxx'
   projectID: 'xxxx'
   totalUsers: "31"
   duration: "7"
   rampUp: "2"
   steps: "2"
   throughput: "4"
   concurrencyControlEnabled: "true"
```

**8. Create New Test with disable load parameters**

```
uses: BlazeRunner-BZR/Github-Action@v8
with:
   apiKey: 'xxx'
   apiSecret: 'xxx'
   createTest: 'xxx'
   inputStartFile: 'xxx'
   testName: 'xxx'
   projectID: 'xxxx'
   disableLoadConfig: "true"
```
