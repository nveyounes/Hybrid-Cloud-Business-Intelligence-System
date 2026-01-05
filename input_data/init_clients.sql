
CREATE TABLE IF NOT EXISTS clients (
    ClientID INT PRIMARY KEY,
    NomClient VARCHAR(255),
    Pays VARCHAR(50),
    DateInscription DATE
);
TRUNCATE TABLE clients;
INSERT INTO clients (ClientID, NomClient, Pays, DateInscription) VALUES
(2001, 'John Doe', 'France', '2023-05-10'),
(2002, 'Jane Smith', 'USA', '2023-06-15'),
(2003, 'Carlos Garcia', 'Espagne', '2023-07-20');
