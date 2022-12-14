CREATE TABLE Persons (
    PersonID int NOT NULL PRIMARY KEY,
    LastName nvarchar(255),
    FirstName nvarchar(255),
    ContractAddress nvarchar(255)
);


CREATE TABLE Address (
    PersonID int NOT NULL PRIMARY KEY,
    Address1 nvarchar(255),
    Address2 nvarchar(255),
    Address3 nvarchar(255)
);

INSERT INTO Persons (PersonID, FirstName, LastName, ContractAddress)
VALUES (1, "Son", "Goku", ""),(2, "Son", "Gohan", "");

INSERT INTO Address (PersonID, Address1, Address2, Address3)
VALUES (1, "MushroomCity", "Earth", "Universe7"),(2, "SatanCity", "Earth", "Universe7");



UPDATE Persons P
JOIN Address A ON P.PersonID = A.PersonID
SET P.ContractAddress = CONCAT(A.Address1," ",A.Address2," ",A.Address3);


SELECT * FROM Persons