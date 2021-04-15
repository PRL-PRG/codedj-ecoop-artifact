use djanco::*;
use djanco::log::*;
use djanco::utils::*;
use clap::Clap;

use paper_queries;

const PROJECT_NAME: &'static str = "paper_queries";

pub fn main() {

    let options = CommandLineOptions::parse();
    let log = Log::new(options.verbosity);
    let dataset = options.dataset_path_as_str();
    let cache = options.cache_path_as_str();

    let repository = if let Some(repository) = options.repository.as_ref() {
        Some(create_project_archive(PROJECT_NAME, repository.as_str()))
    } else {
        None
    };

    macro_rules! execute_query {
        ($database:expr, $method:path) => {
            timed_query!($method[&$database, &log, &options.output_path]);
        }
    }

    macro_rules! prepare_database {
        ($savepoint:expr, $stores:expr) => {
            Djanco::from_spec(dataset, cache, $savepoint, $stores, log.clone())
                .expect("Error initializing Djanco!");
        }
    }

    let database = prepare_database!(1617235200 /* = April 2021*/, stores!(Generic));
    execute_query!(database, paper_queries::stars);
    execute_query!(database, paper_queries::mean_changed_paths);
    execute_query!(database, paper_queries::median_changed_paths);
    execute_query!(database, paper_queries::experienced_author);
    execute_query!(database, paper_queries::experienced_authors_ratio);
    execute_query!(database, paper_queries::mean_commit_message_sizes);
    execute_query!(database, paper_queries::median_commit_message_sizes);
    execute_query!(database, paper_queries::commits);
    execute_query!(database, paper_queries::dump);


    if options.repository.is_some() && !options.do_not_archive_results {
        add_results(PROJECT_NAME, &repository.unwrap(), &options.output_path, options.size_limit);
    }
}
