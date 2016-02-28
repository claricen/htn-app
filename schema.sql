drop table if exists Person;
create table Person (
  id integer primary key,
  name text not null,
  email text not null,
  company text not null,
  latitude real not null,
  longitude real null,
  phone text not null,
  picture text not null
);

drop table if exists Skills;
create table Skills (
  id integer primary key,
  name text not null,
  rating real not null,
  person integer not null,
  FOREIGN KEY(person) REFERENCES Person(id)
);

