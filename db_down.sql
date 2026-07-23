-- DROP DATABASE can't run inside of a transation block
DROP DATABASE tmdb;

BEGIN;

DROP ROLE application_service;
DROP ROLE migration_service;
DROP TYPE status;

COMMIT;
-- Run this with: psql -U postgres -d postgres -f db_setdown.sql
