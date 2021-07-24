-- Table Definition ----------------------------------------------

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email character varying NOT NULL UNIQUE,
    first_name character varying NOT NULL,
    last_name character varying,
    password character varying NOT NULL
);

CREATE TABLE revoked_tokens (
    id SERIAL PRIMARY KEY,
    jti character varying(120)
);