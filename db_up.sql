-- Begin the transaction
BEGIN;

-- Don't let just anyone connect to the database
REVOKE CONNECT ON DATABASE tmdb FROM PUBLIC;

-- Create the roles
CREATE ROLE application_service LOGIN PASSWORD 'password';
CREATE ROLE migration_service LOGIN PASSWORD 'password';

-- Privileges

-- General privileges
GRANT CONNECT ON DATABASE tmdb TO application_service;
GRANT CONNECT ON DATABASE tmdb TO migration_service;

-- Application service privileges
GRANT USAGE ON SCHEMA public TO application_service; 
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO application_service;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO application_service;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO application_service;

-- Migration service privileges
ALTER SCHEMA public OWNER TO migration_service;

-- For objects created in the future
ALTER DEFAULT PRIVILEGES FOR ROLE migration_service IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO application_service;
ALTER DEFAULT PRIVILEGES FOR ROLE migration_service IN SCHEMA public 
GRANT USAGE, SELECT ON SEQUENCES TO application_service;
ALTER DEFAULT PRIVILEGES FOR ROLE migration_service IN SCHEMA public
GRANT EXECUTE ON FUNCTIONS TO application_service;

-- End the transaction
COMMIT;

-- Run the script with psql (Assuming trust authentication):
-- psql -U postgres -f db_setup.sql -d (your database name)
