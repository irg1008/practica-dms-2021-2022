- [DMS Backend service REST API](#dms-backend-service-rest-api)
  - [Version: 1.0](#version-10)
    - [/](#)
    - [/user/{username}/stats](#userusernamestats)
      - [GET](#get)
        - [Summary:](#summary)
        - [Parameters](#parameters)
        - [Responses](#responses)
        - [Security](#security)
    - [/user/teacher/students/stats](#userteacherstudentsstats)
      - [GET](#get-1)
        - [Summary:](#summary-1)
        - [Responses](#responses-1)
        - [Security](#security-1)
    - [/user/{username}/questions/answer/{id}](#userusernamequestionsanswerid)
      - [POST](#post)
        - [Summary:](#summary-2)
        - [Parameters](#parameters-1)
        - [Responses](#responses-2)
        - [Security](#security-2)
    - [/user/{username}/questions/answered](#userusernamequestionsanswered)
      - [GET](#get-2)
        - [Summary:](#summary-3)
        - [Parameters](#parameters-2)
        - [Responses](#responses-3)
        - [Security](#security-3)
    - [/user/{username}/questions/unanswered](#userusernamequestionsunanswered)
      - [GET](#get-3)
        - [Summary:](#summary-4)
        - [Parameters](#parameters-3)
        - [Responses](#responses-4)
        - [Security](#security-4)
    - [/question/all](#questionall)
      - [GET](#get-4)
        - [Summary:](#summary-5)
        - [Responses](#responses-5)
        - [Security](#security-5)
    - [/question/new](#questionnew)
      - [POST](#post-1)
        - [Summary:](#summary-6)
        - [Responses](#responses-6)
        - [Security](#security-6)
    - [/question/{id}](#questionid)
      - [GET](#get-5)
        - [Summary:](#summary-7)
        - [Parameters](#parameters-4)
        - [Responses](#responses-7)
        - [Security](#security-7)
      - [PATCH](#patch)
        - [Summary:](#summary-8)
        - [Parameters](#parameters-5)
        - [Responses](#responses-8)
        - [Security](#security-8)
    - [Models](#models)
      - [Question](#question)
      - [QuestionResponse](#questionresponse)
      - [AnsweredQuestionResponse](#answeredquestionresponse)
      - [UserStats](#userstats)


# DMS Backend service REST API
REST API for the backend service.

This is part of the mandatory exercise.

Diseño y Mantenimiento del Software. Grado en Ingeniería Informática, Universidad de Burgos, 2021-2022.


## Version: 1.0

**Contact information:**  
Universidad de Burgos  

### /

### /user/{username}/stats

#### GET
##### Summary:

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

### /user/teacher/students/stats

#### GET
##### Summary:

Gets each student answered stats

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

### /user/{username}/questions/answer/{id}

#### POST
##### Summary:

Sets the question answer

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| username | path |  | Yes | string |
| id | path |  | Yes | number |

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
##### Summary:

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
##### Summary:

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
##### Summary:

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
##### Summary:

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
##### Summary:

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
##### Summary:

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
| title | string |  | Yes |
| statement | string |  | Yes |
| correct_answer | string |  | Yes |
| incorrect_answers | [ string ] |  | Yes |
| image_url | string |  | Yes |
| score | number |  | Yes |
| penalty | number |  | Yes |
| public | boolean |  | No |

#### QuestionResponse

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | Yes |
| user_ans | object |  | Yes |

#### AnsweredQuestionResponse

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| answer | string |  | Yes |
| date | integer | UTC Unix Timestamp | Yes |

#### UserStats

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| user_id | integer |  | Yes |
| n_answered | integer |  | Yes |
| n_correct | integer |  | Yes |
| score | number |  | Yes |