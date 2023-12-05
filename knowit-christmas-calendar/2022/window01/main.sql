CREATE TABLE inp (
	value TEXT NOT NULL
);

CREATE TABLE dictionary (
	shona TEXT NOT NULL,
	english TEXT NOT NULL
);

CREATE INDEX dictionary_shona_idx ON dictionary(shona);

WITH RECURSIVE trans(shona_letter, english_letter) AS (
		SELECT value, NULL FROM letter
	UNION ALL 
	   	SELECT
	   		substring(shona_letter, length(shona) + 1, length(shona_letter)),
	   		CASE 
	   			WHEN english_letter IS NOT NULL THEN english_letter || ' ' || english
	   			ELSE english
	   		END
  	   	FROM trans
  	   		LEFT JOIN LATERAL (
  	   			-- Find the next word, picking the longest word if there are multiple options
  	   			SELECT shona, english
  	   			FROM dictionary
  	   			WHERE shona_letter LIKE shona || '%'
  	   			ORDER BY length(shona) DESC
  	   			LIMIT 1
			) AS next_word on (shona_letter LIKE shona || '%')
		WHERE length(shona_letter) > 0
)
SELECT MAX(LENGTH(english_letter)) AS english_letter_length FROM trans;
