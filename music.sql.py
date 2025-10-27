-- Artists table
CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
-- Albums table
CREATE TABLE album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER,
    release_year INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);
-- Songs table
CREATE TABLE song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    album_id INTEGER,
    track_number INTEGER,
    length_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES album(id)
);
-- Sample data (optional)
INSERT INTO artist (name) VALUES ('Taylor Swift'), ('Drake'), ('Adele');
INSERT INTO album (name, artist_id, release_year) VALUES
('1989', 1, 2014),
('Views', 2, 2016),
('25', 3, 2015);
INSERT INTO song (name, album_id, track_number, length_seconds) VALUES
('Blank Space', 1, 2, 231),
('Style', 1, 3, 231),
('Hotline Bling', 2, 5, 267),
('One Dance', 2, 3, 173),
('Hello', 3, 1, 295),
('Send My Love', 3, 2, 223);
