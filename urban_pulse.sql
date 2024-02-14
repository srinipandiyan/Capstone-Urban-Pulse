\echo 'Delete and recreate ganzkorper db?'
\prompt 'Return for yes or control-C to cancel > ' foo

DROP DATABASE urban_pulse;
CREATE DATABASE urban_pulse;
\connect urban_pulse

\i urban_pulse_seed.sql

\echo 'Delete and recreate urban_pulse_test db?'
\prompt 'Return for yes or control-C to cancel > ' foo

DROP DATABASE urban_pulse_test ;
CREATE DATABASE urban_pulse_test ;
\connect urban_pulse_test

\i urban_pulse_schema.sql