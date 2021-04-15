use std::path::Path;

use djanco::*;
use djanco::data::*;
use djanco::time::*;
use djanco::csv::*;
use djanco::log::*;
use djanco::fraction::Fraction;

use djanco_ext::*;

#[djanco(April, 2021, subset(Generic))]
pub fn stars(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        .sort_by(project::Stars)
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .into_csv_in_dir(output, "stars.csv")
}

#[djanco(April, 2021, subset(Generic))]
pub fn mean_changed_paths(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        .sort_by(Mean(FromEach(project::Commits, Count(commit::Paths))))
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .ungroup()
        .into_csv_in_dir(output, "mean_changed_paths.csv")       
}

#[djanco(April, 2021, subset(Generic))]
pub fn median_changed_paths(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        .sort_by(Median(FromEach(project::Commits, Count(commit::Paths))))
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .ungroup()
        .into_csv_in_dir(output, "median_changed_paths<.csv")       
}

#[djanco(April, 2021, subset(Generic))]
pub fn experienced_author(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        //.filter_by_attrib(AsetLeast(Count(project::Users), 1))
        .filter_by(AtLeast(Count(FromEachIf(project::Users, AtLeast(user::Experience, Duration::from_years(2)))), 1))
        //.filter_by_attrib(Exists(project::UsersWith(MoreThan(user::Experience, Seconds::from_years(2)))))
        .sort_by(Count(project::Commits))
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .ungroup()
        .into_csv_in_dir(output, "experienced_author.csv")       
}

#[djanco(April, 2021, subset(Generic))]
pub fn experienced_authors_ratio(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        .filter_by(AtLeast(Count(project::Users), 2))
        .filter_by(AtLeast(Ratio(FromEachIf(project::Users, AtLeast(user::Experience, Duration::from_years(2))), project::Users), Fraction::new(1, 2)))
        //.sample(Distinct(Random(50, Seed(42)), MinRatio(project::Commits, 0.9)))
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .ungroup()
        .into_csv_in_dir(output, "experienced_authors_ratio.csv")       
}

#[djanco(April, 2021, subset(Generic))]
pub fn mean_commit_message_sizes(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        .sort_by(Mean(FromEach(project::Commits, commit::MessageLength)))
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .ungroup()
        .into_csv_in_dir(output, "mean_commit_message_sizes.csv")       
}

#[djanco(April, 2021, subset(Generic))]
pub fn median_commit_message_sizes(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        .sort_by(Median(FromEach(project::Commits, commit::MessageLength)))
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .ungroup()
        .into_csv_in_dir(output, "median_commit_message_sizes.csv")       
}

#[djanco(April, 2021, subset(Generic))]
pub fn commits(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    database.projects()
        .group_by(project::Language)
        .sort_by(Count(project::Commits))
        .sample(Distinct(Top(50), MinRatio(project::Commits, 0.9)))
        .ungroup()
        .into_csv_in_dir(output, "commits.csv")       
}

#[djanco(April, 2021, subset(Generic))]
pub fn dump(database: &Database, _log: &Log, output: &Path) -> Result<(), std::io::Error>  {
    let dump_dir = format!("{}/{}", output.as_os_str().to_str().unwrap(), "dump");
    database.projects().dump_all_info_to(dump_dir)
}