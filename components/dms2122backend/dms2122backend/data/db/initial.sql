BEGIN TRANSACTION;
CREATE TABLE Users (
        username VARCHAR(32),
        password VARCHAR(64) NOT NULL,
        PRIMARY KEY (username)
);

CREATE TABLE Question(
    id integer PRIMARY KEY,
    statement varchar(250),
    correctOption varchar(250),
    incorrectOptions varchar,
    score float,
    penalty float,
    public boolean,
    ncorrect integer,
    nanswered integer
);

CREATE TABLE AnsweredQuestion(
    idquestion integer, --FOREIGN KEY REFERENCES Question(id),
    iduser integer,
    answer varchar(250),
    score float,
    creation date,
    PRIMARY KEY(idquestion, iduser),
    FOREIGN KEY(idquestion) REFERENCES Question(id)
);

CREATE TABLE UserStats(
    iduser varchar(32) PRIMARY KEY REFERENCES Users(id),
    nanswered integer,
    ncorrect integer,
    score float
);

COMMIT;