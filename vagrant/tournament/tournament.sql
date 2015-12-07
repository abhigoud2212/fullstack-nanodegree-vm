-- Table definitions for the tournament project.
--
-- Delete database if it exists
DROP DATABASE IF EXISTS tournament;

-- Create tournament database
CREATE DATABASE tournament;

-- connect to database
\c tournament;

-- table for storing players
CREATE TABLE players (id serial primary key,
                     name varchar(40) not null
                     );

-- table for store match details
CREATE TABLE matches (match_id serial primary key,
                     winner integer references players(id) not null,
                     loser integer references players(id) not null
                     );

-- VIEW to display id, name, Total wins, Total matches
CREATE VIEW standings AS select players.id, players.name,
                         (select count(matches.winner) from
                         matches where players.id = matches.winner)
                         as wins,
                         (select count(matches.match_id) from matches
                         where players.id = matches.winner
                         or players.id = matches.loser)
                         as total_matches
                         from players
                         order by wins desc, total_matches desc;
