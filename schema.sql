drop table if exists Person;
create table Person (
  id integer primary key autoincrement,
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
  name text primary key,
  rating real not null,
  person integer not null
);

