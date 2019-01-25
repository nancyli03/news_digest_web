CREATE DATABASE news ENCODING="utf8";
GRANT ALL PRIVILEGES ON DATABASE "news" to docker;
\c news;
CREATE TABLE IF NOT EXISTS sina_news (
    title character varying(255) NOT NULL,
    url character varying(255),
    timestamp timestamp default current_timestamp
);
