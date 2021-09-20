#include <uwsgi.h>

/*

	Busyness cheaper algorithm (by Łukasz Mierzwa)

*/

extern struct uwsgi_server uwsgi;

// this global struct containes all of the relevant values
struct uwsgi_cheaper_busyness_global {
	uint64_t busyness_max;
	uint64_t busyness_min;
	uint64_t *last_values;
	uint64_t *current_busyness;
	uint64_t total_avg_busyness;
	int *was_busy;
	uint64_t tcheck;
	uint64_t last_cheaped;      // last time worker was cheaped due to low busyness
	uint64_t next_cheap;        // timestamp, we can cheap worker after it
	uint64_t penalty;       // penalty for respawning to fast, it will be added to multiplier
	uint64_t min_multi;     //initial multiplier will be stored here
	uint64_t cheap_multi;   // current multiplier value
	int last_action;            // 1 - spawn workers ; 2 - cheap worker
	int verbose;                // 1 - show debug logs, 0 - only important
	uint64_t tolerance_counter; // used to keep track of what to do if min <= busyness <= max for few cycles in row
	int emergency_workers; // counts the number of running emergency workers
#ifdef __linux__
	int backlog_alert;
	int backlog_step;
	uint64_t backlog_multi; // multiplier used to cheap emergency workers
	uint64_t backlog_nonzero_alert;
	int backlog_is_nonzero;
	uint64_t backlog_nonzero_since; // since when backlog is > 0
#endif
} uwsgi_cheaper_busyness_global;

struct uwsgi_option uwsgi_cheaper_busyness_options[] = {

	{"cheaper-busyness-max", required_argument, 0,
		"set the cheaper busyness high percent limit, above that value worker is 