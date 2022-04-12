-- user table
CREATE TABLE IF NOT EXISTS user(
      user_id text primary key not null, 
      name text, 
      password text , 
      address text ,
      sin integer,
      covid_status text
      );

CREATE TABLE IF NOT EXISTS store(
      store_id text primary key not null, 
      type text, 
      location text , 
      name text ,
      covid_status text
      );

CREATE TABLE IF NOT EXISTS hub(
      hub_id text primary key not null, 
      city text, 
      );