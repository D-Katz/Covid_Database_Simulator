PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS cds(
      cd_id text primary key not null, --cd unique id
      title text NOT NULL, --title of CD
      artist text NOT NULL, --artist whose CD it is or "various artists"
      producer text default NULL,
      year integer,
      contributer text --student number who contirbuted the data
      );

CREATE TABLE IF NOT EXISTS songs(
      song_id integer primary key not null, --auto incrementing key
      title text NOT NULL, --title of song
      composer text NOT NULL, --person or persons who wrote the song
      cd_id text NOT NULL, --cd this song appears on
      track integer NOT NULL, --track number of the song
      contributer text --student number who contirbuted the data
      );


DELETE FROM cds WHERE contributer="101157096";
DELETE FROM songs WHERE contributer="101157096";

INSERT INTO cds VALUES('101157096CD1','Discovery','Daft Punk','Thomas Bangalter, Guy-Manuel de Homem-Christo, Todd Edwards, Romanthony, DJ Sneak',2001,'101157096');
INSERT INTO cds VALUES('101157096CD2','Random Access Memories','Daft Punk','Thomas Bangalter, Guy-Manuel de Homem-Christo',2013,'101157096');

INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('One More Time','Thomas Bangalter, Guy-Manuel de Homem-Christo, Anthony Moore','101157096CD1',1,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Aerodynamic','Thomas Bangalter, Guy-Manuel de Homem-Christo','101157096CD1',2,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Digital Love','Thomas Bangalter, Guy-Manuel de Homem-Christo, Carlos Sosa, George Duke','101157096CD1',3,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Harder, Better, Faster, Stronger','Thomas Bangalter, Guy-Manuel de Homem-Christo, Edwin Birdsong','101157096CD1',4,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Crescendolls','Thomas Bangalter, Guy-Manuel de Homem-Christo, Dwight Brewster, Aleta Jennings','101157096CD1',5,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Nightvision','Thomas Bangalter, Guy-Manuel de Homem-Christo','101157096CD1',6,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Superheroes','Thomas Bangalter, Guy-Manuel de Homem-Christo, Barry Manilow, Marty Panzer','101157096CD1',7,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('High Life','Thomas Bangalter, Guy-Manuel de Homem-Christo','101157096CD1',8,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Something About Us','Thomas Bangalter, Guy-Manuel de Homem-Christo','101157096CD1',9,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Voyager','Thomas Bangalter, Guy-Manuel de Homem-Christo','101157096CD1',10,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Give Life Back to Music','Thomas Bangalter, Guy-Manuel de Homem-Christo, Paul Jackson Jr, Nile Rodgers','101157096CD2',1,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('The Game of Love','Thomas Bangalter, Guy-Manuel de Homem-Christo','101157096CD2',2,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Giorgio by Moroder','Thomas Bangalter, Guy-Manuel de Homem-Christo, Giovanni Moroder','101157096CD2',3,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Within','Thomas Bangalter, Guy-Manuel de Homem-Christo, Jason Beck','101157096CD2',4,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Instant Crush','Thomas Bangalter, Guy-Manuel de Homem-Christo, Julian Casablancas','101157096CD2',5,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Lose Yourself to Dance','Thomas Bangalter, Guy-Manuel de Homem-Christo, Nile Rodgers, Pharell Williams','101157096CD2',6,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Touch','Thomas Bangalter, Guy-Manuel de Homem-Christo, Christopher Paul Caswell, Paul Williams Jr','101157096CD2',7,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Get Lucky','Thomas Bangalter, Guy-Manuel de Homem-Christo, Pharrell Williams, Nile Rodgers','101157096CD2',8,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Beyond','Thomas Bangalter, Guy-Manuel de Homem-Christo, Paul Williams Jr, Christopher Paul Caswell','101157096CD2',9,'101157096');
INSERT INTO songs (title, composer, cd_id, track, contributer) VALUES('Motherboard','Thomas Bangalter, Guy-Manuel de Homem-Christo','101157096CD2',10,'101157096');
COMMIT;
