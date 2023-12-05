CREATE TABLE machine_log (
	machine TEXT NOT NULL,
	temperature TEXT NOT null,
	water text not null,
	bubbles text not null
);

-- Fill table with values from input file...

with soda_log as (
	select 
		substring(machine from '^Maskin (.*)') as machine,
		substring(temperature from '^ temperatur (.*)C')::integer as temperature,
		substring(water from '^ vann (.*)L')::integer as water,
		substring(bubbles from '^ kullsyre (.*)L')::integer as bubbles
	from machine_log
),
production_log as (
	select machine, sum(case
		when temperature >= 100 then floor(((water - 100) + (bubbles / 10)) - ((water - 100) + (bubbles / 10)) / 40)::integer
		else floor(((water - 100) + (bubbles / 10)))::integer
	end) as produced
	from soda_log
	where 
		temperature >= 95 and temperature <= 105 and 
		water >= 400 and water <= 1500 and 
		bubbles >= 300 and bubbles <= 500
	group by machine
)
(
	select machine as best_machine, null as total_production
	from production_log
	order by produced desc
	limit 1
)
union all
(
	select null as best_machine, sum(produced) as total_production
	from production_log
);
