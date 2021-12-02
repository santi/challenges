CREATE TABLE points (id SERIAL PRIMARY KEY, name TEXT, location GEOGRAPHY);
CREATE INDEX points_location_gix
  ON points
  USING GIST (location);
CREATE INDEX points_location_idx
  ON points (location);


CREATE FUNCTION read_file(file TEXT) RETURNS VOID AS
$$
DECLARE
    content TEXT[];
    line TEXT[];
    index INTEGER;

BEGIN
content := regexp_split_to_array(pg_read_file(file), E'\\n');

index := 2;
WHILE index < array_upper(content, 1) LOOP

    line := regexp_split_to_array(content[index], ',');
    INSERT INTO points (name, location) VALUES (line[1], ('SRID=4326;' || line[array_upper(line, 1)])::GEOGRAPHY);

    index := index + 1;
END LOOP;

END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION closest_point (point GEOGRAPHY) RETURNS GEOGRAPHY AS
$$
    SELECT location
    FROM points
    ORDER BY location <-> point
    LIMIT 1
$$ LANGUAGE SQL ;


CREATE FUNCTION santa_distance () RETURNS BIGINT AS 
$$
DECLARE
    travelled DOUBLE PRECISION := 0.0;
    position GEOGRAPHY := 'SRID=4326;POINT(0 90)'::GEOGRAPHY;
    closest GEOGRAPHY;

BEGIN
    WHILE (SELECT count(*) FROM points) > 0 LOOP
        closest := closest_point(position);
        travelled := travelled + ST_Distance(position, closest, false);

        DELETE FROM points WHERE location = closest;
        position := closest;
    END LOOP;

    travelled := travelled + ST_Distance(position, 'SRID=4326;POINT(0 90)'::geography, false);


    RETURN (travelled / 1000)::bigint; 
END
$$ LANGUAGE plpgsql;


select read_file('/tmp/cities.csv');
select santa_distance();
