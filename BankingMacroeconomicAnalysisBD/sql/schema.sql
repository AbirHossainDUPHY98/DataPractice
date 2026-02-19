-- ===================================================
-- DIMENSION TABLES
-- ===================================================

-- Time dimension
CREATE TABLE IF NOT EXISTS dim_time (
    time_id SERIAL PRIMARY KEY,
    year INT UNIQUE NOT NULL
);

-- Indicator dimension
CREATE TABLE IF NOT EXISTS dim_indicator (
    indicator_id SERIAL PRIMARY KEY,
    indicator_code TEXT UNIQUE NOT NULL,
    indicator_name TEXT NOT NULL,
    domain TEXT NOT NULL  -- 'macro' or 'banking'
);

-- Source dimension
CREATE TABLE IF NOT EXISTS dim_source (
    source_id SERIAL PRIMARY KEY,
    source_name TEXT UNIQUE NOT NULL
);

-- ===================================================
-- FACT TABLES
-- ===================================================

-- Macro indicators fact table
CREATE TABLE IF NOT EXISTS fact_macro (
    fact_id SERIAL PRIMARY KEY,
    time_id INT NOT NULL REFERENCES dim_time(time_id),
    indicator_id INT NOT NULL REFERENCES dim_indicator(indicator_id),
    value NUMERIC,
    source_id INT NOT NULL REFERENCES dim_source(source_id)
);

-- Banking indicators fact table
CREATE TABLE IF NOT EXISTS fact_banking (
    fact_id SERIAL PRIMARY KEY,
    time_id INT NOT NULL REFERENCES dim_time(time_id),
    indicator_id INT NOT NULL REFERENCES dim_indicator(indicator_id),
    value NUMERIC,
    source_id INT NOT NULL REFERENCES dim_source(source_id)
);

