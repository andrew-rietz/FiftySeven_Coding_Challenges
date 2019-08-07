DROP TABLE IF EXISTS snippet;
DROP TABLE IF EXISTS users;


CREATE TABLE users(
  id        serial primary key,
  username  text unique not null,
  password  text not null
);

CREATE TABLE snippet(
  id        serial primary key,
  author_id integer not null,
  created   timestamp not null default current_timestamp,
  title     text not null,
  body      text not null,
  foreign key (author_id) references users (id)
);
