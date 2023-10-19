### Note: 

The release process is done through Jenkins pipeline (https://blazect-jenkins.blazemeter.com/view/blazerunner-plugins/job/github-action-release) which usages github token. \

***The token expires on 19/10/2024. Please renew it in advance*** \

To renew the githhub token follow the link - https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens \

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
## Example
**1. Run Existing Test**
```
uses: BlazeRunner-BZR/Github-Action@v8.1
with:
   apiKey: ""
   apiSecret: ""
   testID: ""
```
**2. Create New Test**
```
uses: BlazeRunner-BZR/Github-Action@v8.1
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
uses: BlazeRunner-BZR/Github-Action@v8.1
with:
   apiKey: ""
   apiSecret: ""
   testID: ""
   webhookURL : ""
   continuePipeline: "false"
 ```
