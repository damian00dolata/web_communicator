PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY,
    roomId TEXT,
    name TEXT,
    maxUsers INTEGER,
    isTemporary INTEGER
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT,
    isLogged INTEGER
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    clientName TEXT,
    message TEXT,
    roomId INTEGER,
    date TIMESTAMP,
    FOREIGN KEY (roomId) REFERENCES rooms (id)
);
