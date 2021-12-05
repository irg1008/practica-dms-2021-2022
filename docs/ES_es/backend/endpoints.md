
# DMS Backend service REST API

Diseño y Mantenimiento del Software. Grado en Ingeniería Informática, Universidad de Burgos, 2021-2022.

## Version: 1.0

**Contact information:**  
Universidad de Burgos  

### /

### /user/{username}/stats

#### GET
##### Summary

Gets the user stats

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| username | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Success fetch of user stats. |
| 400 | A user was not provided. |
| 403 | The user does not have the privileges to view the given user's stats. |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

### /user/{username}/questions/answer/{id}

#### GET
##### Summary

Gets the question answer

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| username | path |  | Yes | string |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Success fetch of user answer for specific question. |
| 400 | There was an error while getting the answer. |
| 403 | The requestor has no privilege to get the answer |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

#### POST
##### Summary

Sets the question answer

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| username | path |  | Yes | string |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Success set of user answer. |
| 400 | There was an error while setting the answer. |
| 403 | The requestor has no privilege to set the answer. |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

### /user/{username}/questions/answered

#### GET
##### Summary

Gets user answered questions

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| username | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | OK Response, returns user's answered questions |
| 400 | There was an error while getting the questions. |
| 403 | The requestor has no privilege to get the questions. |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

### /user/{username}/questions/unanswered

#### GET
##### Summary

Gets user unanswered questions

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| username | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | OK Response, returns user's unanswered questions |
| 400 | There was an error while getting the questions. |
| 403 | The requestor has no privilege to get the questions. |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

### /question/all

#### GET
##### Summary

Retrieves every single stored questions (This should be paginated)

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Question Lis |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

### /question/new

#### POST
##### Summary

Creates a new question

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | OK Response, returns the question ID |
| 400 | There was an error while creating the question. |
| 403 | The requestor has no privilege to add a question. |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

### /question/{id}

#### GET
##### Summary

Gets a question by ID

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | number |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | OK Response, returns the question ID |
| 400 | There was an error while creating the question. |
| 403 | The requestor has no privilege to add a question. |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

#### PATCH
##### Summary

Updates a question by ID

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | A test message |

##### Security

| Security Schema | Scopes |
| --- | --- |
| user_token | |
| api_key | |

### Models

#### Question

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| title | string | Question title | Yes |
| statement | string | Question answer | Yes |
| correct_answer | string | Statement correct answer | Yes |
| incorrect_answers | [ string ] | String for the json with the incorrect answers | Yes |
| image_url | string | Question image | No |
| score | number | Correct answer score | Yes |
| penalty | number | Incorrect answers penalty | Yes |
| public | boolean | Question privacity status | No |

#### QuestionResponse

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer | Question id | Yes |
| user_ans | object | User answer | Yes |

#### AnsweredQuestionResponse

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| answer | string | User answer | Yes |
| date | integer | UTC Unix Timestamp | Yes |

#### UserStats

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| user_id | integer | User id | Yes |
| n_answered | integer | Number of answered questions | Yes |
| n_correct | integer | Number of correct answered questions | Yes |
| score | number | Total score of answered questions | Yes |
